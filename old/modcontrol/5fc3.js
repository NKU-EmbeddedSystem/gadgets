function jsc5ac3(rdx, rcx, rdi, r8, r9, r11, r12, r14, r15, rax) {
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
    let i0 = rdi + 0x11;
    //leal rbx, rdi
    let rbx = rdi - 0x3d;
    return (i0 + rbx) + rdx + rcx + rdi + r8 + r9 + r11 + r12 + r14 + r15 + rax;
}

for (let i = 0; i < 0x10000; i++) {
    jsc5ac3(0xc0, 0xc1, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xc10, 0xc11);
}
