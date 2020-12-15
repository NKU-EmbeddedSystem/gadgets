function jsc(rcx, rdi, r9){
	var rcx = rcx ^ 0x1234;
	var rdi = rdi ^ 0x2345;
	var r8 = r8 ^ 0x3456;
	var r9 = r9 ^ 0x4567;
	var extra = r9 + 0xc3;
	return rcx | rdi | r8 | r9 | extra;
}

for(var i = 0; i < 0x10240; i++)
{
	jsc(0x2342, 0x2343, 0x2344);
}
