i=0
listt=[]
while True:
    x=input('please enter your name:')
    y=input(" please enter your last name:  ")
    ez=x+' '+y
    listt.append(ez)
    print(listt)
    d=str(input('Do you want to continue?')).strip().lower()
    if d=="yes".lower() :
        i+=1
    elif d=="no".lower() :
        print('thank you')
        exit()
    else:
        print('Please enter yes or no')
    continue


