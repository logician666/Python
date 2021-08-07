from sys import exit

def read_int(prompt, min, max):
    while True:
        try:
            assert min <= (n := int(input(prompt))) <= max
        except ValueError:
            print("Error: wrong input"); continue
        except AssertionError:
            print("Error: the value is not within permitted range ({}..{})".format(min, max)); continue
        except KeyboardInterrupt:
            exit(0)
        return n 
    
v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

