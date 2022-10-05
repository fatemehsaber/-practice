import random as rnd
from tabulate import tabulate  
from colorama import Fore,Back,Style
count1=0
count2=0
a='Rock'
b='Paper'
c='Scissor'
list=['Rock','Paper','Scissor']
option_table = [['choose an option :'],
['1) 1 people'],
['2) 2 people'],
['3) exit']]
print(tabulate(option_table,tablefmt='fancy_grid'))
answer=int(input(Fore.BLUE+'enter your desired option : \n'+Style.RESET_ALL))
if answer == 2:
    name1 = input(Fore.LIGHTWHITE_EX+"please enter your name: "+Style.RESET_ALL)
    name2 = input(Fore.LIGHTWHITE_EX+"please enter your name: "+Style.RESET_ALL)
        
    num_table = [['how many rounds should be played to determine the winner ?'],
    ['1) 1 round'],
    ['2) 3 round'],
    ['3) 5 round']]

    print(tabulate(num_table,tablefmt='fancy_grid'))
    round = int(input(Fore.BLUE+'enter your desired option : \n'+Style.RESET_ALL))
    
    if (round == 1):
            
        while True:
                    
            play_table = [['choose one :'],
            ['a) Rock'],
            ['b) Paper'],
            ['c) Scissors']]
            print(tabulate(play_table,tablefmt='fancy_grid'))
            play1 = input(Fore.BLUE+'enter your desired option : \n'+Style.RESET_ALL)
            play2 = input(Fore.BLUE+'enter your desired option : \n'+Style.RESET_ALL)

            if(play1 == 'a' and play2 == 'c') or (play1 == 'b' and play2 == 'a') or (play1 == 'c' and play2 == 'b'):
                print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name1+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                option_table=[[name1,play1],
                [name2,play2]]
                print(tabulate(option_table,tablefmt='fancy_grid'))
                break

            elif(play1 == 'a' and play2 == 'a') or (play1 == 'b' and play2 == 'b' )or( play1 == 'c' and play2 == 'c' ):
                print(Fore.LIGHTYELLOW_EX+"equal"+Style.RESET_ALL)
                continue

            elif(play1 == 'c' and play2 == 'a') or( play1 == 'a' and play2 == 'b' )or (play1 == 'b' and play2 == 'c'):
                print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name2+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                option_table=[[name1,play1],
                [name2,play2]]
                print(tabulate(option_table,tablefmt='fancy_grid'))
                break

            else:
                print(Fore.LIGHTRED_EX+'wrong'+Style.RESET_ALL)   

    elif (round == 2):     
        while True:
            if (count1 < 3) and (count2 < 3):
                play_table = [['choose one :'],
                ['a) Rock'],
                ['b) Paper'],
                ['c) Scissors']]
                print(tabulate(play_table,tablefmt='fancy_grid'))
                play1 = input(Fore.BLUE+'enter your desired option : \n'+Style.RESET_ALL)
                play2 = input(Fore.BLUE+'enter your desired option : \n'+Style.RESET_ALL)

                if(play1 == 'a' and play2 == 'c') or (play1 == 'b' and play2 == 'a') or (play1 == 'c' and play2=='b'):
                    option_table=[[name1,play1],
                    [name2,play2]]
                    print(tabulate(option_table,tablefmt='fancy_grid'))
                    print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name1+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                    count1+=1
                    print( name1,':',play1,'\n'+name2,':',play2,'\n')

                elif(play1 == 'a' and play2 == 'a') or (play1 == 'b' and play2 == 'b') or (play1 == 'c' and play2 == 'c' ):
                    print(Fore.LIGHTYELLOW_EX+"equal"+Style.RESET_ALL)
                    continue

                elif(play1== 'c' and play2== 'a') or (play1== 'a' and play2 == 'b') or (play1 == 'b' and play2 == 'c'):
                    option_table=[[name1,play1],
                    [name2,play2]]
                    print(tabulate(option_table,tablefmt='fancy_grid'))
                    print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name2+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                    count2 += 1

                else:        
                    print(Fore.LIGHTRED_EX+'wrong'+Style.RESET_ALL)
            else:
                option_table=[['name','round'],
                [name1,count1],
                [name2,count2]]
                print(tabulate(option_table,tablefmt='fancy_grid'))
                break

    elif (round == 3) :
        while True:
            if (count1 < 5) and (count2 < 5) :

                play_table = [['choose one :'],
                ['a) Rock'],
                ['b) Paper'],
                ['c) Scissors']]
                print(tabulate(play_table,tablefmt='fancy_grid'))
                play1 = input(Fore.BLUE+'enter your desired option : \n'+Style.RESET_ALL)
                play2 = input(Fore.BLUE+'enter your desired option : \n'+Style.RESET_ALL)
                if(play1 == 'a' and play2 == 'c') or (play1 == 'b' and play2 == 'a') or (play1 == 'c' and play2 =='b'):
                    option_table=[[name1,play1],
                    [name2,play2]]
                    print(tabulate(option_table,tablefmt='fancy_grid'))
                    print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name1+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                    count1+=1
                    print( name1,':',play1,'\n'+name2,':',play2,'\n')

                elif(play1== 'a' and play2 == 'a') or (play1 == 'b' and play2 == 'b') or (play1 == 'c' and play2 == 'c' ):
                    print(Fore.LIGHTYELLOW_EX+"equal"+Style.RESET_ALL)
                    continue

                elif(play1 == 'c' and play2 == 'a') or (play1 == 'a' and play2 == 'b') or (play1 == 'b' and play2 == 'c'):
                    option_table=[[name1,play1],
                    [name2,play2]]
                    print(tabulate(option_table,tablefmt='fancy_grid'))
                    print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name2+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                    count2 += 1

                else:         
                    print(Fore.LIGHTRED_EX+'wrong'+Style.RESET_ALL)
            
            else:
                option_table=[['name','round'],
                [name1,count1],
                [name2,count2]]
                print(tabulate(option_table,tablefmt='fancy_grid'))
                break

    else:
         print(Fore.CY2AN+'try again.'+Style.RESET_ALL)


