from sys import exit

def anagrams(word1, word2):
    word1, word2    = map(lambda s: s.strip().replace(' ', '').lower(), (word1, word2))
    chars1, chars2  = map(lambda s: set(s), (word1, word2))

    if word1 and word2 and chars1 == chars2:
        print('Anagrams'); return True
    print('Not Anagrams'); return False
    
try:
    while True:
        word1, word2 = input(), input()
        anagrams(word1, word2)
except KeyboardInterrupt:
    print('\nExiting...'); exit(0)

