
var array = new Uint8Array();
function syscall_jsc(var1, var2, var3, var4){
    var a0 = var1 + 0.111;
    var a1 = var1 * 0.112;
    var a2 = var1 / 0.113;
	var t0 = var1 + 0.114;
	var s = a1 * 2 + a2 + 0.13;
    return a0 | a1 + a2 | t0 | s;
}
for(var i = 0; i < 10000; i++)
{
    syscall_jsc(0.135, 0.122, 0.132, 0.155);
}
