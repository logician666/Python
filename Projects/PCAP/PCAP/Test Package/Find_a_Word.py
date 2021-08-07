word, sentence = input(), input()

ans = 'Yes'
last_index = 0
for c in word:
    if _ := sentence.find(c, last_index + 1) != -1:
        last_index = _
        continue
    else:
        ans = 'No'

print(ans)