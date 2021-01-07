
var array = new Uint8Array();
function syscall_jsc(var1, var2, var3, var4){
    var a0 = var1 ^ 0x111;
    var a1 = var1 ^ 0x112;
    var a2 = var1 ^ 0x113;
	var t0 = var1 & 0x114;
	var t1 = var1 + 0x115;
	var t2 = var1 | 0x116;
	var t3 = var1 ^ 0x117;
	var t4 = var1 & 0x118;
	var t5 = var1 + 0x119;
	var t6 = var1 | 0x120;
	var t7 = var1 ^ 0x121;
	var t8 = var1 & 0x122;
	var t9 = var1 + 0x123;
	var t10 = var1 | 0x124;
	var s = t9 + t10 * 2 + 0xc3;
    return a0 + a1 + a2 + t0 & t1 + t2 | t3 ^ t4 & t5 + t6 | t7 ^ t8 & t9 + t10
}
for(var i = 0; i < 0x10000; i++)
{
    syscall_jsc(0xc35, 0xc22, 0xc32, 0xc55);
}
