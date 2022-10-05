def m_n(m,n):
    for i in range(n):

        if i % 2 == 0: 

            print("$&"*m)
    
        else:
            
            print("&$"*m)

n1=int(input("please enter rows: "))
m1=int(input("please enter columns: "))
print(m_n(m1,n1))