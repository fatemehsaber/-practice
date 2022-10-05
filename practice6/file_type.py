from tabulate import tabulate 
from colorama import Fore,Back,Style

def file_type(file):
    s = file.split('.')
    ans= s [-1]
    return (ans)
file = input(Fore.LIGHTYELLOW_EX+'please enter your file : '+Style.RESET_ALL)
f=file_type(file)
print(Back.LIGHTMAGENTA_EX+"file name and type"+Style.RESET_ALL)
ta=[['file name','file type'],
[file,f]]
print(tabulate(ta,tablefmt='fancy_grid'))