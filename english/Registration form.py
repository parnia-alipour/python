import tkinter as tk

m=tk.Tk() # Creating a form
m.geometry('500x200') #Dimensions

lbl=tk.Label(m,text='Name')#name
lbl.grid(row=0,column=1)
my_Entry=tk.Entry(m)
my_Entry.grid(row=0,column=2,padx=10,pady=10)
#The rest are the same.
lbl=tk.Label(m,text='Last name')
lbl.grid(row=1,column=1)
my_Entry2=tk.Entry(m)
my_Entry2.grid(row=1,column=2,padx=10,pady=10)

lbl=tk.Label(m,text='Age')
lbl.grid(row=1,column=3)
my_Entry3=tk.Entry(m)
my_Entry3.grid(row=0,column=4,padx=10,pady=10)


lbl=tk.Label(m,text='job')
lbl.grid(row=0,column=3)
my_Entry4=tk.Entry(m)
my_Entry4.grid(row=1,column=4,padx=10,pady=10)


button=tk.Button(m,text='Show text',font=50,bg='green',activebackground='blue',fg='white',
                 command=lambda:human_print())

# Button dimensions and placement direction
button.grid(row=2,column=3,padx=10,pady=10)

# A function for creating a form.
def human_print():
    print(my_Entry.get()+' '+my_Entry2.get()+' '+my_Entry3.get()+' '+my_Entry4.get())

#run
m.mainloop()
