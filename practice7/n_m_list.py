list=[]
p=''.join(list)
n_row = int(input('enter the number : '))
m_column = int(input('enter the number : '))
one=1
tow=1
for i in range(n_row):
    for i in range(m_column):
        c = one*tow
        tow+=1
        list.append(c)
    for i in range(m_column):
        l=list[:m_column]  
        if len(list)>0:
            del list[0:m_column]
            print(l)
        else:
            break 
    one+=1
    tow=1
    
 

          