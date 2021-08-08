from sys import exit

def is_palindrome(text):
    is_palindrome = True if len(text) != 0 else False

    if is_palindrome:
        # Define a variable l used to index the variable text:
        l = len(text) - 1
        for i in range(len(text) // 2):
            if text[i] != text[l - i]:
                is_palindrome = False
    
    print(['Not a palindrome.', 'Is a palindrome.'][is_palindrome])
    return is_palindrome

try:
    while True:
        text = input().strip().replace(' ', '').lower()
        is_palindrome(text)
except KeyboardInterrupt:
    print('Exiting...'); exit(0)

