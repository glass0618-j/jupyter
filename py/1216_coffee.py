from tkinter import *

window = Tk( )
window.title("커피 자동 주문기")
e = Entry(window, width=40, bg='black', fg='white', bd=5)
e.grid(row=0, column=0, columnspan=3)

buttons = [
    'Americano(hot)','Caffè latte(hot)','Cappuccino(hot)',
    'Americano(ice)','Caffè latte(ice)','Cappuccino(ice)',
    'Caramel macchiato','Hot chocolate','Lemonade',
    'Grapefruit ade','Order','Cancel']

def click(key):
    if key == 'Order':
        result = eval(e.get())
        s = str(result)
        s += ' 원을 결제하세요.'
        e.delete(0, END)
        e.insert(0, s)
        
    elif key == 'Cancel':
        e.delete(0, END)
        
    else:
        if key == 'Americano(hot)' or key == 'Hot chocolate':
            cost = '3000'
        else: cost = '4000'
        if e.get( ) != "":
            s = "+" +cost
            e.insert(END, s)
        else: e.insert(END, cost)


row=1
col=0
for text in buttons:
            def process(t=text):
                    click(t)
            b=Button(window, text=text, width=15, height=3, command=process)
            b.grid(row=row, column=col)
            col += 1
            if col>3:
                row += 1
                col = 0
