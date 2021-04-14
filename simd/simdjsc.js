function jsc(rdx, rcx, rdi, r8, r9, r11, r12, r14, r15, rax, rbx, rsi){
	let xmm0 = rdx + 1.01;
	let xmm1 = rcx + 1.02;
	let xmm2 = rdi + 1.03;
	let xmm3 = r8 + 1.04;
	let xmm4 = r9 + 1.05;
	let xmm5 = r11 + 1.06;
	let xmm6 = r12 + 1.07;
	let xmm7 = r14 + 1.08;
	let xmm8 = r15 + 1.09;
	let xmm9 = rax + 1.1;
	let xmm10 = rbx + 1.11;
	let xmm11 = rsi + 1.12;

	//jsc xmm0,xmm0,xmm3
	let i0 = xmm3 + xmm0;

	return xmm0 * xmm1 * xmm2 * xmm3 * xmm4 * xmm5 * xmm6 * xmm7 * xmm8 * xmm9 * xmm10 * xmm11 + (i0);
}


for(let i = 0; i < 0x1000; i++)
{
	jsc(1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.1, 1.11, 1.2);
}