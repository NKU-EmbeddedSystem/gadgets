import sys
def ana(filename):
    f = open(filename, 'r')
    base = 110
    nums = []
    for i in range(base, base + 12):
        nums.append('0x' + str(i))

    lines = f.readlines()
    mm = dict()
    for line in lines:
        if line.find('0xc3') != -1 and line.find(',[') != -1:
            dd = line.split()
            print(dd[2], ' '.join(dd[3:]))
        for num in nums:
            if line.find(num) != -1 and line[line.find(num) - 1] == ',':
                mm[num] = line[line.find('r') : line.find(num) - 1]
                break
    print(mm)
if __name__ == '__main__':
    path = 'test.txt'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    ana(path)
