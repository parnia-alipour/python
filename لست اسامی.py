from numpy.ma.core import append

i=0
listt=[]
for i in range(1,100):
    x=str(input('لطفا نام خود را وارد کنید:'))
    y=str(input(" لطفا نام خانودگی خود را وارد کنید"))
    ez=x+" "+y
    listt.append(ez)
    print(listt)
    d=input('آیا میخواهید ادامه دهید؟')
    if d=="بله" or d=="آره" or d=='اره':
        continue
    elif d=='نه':
        print("ممنون از شما")
        exit()
    else:
        print('لطفا اطلاعات را درست وارد کنید')
        i+=1