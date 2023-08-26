from capstone import *
import sys

begin = "real instructions begin"
end = "end"  # empty line


def ljust_hex(hex_number, width):
    """
    在十六進位數字前面補充 0。

    Args:
      hex_number: 十六進位數字。
      width: 十六進位數字的寬度。

    Returns:
      十六進位數字，前面補充了 0 以達到指定的寬度。
    """

    hex_string = hex(hex_number).lstrip('0x')
    while len(hex_string) < width:
        hex_string = '0' + hex_string

    return hex_string


def byte_parse_rm(byte):
    # return modrm or scale
    rm = byte & 7
    byte >>= 3
    byte >>= 3
    return rm


danger1 = {
    0x58,
    0x59,
    0x5a,
    0x5b,
    0x5c,
    0x5e,
    0x5f,
    0xa4,
    0xa6,
    0xa7,
    # 0xc3,
    0xcc,
    0xf1,
}

danger2 = {
    0x74,
    0x7c,
    0x84,
    0x8c,
    0xa4,
    0xb4,
}


def instr2gadget(modrm, line, rm):
    begin = 0
    while begin < len(line):
        if line[begin:begin + 2] == modrm:
            if rm == 4:
                return line[begin:begin + 6]
            else:
                return line[begin:begin + 4]

        begin += 2


def check3(gadget):
    # if int(gadget[0:2], 16) in danger2 and int(gadget[4:6], 16) == 0xc3:
    if int(gadget[0:2], 16) in danger2:
        return True


def check2(gadget):
    # if int(gadget[0:2], 16) in danger1 and int(gadget[2:4], 16) == 0xc3:
    if int(gadget[0:2], 16) in danger1:
        return True


def process_line(line):
    components = line.split()
    if len(components) < 4:
        return
    inst = line.split()[2]
    try:
        inst_hex = int(inst, 16)
    except ValueError:
        return
    modrm_byte = 0
    for instr in md.disasm(inst_hex.to_bytes(len(inst) // 2, 'big'),
                           0x1234_5678):
        if instr.modrm:
            modrm_byte = instr.modrm
            break

    if modrm_byte == 0:
        return

    # check gadget from modrm byte
    # if rm == 0b100: check danger2 else check danger1
    # if rm == 0b100: sib also check danger1
    rm = byte_parse_rm(modrm_byte)
    inst = instr2gadget(ljust_hex(modrm_byte, 2), inst, rm)
    # 直接检查code 吧，不要载disasm了
    if rm == 4:
        if len(inst) < 4:
            return
        if check2(inst) or check3(inst):
            print(line, inst)
        inst = inst[2:]
    if len(inst) < 4:
        return
    if check2(inst):
        print(line, inst)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 checkoptcode.py <file>")
        exit(1)

    f = open(sys.argv[1])
    going = False
    lines = f.readlines()
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    md.detail = True
    i = 0
    while i < len(lines):
        line = lines[i]
        if not going and begin in line:
            i += 2
            going = True
            continue
        if going and end in line:
            going = False
            i += 2
            continue
        if going:
            process_line(line)
        i += 1
