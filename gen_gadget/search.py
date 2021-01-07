import re

if __name__ == "__main__":
    registers = [('rax', 'rbx'), ('rdi', 'rbx'), ('rsi', 'rbx'), ('rdx', 'rbx')]
    for j in range(len(registers)):
        for i in range(32):
            file = str(i) + '.txt'
            f = open(file)
            flags = [False, False]
            lines = f.readlines()
            f.close()

            for line in lines:
                if line.find(registers[j][0]) != -1:
                    flags[0] = True
                if line.find(registers[j][1]) != -1:
                    flags[1] = True
            
            if flags[0] and flags[1]:
                print(registers[j], i)
                break