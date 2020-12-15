print("var obja = new Array();")
for i in range(1, 0xff):
    print("obja[" + str(i) + "]=0x123;")


print(
"function readobj(obj, x) { \n"
"	x = x ^ 23333334;\n"
"	obj[0xfe] = obj[0xfe] ^ 0x233335;\n"
"	return x ^ 0x23333;\n"
"}\n"
"for (var i = 0; i < 0x233332; i++) {\n"
"	readobj(obja, 2);\n"
"}\n"
)