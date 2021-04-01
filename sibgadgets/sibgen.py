# import os
# import pathlib
# import sys

registers = ['rdx', 'rcx', 'rdi', 'r8', 'r9', 'r11', 'r12', 'r14', 'r15', 'rax', 'rbx', 'rsi']


def get_header(func_name: str):
    header = f'function jsc{func_name}('

    for i in range(len(registers) - 1):
        header += registers[i] + ', '
    header += registers[-1] + '){\n'

    for i in range(len(registers)):
        header += f'\t{registers[i]} &= 0x{10 + i};\n'
    return header


def get_tail(func_name: str):
    tail = f'''
for(let i = 0; i < 0x10000; i++)
'''
    tail += '{\n'
    tail += f'\tjsc{func_name}('
    for i in range(len(registers) - 1):
        tail += f'0xc{i}, '
    tail += f'0xc{len(registers) - 1});\n'
    tail += '}\n'
    return tail


def gen_jsc(r1: str, r2: str, scale=2, imm='c3'):
    jsc = f'\tlet s = {r1} + {r2} * {scale} + 0x{imm};\n\treturn '

    for i in range(len(registers)):
        if i == registers.index(r1) or i == registers.index(r2):
            continue
        jsc += f'{registers[i]} + '

    jsc += 's;\n}\n'
    return jsc


def execute_js(js: str, filename: str):
    f = open(filename + '.js', 'w')
    f.write(js)
    f.close()
    # os.system(exec_path + ' --print-opt-code ' + filename + '.js > ' + filename + '.txt')


def generate_js():
    # 428d945ac3000000 ;leal rdx,[rdx+r11*2+0xc3]
    jsc5ac3 = gen_jsc('rdx', 'r11')
    execute_js(get_header('5ac3') + jsc5ac3 + get_tail('5ac3'), '5ac3')

    # 8d8c5ec3000000 ;leal rcx,[rsi+rbx*2+0xc3]
    jsc5ec3 = gen_jsc('rsi', 'rbx')
    execute_js(get_header('5ec3') + jsc5ec3 + get_tail('5ec3'), '5ec3')

    # 428d8c5fc3000000 ;leal rcx,[rdi+r11*2+0xc3]
    jsc5fc3 = gen_jsc('rdi', 'r11')
    execute_js(get_header('5fc3') + jsc5fc3 + get_tail('5fc3'), '5fc3')

    # 438d8c58c3000000 ;leal rcx,[r8+r11*2+0xc3]
    jsc58c3 = gen_jsc('r8', 'r11')
    execute_js(get_header('58c3') + jsc58c3 + get_tail('58c3'), '58c3')

    # 8d4c0f05   	;leal rcx,[rdi+rcx*1+0x5]
    jsc0f05 = gen_jsc('rcx', 'rdi', 1, '05')
    execute_js(get_header('0f05') + jsc0f05 + get_tail('0f05'), '0f05')

    # out = open('jsc.js', 'w')


if __name__ == '__main__':
    generate_js()
