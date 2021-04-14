function jsc58c3(rdx, rcx, rdi, r8, r9, r11, r12, r14, r15, rax, rbx, rsi){
	rdx &= 0x10;
	rcx &= 0x11;
	rdi &= 0x12;
	r8 &= 0x13;
	r9 &= 0x14;
	r11 &= 0x15;
	r12 &= 0x16;
	r14 &= 0x17;
	r15 &= 0x18;
	rax &= 0x19;
	rbx &= 0x20;
	rsi &= 0x21;
	var i0 = rax + 0x11;
	var i1 = rax + 0x12;
	var i2 = rax - 0x3d;
	var i3 = rax + 0x14;
	var i4 = rax + 0x15;
	var i5 = rax + 0x16;
	var i6 = rax + 0x17;
	var i7 = rax + 0x18;
	var i8 = rax + 0x19;
	var i9 = rax + 0x20;
	var i10 = rax + 0x21;
	var i11 = rax + 0x22;
	return rdx + rcx + rdi + r8 + r9 + r11 + r12 + r14 + r15 + rax + rbx + rsi + (i0 + i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11);
}

for(let i = 0; i < 0x10000; i++)
{
	jsc58c3(0xc0, 0xc1, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xc10, 0xc11);
}
