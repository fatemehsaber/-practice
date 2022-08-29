import random

length = int (input('enter your desired length : '))

list = []
c = 0
while length > c:

    rnd = random.randint(10,80)
    if not ( rnd in list):
        list.append(rnd)
        c += 1
        
    else:
        print('repeated')
        
print(list)
