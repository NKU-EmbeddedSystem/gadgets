
function jsc(var0, var1, var2, var3, var4, var5, var6){
	var t0 = var0 + 0x110;
	var t1 = var0 + 0x111;
	var t2 = var0 + 0x112;
	var t3 = var1 + 0x113;
	var t4 = var1 + 0x114;
	var t5 = var1 + 0x115;
	var t6 = var2 - 0x3d;
	var t7 = var2 + 0x117;
	var t8 = var2 + 0x118;
	var t9 = var3 + 0x119;
	var t10 = var3 + 0x120;
	var t11 = var3 + 0x121;
	var t12 = var4 + 0x122;
	var t13 = var4 + 0x123;
	var t14 = var4 + 0x124;
	var t15 = var5 + 0x125;
	var t16 = var5 + 0x126;
	var t17 = var5 + 0x127;
	var t18 = var6 + 0x128;
	var t19 = var6 + 0x129;
	var t20 = var6 + 0x130;
	return t0 & t1 | t2 ^ t3 & t4 | t5 ^ t6 & t7 | t8 ^ t9 & t10 | t11 ^ t12 & t13 | t14 ^ t15 & t16 | t17 ^ t18 & t19 | t20;
}

for(var i = 0; i < 0x10000; i++)
{
	jsc(0xc0, 0xc1, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6);
}
