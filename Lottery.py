import random


try:
    li=[]
    x=str(input('Enter your name for the lottery'))
    li.append(x)
    winner=random.choose(li)
    print(f"🎉 The winner is: {winner}")


except ValueError:
    print("Invalid input. Please try again.")
