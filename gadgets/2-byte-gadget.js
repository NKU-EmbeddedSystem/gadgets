var array = new Uint8Array();

function jsc(a)
{
    var gadget = 0x12f70e;
    return a ^ gadget ^ 0x123456;
}


for(var i = 0; i < 100000; ++i)
{
	jsc(0x1);
}
