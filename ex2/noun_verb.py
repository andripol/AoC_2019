from turing_machine import initialize_and_execute

WANTED_RESULT = 19690720

def search_and_output():
    for noun in range (0,99):
        for verb in range (0,99):
            result = initialize_and_execute(noun, verb)
            if (result == WANTED_RESULT):
                print("noun = ", noun, " verb = ", verb)
                print("Result = ", 100*noun + verb)
                return

def main():
    search_and_output()

if __name__ == "__main__":
    main()
