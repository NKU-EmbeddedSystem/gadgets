const buffer = new ArrayBuffer(0x7000000);
const scale2 = new Uint16Array(buffer);
function jsc5ec3(rdx, rcx, rdi, r8, r9, r11, r12, r14, r15, rax, rbx, rsi) {
    rdx &= 0x10;
    rcx &= 0x11;
    rdi &= 0x12;
    r8 &= 0x13;
    r9 &= 0x14;
    r11 &= 0x15;
    r12 &= 0x16;
    r14 &= 0x17;
    r15 &= 0x18;
    rax &= 0x19;
    rbx &= 0x20;
    rsi &= 0x21;
    //leal rbx, [rsi-0x3d]
    scale2[rbx] = 0xc3;
    return rdx + rcx + rdi + r8 + r9 + r11 + r12 + r14 + r15 + rax + rbx;
}

for (let i = 0; i < 0x10000; i++) {
    jsc5ec3(0xc0, 0xc1, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xc10, 0xc11);
}
