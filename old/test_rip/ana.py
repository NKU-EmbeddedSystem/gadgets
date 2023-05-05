import sys
def get_offset(log:str):
    f = open(log, 'r')
    lines = f.readlines()
    base = 11
    beq = -1
    res = []
    for i, line in enumerate(lines):
        if line.find(',0x' + str(base)) != -1:
            if beq == -1:
                beq = i
            base += 1
    lines = lines[beq : ]
    for line in lines:
        if line.find('rip+') != -1:
            res.append(0xffffffff - int(line[line.find('+0x') + 3 : -2], 16))
    
    return res[:-2]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('please input path of log file')
    
    res = get_offset(sys.argv[1])
    for line in res:
        print('%#x'%line)