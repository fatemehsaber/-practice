import random as rnd

list1 =['apple','home' ,'tea' ,'sea','nice','hi','hello','programing','development','engineer','doctor','dog','cat','rabit','fox','color','green','oreng','brown','blue','red','computer','laptap','adaptor']
def re_place(l,i,v):
    l.insert(i,v)
    l.pop(i+1)
    return l

def print_list(l):
    for i in range(len(l)):
        print(l[i],end= " ")
def in_word ():
    u=( rnd.choice(list1))
    return u
    
word = in_word()
list_full = []
list_kh = []
s = 0
for i in range(len(word)):
    list_full.append(word[i])
    list_kh.append(" _ ")


level = input('wellcom to the hangman , please chose the level  : \n (a) easy \n (b) normal \n (c) hard \n')
if level == "a":
    times = len (word) + 5
    print('you have chosen the easy dificulity , you have', times , 'guess')
elif level == "b":
    times = len (word) + 3
    print('you have chosen the normal dificulity , you have', times , 'guess')
elif level == "c":
    times = len (word) + 1
    print('you have chosen the hard dificulity , you have', times , 'guess')
else:
    print('woring!')

while s != times :
    s += 1
    n = input('guess : ')
    if len(n) == 1 :
        if n in word :
            print("goodjob , that was correct :) ")
            for i in range(len(word)):
                if n == list_full[i]:
                  re_place(list_kh,i,n)
            print(list_kh)
            print("\n")
        else:
            print("wrong letter ! pleas try again :( ")
            print_list(list_kh)
            print("\n")
    if len(n) > 1 :
        if n == word:
            print('goodjob , you have chosen the correct word!')
            break
        else:
            print('you woring! try again.')
    if list_kh == list_full:
        break
        print('goodjob , you have chosen the correct word!')