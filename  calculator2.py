from tkinter import *

root = Tk()
root.title("Diva Calculator")
root.geometry("320x500")
root.configure(bg="#ff69b4")

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = StringVar()

display = Entry(
    root,
    textvariable=equation,
    font=("Arial", 24),
    justify="right",
    bd=5
)
display.pack(fill="x", padx=20, pady=20)

buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+']
]

for row in buttons:
    frame = Frame(root, bg="#ff69b4")
    frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            Button(
                frame,
                text=btn,
                font=("Arial",18),
                bg="#ff1493",
                fg="white",
                command=equal
            ).pack(side="left", expand=True, fill="both", padx=3, pady=3)

        else:
            Button(
                frame,
                text=btn,
                font=("Arial",18),
                bg="#ffe4ec",
                command=lambda x=btn: press(x)
            ).pack(side="left", expand=True, fill="both", padx=3, pady=3)

Button(
    root,
    text="AC",
    font=("Arial",18),
    bg="#ffc0cb",
    command=clear
).pack(fill="x", padx=20, pady=10)

root.mainloop()