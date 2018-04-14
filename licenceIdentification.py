from Tkinter import *
from PIL import Image, ImageTk
from Main import main
import cv2
import thread
import time
import subprocess
from Database import check2
root = Tk()


def destroy(threadname,delay):
    time.sleep(delay)
    root.destroy()

def openn(threadname,delay):
    time.sleep(delay)
    subprocess.call("python pageuser.py" , shell=True)

def add_Car():
    try:
        thread.start_new_thread( destroy, ("Thread-1", 0.4, ) )
        thread.start_new_thread( openn, ("Thread-2", 0, ) )
    except:
        print "Error: unable to start thread"

root.bind('<Escape>', lambda e: root.quit())
root.attributes('-fullscreen', True)
root.configure(background='blue')

img_panel = Label(root)
img_panel.place(x=500,y=100,width=1000,height=600)

licence_num_lbl = Label(root,bg='blue',fg='black',text='LicenceNumber\n',font='Calibri 22')


# img_plate = ImageTk.PhotoImage(file='imgPlate.png')
# img_plate_lbl = Label(root,image=img_plate)
# img_plate_lbl.place(x=600,y=750)

# img_plate_threshold = ImageTk.PhotoImage(file='imgThresh.png')
# img_plate_threshold_lbl = Label(root,image=img_plate_threshold)
# img_plate_threshold_lbl.place(x=900,y=750)
from tkFileDialog import askopenfilename
filenamee = ""
def load_image():
    global filenamee
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()
    img = ImageTk.PhotoImage(file=filename,size=(10,10))

    img_panel.config(image=img)
    img_panel.image = img
    filenamee = filename
    # print filename

def check_img():
    print "check "+filenamee
    if filenamee == "":
        print "error"
    else:
        result = main(filenamee)



        details = check2(result)
        print "info",details
        if details == []:
            print "Emptyyyyy"
            licence_num_lbl.config(text = 'LicenceNumber\nNOLicense')
            licence_img_lbl.text='LicenceNumber\nNOLicense'

            lic_img = ImageTk.PhotoImage(file='error.png')
            licence_img_lbl.config(image=lic_img)
            licence_img_lbl.image=lic_img

            color_lbl.config(text="Color\n")
            color_lbl.text = "Color\n"

            phone_lbl.config(text="Phone\n")
            phone_lbl.text = "Phone\n"

            Address_lbl.config(text="Address\n")
            Address_lbl.text = "Address\n"

            model_lbl.config(text="Model\n")
            model_lbl.text = "Model\n"

            name_lbl.config(text="OwnerName\n")
            name_lbl.text = "OwnerName\n"

            NationalId.config(text="ID\n")
            NationalId.text = "ID\n"

            TotalFines.config(text="Fines$\n")
            TotalFines.text = "Fines$\n"
        else:
            licence_num_lbl.config(text = 'LicenceNumber\n'+str(result))
            licence_img_lbl.text='LicenceNumber\n'+str(result)

            lic_img = ImageTk.PhotoImage(file='imgPlate.png')
            licence_img_lbl.config(image=lic_img)
            licence_img_lbl.image=lic_img

            color_lbl.config(text="Color\n"+str(details[0][5]))
            color_lbl.text = "Color\n"+str(details[0][5])

            phone_lbl.config(text="Phone\n"+str(details[0][4]))
            phone_lbl.text = "Phone\n"+str(details[0][4])

            Address_lbl.config(text="Address\n"+str(details[0][3]))
            Address_lbl.text = "Address\n"+str(details[0][3])

            model_lbl.config(text='Model\n'+str(details[0][2]))
            model_lbl.text = 'Model\n'+str(details[0][2])

            name_lbl.config(text="OwnerName\n"+str(details[0][1]))
            name_lbl.text = "OwnerName\n"+str(details[0][1])

            NationalId.config(text="ID\n"+str(details[0][0]))
            NationalId.text = "ID\n"+str(details[0][0])

            TotalFines.config(text="Fines$\n"+str(details[0][7]))
            TotalFines.text = "Fines$\n"+str(details[0][7])

def Quit():
    root.destroy()

original_img_lbl = Label(root,bg='blue',fg='black',text='Original image',font='Calibri 22')
name_lbl=Label(root,bg='blue',fg='black',text='OwnerName\n',font='Calibri 22',justify=LEFT)
model_lbl=Label(root,bg='blue',fg='black',text='Model\n',font='Calibri 22',justify=LEFT)
Address_lbl=Label(root,bg='blue',fg='black',text='Address\n',font='Calibri 22',justify=LEFT)
phone_lbl=Label(root,bg='blue',fg='black',text='Phone\n',font='Calibri 22',justify=LEFT)
color_lbl=Label(root,bg='blue',fg='black',text='Color\n',font='Calibri 22',justify=LEFT)
NationalId=Label(root,bg='blue',fg='black',text='ID\n',font='Calibri 22',justify=LEFT)
TotalFines=Label(root,bg='blue',fg='black',text='Fines$\n',font='Calibri 22',justify=LEFT)

original_img_lbl.place(x=900,y=50)
name_lbl.place(x=100,y=200)
model_lbl.place(x=100,y=700)
Address_lbl.place(x=100,y=300)
phone_lbl.place(x=100,y=400)
color_lbl.place(x=100,y=500)
NationalId.place(x=100,y=100)
TotalFines.place(x=100,y=600)
licence_num_lbl.place(x=1300,y=750)

load_img_button = Button(root,text="Load Image",bg='white',fg='blue',font='Calibri 22',command=load_image)
check_button = Button(root,text="Check",bg='white',fg='blue',font='Calibri 22',command = check_img)
exit_button = Button(root,text="Exit",bg='white',fg='blue',font='Calibri 22',command=Quit)

load_img_button.place(x=700,y=900)
check_button.place(x=1000,y=900)
exit_button.place(x=1800,y=1000)

licence_img_lbl = Label(root,text="licence\nimg",bg='blue',fg='black',font='Calibri 14')

licence_img_lbl.place(x=500,y=750)

insert_new_info = Button(root,text="\nAdd Vehicle\n",bg='white',fg='blue',font='Calibri 22',command=add_Car)
insert_new_info.place(x=1600,y=600)


root.mainloop()
