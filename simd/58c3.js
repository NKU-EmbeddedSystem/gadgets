function jsc58c3(p_xmm0, p_xmm1, p_xmm2, p_xmm3)
{
    let v_xmm0 = p_xmm0 * 1.01;
    let v_xmm1 = p_xmm1 * 1.02;
    let v_xmm2 = p_xmm2 * 1.03;
    let v_xmm3 = p_xmm3 * 1.04;
    let s = v_xmm0 % v_xmm3;
    return v_xmm1 + v_xmm2 + s;
}

for(let i = 0; i < 0x10000; i++)
{
    jsc58c3(0.61, 0.71, 0.72, 0.63);
}
