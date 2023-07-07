from string import ascii_uppercase
alphabet = list(ascii_uppercase)
word = list(input())
time = 0

for i in word:
    for i1 in alphabet[0:3]:
        if i == i1:
            time += 3

    for i2 in alphabet[3:6]:
        if i == i2:
            time += 4

    for i3 in alphabet[6:9]:
        if i == i3:
            time += 5

    for i4 in alphabet[9:12]:
        if i == i4:
            time += 6
    
    for i5 in alphabet[12:15]:
        if i == i5:
            time += 7
    
    for i6 in alphabet[15:19]:
        if i == i6:
            time += 8
    
    for i7 in alphabet[19:22]:
        if i == i7:
            time += 9
    
    for i8 in alphabet[22:26]:
        if i == i8:
            time += 10

    for i9 in alphabet[27:]:
        if i == i9:
            time += 11

print(time)