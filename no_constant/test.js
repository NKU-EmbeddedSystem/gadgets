var array = new Uint8Array();
// %DebugPrint(array);

function syscall_jsc(var1, var2, var3, var4){
	var rdi = var1 | 0x123;
	var rcx = var1 & 0x234;
	var b = var2 % 0x345;
	var c = var2 * 0x456;
	var e = var2 ^ 0x567;
	
	//release rdi and rcx
	e += rdi;
	e += rcx * 2;

	//force to use rdi and rcx
	var extra = e + 0xc3;

	var result = b + c | extra;
	return result;
}

for(var i = 0; i < 0x1000; ++i)
{
	array[i] = 0x1;
}

//var tmp = 0;
for(var i = 0; i < 0x10000; i++)
{
	syscall_jsc(0xc35, 0xc22, 0xc32, 0xc55);
}

//console.log(tmp);
