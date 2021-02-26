import sys
count = 48
def get_registers(log:str):
    f = open(log, 'r')
    base = 110
    nums = []
    for i in range(base, base + count):
        nums.append('0x' + str(i))

    lines = f.readlines()
    mm = dict()
    for line in lines:
        for num in nums:
            if line.rfind(num) != -1 and line.find(',') != -1 and (line.find('leal') != -1 or line.find('addl') != -1):
                print(line)
                if line.find('leal') != -1:
                    mm[line[line.rfind('r'):line.rfind('+')]] ='var' + str(int(num[2:]) - base)
                    mm[line[line.find('r'):line.find(',')]] = 't' + str(int(num[2:]) - base)
                else:
                    mm[line[line.rfind('r'):line.rfind(',')]] = 'var' + str(int(num[2:]) - base)
                break
    return mm
if __name__ == '__main__':
    path = 'test.txt'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    print(get_registers(path))
