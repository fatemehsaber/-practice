import random as  rnd
dice = []

while True:
    dice.append(rnd.randint(1,6))
    if 6 in dice:
        print('\nsum numbers : ',str(sum (dice)))
        print('------------------------------')
        print('list number : ',dice)
        print('------------------------------')
        break
    else:
        continue

print('number of number entered :',str(len(dice)))
        
