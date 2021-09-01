
function f5ac3(var1, var2, var3, var4){    
    var rcx = var1 ^ 0x111;
    var rdx = var1 ^ 0x112;
    var r11 = var1 ^ 0x113;
	var s = rdx + r11 * 2 + 0xc3;
    return rcx | rdx + r11 | s;
}


for(var i = 0; i < 0x10000; i++)
{
    f5ac3(0xc35, 0xc22, 0xc32, 0xc55);
}
