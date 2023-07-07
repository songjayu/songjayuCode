from string import ascii_lowercase
alphabetList = list(ascii_lowercase)
word = list(input())

for i in word:
    for j in alphabetList:
        if i == j:
            alphabetList[alphabetList.index(j)] = word.index(i)

for k in alphabetList:
    if isinstance(alphabetList[alphabetList.index(k)], str):
        alphabetList[alphabetList.index(k)] = -1

for l in alphabetList:
    if isinstance(alphabetList[alphabetList.index(l)],int):
        alphabetList[alphabetList.index(l)] = str(alphabetList[alphabetList.index(l)])

print(' '.join(alphabetList))