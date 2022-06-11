from tkinter import *


root= Tk()

root.title("Calcualtor")
root.config(bg='black')
root.iconbitmap('calc.ico')


e =Entry(root,width=25,justify='right',font='{microsoft sans serif} 15 bold',border=0,highlightbackground='white',fg='white',highlightthickness=3,background='black')
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)


#BUtton Click function
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))


#BUTTON FUNCTIONS
def clear():
    e.delete(0, END)

def add():
    firstnum=e.get()
    global f_num,a
    f_num=int(firstnum)
    e.delete(0,END)
    a=1
    

def sub():
    firstnum=e.get()
    global f_num,a
    f_num=int(firstnum)
    e.delete(0,END)
    a=2
    

def mul():
    firstnum=e.get()
    global f_num,a
    f_num=int(firstnum)
    e.delete(0,END)
    a=3
    
def div():
    firstnum=e.get()
    global f_num,a
    f_num=int(firstnum)
    e.delete(0,END)
    a=4
    


def equal():
    second_num=e.get()
    e.delete(0,END)
    if a==1:
        e.insert(0,f_num+int(second_num))
    elif a==2:
        e.insert(0,f_num-int(second_num))
    elif a==3:
        e.insert(0,f_num*int(second_num))
    elif a==4:
        e.insert(0,f_num/int(second_num))
    else:
        print('Invalid operation')

#setting up images
bag=PhotoImage(file='Button.png')
smallbag=PhotoImage(file='funct.png')


#normal btns
button_1= Button(root,image=bag,compound=CENTER,bg='black',border=0,fg='white',text="1",relief='raised',activebackground='black',command=lambda:button_click(1))
button_2= Button(root,image=bag,compound=CENTER,bg='black',border=0,fg='white',text="2",relief='raised',activebackground='black',command=lambda:button_click(2))
button_3= Button(root,image=bag,compound=CENTER,bg='black',border=0,fg='white',text="3",relief='raised',activebackground='black',command=lambda:button_click(3))
button_4= Button(root,image=bag,compound=CENTER,bg='black',border=0,fg='white',text="4",relief='raised',activebackground='black',command=lambda:button_click(4))
button_5= Button(root,image=bag,compound=CENTER,bg='black',border=0,fg='white',text="5",relief='raised',activebackground='black',command=lambda:button_click(5))
button_6= Button(root,image=bag,compound=CENTER,bg='black',border=0,fg='white',text="6",relief='raised',activebackground='black',command=lambda:button_click(6))
button_7= Button(root,image=bag,compound=CENTER,bg='black',border=0,fg='white',text="7",relief='raised',activebackground='black',command=lambda:button_click(7))
button_8= Button(root,image=bag,compound=CENTER,bg='black',border=0,fg='white',text="8",relief='raised',activebackground='black',command=lambda:button_click(8))
button_9= Button(root,image=bag,compound=CENTER,bg='black',border=0,fg='white',text="9",relief='raised',activebackground='black',command=lambda:button_click(9))
button_0= Button(root,image=bag,compound=CENTER,bg='black',border=0,fg='white',text="0",relief='raised',activebackground='black',command=lambda:button_click(0))


#operation btns
button_equal=Button(root,text="=",bg='black',border=0,image=smallbag,compound=CENTER,activebackground='black',foreground='white',command=equal,relief='groove')
button_add= Button(root,text="+",bg='black',border=0,image=smallbag,compound=CENTER,activebackground='black',foreground='white',command= add,relief='groove')
button_clear=Button(root,text='C',border=0,image=smallbag,compound=CENTER,activebackground='black',bg='black',foreground='white',command=clear,relief='groove')
button_sub= Button(root,text="-",bg='black',border=0,image=smallbag,compound=CENTER,activebackground='black',foreground='white',relief='groove',command=sub)
button_mul= Button(root, text="x",relief='groove',border=0,image=smallbag,compound=CENTER,activebackground='black' ,bg='black',foreground='white',command =mul)
button_div= Button(root, text="÷",relief='groove',border=0,image=smallbag,compound=CENTER,activebackground='black', bg='black',foreground='white',command =div)

#placing the button using grid
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)


button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)


button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=2)
button_add.grid(row=4,column=1)
button_equal.grid(row=4,column=3)

button_sub.grid(row=1,column=3)
button_mul.grid(row=2,column=3)
button_div.grid(row=3,column=3)

#binding the buttons
root.bind('1',lambda e:button_click(1))
root.bind('2',lambda e:button_click(2))
root.bind('3',lambda e:button_click(3))
root.bind('4',lambda e:button_click(4))
root.bind('5',lambda e:button_click(5))
root.bind('6',lambda e:button_click(6))
root.bind('7',lambda e:button_click(7))
root.bind('8',lambda e:button_click(8))
root.bind('9',lambda e:button_click(9))
root.bind('0',lambda e:button_click(0))
root.bind('<+>',lambda e:add())
root.bind('-',lambda e:sub())
root.bind('<*>',lambda e:mul())
root.bind('</>',lambda e:div())
root.bind('<Return>',lambda e:equal())
root.bind('<BackSpace>',lambda e:clear())

#some change

root.mainloop()

