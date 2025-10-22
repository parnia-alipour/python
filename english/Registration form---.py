list_t = []

while True:
    try:
        name = input("enter your name: ")
        if  not name.isalpha(): # To check if it's a string.
            print('Please enter the requested information correctly.')
            continue
        lastname = input("enter your last name: ")
        if not lastname.isalpha():
            print(' Please enter the requested information correctly.')
            continue
        age = int(input("enter your age: "))
        email = input("enter your email: ").strip()
        if  not email.isalpha():
            print(' Please enter the requested information correctly.')
            continue
        phone = input("enter your number phone: ").strip()
        national_id = input("enter your National code:").strip()
        if  not national_id.isalpha():
            print('Please enter the requested information correctly.')
            continue
        if name.isalpha():
            print(' Please enter the requested information correctly.')
            continue
        person = { # Enter the information into a Python dictionary
            "Name": name,
            "Last name": lastname,
            "Age": age,
            "Email": email,
            "Phone number": phone,
            " National code": national_id
        }
        list_t.append(person) #
        print(" Thank you, your information has been recorded in the system.")
        print(list_t)

        sbt = input("Please enter your national code, email or mobile number: ").strip()

        found = False
        for p in list_t:
            if p["Phone number"] == sbt or p["National code"] == sbt or p["Email"] == sbt:#If this information exists in the system, let me know. If not , please told register.
                found = True
                break

        if found:
            print(" Your information has already been registered, please log in to the login panel.")
        else:
            print(" Your information does not exist in the system, please register.")

    except ValueError:# If the user enters a non-numeric value for age by mistake, show an error message asking them to enter a valid number
        print(" Please enter the numeric information correctly.")