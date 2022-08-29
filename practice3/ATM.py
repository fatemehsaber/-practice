password = 4255
reverse_passsword = 5524
i = 0
while i <= 2:
    print('you can enter the password only 3 times!')
    pass1 = int(input('enter the 4_digit password : '))
    c = 0 
    pas = pass1 
    while pass1 >= 1:
        pass1= pass1/ 10
        c +=1
        
    if (c == 4):
        if(pas == password):
            print('password is true')
            i +=1
            break
            
        elif(pas == reverse_passsword ):
            print('call the police.')
            i+=1
            break
        else:
            print('try again !') 
            i += 1
        

    else:
        print('try again !')
        continue
        i += 1


        










