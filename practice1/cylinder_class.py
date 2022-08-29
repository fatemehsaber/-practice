#ertfa vared konid :
height = float(input('enter the height : '))

#shoa vard konid : 
radius = float(input('enter the radius : '))
#estefade az tabe math
import math
Pi = 3.1315
#formol ha :
volume = (Pi * height * radius ** 2)
lateralArea = (2 * Pi * radius * height)
totalArea = ((2 * Pi) * radius ** 2) + lateralArea
#chap
print('lateralArea = %f  \n volume = %f \n totalArea = %f' %(lateralArea,volume,totalArea))


