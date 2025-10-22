import tkinter as tk

m=tk.Tk() # ساخت فرم
m.geometry('500x200') # ابعاد

lbl=tk.Label(m,text='نام')
lbl.grid(row=0,column=1)
my_Entry=tk.Entry(m) # فیلد ورود متنی رو میسازه برای نام
my_Entry.grid(row=0,column=2,padx=10,pady=10) # جهت قرار گیری و ابعاد
#بقیه هم به همین صورت
lbl=tk.Label(m,text='نام خوانوادگی')
lbl.grid(row=1,column=1)
my_Entry2=tk.Entry(m)
my_Entry2.grid(row=1,column=2,padx=10,pady=10)

lbl=tk.Label(m,text='سن')#age
lbl.grid(row=1,column=3)
my_Entry3=tk.Entry(m)
my_Entry3.grid(row=0,column=4,padx=10,pady=10)


lbl=tk.Label(m,text='شغل')
lbl.grid(row=0,column=3)
my_Entry4=tk.Entry(m)
my_Entry4.grid(row=1,column=4,padx=10,pady=10)

# برای درست کردن دکمه ثبت سایز فونت رنگ اصلی زمینه و دکمه و رنگ دکمه زمانی که روی آن کلیک میشه
button=tk.Button(m,text='ثبت نام',font=50,bg='green',activebackground='blue',fg='white',
                 command=lambda:human_print())
# ابعاد دکمه و جهت قرارگیری
button.grid(row=2,column=3,padx=10,pady=10)

# تابعه ای برام اعمال و ساخت این فرم
def human_print():
    print(my_Entry.get()+' '+my_Entry2.get()+' '+my_Entry3.get()+' '+my_Entry4.get())

#اجرا کن
m.mainloop()
