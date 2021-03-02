array1 = new Uint8Array();
array2 = new Uint16Array();
array3 = new Uint32Array();

// rax : 0x3b rdx/risi: 0 rdi : string
function jsc(v1) {
    var a1 = 0x3b;
    var a2 = 0;
    var a3 = 0x2233;
    var a4 = 0x3344;
    var a5 = 0x1234;
    var a6 = 0x2345;
    var a7 = 0x3456;
    var a8 = 0x4567;
    return v1 + a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6 ^ a7 ^ a8;
}

tmp = 0;

for(var i = 0; i < 100000; ++i)
{
    tmp += jsc(i);
}

console.log(tmp);
