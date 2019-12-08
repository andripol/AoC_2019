global layers
layers = []
WIDTH = 25
HEIGHT = 6

def input(fname):
    with open(fname) as f:
        line = f.readlines()[0].strip('\n')
        for l in range(int(len(line)/(WIDTH*HEIGHT))):
            layers.append([])
            offset = l*WIDTH*HEIGHT
            for i in range(0, HEIGHT):
                for j in range(0, WIDTH):
                    idx = offset + i*WIDTH + j
                    layers[l].append(int(line[idx]))

def solve():
    #min_zeros[count, layer_idx]
    min_zeros = [float('Inf'), -1]
    for i in range(len(layers)):
        if layers[i].count(0) < min_zeros[0]:
            min_zeros = [layers[i].count(0), i]
    print((layers[min_zeros[1]].count(1)*layers[min_zeros[1]].count(2)))

def solve2():
    final_layer = [-1]*HEIGHT*WIDTH

    for i in range(len(layers)):
        for j in range(len(layers[i])):
            if (final_layer[j] < 0) and (layers[i][j] < 2):
                final_layer[j] = layers[i][j]

    for i in range(0, HEIGHT):
        print()
        for j in range(0, WIDTH):
            if (final_layer[i*WIDTH + j] == 0): print(' ', end='') 
            else: print(final_layer[i*WIDTH + j], end='')
    print()

input('input8')
solve()
solve2()
