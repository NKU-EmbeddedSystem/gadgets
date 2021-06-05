function jsc58c3(p_rdx, p_rcx, p_rdi, p_r8, p_r9, p_r11, p_r12, p_r14, p_r15, p_rax, p_rbx, p_rsi){
    let v_rdx = p_rdx & 0x10;
    let v_rcx = p_rcx & 0x11;
    let v_rdi = p_rdi & 0x12;
    let v_r8  = p_r8  & 0x13;
    let v_r9  = p_r9  & 0x14;
    let v_r11 = p_r11 & 0x15;
    let v_r12 = p_r12 & 0x16;
    let v_r14 = p_r14 & 0x17;
    let v_r15 = p_r15 & 0x18;
    let v_rax = p_rax & 0x19;
    let v_rbx = p_rbx & 0x20;
    let v_rsi = p_rsi & 0x21;
    v_rbx = v_rax - 0x3d;
    //let i0  = v_rax + 0x11;
    return v_rbx + v_rdx + v_rcx + v_rdi + v_r8 + v_r9 + v_r11 + v_r12 + v_r14 + v_r15 + v_rax + v_rsi;
}

for(let i = 0; i < 0x10000; i++)
{
    jsc58c3(0xc0, 0xc1, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xc10, 0xc11);
}
