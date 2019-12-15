import math
# ingredient -> {(quantity, name)}
reactions = {}
quantity_quantum = {}
global remainder 
remainder = {} 

BILLION = 1000000000000

def input(fname):
    with open(fname) as f:
        for line in f:
            reaction = line.strip("\n").split(",")
            output = reaction[-1].split(" ")
            reactions[output[1]] = []
            quantity_quantum[output[1]] = int(output[0])
            remainder[output[1]] = 0
            for i in range(len(reaction) - 1):
                ingr = reaction[i].split(" ")
                reactions[output[1]].append((int(ingr[0]), ingr[1]))

def solve_rec(ingr):
    quantity = ingr[0]
    name = ingr[1]
    mul = math.ceil((quantity - remainder[name]) / quantity_quantum[name])
    remainder[name] = (mul*quantity_quantum[name] + remainder[name]) - quantity
    frontier = list(map(lambda x: (x[0]*mul, x[1]),[reactions[name][i] for i in range(len(reactions[name]))]))
    counter = 0
    for i in frontier:
        # base case
        if (i[1] == 'ORE'):
            return i[0]
        else:
            counter+=solve_rec(i)
    return counter 

def solve():
    frontier = [reactions['FUEL'][i] for i in range(len(reactions['FUEL']))]
    counter = 0
    for i in frontier:
        counter+= solve_rec(i)
    print("Needed ", counter, " ORE for 1 FUEL.")

def solve2():
    global remainder
    mul_min = 2463973
    mul_max = 4000000
    mul = math.ceil((mul_max + mul_min) / 2)
    while True:
        for i in quantity_quantum.keys():
            remainder[i] = 0
        print("mul = ", mul)
        frontier = list(map(lambda x: (x[0]*mul, x[1]),[reactions['FUEL'][i] for i in range(len(reactions['FUEL']))]))
        counter = 0
        for i in frontier:
            counter+= solve_rec(i)
        print(counter)
        if (counter < BILLION):
            mul_min = mul
            mul = math.ceil((mul_max + mul_min) / 2)
        elif (counter > BILLION):
            mul_max = mul
            mul = math.ceil((mul_max + mul_min) / 2)
        else:
            print("Needed ", counter, " ORE for ", mul, " FUEL.")
            break

input("input14")
solve()
solve2()
