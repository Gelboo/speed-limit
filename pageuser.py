from Tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.bind('<Escape>', lambda e: root.quit())
root.attributes('-fullscreen', True)
root.configure(background='blue')

licence_lbl = Label(root,text="Enter your licence number: ",font='Calibri 22',bg='blue',fg='black')
licence_lbl.place(x=200,y=200)

licence_txt = Text(root,font='Calibri 22',bg='black',fg='white')
licence_txt.place(x=600,y=200,width=400,height=40)

calculate_button = Button(root,text='Calculate',font='Calibri 22')
calculate_button.place(x=400,y=300)

total_fines_lbl = Label(root,text="Total Fines = ",font='Calibri 22',bg='blue',)
total_fines_lbl.place(x=200,y=400)

total_fines = Label(root,text="1200EGP",font='Calibri 22',bg='blue',fg='red')
total_fines.place(x=400,y=400)

More_info_button = Button(root,text="More Info",bg='black',fg='white',font='Calibri 22')
More_info_button.place(x=400,y=500)

Info_frame = Frame(root)
Info_frame.place(x=200,y=600)

height = 5
width = 4
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(Info_frame, text="",font='Calibri 22',bg='black',fg='yellow')
        b.grid(row=i, column=j,ipadx=10,ipady=20)

mainloop()



root.mainloop()
