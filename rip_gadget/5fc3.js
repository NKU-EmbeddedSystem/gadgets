
array = new Uint8Array();
const constant = 0x1234;
function payload3(v1, v2) {
	array[10] = v1 + 0x11;
	array[11] = v1 + 0x22;
	array[12] = v1 + 0x33;
	array[13] = v1 + 0x44;
	array[14] = v1 + 0x55;
	array[15] = v1 + 0x66;
	array[1];
	if (v1 > 0){
		array[1] = 0x00;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;
        array[15] &= 0x56;
        array[15] *= 0x56;

	}
	else{
		array[1] = 0x01;
	}
	array[16] = v1 * 0x77;
	array[2];
	if (v1 > 0)
		array[2] = 0x00;
	else
		array[2] = 0x01;
	array[17] = v1 * 0x88;
	array[18] = v1 * 0x99;
	array[19] = v1 * 0x12;
	array[20] = v1 * 0x23;
	array[21] = v1 * 0x34;
	return array[1] ^ array[2] ^ array[10] ^ array[11] ^ array[12] ^ array[13] ^ array[14] ^ array[15] ^ array[16] ^ array[17] ^ array[18] ^ array[19] ^ array[20] ^ array[21];
}


for (var i = 0; i < 0x1; i++) {
	payload3(i, i % 32);
}
