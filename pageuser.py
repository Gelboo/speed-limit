from Tkinter import *
from PIL import Image, ImageTk
import random
from Database import insert2
import tkMessageBox

root = Tk()

root.bind('<Escape>', lambda e: root.quit())
root.attributes('-fullscreen', True)
root.configure(background='blue')



def add_car():
    try:
        insert2(Label_txt[0].get(),Label_txt[1].get(),Label_txt[2].get(),Label_txt[3].get(),Label_txt[4].get(),Label_txt[5].get(),Label_txt[6].get(),random.randint(100,500))
        tkMessageBox.showinfo(title="Done", message="Car Added")
    except:
        tkMessageBox.showinfo(title="Error", message="Invalid Data")

labels = ['ID','Name','Model','Address','PhoneNumber','Color','LicensePlate']
Label_txt = [0 for x in labels]
for i,lbl in enumerate(labels):
    Label1 = Label(root,text="Enter your {} : ".format(lbl),font='Calibri 22',bg='blue',fg='black')
    Label1.place(x=400,y=(i+1)*130)

    Label_txt[i] = Entry(root,font='Calibri 22',bg='black',fg='white')
    Label_txt[i].place(x=800,y=(i+1)*130,width=400,height=40)
# print Label_txt
insert = Button(root,text="Insert",bg='white',fg='blue',font='Calibri 22',command=add_car)
insert.place(x=1400,y=900,width=200,height=100)

root.mainloop()
