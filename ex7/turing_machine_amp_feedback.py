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
OP_HALT = 99

POS_MODE = 0
I_MODE = 1
# dummy initialization
global INPUT_VALUE 

def add(number1, number2, idx, ip):
    program[idx] = number1 + number2
    return ip+4

def mul(number1, number2, idx, ip):
    program[idx] = number1 * number2
    return ip+4

def save_value(value, idx, ip):
    program[idx] = value
    return ip+2

def output_value(number, ip):
    print("Output = ", number)
    return [number, ip+2]

def jump_if_true(flag, value, ip):
    if (flag != 0): return value
    return ip+3

def jump_if_false(flag, value, ip):
    if (flag == 0): return value
    return ip+3

def less_than(param1, param2, idx, ip):
    if (param1 < param2): program[idx] = 1
    else: program[idx] = 0
    return ip+4

def equals(param1, param2, idx, ip):
    if (param1 == param2): program[idx] = 1
    else: program[idx] = 0
    return ip+4

def command_and_modes(cmd):
    abcde = ['0','0','0','0','0']
    for i in cmd:
        abcde.pop(0)
        abcde.append(i)
    return [list(map(int,abcde[0:3])), int(abcde[-2] + abcde[-1])]

def mode_val(value, mode):
    if mode == POS_MODE: return (program[value])
    return value

def execute_program(inputs, prog_mem, prog_ip):
    global INPUT_VALUE, program
    program = prog_mem
    ip = prog_ip 
    INPUT_VALUE = inputs.pop()
    if (INPUT_VALUE < 0): INPUT_VALUE = inputs.pop()
    while ip < len(program):
        [abc, cmd] = command_and_modes(str(program[ip])) 
        if (cmd == OP_ADD):
            ip = add(mode_val(program[ip+1], abc[-1]), mode_val(program[ip+2], abc[-2]), program[ip+3], ip)
        elif (cmd == OP_MUL):
            ip = mul(mode_val(program[ip+1], abc[-1]), mode_val(program[ip+2], abc[-2]), program[ip+3], ip)
        elif(cmd == OP_IN):
            # always position mode
            ip = save_value(INPUT_VALUE, program[ip+1], ip)
            if (len(inputs) > 0): INPUT_VALUE = inputs.pop()
        elif (cmd == OP_OUT):
            [result, ip] = output_value(mode_val(program[ip+1], abc[-1]), ip)
            return [result, program, ip]
        elif (cmd == OP_JT):
            ip = jump_if_true(mode_val(program[ip+1], abc[-1]), mode_val(program[ip+2], abc[-2]), ip)
        elif (cmd == OP_JF):
            ip = jump_if_false(mode_val(program[ip+1], abc[-1]), mode_val(program[ip+2], abc[-2]), ip)
        elif (cmd == OP_LT):
            ip = less_than(mode_val(program[ip+1], abc[-1]), mode_val(program[ip+2], abc[-2]), program[ip+3], ip)
        elif (cmd == OP_EQ):
            ip = equals(mode_val(program[ip+1], abc[-1]), mode_val(program[ip+2], abc[-2]), program[ip+3], ip)
        elif (cmd == OP_HALT):
            break
        else:
            print("Something went wrong, no such cmd exists. Command =  ", cmd)
    # return values < 0 if program has halted
    return [-1, [], -1]

# phase_value < 0 when it will not be used! e.g. amplifiers with feedback
def run(prog_mem, prog_ip, input_value, phase_value):
    #print(input_value, phase_value)
    return execute_program([input_value, phase_value], prog_mem, prog_ip)

def main():
    run(0, 2)

if __name__ == '__main__':
    main()
