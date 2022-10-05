letter_seda = ['a' , 'e' , 'o' , 'u' ,'i']
word = input('enter the word : ')

for w in word:
    for letter in letter_seda:
        if w == letter:
            word = word.replace(w, "?")
print(word)        