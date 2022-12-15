wordlength = "______"
word = "animal"
guess = "a"
index = 0
while index < len(word): 
    index = word.find(guess, index)
    if index == -1:
        break
    wordlength = wordlength[:index] + wordlength[index:]
    print(wordlength[:index] + guess + wordlength[index+1:])
    index += 1

print(wordlength)