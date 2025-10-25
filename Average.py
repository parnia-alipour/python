n=0
num=int(input('How many scores do you want to enter?'))
for i in range(num):
    numbers=float(input('enter number:'))
    n+=numbers

    avg=n/num

print(f'average is {avg}')