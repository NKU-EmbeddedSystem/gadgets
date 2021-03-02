var array = new Uint8Array();
// %DebugPrint(array);

function jsc(var1, var2, var3, var4){
	var rdi = var1 + 0x110;
	var rbx = var1 + 0x111;
	var rcx = var1 + 0x112;
	var r8 = var1 + 0x113;
	var r9 = var1 + 0x114;
	var d = var2 + 0x115;
	var e = var1 + 0x116;
	var f = var1 + 0x117;
	var g = var1 + 0x118;
	var h = var1 + 0x119;

	//release rdi and rcx
	rdi += rcx + 0x05;

	var result = r8 ^ r9 & rbx + r8 ^ r9 & d + e ^ f & g ^ h + d | rdi;
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
