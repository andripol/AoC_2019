import sys

global program;
program = []
# panel_map = {(x,y): tile_id}
panel_map = {}

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
            ip = save_value(in_value, mode_val_p(program[ip+1], abc[-1]), ip)
            return ([-2,-2], ip)
        elif (cmd == OP_OUT):
            value, ip = output_value(mode_val(program[ip+1], abc[-1]), ip)
            outputs.append(value)            
            if len(outputs) == 3:
                return(outputs, ip)
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

def solve():
    # initialize
    ip = 0
    counter = 0
    while True:
        values, ip = execute_program(ip, 0)
        if (ip < 0):
            break
        panel_map[(values[0], values[1])] = values[2]
        if values[2] == 2: counter+=1
    print("Number of block tiles: ", counter )

def play():
    # now play!
    # play for free
    score = 0
    ip = 0
    in_value = 0
    program[0] = 2
    player_map = {} 
    player_map[4] = (0,0)
    prev_bal_pos = [0,0]
    while True:
        print("in_value= ", in_value)
        values, ip = execute_program(ip, in_value)
        if (ip < 0):
            break
        if (values == [-1,0]):
            score = values[2]
            print(score)
        if (values == [-2,-2]):
            show_panel(score, panel_map)
            # uncomment to play online!
            #for line in sys.stdin:
            #    in_value = int(line)
            #    break
            # going upwards
            if (prev_bal_pos[1] < player_map[4][1]):
                if (player_map[3][0] < player_map[4][0]):
                    in_value = -1
                elif (player_map[3][0] > player_map[4][0]): in_value = 1
                else: in_value = 0
            else:
                # ball goes downwards left
                if (prev_bal_pos[0] < player_map[4][0]):
                    if (player_map[3][0] > player_map[4][0]) - abs(player_map[4][1] - player_map[3][1] - 1):
                        in_value = -1
                    elif (player_map[3][0] < player_map[4][0]) - abs(player_map[4][1] - player_map[3][1] - 1): in_value = 1
                    else: in_value = 0
                # ball goes downwards right 
                else:
                    if (player_map[3][0] > player_map[4][0]) + abs(player_map[4][1] - player_map[3][1] - 1):
                        in_value = -1
                    elif (player_map[3][0] < player_map[4][0]) + abs(player_map[4][1] - player_map[3][1] - 1): in_value = 1
                    else: in_value = 0
        else:
            panel_map[(values[0], values[1])] = values[2]
            # paddle
            if values[2] == 3:
                player_map[3] = values
                # ball
            if values[2] == 4:
                prev_bal_pos = player_map[4]
                player_map[4] = values


def show_panel(score, panel_map):
    #part 2
    print("SCORE: ", score)
    print()
    min_x = min(key[0] for key in panel_map.keys())
    max_x = max(key[0] for key in panel_map.keys())
    min_y = min(key[1] for key in panel_map.keys())
    max_y = max(key[1] for key in panel_map.keys())
    for j in range(min_y, max_y + 1):
        for i in range(min_x, max_x + 1):
            if (i,j) in panel_map.keys():
                if panel_map[(i,j)] == 1:
                    print('|', end = '')
                elif panel_map[(i,j)] == 2:
                    print('*', end = '')
                elif panel_map[(i,j)] == 3:
                    print('_', end = '')
                elif panel_map[(i,j)] == 4:
                    print('O', end = '')
                else:
                    print(' ', end='')
            else:
                print(' ', end = '')
        print()
    print()

input_to_array('input13')
solve()
play()
