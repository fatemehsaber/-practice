list_operator=[]
list_ans=[]
phrase=input("enter your math phrase: ")

a=phrase.split("*")
b=' '.join(a)
c=b.split("/")
d=' '.join(c)
e=d.split("+")
f=' '.join(e)
g=f.split("-")
h="".join(g)
list=h.split()

for math in phrase:
   if math=='/' or math=='*' or math=='+' or math=='-':
        list_operator.append(math)

for i in range (len(list)-1):
       a="".join(list_operator)
       m=a.find('/')
       
       if m!=-1:
        a=float(list[m])
        b=float(list[m+1])
        
        list.pop(m)
        list.insert(m,a/b)
        list.pop(m+1)
        list_operator.pop(m)
       else:
        a="".join(list_operator)
        m=a.find('*')
        if m!=-1:
            a=float(list[m])
            b=float(list[m+1])
            
            list.pop(m)
            list.insert(m,a*b)
            list.pop(m+1)
            list_operator.pop(m)

for i in range (len(list)-1):
       a="".join(list_operator)
       m=a.find('+')
       
       if m!=-1:
        a=float(list[m])
        b=float(list[m+1])
        
        list.pop(m)
        list.insert(m,a+b)
        list.pop(m+1)
        list_operator.pop(m)
       else:
        a="".join(list_operator)
        m=a.find('-')
        if m!=-1:
            a=float(list[m])
            b=float(list[m+1])
            
            list.pop(m)
            list.insert(m,a+b)
            list.pop(m+1)
            list_operator.pop(m)

print(phrase,'=',list)