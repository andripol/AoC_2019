from itertools import cycle

base_pattern = [0, 1, 0, -1]

def input(fname):
    input_string = []
    with open(fname) as f:
        for line in f:
            input_string = [int(d) for d in line.strip('\n')]
    return input_string

def phase(in_str):
    res_str = []
    # for every position in the output list
    for i in range(len(in_str)):
        pool = cycle(base_pattern)
        # idx in the newly calculated string
        idx = 0
        sum = 0
        for item in pool:
            if (idx == len(in_str)):
                break
            flag = True
            for times in range(i+1):
                if (idx == len(in_str)):
                    break
                # drop the very first value of the pattern
                if ((idx, item) == (0,base_pattern[0]) and flag):
                    flag = False
                    continue
                sum+=in_str[idx]*item
                idx+=1
        number = str(abs(sum))
        res_str.append(int(number[len(number) -1]))
    return res_str
                
def solve():
    in_str = input('input16')
    for i in range(100):
        in_str = phase(in_str)
    print(in_str[:8])

solve()
