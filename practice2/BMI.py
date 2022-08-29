# heigh = float(input('enter your heigh (cm): '))
heigh = float(input('enter your heigh (m): '))
weight = float(input('enter your weight (kg): '))
age = int (input(' enter your age (24 be bala): '))

BMI = weight // (heigh ** 2)
# heigh_cm = heigh / 100
# BMI= weight / (heigh_cm ** 2)

print(BMI)
if (BMI <= 15):
    print('your BMI is : ',BMI,'\n You are severely underweight.')
    
elif(15 < BMI <=18.5):
    print('your BMI is : ',BMI,'\n You are underweight.')
   
elif(18.5 < BMI <= 25):
    print('your BMI is : ',BMI,'\n You have a normal weight.')
    
elif(25 < BMI <= 30):
    print('your BMI is : ',BMI,'\n You are overweight.')
    
elif(30 < BMI <= 35):
    print('your BMI is : ',BMI,'\n You have normal obesity.')
    
elif(35 < BMI <= 40):
    print('your BMI is : ',BMI,'\n You are severely obese.')
    
elif(40> BMI):
    print('your BMI is : ',BMI,'\n You are very obese.')

    

if (19 < age <=25):
    print('BMI monaseb sen shoma:22')
elif(25 < age <= 35):
    print('BMI monaseb sen shoma:23')
elif(35 < age <= 45):
    print('BMI monaseb sen shoma:24')
elif(45 < age <= 55):
    print('BMI monaseb sen shoma:25')
elif(55 < age <= 65):
    print('BMI monaseb sen shoma:26')
elif(age > 65):
    print('BMI monaseb sen shoma:27')
