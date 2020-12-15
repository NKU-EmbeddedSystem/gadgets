var obja = new Array();
var i = 0;
for(i=0; i < 0x7000000;i++)
{
	obja[i] = 0x1;
}

function readobj(obj, x) { 
	x = x ^ 23333334;
	obj[0x6fffff] = obj[x] ^ 0xc3;
	return x ^ 0x23333;
}
for (var i = 0; i < 0x233332; i++) {
	readobj(obja, 2);
}

