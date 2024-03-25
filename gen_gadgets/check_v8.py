import sys
import os
import multiprocessing


def search_file(file_name):
    danger1 = open(file_name, "r").readlines()
    for line in danger1:
        line = line.strip()
        gadget = line.split(" ")[0][2:]
        gadget += "c3"
        gen_cmd = 'python3 gen.py ' + gadget + " > jsc.js"
        os.system(gen_cmd)

        cmd = d8_path + " --print-opt-code jsc.js | grep " + gadget
        os.system(cmd)


def search_file2(file_name):
    danger1 = open(file_name, "r").readlines()
    for line in danger1:
        line = line.strip()
        gadget = line.split(" ")[0][2:]
        gadget += "c3c3"
        gen_cmd = 'python3 gen.py ' + gadget + " > jsc.js"
        os.system(gen_cmd)

        cmd = d8_path + " --print-opt-code jsc.js | grep " + gadget
        os.system(cmd)


def run(f1, f2):
    search_file(f1)
    search_file(f2)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 check_v8.py D8_PATH iterations")
        sys.exit(1)
    d8_path = sys.argv[1]
    iterations = int(sys.argv[2])
    p_list = []
    for i in range(iterations):
        p = multiprocessing.Process(
            target=run, args=('danger1.txt', 'danger2.txt'))
        p.start()
        p_list.append(p)
        if len(p_list) == 10:
            for p in p_list:
                p.join()
