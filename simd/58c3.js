function jsc(rdx, rcx, rdi, r8){
	let xmm0 = rdx + 1.01;
	let xmm1 = rcx + 1.02;
	let xmm2 = rdi + 1.03;
	let xmm3 = r8 + 1.04;
	//jsc xmm0,xmm0,xmm3
	let i0 = xmm3 + xmm0;
	return xmm0 * xmm1 * xmm2 * xmm3  + (i0);
}


for(let i = 0; i < 0x1000; i++)
{
	jsc(1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.1, 1.11, 1.2);
}