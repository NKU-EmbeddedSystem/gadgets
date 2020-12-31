var array = new Uint8Array();
// %DebugPrint(array);

function syscall_jsc(var1, var2, var3, var4){
	var rdi = var1 | 0x123;
	var rdx = var1 ^ 0x345;
	var rsi = var1 & 0x456;
	var r9 = var1 + 0x567;
	var r11 = var1 * 0x678;
	var r14 = var2 - 0x789;
	//rax rdx
	var c = var2 % 0x223;
	var r15 = var2 * 0x334;
	var rbx = var2 - 0x445;
	var rcx = var2 ^ 0x556;

	//release rdi and rcx
	rbx += rdi;
	rbx += rdx;

	//force to use rdi and rcx
	var extra = rbx + 0x05;

	var result = rdi + rdx + rsi * r9 + rsi + r11 * r14 * c * r15 + rbx * rcx;
	return result;
}

for(var i = 0; i < 0x1000; ++i)
{
	array[i] = 0x1;
}

//var tmp = 0;
for(var i = 0; i < 0x10000; i++)
{
	syscall_jsc(0xc35, 0xc22, 0xc32, 0xc55);
}