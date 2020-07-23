from tkinter import *

root = Tk()
root.title('Calculator')

entry = Entry(root, width=40, bg='aliceblue', borderwidth=5, highlightthickness=0)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def clear():
    entry.delete(0, END)

def neg():
    current = entry.get()
    if float(entry.get()) < 0:
        entry.delete(0, END)
        entry.insert(0, abs(float(current)))
    else:
        entry.insert(0, '-')

def roundnum():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, round(float(current)))

def operator(operation):
    global num1 
    global math
    math = operation
    num1 = entry.get()
    entry.delete(0, END)

def equal():
    num2 = entry.get()
    entry.delete(0, END)
    if math == 'addition':
        ans = float(num1) + float(num2)
    if math == 'subtraction':
        ans = float(num1) - float(num2)
    if math == 'multiplication':
        ans = float(num1) * float(num2)
    if math == 'division':
        ans = float(num1) / float(num2)
    entry.insert(0, ans)

button1 = Button(root, text='1', padx=40, pady=20, command=lambda: click(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: click(2))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: click(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: click(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: click(5))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: click(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: click(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: click(8))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: click(9))
button0 = Button(root, text='0', padx=88, pady=20, command=lambda: click(0))
buttonAdd = Button(root, text='+', padx=40, pady=20, command=lambda: operator('addition'))
buttonSub = Button(root, text='-', padx=40, pady=20, command=lambda: operator('subtraction'))
buttonMul = Button(root, text='x', padx=40, pady=20, command=lambda: operator('multiplication'))
buttonDiv = Button(root, text='/', padx=42, pady=20, command=lambda: operator('division'))
buttonEql = Button(root, text='=', padx=40, pady=20, command=equal)
buttonNeg = Button(root, text='+/-', padx=35, pady=20, command=neg)
buttonDec = Button(root, text='.', padx=42, pady=20, command=lambda: click('.'))
buttonClr = Button(root, text='AC', padx=35, pady=20, command=lambda: clear())
buttonRound = Button(root, text='R', padx=40, pady=20, command=roundnum)

buttonClr.grid(row=1, column=0)
buttonNeg.grid(row=1, column=1)
buttonRound.grid(row=1, column=2)
buttonDiv.grid(row=1, column=3)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
buttonMul.grid(row=2, column=3)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
buttonSub.grid(row=3, column=3)

button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
buttonAdd.grid(row=4, column=3)

button0.grid(row=5, column=0, columnspan=2)
buttonDec.grid(row=5, column=2)
buttonEql.grid(row=5, column=3)

root.mainloop()
