print("obja = new Object();")
for i in range(1, 0x3ff):
    print("obja.paddings" + str(i) + "="+ "0x123;")


print(
"function readobj(x) { \n"
"	x = x ^ 23333334;\n"
"   obja.id = obja.id ^ 0x233335;\n"
"	return x ^ 0x23333;\n"
"}\n"
"for (var i = 0; i < 0x233332; i++) {\n"
"	readobj(2);\n"
"}\n"
)
