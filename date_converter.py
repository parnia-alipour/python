import tkinter as tk
import jdatetime
from datetime import datetime
m=tk.Tk()
def convert_date():
    try:
        day=int(day_entry.get())
        month=int(month_entry.get())
        year=int(year_entry.get())
        d=datetime(year,month,day)
        shamsi=jdatetime.date.fromgregorian(date=d)
        print(shamsi)
        result_label.config(text=f' {shamsi}')
    except Exception as e:
        result_label.config(text=f'ERROR: {e}')
        print(f'error: {e}')

m.title('Convert to Solar Hijri date')
tk.Label(m,text='year:').grid(row=0,column=0)
year_entry=tk.Entry(m)
year_entry.grid(row=0,column=1)

tk.Label(m,text='month:').grid(row=1,column=0)
month_entry=tk.Entry(m)
month_entry.grid(row=1,column=1)

tk.Label(m,text='day:').grid(row=2,column=0)
day_entry=tk.Entry(m)
day_entry.grid(row=2,column=1)

button=tk.Button(m,text='Convert',command=lambda :convert_date(),background='purple',activebackground='black',fg='white',font=('arial',10,'bold'))
button.grid(row=3,column=1)
button.grid(row=3,column=0,columnspan=2)

result_label=tk.Label(m,text='')
result_label.grid(row=4,column=0,columnspan=2)

m.mainloop()