board = []

def prod(l):
    x = 1
    for k in l:
        x *= k
    return x

board = []
for i in range(9):
    board.append(input())

prod = factorial(9)

for row in board:
    if prod(row.split('')) != prod:
        # return False

