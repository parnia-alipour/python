import random

li = []
try:

    for i in range(1,101):
        x=str(input('Enter your name for the lottery'))
        li.append(x)
        print(li)

    if len(li)==100:
        winner = random.choice(li)
        print(f"🎉 The winner is: {winner}")

except ValueError:
    print("Invalid input. Please try again.")


#short

x=['amir','fatemh','zahra','mohamad','ali']
winner=random.choice(x)
print(winner)