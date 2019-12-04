global wire1_map
global wire2_map
# each wire's route is a list of pairs (consecutive (x,y) points)
# source is the point of reference and the very first point of each wire
wire1_map = [(0, 0)]
wire2_map = [(0, 0)]

def add_in_mapping(orientation, steps, wire_map):

    # previous point's horizontal and vertical (x,y) values
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

def get_input_and_map():
    with open("input3") as f:
        array = [[x for x in line.split(',')] for line in f]
    open_wire_up(array[0], wire1_map)
    open_wire_up(array[1], wire2_map)

def check_for_point_in_range(point, vertice1, vertice2):
    if (vertice1 >= point and vertice2 <= point) or (vertice1 <= point and vertice2 >= point):
        return True
    return False

def find_nearest_connection():
    min_connection_distance = float('Inf')
    for index2 in range(0, len(wire2_map) - 1, 1):
        # vertices of wire2's current edge
        point21 = wire2_map[index2]
        point22 = wire2_map[index2+1]
        for index1 in range(0, len(wire1_map) - 1, 1):
            # vertices of wire1's current edge
            point11 = wire1_map[index1]
            point12 = wire1_map[index1+1]
            # same horizontal value -> vertical line for wire2
            if (point21[0] == point22[0]):
                if check_for_point_in_range(point21[0], point11[0], point12[0]):
                    if check_for_point_in_range(point11[1], point21[1], point22[1]):
                        manh_dist = point21[0] + point11[1] 
            # horizontal line for wire2
            else:
                if check_for_point_in_range(point21[1], point11[1], point12[1]):
                    if check_for_point_in_range(point11[0], point21[0], point22[0]):
                        manh_dist = point21[1] + point11[0] 
            
            if (manh_dist < min_connection_distance) and (manh_dist > 0):
                min_connection_distance = manh_dist 
    print(min_connection_distance)

def main():
    get_input_and_map()
    find_nearest_connection()

if __name__ == "__main__":
    main()
