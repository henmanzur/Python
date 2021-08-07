
import tkinter as tk
from PIL import Image, ImageTk
from random import randint
root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=5, rowspan=5)

# logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = tk.Label(root, text="תוכנת לוטומט להגרלת מספרי הלוטו", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)



def LotteryGenerate():
    #############Lines###############
    Line1 = []
    Strong1 = []
    Line2 = []
    Strong2 = []
    Line3 = []
    Strong3 = []
    Line4 = []
    Strong4 = []
    Line5 = []
    Strong5 = []
    Line6 = []
    Strong6 = []
    #################################

    for line in range (0,6):
        number = randint(1,37)
        while number in Line1:
            number = randint(1,37)
        Line1.append(number)

        number2 = randint(1, 37)
        while number2 in Line2:
            number2 = randint(1, 37)
        Line2.append(number2)

        number3 = randint(1, 37)
        while number3 in Line3:
            number3 = randint(1, 37)
        Line3.append(number3)

        number4 = randint(1, 37)
        while number4 in Line4:
            number4 = randint(1, 37)
        Line4.append(number2)

        number5 = randint(1, 37)
        while number5 in Line5:
            number5 = randint(1, 37)
        Line5.append(number5)

        number6 = randint(1, 37)
        while number6 in Line6:
            number6 = randint(1, 37)
        Line6.append(number6)

    for strong in range (1):

        number1 = randint(1,7)
        while number1 in Strong1:
            number1 = randint(1,7)
        Strong1.append(number1)

        number2 = randint(1, 7)
        while number2 in Strong2:
            number2 = randint(1,7)
        Strong2.append(number2)

        number3 = randint(1, 7)
        while number3 in Strong3:
            number3 = randint(1,7)
        Strong3.append(number3)

        number4 = randint(1, 7)
        while number4 in Strong4:
            number4 = randint(1,7)
        Strong4.append(number4)

        number5 = randint(1, 7)
        while number5 in Strong5:
            number5 = randint(1,7)
        Strong5.append(number5)

        number6 = randint(1, 7)
        while number6 in Strong6:
            number6 = randint(1,7)
        Strong6.append(number6)


    # text box
    text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
    text_box.insert(1.0, "--- המספרים שהוגרלו לטופס הלוטומט ---\n---------------------------\nLine 1 : " + str(Line1) + " " + str(Strong1)
                    + "\n---------------------------\n" + "Line 2 : " + str(Line2) + " " + str(Strong2)
                    + "\n---------------------------\n" + "Line 3 : " + str(Line3) + " " + str(Strong3)
                    + "\n---------------------------\n" + "Line 4 : " + str(Line4) + " " + str(Strong4)
                    + "\n---------------------------\n" + "Line 5 : " + str(Line5) + " " + str(Strong5)
                    + "\n---------------------------\n" + "Line 6 : " + str(Line6) + " " + str(Strong6)
                    + "\n---------------------------\n" + " --- ! בהצלחה ---")
    text_box.grid(column=1, row=5)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")

    generate_text.set("הגרל מחדש")


# generate button
generate_text = tk.StringVar()
generate_btn = tk.Button(root, textvariable=generate_text, command=lambda: LotteryGenerate(), font="Raleway",
                       bg="#20bebe", fg="white", height=1, width=15)
generate_text.set("הגרל מספרים")
generate_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=700, height=250)
canvas.grid(columnspan=3)



root.mainloop()