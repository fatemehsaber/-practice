text = input('enter tthe original  text : ')
break_text = input ('enter the text to bteak :')
connect_text = input('enter rhe texxt thaat connects the pieces :')
print('\n',text)
print(50*'_')
split = text.split(break_text)
print(split)
print(50*'_')
connect = connect_text.join(split)
print(connect,'\n')