function jsc5ec3(rdx, rcx, rdi, r8, r9, r11, r12, r14, r15, rax, rbx, rsi){
	var t0 = rdx & 0x110;
	var t1 = rcx & 0x111;
	var t2 = rdi & 0x112;
	var t3 = r8 & 0x113;
	var t4 = r9 & 0x114;
	var t5 = r11 & 0x115;
	var t6 = r12 & 0x116;
	var t7 = r14 & 0x117;
	var t8 = r15 & 0x118;
	var t9 = rax & 0x119;
	var t10 = rbx & 0x120;
	var t11 = rsi & 0x121;
	var s = t11 + t10 * 2 + 0xc3;
	return t0 + t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9 + s;
}

for(var i = 0; i < 0x10000; i++)
{
	jsc5ec3(0xc0, 0xc1, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xc10, 0xc11, 0xc11);
}
