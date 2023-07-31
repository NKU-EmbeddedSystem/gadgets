import sys
from iced_x86 import *

regs = ['rdx', 'rcx', 'rdi', 'r8', 'r9', 'r11',
        'r12', 'r14', 'r15', 'rax', 'rbx', 'rsi']

code2reg = ['rax', 'rcx', 'rdx', 'rbx', 'r12', None, 'rsi', 'rdi']
header = '''function jsc(p_rdx, p_rcx, p_rdi, p_r8, p_r9, p_r11, p_r12, p_r14, p_r15, p_rax, p_rbx, p_rsi){
    p_rdx &= 0x10; // 83e210   andl rdx,0x10
    p_rcx &= 0x11; // 83e111   andl rcx,0x11
    p_rdi &= 0x12; // 83e712   andl rdi,0x12
    p_r8  &= 0x13; // 4183e013 andl r8, 0x13
    p_r9  &= 0x14; // 4183e114 andl r9, 0x14
    p_r11 &= 0x15; // 4183e315 andl r11,0x15
    p_r12 &= 0x16; // 4183e416 andl r12,0x16
    p_r14 &= 0x17; // 4183e617 andl r14,0x17
    p_r15 &= 0x18; // 4183e718 andl r15,0x18
    p_rax &= 0x19; // 83e019   andl rax,0x19
    p_rbx &= 0x20; // dead code
    p_rsi &= 0x21; // 83e621   andl rsi,0x21
'''

tail = '''}

for(let i = 0; i < 0x10000; i++)
{
    jsc(0xc0, 0xc1, 0xc2, 0xc3, 0xc4, 0xc5,
        0xc6, 0xc7, 0xc8, 0xc9, 0xc10, 0xc11);
}
'''


def get_reg(code):
    if code >= len(code2reg):
        return None
    return code2reg[code]


def byte_parse(byte):
    # return modrm or scale
    rm = byte & 7
    byte >>= 3
    reg = byte & 7
    byte >>= 3
    mod = byte
    return (mod, reg, rm)


def negative(num):
    return (num & 128) != 0


def unsigned_convert(num):
    if negative(num):
        return -(256 - num)
    else:
        return num


def gen_3byte(gadget):
    mod, reg, rm = byte_parse(int(gadget[0:2], 16))
    if rm != 0b100:
        return None
    if mod == 0b11 or mod == 0b00:
        return None

    op1 = get_reg(reg)
    if not op1:
        return None
    scale, index, base = byte_parse(int(gadget[2:4], 16))
    pow = 2 ** scale
    op2 = get_reg(index)
    if not op2:
        return None
    op3 = get_reg(base)
    if not op3:
        return None
    js_inst = f'    p_{op1} = p_{op2} * {pow} + p_{op3}'

    disp = int(gadget[4:6], 16)
    if mod == 1:
        if negative(disp):
            js_inst += " " + hex(unsigned_convert(disp)) + ";\n"
        else:
            js_inst += " + " + hex(disp) + ";\n"
    else:
        if negative(disp):
            js_inst += " + " + hex(disp) + ";\n"
        else:
            return None

    next_line = f"    let i0 = p_{op1} + 0x11;\n"
    return_inst = f"    return (i0 + p_{op1})"
    for i in range(len(regs)):
        if regs[i] != op1:
            return_inst += f" + p_{regs[i]}"
    return_inst += ';\n'

    return header + js_inst + next_line + return_inst + tail


def gen_sibgadget(gadget):
    return gen_3byte("74" + gadget)


def gen_modgadget(gadget):
    mod, reg, rm = byte_parse(int(gadget[0:2], 16))
    if mod == 0b11:
        return None

    op1 = get_reg(reg)
    if not op1:
        return None
    js_inst = ''
    if rm == 0b100:
        scale, index, base = byte_parse(int(gadget[2:4], 16))
        pow = 2 ** scale
        op2 = get_reg(index)
        if not op2:
            return None
        op3 = get_reg(base)
        if not op3:
            return None
        js_inst = f'    p_{op1} = p_{op2} * {pow} + p_{op3}'
        disp = 0xc3
        if mod == 0:
            js_inst += ";\n"
        elif mod == 1:
            js_inst += " " + hex(unsigned_convert(disp)) + ";\n"
        else:
            js_inst += " + " + hex(disp) + ";\n"
    else:
        disp = int(gadget[2:4], 16)
        op2 = get_reg(rm)
        if not op2:
            return None
        js_inst = f'    p_{op1} = p_{op2}'
        if mod == 1:
            if negative(disp):
                js_inst += " " + hex(unsigned_convert(disp)) + ";\n"
            else:
                js_inst += " + " + hex(disp) + ";\n"
        else:
            if negative(disp):
                js_inst += " + " + hex(disp) + ";\n"
            else:
                return None

    next_line = f"    let i0 = p_{op1} + 0x11;\n"
    return_inst = f"    return (i0 + p_{op1})"
    for i in range(len(regs)):
        if regs[i] != op1:
            return_inst += f" + p_{regs[i]}"
    return_inst += ';\n'

    return header + js_inst + next_line + return_inst + tail


def gen_vexgadget(gadget):
    pass


def gen_2byte(gadget):
    res = gen_modgadget(gadget)
    if res:
        return res
    res = gen_sibgadget(gadget)
    if res:
        return res


def gen_gadget(gadget):
    if len(gadget) == 6:
        res = gen_3byte(gadget)
        if res:
            return res
        else:
            return None
    elif len(gadget) == 4:
        res = gen_2byte(gadget)
        if res:
            return res
        else:
            return None


danger_ops = ['pop', 'j', 'call', 'ret', 'jmp', 'mov', 'add', 'sub',
              'inc', 'dec', 'adc', 'sbc', 'int', 'xor', 'or', 'test', 'cmp']

danger_1_codes = dict()
danger_2_codes = dict()
all_codes = dict()

if __name__ == "__main__":
    df = open('danger.txt', 'w')
    af = open('all.txt', 'w')

    for i in range(0xffff):
        iter = (i << 8) + 0xc3
        gadget = gen_gadget(hex(iter)[2:])
        if not gadget:
            continue
        length = 1
        if i > 0xff:
            length = 2
        decoder = Decoder(64, i.to_bytes(length, 'big'), ip=0x1234_5678)
        instr = decoder.decode()
        str_inst = f"{instr:f}"
        if str_inst.find("bad") != -1:
            continue
        af.write(str_inst + " " + hex(i) + '\n')
        if i > 0xff:
            all_codes[i >> 8] = str_inst
        else:
            all_codes[i] = str_inst
        for op in danger_ops:
            if str_inst.find(op) != -1:
                if i > 0xff:
                    danger_2_codes[i >> 8] = str_inst
                else:
                    danger_1_codes[i] = str_inst

                df.write(str_inst + " " + hex(i) + '\n')
                break
    df.close()
    af.close()
    print('danger_1_codes')
    for op in danger_1_codes:
        print(hex(op), danger_1_codes[op])
    print('danger_2_codes')
    for op in danger_2_codes:
        print(hex(op), danger_2_codes[op])
    print('all_codes')
    for op in all_codes:
        print(hex(op), all_codes[op])
