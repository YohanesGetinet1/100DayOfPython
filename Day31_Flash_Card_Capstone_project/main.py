from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
word = {}
to_learn = {}

try:
    data = pd.read_csv("data/known_words.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:

    to_learn = data.to_dict(orient="records")


def random_words():
    global word
    global timer
    window.after_cancel(timer)
    word = random.choice(to_learn)
    french_word = word["French"]
    canvas.itemconfig(card_title, text="French word", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(front_image, image=front_pic)
    timer = window.after(3000, func=flip_card)


def flip_card():
    english_word = word["English"]
    canvas.itemconfig(card_title, text="English word", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(front_image, image=back_pic, )


def is_know():
    to_learn.remove(word)
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("data/known_words.csv", index=False)
    random_words()


window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

back_pic = PhotoImage(file="images/card_back.png")
front_pic = PhotoImage(file="images/card_front.png")

front_image = canvas.create_image(400, 263, image=front_pic)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Aerial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_pic = PhotoImage(file="images/right.png")
right_button = Button(image=right_pic, highlightthickness=0, command=is_know)
right_button.grid(column=1, row=1)

wrong_pic = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_pic, highlightthickness=0, command=random_words)
wrong_button.grid(column=0, row=1)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
random_words()
window.mainloop()
