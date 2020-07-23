from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Funny Cat Pics')

img = ImageTk.PhotoImage(Image.open('cat1.jpeg'))
img2 = ImageTk.PhotoImage(Image.open('cat2.jpeg'))
img3 = ImageTk.PhotoImage(Image.open('cat3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('cat4.jpg'))
img5 = ImageTk.PhotoImage(Image.open('cat5.jpg'))

imgLst = [img, img2, img3, img4, img5]

status = Label(root, text='1/' + str(len(imgLst)), bd=1, relief=SUNKEN, anchor=E)

label = Label(image=img)
label.grid(row=0, column=0, columnspan=3)

def view(imgNum):
    global label
    global forwardb
    global backb

    label.grid_forget()
    label = Label(image=imgLst[imgNum-1])
    forwardb = Button(root, text='>>', command=lambda: view(imgNum+1))
    backb = Button(root, text='<<', command=lambda: view(imgNum-1))

    if imgNum==5:
        forwardb = Button(root, text='>>', state=DISABLED)
    elif imgNum==1:
        backb = Button(root, text='<<', state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    backb.grid(row=1, column=0)
    forwardb.grid(row=1, column=2)

    status = Label(root, text=str(imgNum) + '/' + str(len(imgLst)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

backb = Button(root, text='<<', command=view, state=DISABLED)
exitb = Button(root, text='exit', command=root.quit)
forwardb = Button(root, text='>>', command=lambda: view(2))

backb.grid(row=1, column=0)
exitb.grid(row=1, column=1)
forwardb.grid(row=1, column=2)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
