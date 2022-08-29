num = int(float (input('enter the  oposit number : ')))
number =num
count = 0

while (num > 0) :
    temp = num % 10 # 432 % 10 = 2
    count = (count * 10) + temp #2
    num //= 10    #43

if (number == count):
    print(count,'Yes')
else:
    print(count,'NO')

#tafrigh
sum = number + count

#jam
taf = number - count

print(sum,taf)