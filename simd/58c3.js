function jsc58c3(p_xmm0, p_xmm1, p_xmm2, p_xmm3, p_xmm4, p_xmm5, p_xmm6, p_xmm7, p_xmm8, p_xmm9, p_xmm10, p_xmm11, p_xmm12, p_xmm13, p_xmm14)
{
    p_xmm0 *= p_xmm0;
    p_xmm1 *= p_xmm1;
    p_xmm2 *= p_xmm2;
    p_xmm3 *= p_xmm3;
    p_xmm4 *= p_xmm4;
    p_xmm5 *= p_xmm5;
    p_xmm6 *= p_xmm6;
    p_xmm7 *= p_xmm7;
    p_xmm8 *= p_xmm8;
    p_xmm9 *= p_xmm9;
    p_xmm10 *= p_xmm10;
    p_xmm11 *= p_xmm11;
    p_xmm12 *= p_xmm12;
    p_xmm13 *= p_xmm13;
    p_xmm14 *= p_xmm14;
    p_xmm0 += p_xmm3;
    return p_xmm0 + p_xmm14 + p_xmm13 + p_xmm12 + p_xmm11 + p_xmm10 + p_xmm9 + p_xmm8 + p_xmm7 + p_xmm6 + p_xmm5 + p_xmm4 + p_xmm3 + p_xmm2 + p_xmm1;
}

for(let i = 0; i < 0x10000; i++)
{
    jsc58c3(1.010, 1.011, 1.012, 1.013, 1.014, 1.015, 1.016, 1.017);
}
