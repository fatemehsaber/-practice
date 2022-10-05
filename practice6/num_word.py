def num_word(sen):
    element=["." , "," , "/" , "\\" , "[" , "]" , "{" , "}" , "!" , "#" , "&" , "(" , 
                 ")" , "*" , "^" , ":" , ";" , "\'" , "\"" , "<" , ">" , "|" , "$" , "%" ,
                 "~" , "`" , "@" , "?" ]
    for elments in element:
     string= sen.replace(elments , " ")

     word = string.split()
     c = len(word)

    return(c)


stri=input("enter your string^_^ : ")
b=num_word(stri)
print("you'r string have ",(b)," words")