var array = new Uint8Array();

function jsc(a, b, c)
{
	array[0x58] = 0xc3;
	array[0x59] = 0xc3;
	array[0x5a] = 0xc3;

	return a ^ b ^ c;
}


for(var i = 0; i < 100000; ++i)
{
	jsc(0x1, 0x2, 0x3);
}
