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

abl=Label(root,text="Is the patient admitted through Emergency Block ?",foreground="black",background="white")

ar1=Radiobutton(root,text="Yes", value=3 , variable=admission)
ar2=Radiobutton(root,text="No", value=0 ,variable=admission)

abl.grid(column=0,row=8)
ar1.grid(column=1,row=8)
ar2.grid(column=1,row=9)

c0bl=Label(root,text="For the following Enter 1 if the disease/disorder applicable else 0",foreground="black",background="white")
c1bl=Label(root,text="Myocardial Infaction ,Cerebrovascular Disease , Vascular Disease , Diabetes without complications")
c2bl=Label(root,text="Cogestive Heartfailure , Diabetes with end organ damage , Chronic Pulmonary Disease , Mid Liver or Renal Disease , Any Tumour")
c3bl=Label(root,text="Dementia , Connective Tissue Disease")
c4bl=Label(root,text="AIDS , Severe Liver or Renal Disease")
c5bl=Label(root,text="Metastatic Solid Tumor")

c1e=Entry(root,width=10)
c2e=Entry(root,width=10)
c3e=Entry(root,width=10)
c4e=Entry(root,width=10)
c5e=Entry(root,width=10)


c0bl.grid(column=0,row=11)
c1bl.grid(column=0,row=12)
c2bl.grid(column=0,row=13)
c3bl.grid(column=0,row=14)
c4bl.grid(column=0,row=15)
c5bl.grid(column=0,row=16)

c1e.grid(column=1,row=12)
c2e.grid(column=1,row=13)
c3e.grid(column=1,row=14)
c4e.grid(column=1,row=15)
c5e.grid(column=1,row=16)

root.mainloop()
