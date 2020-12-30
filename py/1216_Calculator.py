from tkinter import *

window = Tk( )
window.title("계산기 만들기")

e = Entry(window, width=40, bg="black", fg="white", bd=20)
e.grid(row=0, column=0, columnspan=5)

buttons = [
    '0','1','2','+','%',
    '3','4','5','-','//',
    '6','7','8','*','**',
    '9','.','=','/','C' ]

def click(key) :
    if key == '=':
        result = eval(e.get())
        s = str(result)
        e.delete(0, END)
        e.insert(0, s)
    elif key == 'C':
        e.delete(0, END)
    else:
        e.insert(END, key)

row=1
col=0
for text in buttons:
            def process(t=text):
                    click(t)
            b=Button(window, text=text, width=7, height=3, command=process)
            b.grid(row=row, column=col)
            col += 1
            if col>3:
                row += 1
                col = 0
