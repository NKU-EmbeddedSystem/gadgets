const buffer = new ArrayBuffer(0x7000000);
// scale 2
const objb = new Uint16Array(buffer);
function jsc58c3(p_rdx, p_rcx, p_rdi, p_r8, p_r9, p_r11, p_r12, p_r14, p_r15, p_rax, p_rbx, p_rsi){
    p_rdx &= 0x10; // 83e210   andl rdx,0x10
    p_rcx &= 0x11; // 83e111   andl rcx,0x11
    p_rdi &= 0x12; // 83e712   andl rdi,0x12
    p_r8  &= 0x13; // 4183e013 andl r8, 0x13
    p_r9  &= 0x14; // 4183e114 andl r9, 0x14
    p_r11 &= 0x15; // 4183e315 andl r11,0x15
    p_r12 &= 0x16; // 4183e416 andl r12,0x16
    p_r14 &= 0x17; // 4183e617 andl r14,0x17
    p_r15 &= 0x18; // 4183e718 andl r15,0x18
    p_rax &= 0x19; // 83e019   andl rax,0x19
    p_rbx &= 0x20; // 83e320   andl rbx,0x20
    p_rsi &= 0x21; // 83e621   andl rsi,0x21
    //8d4c58c3  leal rcx,[rax+rbx*2-0x3d]
    let s = p_rax + p_rbx * 2 - 0x3d; 
    return p_rdx + p_rcx + p_rdi + p_r8 + p_r9 + p_r11 + p_r12 + p_r14 + p_r15 + s;
}

for(let i = 0; i < 0x100000; i++)
{
	jsc58c3(0xc0, 0xc1, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xc10, 0xc11);
}
