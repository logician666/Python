from symbol import encoding_decl


line = input('Enter the line to be ciphered: ')

shift = ''
while type(shift) != int:
    try:
        shift = int(input('Enter a shift value (between 1 and 25 inclusive): '))
        if shift not in range(1, 26):
            raise ValueError
    except:
        print('Not a valid input.\n')
        continue

code = ''
for char in line:
    if not char.isalpha():
        code += char
        continue
    # Determine the beginning of the subset of alphabet to which the character belongs
    if char.isupper():
        n = ord('A')
    else:
        n = ord('a')
    # Encode the character and add it to the code string:
    code += chr(((ord(char) - n) + shift) % 26 + n)

print(code)
    