from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

root=Tk()
root.title("LACE Tool")
root.geometry('1000x400')

length=IntVar()
admission=IntVar()
c1=IntVar()
c2=IntVar()
c3=IntVar()
c4=IntVar()
c5=IntVar()

def clicked():
    result=length.get()
    if(result<5):
        summary="Low"
    elif(result<10):
        summary="Moderate"
    else:
        summary="High"
    messagebox.showinfo("LACE Score" , "Score : "+str(result)+"; Condition : "+str(summary))


lbl=Label(root,text="Select Maximum Number of Days Stayed",foreground="black",background="white")

lr1 = Radiobutton(root,text='1', value=1, variable=length)
lr2 = Radiobutton(root,text='2', value=2, variable=length)
lr3 = Radiobutton(root,text='3', value=3, variable=length)
lr4 = Radiobutton(root,text='6', value=4, variable=length)
lr5 = Radiobutton(root,text='13', value=5, variable=length)
lr6 = Radiobutton(root,text='more than 14', value=7, variable=length)


btn = Button(root, text="Get Result", command=clicked)

lbl.grid(column=0,row=1)
lr1.grid(column=1,row=1)
lr2.grid(column=1,row=2)
lr3.grid(column=1,row=3)
lr4.grid(column=1,row=4)
lr5.grid(column=1,row=5)
lr6.grid(column=1,row=6)

root.mainloop()
