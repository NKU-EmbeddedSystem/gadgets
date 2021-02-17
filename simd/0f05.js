
var array = new Uint8Array();
function syscall_jsc(var1, var2, var3, var4){
    var a0 = var1 + 0.111;
    var a1 = var1 * 0.112;
    var a2 = var1 / 0.113;
	var t0 = var1 + 0.114;
	var t1 = var1 * 0.115;
	var t2 = var1 / 0.116;
	var t3 = var1 + 0.117;
	var t4 = var1 * 0.118;
	var t5 = var1 / 0.119;
	var t6 = var1 + 0.120;
	var t7 = var1 * 0.121;
	var t8 = var1 / 0.122;
	var t9 = var1 + 0.123;
	var t10 = var1 * 0.124;
	var t11 = var1 / 0.125;
	var t12 = var1 + 0.126;
	var t13 = var1 * 0.127;
	var t14 = var1 / 0.128;
	var t15 = var1 + 0.129;
	var t16 = var1 * 0.130;
	var t17 = var1 / 0.131;
	var t18 = var1 + 0.132;
	var t19 = var1 * 0.133;
	var t20 = var1 / 0.134;
	var s = t12*2 + t15 + 0.13;
    return a0 * a1 + a2 *t0 + t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9 + t10 + t11 + t12 + t13 + t14 + t15 + t16 + t17 + t18 + t19 + t20 * s;
}
for(var i = 0; i < 10000; i++)
{
    syscall_jsc(0.135, 0.122, 0.132, 0.155);
}
