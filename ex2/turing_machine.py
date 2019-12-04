global turing_array;

def read_input_into_array():
    global turing_array
    turing_array = [] 
    with open("input2") as f:
        for line in f:
            for x in line.split(','):
                turing_array.append(int(x)) 

def restore_gravity_assist_program(value1, value2):
    global turing_array
    turing_array[1] = value1
    turing_array[2] = value2 

def add_and_save(number1, number2, save_pos):
    global turing_array
    turing_array[save_pos] = number1 + number2

def mul_and_save(number1, number2, save_pos):
    global turing_array
    turing_array[save_pos] = number1 * number2

def execute_program():
    global turing_array
    for x in range(0, len(turing_array), 4):
        command = int(turing_array[x])
        if (command == 1):
            add_and_save(turing_array[turing_array[x + 1]], turing_array[turing_array[x + 2]], turing_array[x + 3])
        elif (command == 2):
            mul_and_save(turing_array[turing_array[x + 1]], turing_array[turing_array[x + 2]], turing_array[x + 3])
        elif (command == 99):
            break
        else:
            print("Something went really wrong...", command)
    return

def initialize_and_execute(value1, value2):
    global turing_array
    read_input_into_array()
    restore_gravity_assist_program(value1, value2)
    execute_program()
    #print(turing_array[0])
    return(turing_array[0])


def main():
    initialize_and_execute(12, 2)

if __name__ == "__main__":
    main()
