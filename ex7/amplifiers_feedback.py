from turing_machine_amp_feedback import *
import itertools

global output
global output_list
global initial_program_mem
initial_program_mem = []
output_list = []

global ampl_mems
ampl_mems = [[],[],[],[],[]]
global ampl_ips
ampl_ips = []

def input_to_array(fname):
    with open(fname) as f:
        for line in f:
            for x in line.split(','): initial_program_mem.append(int(x))

def solve():
    global output, output_list
    for i in list(itertools.permutations([5,6,7,8,9])):
        setting_seq = list(i)
        # initialization
        ampl_ips = []
        for j in range(0,5):
            ampl_mems[j] = initial_program_mem[:]
            ampl_ips.append(0)
        # initial input of ampl A
        output = 0
        for j in range(0,5):
            [output, ampl_mems[j], ampl_ips[j]] = run(ampl_mems[j], ampl_ips[j], output, setting_seq[j])
            output_list.append(output)
        while (output >= 0):
            for j in range(0,5):
                [output, ampl_mems[j], ampl_ips[j]] = run(ampl_mems[j], ampl_ips[j], output, -1)
                output_list.append(output)

    print("final result = ", max(output_list))
        
input_to_array('input7')
solve()
