username = ('fatemeh_saber79')
password = 1234
i=0
print('"you can only test 3 times"\n')
while i <= 2 :
  user_name = input('please enter your username : ')
  passwords =int(input('please enter your password : '))

  if (username == user_name) and (password ==passwords):
     print('wellcom to account :)')
     break
  else:
    print('please try again :')
    
  i += 1
if (i > 2):
    print('error!')
 

