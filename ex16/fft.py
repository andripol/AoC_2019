from itertools import cycle

base_pattern = [0, 1, 0, -1]

def input(fname):
    for line in open(fname):
        return [int(d) for d in line.strip('\n')]

def pattern_array(length):
    # for every position in the output list
    array = []
    for i in range(length):
        array.append([])
        pool = cycle(base_pattern)
        # idx in the newly calculated string
        idx = 0
        for item in pool:
            if (idx == length):
                break
            flag = True
            for times in range(i+1):
                # new string formed
                if (idx == length): break
                # drop the very first value of the pattern
                if ((idx, item) == (0,base_pattern[0]) and flag):
                    flag = False
                    continue
                array[i].append(item)
                idx+=1
    return array
                
def solve():
    in_str = input('input16b')
    length = len(in_str)
    array = pattern_array(length)
    for phase in range(100):
        res_str = []
        for i in range(len(array)):
            s = 0
            # triangular matrix 
            for j in range(i, length):
                s+=array[i][j]*in_str[j]
            number = str(abs(s))
            res_str.append(int(number[len(number) -1]))
        in_str = res_str
    print(in_str[:8])

solve()
