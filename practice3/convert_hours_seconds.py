#hal1
import datetime 
while True:
    c = input('''convert :
a)convert_second_hur
b)convert_hour_second \n''')
    if (c == 'a'):
        secound = int (input('enter the secound : '))
        convert = str(datetime.timedelta(seconds=secound))
        print(convert,'\n')
    
    elif( c =='b'):
        hour = int (input('enter the hour :'))
        min = int (input('enter the min :'))
        secounds = int (input('enter the secounds :'))
        print(f'\n\n{hour} : {min} : {secounds}')
        new_hour = hour * 3600
        new_min = min * 60
        result = (new_hour + new_min + secounds)
        print('\n secound is :',result)

  




 #hal 2
# c = input('''convert :
# a)convert_hour_second
# b)convert_second_hur
#  \n''')
# if (c == 'a'):
#     hour = int (input('enter the hour :'))
#     min = int (input('enter the min :'))
#     secounds = int (input('enter the secounds :'))
#     print(f'\n\n{hour} : {min} : {secounds}')
#     new_hour = hour * 3600
#     new_min = min * 60
#     result = (new_hour + new_min + secounds)
#     print('\n secound is :',result)

# elif( c =='b'):
#     secound = int (input('enter the secound : '))
#     hour = secound // 3600
#     count = secound - 3600 * hour
#     min =  count // 60
#     secounds = count - 60 * min

#     print(f'{hour} : {min} : {secounds}')












    





