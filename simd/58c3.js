function jsc58c3(p_xmm0, p_xmm1, p_xmm2, p_xmm3, p_xmm4, p_xmm5, p_xmm6, p_xmm7)
{
    let v_xmm0 = p_xmm0 * 0.010;
    let v_xmm1 = p_xmm1 * 0.011;
    let v_xmm2 = p_xmm2 * 0.012;
    let v_xmm3 = p_xmm3 * 0.013;
    let v_xmm4 = p_xmm4 * 0.014;
    let v_xmm5 = p_xmm5 * 0.015;
    let v_xmm6 = p_xmm6 * 0.016;
    let v_xmm7 = p_xmm7 * 0.017;
    let s = v_xmm0 + v_xmm3;
    return v_xmm0 + (v_xmm1 + s) + v_xmm2 + v_xmm4 + v_xmm5 + v_xmm6 + v_xmm7;
}

for(let i = 0; i < 0x10000; i++)
{
    jsc58c3(1.010, 1.011, 1.012, 1.013, 1.014, 1.015, 1.016, 1.017);
}
