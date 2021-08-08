from re import I
from sys import exit

def digit_of_life(s):
    while len(s) > 1:
        s = str(sum([int(d) for d in s]))
    return s

try:
    while True:
        birthdate = input()
        if not birthdate:
            continue
        print(digit_of_life(birthdate))
except KeyboardInterrupt:
    print('\nExiting...'); exit(0)