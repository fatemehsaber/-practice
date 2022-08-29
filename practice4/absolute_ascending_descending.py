list = []
counter = True
for i in range(10):

    print('\nEnter the number :\n')
    numbers = int(input())
    list.append(numbers)

for num in range(len(list) - 1): 

    if (list[num] < list[ num + 1]):
        counter = True
        continue
    
    else:
        counter = False
        break

if (counter ==True):
    print('Yes,absolute ascendaant.')
else:
    print('No,absolute decline.')




