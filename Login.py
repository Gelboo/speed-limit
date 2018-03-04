from Tkinter import *
from PIL import Image, ImageTk
import subprocess
import time
import thread

root = Tk()

def destroy(threadname,delay):
    time.sleep(delay)
    root.destroy()
def openn(threadname,delay):
    time.sleep(delay)
    subprocess.call("python pageuser.py" , shell=True)

def open_user():
    try:
        thread.start_new_thread( destroy, ("Thread-1", 0.4, ) )
        thread.start_new_thread( openn, ("Thread-2", 0, ) )
    except:
        print "Error: unable to start threa"
background_img = ImageTk.PhotoImage(file="bg.jpg")


root.bind('<Escape>', lambda e: root.quit())
root.attributes('-fullscreen', True)
root.configure(background='cyan')

# background_lbl = Label(root)
# background_lbl.config(image = background_img)
# background_lbl.place(x=0,y=0,relwidth=1,relheight=1)


login_button = Button(root,bg='black',fg='white',text="Login As \n Admistrator",font='Calibri 22')
login_button.place(x=800,y=800)

login_button_2 = Button(root,bg='black',fg='white',text="Login As \n User",font='Calibri 22 ',command=open_user)
login_button_2.place(x=1050,y=800)

username_img = ImageTk.PhotoImage(file="user.png")
username_label = Label(root)
username_label.config(image=username_img,bg='cyan')
username_label.place(x=600,y=350,width=128,height=128)

pass_img = ImageTk.PhotoImage(file="pass.png")
password_label = Label(root,bg='cyan')
password_label.config(image=pass_img)
password_label.place(x=600,y=550,width=128,height=128)

username_text = Text(root,font='Calibri 22 ')
username_text.place(x=800,y=400,width=400,height=50)


password_text = Entry(root,font='Calibri 22 ',show="*")
password_text.place(x=800,y=600,width=400,height=50)

root.mainloop()
