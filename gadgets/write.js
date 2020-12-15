obja = new Object();
obja.paddings1=0x123;
/**................. */
obja.paddings766=0x123;
function readobj(x) { 
	x = x ^ 23333334;
	obja.id = x ^ 0x233335;
	return x ^ 0x23333;
}
for (var i = 0; i < 0x233332; i++) {
	readobj(2);
}

