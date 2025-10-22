while True:
    try:
        x = int(input('Please enter your score:'))

        if 0 <= x <= 59:
            print('F')
        elif 60<=x<= 69:
            print('D')
        elif 70 <= x <= 79:
            print('C')
        elif 80 <= x <= 89:
            print('B')
        elif 90 <= x <= 100:
            print('A')
        else:
            print('Please enter a score between 0 and 20.')

    except ValueError:

        print('Please enter a number')
