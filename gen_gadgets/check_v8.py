import sys
import os


def search_file(file_name):
    danger1 = open(file_name, "r").readlines()
    for line in danger1:
        line = line.strip()
        gadget = line.split(" ")[0][2:]
        gadget += "c3"
        gen_cmd = 'python3 gen.py ' + gadget + " > jsc.js"
        print(gen_cmd)
        os.system(gen_cmd)

        cmd = d8_path + " --print-opt-code jsc.js | grep " + gadget
        print(cmd)
        os.system(cmd)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 check_v8.py D8_PATH")
        sys.exit(1)
    d8_path = sys.argv[1]
    search_file('danger1.txt')
    search_file('danger2.txt')
