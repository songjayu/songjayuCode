def print_most_used_alphabet(given_word):
    alphabets = [0] * 26
    given_word = given_word.upper()

    for i in given_word:
        alphabets[ord(i)-65] += 1

    max_alphabet = chr(alphabets.index(max(alphabets))+65)
    cnt = 0
    for i in alphabets:
        if i == max(alphabets):
            cnt += 1
        if cnt > 1:
            return '?'
    return max_alphabet
print(print_most_used_alphabet(input()))