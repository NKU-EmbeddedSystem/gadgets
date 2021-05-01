function jsc(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11)
{
    var xmm0 = var0+ 1.01;
    var xmm1 = var1 + 1.02;
    var xmm2 = var2 + 1.03;
    var xmm3 = var3 + 1.04;
    var i0 = xmm1 + xmm2;
    var i1 = xmm3 + xmm0;
    return i0 + i1;
}

for(let i = 0; i < 0x10000; i++)
{
    jsc(0.61, 0.71, 0.72, 0.63, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.710, 0.711);
}
