num = []
for i in range(1,101):
    try:
        number = int(input("Enter number: "))
        num.append(number)
        print(num)
        x = input("Do you want to continue? (y/n): ")
        if x == "n".strip():
            print('thank you')
            break

    except ValueError:
        print("Invalid input. Please try again.")
        continue