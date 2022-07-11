import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ----------------------------work on Buttons----------------------------#
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(old_image, image=front_img)
    flip_timer = window.after(3000, func=change_flash_card)


# ---------------------------Change Flash Card----------------------------#
def change_flash_card():
    canvas.itemconfig(old_image, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# --------------------------is Known Flash Card---------------------------#
def is_known():
    to_learn.remove(current_card)
    word_to_learn = pd.DataFrame(to_learn)
    word_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# --------------------------UI SETUP------------------------------------#
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=change_flash_card)

wrong_button_img = PhotoImage(file="./images/wrong.png")
right_button_img = PhotoImage(file="./images/right.png")
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526)
old_image = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "bold"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

right_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
