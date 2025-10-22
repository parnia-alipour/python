while True:
    try:
        x = int(input('نمره خود را وارد کنید:'))

        if 0 <= x <= 9: #اگر نمره از 0 تا 9 بود بود تژدید
            print('تژدید')
        elif x == 10:
            print(' قبول')
        elif 10 <= x <= 15:
            print('قابل قبول')
        elif 15 <= x <= 17:

            print('خوب')
        elif 17 <= x <= 20:
            print('عالی/خیلی خوب')
        else:
            print('لطفا نمره ای بین 0 تا 20 وارد کنید.')

    except ValueError: # اگر کاربر عدد وارد نکرد پیام رو پرینت کن

        print('لطفا عدد وارد کنید.')
