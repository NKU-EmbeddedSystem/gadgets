import sys
def ana(filename):
    f = open(filename, 'r')
    base = 10
    nums = []
    for i in range(base, base + 20):
        nums.append('0x' + str(i))

    lines = f.readlines()
    mm = dict()
    for line in lines:
        for num in nums:
            if line.rfind(num) != -1 and line[line.rfind(num) - 1] == '+':
                mm[line[line.rfind('r') : line.rfind(num) - 1]] = num
                break
    print(mm)
if __name__ == '__main__':
    path = 'test.txt'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    ana(path)
