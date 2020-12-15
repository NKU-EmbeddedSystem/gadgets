var array = new Uint8Array();

function jsc(var1, var2, var3, var4){
	var rdi = var1 | 0xc3;
	var rbx = var1 ^ 0xc3;
	var rcx = var1 & 0xc3;
	var r8 = var1 + 0xc3;
	var r9 = var1 * 0xc3;
	var a = var2 - 0xc2;
	var b = var2 % 0xc2;
	var c = var2 * 0xc2;
	var d = var2 - 0xc2;
	var e = var2 ^ 0xc2;
	e += rdi;
	e += rcx;
	var extra = e + 0xc305;
	var result = r8 + r9 + rbx + a + b + c + d | extra;
	return result;
}

for(var i = 0; i < 0x1000; ++i)
{
	array[i] = 0x1;
}

//var tmp = 0;
for(var i = 0; i < 0x10000; i++)
{
	jsc(0xc35, 0xc22, 0xc32, 0xc55);
}

//console.log(tmp);
