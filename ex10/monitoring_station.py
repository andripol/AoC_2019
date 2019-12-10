ast_map = []
counter = []
 
station = [11, 11]

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

def norm(point, ref):
    return [point[0] - ref[0], point[1] - ref[1]]

def solve2(lst):
    lst1, lst2, lst3, lst4 = [],[],[],[]
    for i in lst:
        if (i[1][0] >= 0):
            if (i[1][1] < 0):
                lst1.append(i)
            else:
                lst2.append(i)
        else:
            if (i[1][1] > 0):
                lst3.append(i)
            else:
                lst4.append(i)
    lst1.sort(key = lambda x:  x[1][0]/abs(x[1][1]) if x[1][1] != 0 else float('Inf'))
    lst2.sort(key = lambda x:  x[1][1]/x[1][0] if x[1][0] != 0 else float('Inf'))
    lst3.sort(key = lambda x:  abs(x[1][0])/x[1][1] if x[1][1] != 0 else float('Inf'))
    lst4.sort(key = lambda x:  x[1][1]/x[1][0] if x[1][0] != 0 else float('Inf'))

    return(lst4[-22][0])

def solve():
    my_list = []
    for aster1 in range(len(ast_map)):
        for aster2 in range(aster1 + 1, len(ast_map)):
            if (see_each_other(aster1, aster2)):
                counter[aster1]+=1
                counter[aster2]+=1
                if (ast_map[aster1] == station): my_list.append((aster2, norm(ast_map[aster2], station)))
                if (ast_map[aster2] == station): my_list.append((aster1, norm(ast_map[aster1], station)))

    max_idx = counter.index(max(counter))
    print("Sation built at: ", ast_map[max_idx], "sees ", max(counter), "asteroidds")
    idx = solve2(my_list)
    print("Solution= ", ast_map[idx][0]*100 + ast_map[idx][1])

input('input10')
solve()
