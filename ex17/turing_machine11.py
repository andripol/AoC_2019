global program;
program = []

OP_ADD = 1
OP_MUL = 2
OP_IN = 3
OP_OUT = 4
OP_JT = 5
OP_JF = 6
OP_LT = 7
OP_EQ = 8
OP_REL = 9
OP_HALT = 99

POS_MODE = 0
I_MODE = 1
REL_MODE = 2
global RELATIVE_BASE 
RELATIVE_BASE = 0


def input_to_array(fname):
    with open(fname) as f:
        for line in f:
            for x in line.split(','): program.append(int(x)) 

def adjust_mem_length(idx):
    last_progr_idx = len(program) - 1
    if idx > last_progr_idx:
        for i in range(last_progr_idx, idx):
            program.append(0)

def add(number1, number2, idx, ip):
    adjust_mem_length(idx)
    program[idx] = number1 + number2
    return ip+4

def mul(number1, number2, idx, ip):
    adjust_mem_length(idx)
    program[idx] = number1 * number2
    return ip+4

def save_value(value, idx, ip):
    adjust_mem_length(idx)
    program[idx] = value
    return ip+2

def output_value(number, ip):
    #print("Output = ", number)
    return number, ip+2

def jump_if_true(flag, value, ip):
    if (flag != 0): 
        return value
    return ip+3

def jump_if_false(flag, value, ip):
    if (flag == 0): return value
    return ip+3

def less_than(param1, param2, idx, ip):
    adjust_mem_length(idx)
    if (param1 < param2): program[idx] = 1
    else: program[idx] = 0
    return ip+4

def equals(param1, param2, idx, ip):
    adjust_mem_length(idx)
    if (param1 == param2): program[idx] = 1
    else: program[idx] = 0
    return ip+4

def adjust_rel_base(value, ip):
    global RELATIVE_BASE
    RELATIVE_BASE+=value
    return ip+2

def command_and_modes(cmd):
    abcde = ['0','0','0','0','0']
    for i in cmd:
        abcde.pop(0)
        abcde.append(i)
    return [list(map(int,abcde[0:3])), int(abcde[-2] + abcde[-1])]

def mode_val(value, mode):
    if mode == POS_MODE: 
        adjust_mem_length(value)
        return program[value]
    if mode == REL_MODE: 
        return program[value + RELATIVE_BASE]
    return value

def mode_val_p(value, mode):
    if mode == REL_MODE: 
        return value + RELATIVE_BASE
    return value

def execute_program(ip, in_value):
    outputs = []
    while ip < len(program):
        [abc, cmd] = command_and_modes(str(program[ip])) 
        if (cmd == OP_ADD):
            ip = add(mode_val(program[ip+1], abc[-1]), mode_val(program[ip+2], abc[-2]), mode_val_p(program[ip+3], abc[-3]), ip)
        elif (cmd == OP_MUL):
            ip = mul(mode_val(program[ip+1], abc[-1]), mode_val(program[ip+2], abc[-2]), mode_val_p(program[ip+3], abc[-3]), ip)
        elif(cmd == OP_IN):
            # always position mode
            ip = save_value(in_value, mode_val_p(program[ip+1], abc[-1]), ip)
        elif (cmd == OP_OUT):
            value, ip = output_value(mode_val(program[ip+1], abc[-1]), ip)
            return(value, ip)
        elif (cmd == OP_JT):
            ip = jump_if_true(mode_val(program[ip+1], abc[-1]), mode_val(program[ip+2], abc[-2]), ip)
        elif (cmd == OP_JF):
            ip = jump_if_false(mode_val(program[ip+1], abc[-1]), mode_val(program[ip+2], abc[-2]), ip)
        elif (cmd == OP_LT):
            ip = less_than(mode_val(program[ip+1], abc[-1]), mode_val(program[ip+2], abc[-2]), mode_val_p(program[ip+3], abc[-3]), ip)
        elif (cmd == OP_EQ):
            ip = equals(mode_val(program[ip+1], abc[-1]), mode_val(program[ip+2], abc[-2]), mode_val_p(program[ip+3], abc[-3]), ip)
        elif (cmd == OP_REL):
            ip = adjust_rel_base(mode_val(program[ip+1], abc[-1]), ip)
        elif (cmd == OP_HALT):
            return ([-1, -1], -1)
        else:
            print("Something went wrong, no such cmd exists. Command =  ", cmd)
            exit()
    return

def move(cur_pos, direction, step):
    # move left
    if (step == 0):
        if (direction == '^'):
            new_dir = '<'
            new_pos = (cur_pos[0]-1, cur_pos[1])
        if (direction == '<'):
            new_dir = 'v'
            new_pos = (cur_pos[0], cur_pos[1] + 1)
        if (direction == 'v'):
            new_dir = '>'
            new_pos = (cur_pos[0] + 1, cur_pos[1])
        if (direction == '>'):
            new_dir = '^'
            new_pos = (cur_pos[0], cur_pos[1] - 1)
    # move right
    else:
        if (direction == '^'):
            new_dir = '>'
            new_pos = (cur_pos[0] + 1, cur_pos[1])
        if (direction == '>'):
            new_dir = 'v'
            new_pos = (cur_pos[0], cur_pos[1] + 1)
        if (direction == 'v'):
            new_dir = '<'
            new_pos = (cur_pos[0] - 1, cur_pos[1])
        if (direction == '<'):
            new_dir = '^'
            new_pos = (cur_pos[0], cur_pos[1] - 1)
    return new_pos, new_dir

def translate_ascii(code):
    if (code == 94):
        return '^'
    if code == 60:
        return '<'
    if code == 62:
        return '>'
    if code == 118:
        return 'v'
    if code == 88:
        return 'X'
    if code == 35:
        return '#'
    if code == 46:
        return '.'
    if code == 10:
        return '\n'

def solve():
    panel_map = {}
    # initialize point of reference with black colour
    ip, x, y = 0, -1, 0
    while True:
        output, ip = execute_program(ip, 0)
        code = translate_ascii(output)
        if (ip < 0):
            break
        if (code == '\n'):
            y-=1
            x = -1
        else:
            x = x + 1
            panel_map[(x, y)] = code 

    #part 2
    s = 0
    min_x = min(key[0] for key in panel_map.keys())
    max_x = max(key[0] for key in panel_map.keys())
    min_y = min(key[1] for key in panel_map.keys())
    max_y = max(key[1] for key in panel_map.keys())
    print("Xs: ", min_x, max_x)
    print("Ys: ", min_y, max_y)
    for j in range(min_y, max_y + 1):
        for i in range(min_x, max_x + 1):
            if (i,j) in panel_map.keys():
                print(panel_map[(i,j)], end = '')
                if (panel_map[(i,j)] == '#'):
                    if ((i-1,j) in panel_map.keys() and (i+1,j) in panel_map.keys() and (i,j-1) in panel_map.keys()  and (i,j+1) in panel_map.keys()):
                        if (panel_map[(i-1,j)] == '#' and panel_map[(i+1, j)] == '#' and panel_map[(i, j-1)] == '#' and panel_map[(i, j+1)] == '#'):
                                print(abs(max_x - i), abs(max_y - j))
                                s+=abs(i)*abs(max_y - j)
            else:
                print(' ', end = '')
        print()
    print(s)

input_to_array('input17')
solve()
