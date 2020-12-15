obja = new Object();
function init() {
	// obja.name = "obja";
	obja.padding1 = 0x123;
	obja.padding2 = 0x123;
	obja.id = 0x233331;
}

function readobj(obj, x) {
	for (value in obj) {
		x |= value;
		x = x ^ 0x233334;
	}
	return x ^ 0x233335;
}


for (var i = 0; i < 0x233332; i++) {
	readobj(obja, i);
}
