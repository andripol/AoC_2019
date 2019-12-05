global wire1_map
global wire2_map
# each wire's route is a list of pairs (consecutive points)
wire1_map = [(0, 0)]
wire2_map = [(0, 0)]

def add_in_mapping(orientation, steps, wire_map):

    prev_h = wire_map[len(wire_map)-1][0]
    prev_v = wire_map[len(wire_map)-1][1]

    if (orientation == 'R'):
        wire_map.append((prev_h + steps, prev_v)) 
    elif orientation == 'L':
        wire_map.append((prev_h - steps, prev_v)) 
    elif orientation == 'U':
        wire_map.append((prev_h, prev_v + steps)) 
    elif orientation == 'D':
        wire_map.append((prev_h, prev_v - steps)) 

def open_wire_up(wire, wire_map):
    for i in wire:
        orientation = i[0]
        steps = int(i[1:len(i)])
        add_in_mapping(orientation, steps, wire_map)

def get_input():
    with open("input3") as f:
        array = [[x for x in line.split(',')] for line in f]
    open_wire_up(array[0], wire1_map)
    open_wire_up(array[1], wire2_map)


def point_in_range(point, vertice1, vertice2):
    if (vertice1 >= point and vertice2 <= point) or (vertice1 <= point and vertice2 >= point):
        return True
    return False

def manhattan_dist(point1, point2):
    return (abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]))

def find_nearest_connection():
    wire1_dist = 0
    wire2_dist = 0
    min_total_wires_dist = float('Inf')

    for idx2 in range(0, len(wire2_map) - 1, 1):
        point21 = wire2_map[idx2]
        point22 = wire2_map[idx2+1]
        wire1_dist = 0
        for idx1 in range(0, len(wire1_map) - 1, 1):
            point11 = wire1_map[idx1]
            point12 = wire1_map[idx1+1]
            #same horizontal value -> vertical line
            if (point21[0] == point22[0]):
                if point_in_range(point21[0], point11[0], point12[0]):
                    if point_in_range(point11[1], point21[1], point22[1]):
                        total_dist_temp = wire1_dist + wire2_dist + manhattan_dist(point11, point21)            
            else:
                if point_in_range(point21[1], point11[1], point12[1]):
                    if point_in_range(point11[0], point21[0], point22[0]):
                        total_dist_temp = wire1_dist + wire2_dist + manhattan_dist(point11, point21)            

            if ((total_dist_temp) < min_total_wires_dist) and total_dist_temp > 0:
                min_total_wires_dist = total_dist_temp
            #update wire's dist so far
            wire1_dist+=abs(point11[0] - point12[0]) + abs(point12[1] - point11[1]) 
        wire2_dist+=abs(point22[0] - point21[0])  + abs(point21[1] - point22[1])
    print(min_total_wires_dist)


def main():
    get_input()
    find_nearest_connection()

if __name__ == "__main__":
    main()
