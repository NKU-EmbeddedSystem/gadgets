
var array = new Uint8Array();
function syscall_jsc(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11){
	var t0 = var0 & 1.110;
	var t1 = var1 & 1.111;
	var t2 = var2 & 1.112;
	var t3 = var3 & 1.113;
	var t4 = var4 & 1.114;
	var t5 = var5 & 1.115;
	var t6 = var6 & 1.116;
	var t7 = var7 & 1.117;
	var t8 = var8 & 1.118;
	var t9 = var9 & 1.119;
	var t10 = var10 & 1.120;
	var t11 = var11 & 1.121;
	var i0 = t0 + 1.11;
	var i1 = t1 + 1.12;
	var i2 = t2 + 1.13;
	var i3 = t3 + 1.14;
	var i4 = t4 + 1.15;
	var i5 = t5 + 1.16;
	var i6 = t6 + 1.17;
	var i7 = t7 + 1.18;
	var i8 = t8 + 1.19;
	var i9 = t9 + 1.20;
	var i10 = t10 + 1.21;
	var i11 = t11 + 1.22;
	return t0  + t1  + t2  + t3  + t4  + t5  + t6  + t7  + t8  + t9  + t10  + t11 + (i0 + i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11);
}

for(var i = 0; i < 0x10000; i++)
{
	syscall_jsc(0xc0, 0xc1, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xc10, 0xc11);
}
