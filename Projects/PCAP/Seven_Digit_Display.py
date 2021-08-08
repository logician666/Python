from re import I


def display(num):
    digits = [ 
        '1111110',  # 0
        '0110000',	# 1
        '1101101',	# 2
        '1111001',	# 3
        '0110011',	# 4
        '1011011',	# 5
        '1011111',	# 6
        '1110000',	# 7
        '1111111',	# 8
        '1111011',	# 9
    ]

    num_digits = [int(d) for d in str(num)]
    led = [' ', '#']

    for _ in range(5):
        for digit in num_digits:
            if _ == 0:
                print(led[])

while True:
    number = input('Enter a number: ')
    if not number.isnumeric():
        print('Not a valid number. Reenter a new one!\n')
        continue
    display(int(number))