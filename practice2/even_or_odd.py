num = int(input('enter the number : '))
even = 0 
odd =0

while num != 0:
    temp = num % 10

    if temp % 2 == 0 :
      even += 1
    else:
      odd += 1
    num //=10

print('the number even :',even,'\n the number odd : ',odd)

if even > odd:
    print('the even is max.')
elif(even == odd):
    print('the numbers is equal.')
else:
    print('the odd is max')

