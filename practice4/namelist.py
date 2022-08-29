#hal1
def countx(lst,x):
    return lst.count(x)
    
if __name__ == '__main__':

    n = int ( input('enter number : '))
    
    name1 = []
    for i in range(0,n):
       stri = input('enter sentence : ')
       name1.append(stri)
    
    for i in name1:
       print('{} has occurred {} times' .format(i, countx(name1,i)))
    for j in name1 : 
        if i == j:
            name1.remove(j)




#hal2

# list1 = []
# list2 = []
# num = int (input('chand ta esm vared mikonid ?\n '))
# for i in range(num):
#     name = input('esm ra vared konid.\n')
#     list1.append(name)
# for item in list1:
#     if item not in list2:
#         list2.append(item)

# for item in list2:
#     counter = list1.count(item)
#     print(item, ' = ',counter)