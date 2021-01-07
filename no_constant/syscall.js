function syscall_jsc(var1, var2, var3, var4){
	var a0 = var1 ^ 0x111;
	var a1 = var1 ^ 0x112;
	var a2 = var1 ^ 0x113;

	a0 += a1 + 0x05;
	
	return a2 | a0;
}

for(var i = 0; i < 0x10000; i++)
{
	syscall_jsc(0xc35, 0xc22, 0xc32, 0xc55);
}