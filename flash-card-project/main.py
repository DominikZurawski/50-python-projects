import json
import random
from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
card = {}
timer = None

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    try:
        data = pd.read_csv("./data/spanish_words.csv")
    except FileNotFoundError:
        print("Not found words file")
    else:
        dictionary = data.to_dict(orient="records")
else:
    dictionary = data.to_dict(orient="records")

new_dictionary = dictionary

def wrong():
    global timer
    window.after_cancel(timer)
    new_card()


def correct():
    global timer, card
    window.after_cancel(timer)
    new_dictionary.remove(card)
    new_card()


def turn_card_over():
    global card, timer
    window.after_cancel(timer)
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=card['English'], fill='white')


# ---------------------------- READ CSV ------------------------------- #
def new_card():
    global card
    card = random.choice(dictionary)
    canvas.itemconfig(title, text='Spanish')
    canvas.itemconfig(word, text=card['Espanol'])
    global timer
    timer = window.after(3000, turn_card_over)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('My Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_path_image = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_path_image, highlightthickness=0, command=wrong)
wrong_btn.config(padx=50, pady=50)
wrong_btn.grid(column=0, row=1)
correct_path_image = PhotoImage(file="./images/right.png")
correct_btn = Button(image=correct_path_image, highlightthickness=0, command=correct)
correct_btn.config(padx=50, pady=50)
correct_btn.grid(column=1, row=1)

new_card()

window.mainloop()

pd.DataFrame(new_dictionary).to_csv(path_or_buf="./data/words_to_learn.csv", index=False)
