final_score = 0
win = 0  
equal = 0
loss = 0
score = 0
counter = 1
while (counter < 9):
    print('Enter your points in game : \n win : 3    equal : 1    loss : 0 \n score ',counter,':')
    score =int(input())
    if((score ==0) or (score ==1) or (score ==3)):
        final_score += score
        counter +=1
        if (score == 3):
            win += 1
        elif (score == 1):
            equal += 1
        elif (score == 0):
            loss += 1
    else:
        print('you entered an error!\n')

             
print('final_score   win   equal   loss\n','  ',final_score,'       ',win,'    ',equal,'    ',loss)
    


