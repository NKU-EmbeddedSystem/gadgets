array = new Float32Array();

function jsc58c3(p_xmm0, p_xmm1, p_xmm2, p_xmm3, offset)
{
    let v_xmm0 = p_xmm0 * 0.0100000000000001;
    let v_xmm1 = p_xmm1 * 0.0200000000000001;
    let v_xmm2 = p_xmm2 * 0.0300000000000001;
    let v_xmm3 = p_xmm3 * 0.0400000000000001;
    // avx cmp
    let s = v_xmm0 + v_xmm1 * 2 + 0.1234;
    array[offset * 4 + offset + 0xc3] = s;
    return s + v_xmm2 + v_xmm3;
}

for(let i = 0; i < 0x10000; i++)
{
    jsc58c3(0.010000061, 0.01000000000071, 0.010000000000000072, 0.01000000000000063, 0x43);
}
