const buffer = new ArrayBuffer(0x7000000);
const obja = new Uint8Array(buffer, 0x58);
// Uint32Array 
const objb = new Uint32Array(buffer, 0x60);
var i = 0;
for(i=0; i < 0x7000000;i++)
{
	obja[i] = i;
}

function readobj(obj, x) { 
	x = x ^ 23333334;
    //obja[x + 0x58] = 0xc3;
    objb[x + 0x58] = 0xc3;
	return x ^ 0x23333;
}
for (var i = 0; i < 0x233332; i++) {
	readobj(obja, i);
}

