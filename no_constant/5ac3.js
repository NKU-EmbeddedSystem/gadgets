
function f5ac3(var1, var2, var3, var4){    
    var a0 = var1 ^ 0x111;
    var a1 = var1 ^ 0x112;
    var a2 = var1 ^ 0x113;
	var t0 = var1 & 0x114;
	var t1 = var1 + 0x115;
	var t2 = var1 * 0x116;
	var s = a1 + a2 * 2 + 0xc3;
    return a0 | a1 + a2 |t0 + t1 + t2 | s;
}
for(var i = 0; i < 0x10000; i++)
{
    f5ac3(0xc35, 0xc22, 0xc32, 0xc55);
}
