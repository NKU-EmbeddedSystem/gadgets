function js58c3(xmm0, xmm1, xmm2, xmm3, xmm4, xmm5, xmm6, xmm7, xmm8, xmm9, xmm10, xmm11){
	xmm0 += 0.10;
	xmm1 += 0.11;
	xmm2 += 0.12;
	xmm3 += 0.13;
	xmm4 += 0.14;
	xmm5 += 0.15;
	xmm6 += 0.16;
	xmm7 += 0.17;
	xmm8 += 0.18;
	xmm9 += 0.19;
	xmm10 += 0.20;
	xmm11 += 0.21;
	let s = xmm3 + xmm0;
	return xmm1 + xmm2 + xmm4 + xmm5 + xmm6 + xmm7 + xmm8 + xmm9 + xmm10 + xmm11 + (s);
}

for(let i = 0; i < 0x10000; i++)
{
	js58c3(0.60, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.610, 0.611);
}
