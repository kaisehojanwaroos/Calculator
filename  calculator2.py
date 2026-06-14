 from tkinter import *  # imports Tkinter (GUI toolkit)

root = Tk()  # creates main window
root.title("Diva Calculator")  # sets window title
root.geometry("320x500")  # sets window size
root.configure(bg="lightpink")  # sets background color

expression = ""  # stores the math string as user types

def press(num):
    global expression
    expression += str(num)  # adds clicked button value to expression
    equation.set(expression)  # updates display

def equal():
    global expression
    try:
        result = str(eval(expression))  # evaluates math expression
        equation.set(result)  # shows result
        expression = result  # keeps result for further calculations
    except:
        equation.set("Error")  # if invalid input
        expression = ""  # reset expression

def clear():
    global expression
    expression = ""  # clears stored expression
    equation.set("")  # clears display

equation = StringVar()  # connects display text with variable

display = Entry(
    root,
    textvariable=equation,  # links input box to equation variable
    font=("Arial", 24),  # big readable font
    justify="right",  # text aligned to right (calculator style)
    bd=5  # border thickness
)
display.pack(fill="x", padx=20, pady=20)  # places display at top

buttons = [
    ['7','8','9','/'],  # row 1
    ['4','5','6','*'],  # row 2
    ['1','2','3','-'],  # row 3
    ['0','.','=','+']   # row 4
]

for row in buttons:
    frame = Frame(root, bg="#ff69b4")  # container for each row
    frame.pack(expand=True, fill="both")  # makes rows stretch evenly

    for btn in row:
        if btn == "=":
            Button(
                frame,
                text=btn,
                font=("Arial",18),
                bg="#ff1493",  # darker pink for equals button
                fg="white",
                command=equal  # runs calculation
            ).pack(side="left", expand=True, fill="both", padx=3, pady=3)

        else:
            Button(
                frame,
                text=btn,
                font=("Arial",18),
                bg="#ffe4ec",  # light pink buttons
                command=lambda x=btn: press(x)  # sends clicked value
            ).pack(side="left", expand=True, fill="both", padx=3, pady=3)

Button(
    root,
    text="AC",
    font=("Arial",18),
    bg="#ffc0cb",  # reset button color
    command=clear  # clears everything
).pack(fill="x", padx=20, pady=10)

root.mainloop()  # starts the GUI loop (keeps window running)