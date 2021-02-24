
function f58c3(var1, var2, var3, var4){
    var r12 = var1 ^ 0x111;
	var r11 = var1 ^ 0x112;
	r11 += r12;
    r12 = var1 ^ 0x113;
	var t0 = var1 & 0x114;
	var t1 = var1 + 0x115;
	var t2 = var1 * 0x116;
	var t3 = var1 ^ 0x117;
	var t4 = var1 & 0x118;
	var t5 = var1 + 0x119;
	var s = 0xc3;
    return r11 + r12 + t0 + t1 + t2 + t3 + t4 + t5 + s;
}

for(var i = 0; i < 0x10000; i++)
{
    f58c3(0xc35, 0xc22, 0xc32, 0xc55);
}
