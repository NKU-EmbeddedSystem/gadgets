

if __name__ == "__main__":
    f = open('test.txt')
    lines = f.readlines()
    num = 0xffffffff

    for line in lines:
        tmp = line[line.find('rip') + 4:-2]
        tmp = int(tmp, 16)
        if tmp < num:
            num = tmp
    
    print(hex(num))