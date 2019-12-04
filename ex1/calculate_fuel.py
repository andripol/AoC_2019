def calculate_individual_fuel(mass):
    result = (int(mass/3 - 2))
    if (result <= 0):
        return 0 
    else:
        return (result + calculate_individual_fuel(result))

def calculate_fuel():
    sum = 0
    with open('input') as f:
        for line in f:
            for x in line.split():
                mass = int(x) 
                sum = sum + calculate_individual_fuel(mass)
        print(sum)

def main():
    calculate_fuel()


if __name__ == "__main__":
    main()
