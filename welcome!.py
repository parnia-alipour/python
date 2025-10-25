z=100
while z>0:

    email='your_email'
    password='your_password'

    x=input('enter you email:')
    y=input('enter your password:')

    if x==email and y==password:
        print('welcome')
    else:
        print('Sorry, the information you entered is incorrect.')
        z+=1