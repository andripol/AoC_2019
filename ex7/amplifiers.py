from turing_machine import *
import itertools

global output
global output_list
output_list = []

def solve():
    global output, output_list
    for i in list(itertools.permutations([0,1,2,3,4])):
        setting_seq = list(i)
        output = 0
        for j in setting_seq:
            output = run(j, output)
            output_list.append(output)
    print("final result = ", max(output_list))
        
solve()
