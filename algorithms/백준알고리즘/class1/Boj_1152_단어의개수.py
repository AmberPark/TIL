s = input()

words = s.split(' ')

while '' in words:
    words.remove('')

print(len(words))
