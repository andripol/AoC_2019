import re
global position, velocity

STEPS = 1000

def input(fname):
    global position, velocity
    velocity = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
    with open(fname) as f:
        position = [list(map(int,re.findall('-*\d+', line))) for line in f.readlines()]

def apply_gravity(idx1, idx2, axis):
    if position[idx1][axis] < position[idx2][axis]:
        velocity[idx1][axis]+=1
        velocity[idx2][axis]-=1
    elif position[idx1][axis] > position[idx2][axis]:
        velocity[idx1][axis]-=1
        velocity[idx2][axis]+=1

def apply_velocity(idx):
    position[idx] = [sum(i) for i in zip(position[idx], velocity[idx])]

def solve():
    for step in range(0, STEPS):
        for i in range(0, len(position)):
            for j in range (i+1, len(position)):
                for axis in range(0,3):
                    apply_gravity(i, j, axis)
            apply_velocity(i)

    potential = [sum(list(map(abs,(position[i])))) for i in range(len(position))]
    kinetic = [sum(list(map(abs,(velocity[i])))) for i in range(len(velocity))]
    print("Total: ", sum(potential[i] * kinetic[i] for i in range(len(potential))))

input('input12')
solve()
