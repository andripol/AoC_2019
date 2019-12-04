def calculate_individual_fuel(mass):
    result = (int(mass/3 - 2))
    if (result <= 0): return 0 
    else:
        return (result + calculate_individual_fuel(result))

def calculate_fuel():
    masses = []
    with open('input') as f:
        for x in f.readlines():
            masses.append(int(x)) 
    result = sum(map(calculate_individual_fuel, masses))
    print("Total fuel:", result)

calculate_fuel()
