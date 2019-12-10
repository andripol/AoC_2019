ast_map = []
counter = []
 
def input(fname):
    with open(fname) as f:
        y = 0
        for line in f:
            for x in range(len(line)):
                if (line[x] == '#'): 
                    ast_map.append([x,y])
                    counter.append(0)
            y+=1
            
def see_each_other(idx1, idx2):
    aster1, aster2 = ast_map[idx1], ast_map[idx2]
    if (aster2[0] != aster1[0]):
        # y = Ax + B
        A = (aster2[1] - aster1[1])/(aster2[0] - aster1[0])
        B = -A*aster1[0] + aster1[1]
        for i in range(idx1+1, idx2):
            if abs((ast_map[i][1] - A*ast_map[i][0] - B)) <= 0.00000001 : return False
        return True
    for i in range(idx1+1, idx2):
        if ast_map[i][0] == aster1[0]: return False
    return True

def solve():
    my_list = []
    for aster1 in range(len(ast_map)):
        for aster2 in range(aster1 + 1, len(ast_map)):
            if (see_each_other(aster1, aster2)):
                counter[aster1]+=1
                counter[aster2]+=1

    max_idx = counter.index(max(counter))
    print("Asteroid located in: ", ast_map[max_idx], "sees ", max(counter))

input('input10')
solve()
