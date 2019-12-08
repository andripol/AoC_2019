global layers
layers = []
WIDTH = 25
HIGHT = 6

def input(fname):
    global layers
    with open(fname) as f:
        line = f.readlines()[0].strip('\n')
        pixels = []
        for i in range(len(line)):
            pixels.append(int(line[i]))
        it = iter(pixels)
        l = 0
        while True:
            layers.append([])
            for i in range(0, HIGHT):
                for j in range(0, WIDTH):
                    pixel = next(it, -1)
                    if (pixel < 0): 
                        layers.pop()
                        return
                    layers[l].append(pixel)
            l = l + 1

def solve():
    #min_zeors[count, layer_idx]
    min_zeros = [float('Inf'), -1]
    for i in range(len(layers)):
        if layers[i].count(0) < min_zeros[0]:
            min_zeros = [layers[i].count(0), i]
    print((layers[min_zeros[1]].count(1)*layers[min_zeros[1]].count(2)))

def solve2():
    final_layer = []
    for i in range(0, HIGHT):
        for j in range(0, WIDTH):
            final_layer.append(-1)

    for i in range(len(layers)):
        for j in range(len(layers[i])):
            if (final_layer[j] < 0) and (layers[i][j] < 2):
                final_layer[j] = layers[i][j]

    for i in range(0, HIGHT):
        print()
        for j in range(0, WIDTH):
            if (final_layer[i*WIDTH + j] == 0): print(' ', end='') 
            else: print(final_layer[i*WIDTH + j], end='')
    print()

input('input8')
solve()
solve2()
