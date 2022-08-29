while True:
    dama=float(input(' please enter dama : '))
    type_dama1 =input('''please enter your first temperatuur : 
1)celsius =c
2)fahrenheit = f
3)kelvin  = k
''' )

    type_temp2 =input('''please enter your second temperatuur : 
1)celsius =c
2)fahrenheit = f
3)kelvin  = k
''' )
    if type_dama1 =='c' and type_temp2 =='f':
        f = (dama * 1.8) + 32
        print('fahrenheit = ',f)

    elif type_dama1 == 'f' and type_temp2 == 'c':
        c = (dama - 32) / 1.8
        print('celsius = ',c)

    elif type_dama1 == 'k' and type_temp2 == 'c':
        c = dama - 273.15
        print('celsius = ',c)

    elif type_dama1 == 'c' and type_temp2 == 'k':
        k = dama + 273.15
        print('kelvin = ',k)

    elif type_dama1 == 'f' and type_temp2 == 'k':
        print('kelvin =',(dama + 459.67) / 1.8)


    elif type_dama1 == 'k' and type_temp2 == 'f':
        print('fahrenhit =',(dama * 1.8) - 459.67) 


    else:
        print('mojadad vared shavid')
