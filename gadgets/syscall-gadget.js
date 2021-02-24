var array = new Uint8Array();

function jsc(var1, var2, var3, var4){
	var rdi = var1 | 0xc3;
	var rbx = var1 ^ 0xc3;
	var rcx = var1 & 0xc3;
	var r8 = var1 + 0xc3;
	var r9 = var1 * 0xc3;
	var d = var2 - 0xc2;

	//use two registers
	// rcx += rdi * 2;
	array[rcx + rdi * 2 + 5] = 0xc3;
	var result = r8 + r9 + rbx + d + rcx;
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
