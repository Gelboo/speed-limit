from Tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.bind('<Escape>', lambda e: root.quit())
root.attributes('-fullscreen', True)
root.configure(background='blue')

img = ImageTk.PhotoImage(file='imgOriginalScene.png')
img_panel = Label(root)
img_panel.place(x=500,y=100,width=1000,height=600)
img_panel.config(image=img)

img_plate = ImageTk.PhotoImage(file='imgPlate.png')
img_plate_lbl = Label(root,image=img_plate)
img_plate_lbl.place(x=600,y=750)

img_plate_threshold = ImageTk.PhotoImage(file='imgThresh.png')
img_plate_threshold_lbl = Label(root,image=img_plate_threshold)
img_plate_threshold_lbl.place(x=900,y=750)


original_img_lbl = Label(root,bg='blue',fg='black',text='Original image',font='Calibri 22')
name_lbl=Label(root,bg='blue',fg='black',text='OwnerName\nAhmed',font='Calibri 22',justify=LEFT)
model_lbl=Label(root,bg='blue',fg='black',text='Model\nToyta',font='Calibri 22',justify=LEFT)
Address_lbl=Label(root,bg='blue',fg='black',text='Address\nCalifornia',font='Calibri 22',justify=LEFT)
phone_lbl=Label(root,bg='blue',fg='black',text='Phone\n023576',font='Calibri 22',justify=LEFT)
color_lbl=Label(root,bg='blue',fg='black',text='Color\ngray',font='Calibri 22',justify=LEFT)
licence_num_lbl = Label(root,bg='blue',fg='black',text='LicenceNumber\nU8NTBAD',font='Calibri 22')

original_img_lbl.place(x=900,y=50)
name_lbl.place(x=100,y=100)
model_lbl.place(x=100,y=200)
Address_lbl.place(x=100,y=300)
phone_lbl.place(x=100,y=400)
color_lbl.place(x=100,y=500)
licence_num_lbl.place(x=1300,y=750)

load_img_button = Button(root,text="Load Image",bg='white',fg='blue',font='Calibri 22')
check_button = Button(root,text="Check",bg='white',fg='blue',font='Calibri 22')
exit_button = Button(root,text="Exit",bg='white',fg='blue',font='Calibri 22')

load_img_button.place(x=700,y=900)
check_button.place(x=1000,y=900)
exit_button.place(x=1800,y=1000)

licence_img_lbl = Label(root,text="licence\nimg",bg='blue',fg='black',font='Calibri 14')
threshold_lbl = Label(root,text="threshold\nimg",bg='blue',fg='black',font='Calibri 14')

licence_img_lbl.place(x=500,y=750)
threshold_lbl.place(x=800,y=750)

root.mainloop()
