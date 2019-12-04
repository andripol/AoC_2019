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


def check_for_point_in_range(point, vertice1, vertice2):
    if (vertice1 >= point and vertice2 <= point) or (vertice1 <= point and vertice2 >= point):
        return True
    return False

def find_nearest_connection():
    #min_con_point_dist = float('Inf')
    wire1_distance = 0
    wire2_distance = 0
    min_aggregate_wires_distance = float('Inf')

    for index2 in range(0, len(wire2_map) - 1, 1):
        point21 = wire2_map[index2]
        point22 = wire2_map[index2+1]
        wire1_distance = 0
        for index1 in range(0, len(wire1_map) - 1, 1):
            point11 = wire1_map[index1]
            point12 = wire1_map[index1+1]
            #same horizontal value -> vertical line
            if (point21[0] == point22[0]):
                if check_for_point_in_range(point21[0], point11[0], point12[0]):
                    if check_for_point_in_range(point11[1], point21[1], point22[1]):
                        aggregate_dist_temp = wire1_distance + abs(point21[0] - point11[0]) + wire2_distance + abs(point21[1] - point11[1])
            else:
                if check_for_point_in_range(point21[1], point11[1], point12[1]):
                    if check_for_point_in_range(point11[0], point21[0], point22[0]):
                        aggregate_dist_temp = wire1_distance + abs(point21[1] - point11[1]) + wire2_distance + abs(point21[0] - point11[0])

            if ((aggregate_dist_temp) < min_aggregate_wires_distance) and aggregate_dist_temp > 0:
                min_aggregate_wires_distance = aggregate_dist_temp
            #update wire's distance so far
            wire1_distance+=abs(point11[0] - point12[0]) + abs(point12[1] - point11[1]) 
        wire2_distance+=abs(point22[0] - point21[0])  + abs(point21[1] - point22[1])
    print(min_aggregate_wires_distance)


def main():
    get_input()
    find_nearest_connection()

if __name__ == "__main__":
    main()
