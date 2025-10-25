for i in range(1,101):
    x=int(input('Enter first divisor:'))
    y=int(input('Enter second divisor:'))
    z=int(input('Enter the number to check:'))

    if z%x==0 and z%y==0:
        print('It is divisible by both numbers.')
    else:
        print('It is not divisible by both numbers.')