var array1 = new Uint8Array();
var array2 = new Uint8Array();
function payload3(v1,v2){
var array1 = new Uint8Array();

        var g10 = v1 * 0x1111;
        var g11 = v1 * 0x2222;
        var g12 = v1 * 0x3333;
        var g13 = v1 * 0x4444;
        var g14 = v1 * 0x5555;
        var g15 = v1 * 0x6666;
        var g1;
        if(v1>0)
                g1=0x00;
        else
                g1=0x01;
        var g16 = v1 * 0x7777;
        var g2;
        if(v1>0)
                g2=0x00;
        else
                g2=0x01;
        var g17 = v1 * 0x8888;
        var g18 = v1 * 0x9999;
        var g19 = v1 * 0x1212;
        var g20 = v1 * 0x2323;
        var g21 = v1 * 0x3434;
        return  g1^g2^g10^g11^g12^g13^g14^g15^g16^g17^g18^g19^g20^g21;
}


for(var i = 0; i < 0x10000; i++)
{
        payload3(i,i%32);
}
%DisassembleFunction(payload3);
