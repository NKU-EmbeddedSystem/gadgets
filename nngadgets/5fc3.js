
var array = new Uint8Array();
function syscall_jsc(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11){
	var t0 = var0 & 0x110;
	var t1 = var1 & 0x111;
	var t2 = var2 & 0x112;
	var t3 = var3 & 0x113;
	var t4 = var4 & 0x114;
	var t5 = var5 & 0x115;
	var t6 = var6 & 0x116;
	var t7 = var7 & 0x117;
	var t8 = var8 & 0x118;
	var t9 = var9 & 0x119;
	var t10 = var10 & 0x120;
	var t11 = var11 & 0x121;
var s = t1 + t4 * 2 + 0xc3;
    return  t0 + t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9 + t10 + t11 | s;
}

for(var i = 0; i < 0x10000; i++)
{
	syscall_jsc(0xc0, 0xc1, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xc10, 0xc11);
}
