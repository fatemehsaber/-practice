from re import T


num_fact = int (input('enter the number : '))
c = True
for i in range(1,num_fact - 1):
    num_fact /= i

    if num_fact == 1 :
        c = True
        break
        
    else:
        c = False
        continue
if c == True:
    print('yes')
else:
    print('No')