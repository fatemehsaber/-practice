
def f(l):
    print("%s |%s|%s"  %(l[0][0],l[0][1],l[0][2]))
    print("---- ---- ----")
    print("%s |%s|%s"  %(l[1][0],l[1][1],l[1][2]))
    print("---- ---- ----")
    print("%s |%s|%s"  %(l[2][0],l[2][1],l[2][2]))
    print("\n")

l = [['\t','\t','\t'],['\t','\t','\t'],['\t','\t','\t']]
f(l)
print("\n")
turn = 1
for i in range(9):
    if turn == 1:
        x = int(input("enter the number where you want to input :"))
        if x == 1:
            if l[0][0] == "\t":
                l[0][0] = " X "
                turn = 0
            else:
                turn = 1
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][0] == l[0][1] == l[0][2] != "\t" or l[1][0] == l[1][1] == l[1][2] != "\t" or l[2][0] == l[2][1] == l[2][2] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("X wins")
                break
        elif x == 2:
            if l[0][1] == "\t":
                l[0][1] = " X "
                turn = 0
            else:
                turn = 1
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("X wins")
                break
        elif x == 3:
            if l[0][2] == "\t":
                l[0][2] = " X "
                turn = 0
            else:
                turn = 1
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("X wins")
                break
        elif x == 4:
            if l[1][0] == "\t":
                l[1][0] = " X "
                turn = 0
            else:
                turn = 1
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("X wins")
                break
        elif x == 5:
            if l[1][1] == "\t":
                l[1][1] = " X "
                turn = 0
            else:
                turn = 1
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("X wins")
                break
        elif x == 6:
            if l[1][2] == "\t":
                l[1][2] = " X "
                turn = 0
            else:
                turn = 1
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("X wins")
                break
        elif x == 7:
            if l[2][0] == "\t":
                l[2][0] = " X "
                turn = 0
            else:
                turn = 1
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("X wins")
                break
        elif x == 8:
            if l[2][1] == "\t":
                l[2][1] = " X "
                turn = 0
            else:
                turn = 1
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("X wins")
                break
        elif x == 9:
            if l[2][2] == "\t":
                l[2][2] = " X "
                turn = 0
            else:
                turn = 1
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("X wins")
                break
    else:
        x = int(input("Enter the number where you want to input :"))
        if x == 1:
            if l[0][0] == "\t":
                l[0][0] = " O "
                turn = 1
            else:
                turn = 0
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("O wins")
                break
        elif x == 2:
            if l[0][1] == "\t":
                l[0][1] = " O "
                turn = 1
            else:
                turn = 0
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("O wins")
                break
        elif x == 3:
            if l[0][2] == "\t":
                l[0][2] = " O "
                turn = 1
            else:
                turn = 0
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("O wins")
                break
        elif x == 4:
            if l[1][0] == "\t":
                l[1][0] = " O "
                turn = 1
            else:
                turn = 0
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("O wins")
                break
        elif x == 5:
            if l[1][1] == "\t":
                l[1][1] = " O "
                turn = 1
            else:
                turn = 0
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("O wins")
                break
        elif x == 6:
            if l[1][2] == "\t":
                l[1][2] = " O "
                turn = 1
            else:
                turn = 0
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("O wins")
                break
        elif x == 7:
            if l[2][0] == "\t":
                l[2][0] = " O "
                turn = 1
            else:
                turn = 0
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("O wins")
                break
        elif x == 8:
            if l[2][1] == "\t":
                l[2][1] = " O "
                turn = 1
            else:
                turn = 0
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("O wins")
                break
        elif x == 9:
            if l[2][2] == "\t":
                l[2][2] = " O "
                turn = 1
            else:
                turn = 0
            f(l)
            if l[0][2] == l[1][2] == l[2][2] != "\t" or l[0][0] == l[1][0] == l[2][0] != "\t" or l[0][1] == l[1][1] == l[2][1] != "\t" or l[0][2] == l[0][1] == l[0][0] != "\t" or l[1][2] == l[1][1] == l[1][0] != "\t" or l[2][2] == l[2][1] == l[2][0] != "\t" or l[0][0] == l[1][1] == l[2][2] != "\t" or l[0][2] == l[1][1] == l[2][0] != "\t":
                print("O wins")
                break
if(i>8):
    print("Draw")

 