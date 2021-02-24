function f0f05(var1, var2, var3, var4){
	var rcx = var1 ^ 0x111;
	var rdi = var1 ^ 0x112;
	var rdx = var1 ^ 0x113;
	rdi += rcx + 0x05;
	return rdx | rdi;
}

for(var i = 0; i < 0x10000; i++)
{
	f0f05(0xc35, 0xc22, 0xc32, 0xc55);
}