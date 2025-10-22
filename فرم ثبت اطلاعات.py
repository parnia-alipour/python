list_t = []

while True:
    try:
        name = input("نام خود را وارد کنید: ")
        if  not name.isalpha(): # برای اینکه ببینه استیرنگه یا نه
            print(' لطفا اطلاعات خواسته شده رو درست وارد کنید')
            continue
        lastname = input("نام خانوادگی خود را وارد کنید: ")
        if not lastname.isalpha():
            print(' لطفا اطلاعات خواسته شده رو درست وارد کنید')
            continue
        age = int(input("سن خود را وارد کنید: "))
        email = input("ایمیل خود را وارد کنید: ").strip()
        if  not email.isalpha():
            print(' لطفا اطلاعات خواسته شده رو درست وارد کنید')
            continue
        phone = input("شماره همراه خود را وارد کنید: ").strip()
        national_id = input("کد ملی خود را وارد کنید: ").strip()
        if  not national_id.isalpha():
            print(' لطفا اطلاعات خواسته شده رو درست وارد کنید')
            continue
        if name.isalpha():
            print(' لطفا اطلاعات خواسته شده رو درست وارد کنید')
            continue
        person = { # اطلاعات رو وارد دیکشنری کن
            "نام": name,
            "نام خانوادگی": lastname,
            "سن": age,
            "ایمیل": email,
            "شماره همراه": phone,
            "کدملی": national_id
        }
        list_t.append(person) #اضافه من به لیست
        print(" با تشکر، اطلاعات شما در سیستم ثبت شد.")
        print(list_t)

        sbt = input("لطفا کد ملی یا ایمیل یا شماره همراه خود را وارد کنید: ").strip()

        found = False
        for p in list_t:
            if p["شماره همراه"] == sbt or p["کدملی"] == sbt or p["ایمیل"] == sbt:# اگر این اطلاعات در سیستم هست بگو اگر نه بگو ثبت نام کنید
                found = True
                break

        if found:
            print(" اطلاعات شما از قبل ثبت شده است، لطفاً وارد پنل ورود شوید.")
        else:
            print(" اطلاعات شما در سامانه وجود ندارد، لطفاً ثبت ‌نام کنید.")

    except ValueError:# اگر اشتباهی سن رو عدد وارد نکرد کاربر
        print(" لطفاً اطلاعات عددی را به‌درستی وارد کنید.")