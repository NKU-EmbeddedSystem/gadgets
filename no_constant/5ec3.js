
function f5ec3(var1, var2, var3, var4){    
    var a0 = var1 ^ 0x111;
    var a1 = var1 ^ 0x112;
    var a2 = var1 ^ 0x113;
	var t0 = var1 & 0x114;
	var t1 = var1 * 0x115;
	var t2 = var1 & 0x116;
	var t3 = var1 * 0x117;
	var t4 = var1 & 0x118;
	var t5 = var1 * 0x119;
	var t6 = var1 & 0x120;
	var t7 = var1 * 0x121;
	var t8 = var1 & 0x122;
	var t9 = var1 * 0x123;
	var t10 = var1 & 0x124;
	var t11 = var1 * 0x125;
	var t12 = var1 & 0x126;
	var t13 = var1 * 0x127;
	var t14 = var1 & 0x128;
	var t15 = var1 * 0x129;
	var s = t0*2 + t2 + 0xc3;
    return a0 | a1 + a2 |t0 + t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9 + t10 + t11 + t12 + t13 + t14 + t15 | s;
}
for(var i = 0; i < 0x10000; i++)
{
    f5ec3(0xc35, 0xc22, 0xc32, 0xc55);
}
