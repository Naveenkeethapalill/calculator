
from  tkinter import*
x=Tk()
x.geometry("200x200")
def clicked(num):
    first_num=txt1.get()
    txt1.delete(0,END)
    txt1.insert(0,str(first_num)+str(num))
def add():
    first_number=txt1.get()
    global old_value
    old_value=int(first_number)
    global math
    math="addition"
    txt1.delete(0,END)
def sub():
    frist_number=txt1.get()
    global old_value
    old_value=int(frist_number)
    global math
    math="sub"
    txt1.delete(0,END)
def mul():
    frist_number=txt1.get()
    global old_value
    old_value=int(frist_number)
    global math
    math="mul"
    txt1.delete(0,END)
def div():
    frist_number=txt1.get()
    global old_value
    old_value=int(frist_number)
    global math
    math="div"
    txt1.delete(0,END)
def clr():
    txt1.delete(0,END)
def equal():
    if math=="addition":
            new_value=txt1.get()
            txt1.delete(0,END)
            txt1.insert(0,int(old_value)+int(new_value))
    elif math=="sub":
            new_value=txt1.get()
            txt1.delete(0,END)
            txt1.insert(0,int(old_value)-int(new_value))
    elif math=="mul":
           new_value=txt1.get()
           txt1.delete(0,END)
           txt1.insert(0,int(old_value)*int(new_value))
    else:
        new_value=txt1.get()
        txt1.delete(0,END)
        txt1.insert(0,int(old_value)/int(new_value))
txt1=Entry(x)
lbl1=Label(x, text="enter numbers")
btn1=Button(x, text="1",command=lambda:clicked(1))
btn2=Button(x, text="2", command=lambda:clicked(2))
btn3=Button(x, text="3", command=lambda:clicked(3))
btn4=Button(x, text="4",command=lambda:clicked(4) )
btn5=Button(x, text="5", command=lambda:clicked(5))
btn6=Button(x, text="6", command=lambda:clicked(6))
btn7=Button(x, text="7", command=lambda:clicked(7))
btn8=Button(x, text="8", command=lambda:clicked(8) )
btn9=Button(x, text="9", command=lambda:clicked(9))
btn10=Button(x, text="0", command=lambda:clicked(0))
btn11=Button(x, text="+", command=add)
btn12=Button(x, text="-", command=sub)
btn13=Button(x, text="x", command=mul)
btn14=Button(x, text="/", command=div)
btn15=Button(x, text="=", command=equal)
btn16=Button(x, text="CLR", command=clr)
txt1.place(x=40,y=0)
btn1.place(x=40,y=30)
btn2.place(x=40,y=60)
btn3.place(x=40,y=90)
btn4.place(x=70,y=30)
btn5.place(x=70,y=60)
btn6.place(x=70,y=90)
btn7.place(x=100,y=30)
btn8.place(x=100,y=60)
btn9.place(x=100,y=90)
btn10.place(x=100,y=120)
btn11.place(x=130,y=60)
btn12.place(x=130,y=90)
btn13.place(x=130,y=30)
btn14.place(x=40,y=120)
btn15.place(x=70,y=120)
btn16.place(x=100,y=120)
mainloop()