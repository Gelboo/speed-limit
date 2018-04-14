from Tkinter import *
from PIL import Image, ImageTk
import subprocess
import time
import thread
from Database import check1
import tkMessageBox

root = Tk()

def destroy(threadname,delay):
    time.sleep(delay)
    root.destroy()

def openn2(threadname,delay):
    time.sleep(delay)
    subprocess.call("python licenceIdentification.py" , shell=True)

background_img = ImageTk.PhotoImage(file="bg.jpg")

def Check_user():
    t1 = str(username_text.get())
    t2 = str(password_text.get())
    # print type(t1),type(t2)
    if check1(t1,t2):
        try:
            thread.start_new_thread( destroy, ("Thread-1", 0.4, ) )
            thread.start_new_thread( openn2, ("Thread-2", 0, ) )
        except:
            print "Error: unable to start thread"
    else:
        tkMessageBox.showinfo(title="Error", message="Wrong Username Or Password")



root.bind('<Escape>', lambda e: root.quit())
root.attributes('-fullscreen', True)
root.configure(background='cyan')

# background_lbl = Label(root)
# background_lbl.config(image = background_img)
# background_lbl.place(x=0,y=0,relwidth=1,relheight=1)


login_button = Button(root,bg='black',fg='white',text="\n   Login   \n",font='Calibri 22',command=Check_user)
login_button.place(x=900,y=800)

username_img = ImageTk.PhotoImage(file="user.png")
username_label = Label(root)
username_label.config(image=username_img,bg='cyan')
username_label.place(x=600,y=350,width=128,height=128)

pass_img = ImageTk.PhotoImage(file="pass.png")
password_label = Label(root,bg='cyan')
password_label.config(image=pass_img)
password_label.place(x=600,y=550,width=128,height=128)

username_text = Entry(root,font='Calibri 22 ')
username_text.place(x=800,y=400,width=400,height=50)


password_text = Entry(root,font='Calibri 22 ',show="*")
password_text.place(x=800,y=600,width=400,height=50)


root.mainloop()
