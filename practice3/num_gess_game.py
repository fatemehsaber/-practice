import random as rnd
from unittest import result
counter = 1
start = 1
finish = 99

while True:
    result = rnd.randint(0,99)
    print('\nselected number :',result)
    print('\nchoose a num between 0 and 99 in your mid.\n')
    print('''
choose an option:\n
a)that is evil!
b)no,my num is small
c)no my num is bigger''')
    answer = input()
    
    if (answer == 'a'):
        print('hora!')
        break
    elif(answer == 'b'):
        finish =result
        result = rnd.randint(start,finish)
        counter += 1
    elif(answer == 'c'):
        finish =result
        result = rnd.randint(start,finish)
        counter += 1
    else:
        print('invalid input.')
print(f'number of guesses :',counter)

