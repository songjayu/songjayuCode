word = input()
reversed_word = reversed(word)
first_storage = []
second_storage = []
num = 0

for i in reversed_word:
    first_storage.append(i)
for j in word:
    second_storage.append(j)

for k in range(len(word)):
    if first_storage[k] == second_storage[k]:
        num += 1

if num == len(word):
    print('1')
else: print('0')