elif (answer == 1):
    name1=input(Fore.LIGHTWHITE_EX+"please enter your name: "+Style.RESET_ALL) 
    num_table = [['how many rounds should be played to determine the winner ?'],
    ['1) 1 round'],
    ['2) 3 round'],
    ['3) 5 round']]
    print(tabulate(num_table,tablefmt='fancy_grid'))
    round = int(input(Fore.BLUE+'enter your desired option : \n'+Style.RESET_ALL))
    if (round == 1):
        while True:

            play_table = [['choose one :'],
            ['a) Rock'],
            ['b) Paper'],
            ['c) Scissors']]
            print(tabulate(play_table,tablefmt='fancy_grid'))
            play = input(Fore.BLUE+'enter your desired option : \n'+Style.RESET_ALL)

            if (play == 'a' and rnd.choice ( list ) == 'Scissors') or (play == 'b' and rnd.choice ( list ) == 'Rock') or (play == 'c' and rnd.choice(list) == 'Paper'):
                option_table=[[name1,play],
                ['system',rnd.choice(list)]]
                print(tabulate(option_table,tablefmt='fancy_grid'))
                print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name1+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                break
            
            elif (play== 'c' and rnd.choice(list)=='Scissors') or (play== 'b' and rnd.choice(list)=='Paper') or (play== 'a' and rnd.choice(list)=='Rock'):
                print(Fore.LIGHTYELLOW_EX+"equal"+Style.RESET_ALL)
                continue

            elif (play == 'a' and rnd.choice ( list ) == 'Paper') or (play == 'b' and rnd.choice ( list ) == 'Scissors') or (play == 'c' and rnd.choice(list) == 'Rock'):                       
                option_table=[[name1,play],
                ['system',rnd.choice(list)]]
                print(tabulate(option_table,tablefmt='fancy_grid'))
                print(Fore.RED+'oh, you are faild :('+Style.RESET_ALL)
                break

            else:
                print(Fore.LIGHTRED_EX+'wrong'+Style.RESET_ALL+Style.RESET_ALL)

    elif (round == 2):
        while True:
            if (count1 < 3 ) and (count2 < 3) :
                play_table = [['choose one :'],
                ['a) Rock'],
                ['b) Paper'],
                ['c) Scissors']]
                print(tabulate(play_table,tablefmt='fancy_grid'))
                play = input(Fore.BLUE+'enter your desired option : \n'+Style.RESET_ALL)

                if (play == 'a' and rnd.choice ( list ) == 'Scissors') or (play == 'b' and rnd.choice ( list ) == 'Rock') or (play == 'c' and rnd.choice(list) == 'Paper'):
                    count1+=1
                    option_table=[[name1,play],
                    ['system',rnd.choice(list)]]
                    print(tabulate(option_table,tablefmt='fancy_grid'))
                    print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name1+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                    

                elif (play== 'c' and rnd.choice(list)=='Scissors') or (play== 'b' and rnd.choice(list)=='Paper') or (play== 'a' and rnd.choice(list)=='Rock'):
                    print(Fore.LIGHTYELLOW_EX+"equal"+Style.RESET_ALL)
                    continue

                    
                elif (play == 'a' and rnd.choice ( list ) == 'Paper') or (play == 'b' and rnd.choice ( list ) == 'Scissors') or (play == 'c' and rnd.choice(list) == 'Rock'):                       
                    count2 += 1
                    option_table=[[name1,play],
                    ['system',rnd.choice(list)]]
                    print(tabulate(option_table,tablefmt='fancy_grid'))
                    print(Fore.RED+'oh, you are faild :('+Style.RESET_ALL)
                    

                else:
                        print(Fore.LIGHTRED_EX+'wrong'+Style.RESET_ALL+Style.RESET_ALL)
   
      
            else:
                    option_table=[['name','round'],
                    [name1,count1],
                    ['system',count2]]
                    print(tabulate(option_table,tablefmt='fancy_grid'))
                    break
        
    elif round == 3 :
            while True :
                if (count1 < 5) and (count2 < 5) :
                    play_table = [['choose one :'],
                    ['a) Rock'],
                    ['b) Paper'],
                    ['c) Scissors']]
                    print(tabulate(play_table,tablefmt='fancy_grid'))
                    play = input(Fore.BLUE+'enter your desired option : \n'+Style.RESET_ALL)                   

                    if (play == 'a' and rnd.choice ( list ) == 'Scissors') or (play == 'b' and rnd.choice ( list ) == 'Rock') or (play == 'c' and rnd.choice(list) == 'Paper'):
                        count1+=1
                        option_table=[[name1,play],
                        ['system',rnd.choice(list)]]
                        print(tabulate(option_table,tablefmt='fancy_grid'))
                        print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name1+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                        

                    elif (play== 'c' and rnd.choice(list)=='Scissors') or (play== 'b' and rnd.choice(list)=='Paper') or (play== 'a' and rnd.choice(list)=='Rock'):
                        print(Fore.LIGHTYELLOW_EX+"equal"+Style.RESET_ALL)
                        continue           

                    elif (play == 'a' and rnd.choice ( list ) == 'Paper') or (play == 'b' and rnd.choice ( list ) == 'Scissors') or (play == 'c' and rnd.choice(list) == 'Rock'):                       
                        count2+=1
                        option_table=[[name1,play],
                        ['system',rnd.choice(list)]]
                        print(tabulate(option_table,tablefmt='fancy_grid'))
                        print(Fore.RED+'oh, you are faild :('+Style.RESET_ALL)
                        
                    else:
                    
                        print(Fore.LIGHTRED_EX+'wrong'+Style.RESET_ALL+Style.RESET_ALL)

                else:
                    option_table=[['name','round'],
                    [name1,count1],
                    ['system',count2]]
                    print(tabulate(option_table,tablefmt='fancy_grid'))
                    break
    
    else:
        print(Fore.CYAN+'try again.'+Style.RESET_ALL)
    


                   

elif answer == 2:
    name1=input(Fore.LIGHTWHITE_EX+"please enter your name: "+Style.RESET_ALL)
    name2=input(Fore.LIGHTWHITE_EX+"please enter your name: "+Style.RESET_ALL)
        
    num_table = [['how many rounds should be played to determine the winner ?'],
    ['1) 1 round'],
    ['2) 3 round'],
    ['3) 5 round']]
    print(tabulate(num_table,tablefmt='fancy_grid'))
    round = int(input(Fore.BLUE+'enter your desired option : \n'+Style.RESET_ALL)) 


elif(answer == 3):
    print(Fore.LIGHTMAGENTA_EX+'YOUR EXIT.'+Style.RESET_ALL)
else:
    print(Fore.CYAN+'try again.'+Style.RESET_ALL)