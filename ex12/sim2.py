import re
import math
global position, velocity, initial_position

STEPS = 100000000

def input(fname):
    global position, velocity, initial_position
    velocity = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
    with open(fname) as f:
        position = [list(map(int,re.findall('-*\d+', line))) for line in f.readlines()]
    initial_position = position

def apply_gravity(idx1, idx2, axis):
    if position[idx1][axis] < position[idx2][axis]:
        velocity[idx1][axis]+=1
        velocity[idx2][axis]-=1
    elif position[idx1][axis] > position[idx2][axis]:
        velocity[idx1][axis]-=1
        velocity[idx2][axis]+=1

def apply_velocity(idx):
    position[idx] = [sum(i) for i in zip(position[idx], velocity[idx])]

def axis_repetition(axis):
        if (position[0][axis] == initial_position[0][axis] and position[1][axis] == initial_position[1][axis] and position[2][axis] == initial_position[2][axis] and position[3][axis] == initial_position[3][axis] and velocity[0][axis] == 0 and velocity[1][axis] == 0 and velocity[2][axis] == 0 and velocity[3][axis] ==0):
            return True
        return False

def lcm(a, b):
    return int((int(a*b))/math.gcd(a,b))

def solve():
    num_x, num_y, num_z = 0, 0, 0
    for step in range(0, STEPS):
        if (num_x*num_y*num_z > 0):
            print(num_x, num_y, num_z)
            break
        for i in range(0, len(position)):
            for j in range (i+1, len(position)):
                for axis in range(0,3):
                    apply_gravity(i, j, axis)
            apply_velocity(i)
        if (axis_repetition(0)): num_x = step+1
        if (axis_repetition(1)): num_y = step+1
        if (axis_repetition(2)): num_z = step+1

    print("x: ", num_x, ", y: ", num_y, ", z: ", num_z)
    print("Steps needed in total = ", lcm(num_x, lcm(num_y ,num_z)))

input('input12')
solve()
