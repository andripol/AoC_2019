from scipy.spatial import distance

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

def dist(astro1, astro2):
    return distance.euclidean((astro1[0], astro1[1]), (astro2[0], astro2[1]))
    

def see_each_other(idx1, idx2):
    astro1 = ast_map[idx1]
    astro2 = ast_map[idx2]
    dist12 = dist(astro1, astro2)
    if (astro2[0] - astro1[0]) != 0:
        A = (astro2[1] - astro1[1])/(astro2[0] - astro1[0])
        B = -A*astro1[0] + astro1[1]
        for i in range(idx1+1, len(ast_map)):
            astro_tmp = ast_map[i]
            if (astro_tmp[1] == A*astro_tmp[0] + B):
                if dist(astro1, astro_tmp) < dist12:
                    return False
        return True
    else:
        x_const = astro1[0]
        for i in range(idx1+1, len(ast_map)):
            astro_tmp = ast_map[i]
            if (astro_tmp[0] == x_const):
                if dist(astro1, astro_tmp) < dist12:
                    return False
        return True


def solve():
    for astro1 in range(len(ast_map)):
        for astro2 in range(astro1 + 1, len(ast_map)):
            if (see_each_other(astro1, astro2)):
                counter[astro1]+=1
                counter[astro2]+=1
    print(counter)
    print("Asteroid locating in: ", ast_map[max(counter)], "sees ", max(counter))

input('input10')
#input('test1')
solve()
