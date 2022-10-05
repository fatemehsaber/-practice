from tabulate import tabulate as t
from colorama import Back,Fore,Style
import math

print("\nax^2 + bx + c = 0\n")
def moadeleh_2m(a,b,c):
    delta = (b ** 2) - 4 * (a * c)

    if delta > 0 :

        x1 = ((-b) + math.sqrt(delta)) / (2 * a)
        x2 = ((-b) - math.sqrt(delta)) / (2 * a)

        return(Fore.GREEN+"x1 = "+Style.RESET_ALL+Fore.GREEN+str(x1)+Style.RESET_ALL+Fore.LIGHTYELLOW_EX+"\nx2 = "+str(x2)+Style.RESET_ALL)

    elif delta == 0:

        x = (-b) / (2 * a)

        return(Fore.GREEN+"x1 = :"+Style.RESET_ALL+Fore.LIGHTYELLOW_EX+str(x2)+Style.RESET_ALL)

    else:

        return(Fore.LIGHTRED_EX+"javab nadareh :("+Style.RESET_ALL)
         






a = int(input(Fore.BLUE+"please enter a : "+Style.RESET_ALL))

b = int(input(Fore.BLUE+"please enter b : "+Style.RESET_ALL))

c = int(input(Fore.BLUE+"please enter c : "+Style.RESET_ALL))

ans=moadeleh_2m(a,b,c)

print(Fore.GREEN+Back.LIGHTMAGENTA_EX+"table answers"+Style.RESET_ALL)

table=[['a',a],['b',b],['c',c],['answer',ans]]

print(t(table,tablefmt='fancy_grid'))
