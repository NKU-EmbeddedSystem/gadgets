function jsc(rcx, rdi, r9){
	var rcx = rcx ^ 0x1234;
	var rdi = rdi ^ 0x2345;
	var r8 = r8 ^ 0x3456;
	var r9 = r9 + 2.8628345837198785e-312;
	r9 += -6.7936696184209404e-229;
	r9 += -6.7936699762396021e-229;
	r9 += 3.0226914823032513e+274;
	r9 += -2.6710638803933159e-229;
	r9 += -2.6710638803930354e-229;
	r9 += 2.9212589871283409e+274;
	r9 += -6.8283971717601484e-229;
	r9 += -6.9693174593711226e-229;
	var extra = r9 + 0xc3;
	return rcx + rdi + r8 + r9 + extra;
}

for(var i = 0; i < 0x102400; i++)
{
	jsc(0x2342, 0x2343, 0.0);
}
