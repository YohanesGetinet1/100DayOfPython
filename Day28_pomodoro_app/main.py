#!/usr/bin/python3

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetition = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_button():
    window.after_cancel(timer)
    label.config(text="Timer", font=(FONT_NAME, 35,), fg=GREEN, bg=YELLOW)
    button.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global repetition
    repetition = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_button():
    global repetition
    repetition += 1
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if repetition % 8 == 0:
        timer_counter(long_break)
        label.config(text="Enjoy Break 😃!", fg=RED, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
    elif repetition % 2 == 0:
        timer_counter(break_sec)
        label.config(text="Enjoy Break!😃", fg="#0066ff", bg=YELLOW, font=(FONT_NAME, 30, "bold"))
    else:
        timer_counter(work_sec)
        label.config(text=" Focus Work!🏁", fg="#e100ff", bg=YELLOW, font=(FONT_NAME, 30, "bold"))


# def reset_button():

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer_counter(count):
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        global timer
        timer = window.after(1000, timer_counter, count - 1)
    else:
        start_button()
        session = " "
        work_rep = math.floor(repetition / 2)
        for x in range(work_rep):
            session += "✔"
        button.config(text=session, font=20)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("🇪🇹 Timer 🇪🇹")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
picture = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=picture)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", font=(FONT_NAME, 35,), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

button = Button(fg=GREEN, bg=YELLOW)
button.grid(column=1, row=3)

button2 = Button(text="Reset", fg=PINK, activeforeground=RED, font=(FONT_NAME, 15, "bold"), highlightthickness=0,
                 command=reset_button)
button2.grid(column=2, row=2)

button3 = Button(text="Start", fg=PINK, activeforeground=RED, font=(FONT_NAME, 15, "bold"), highlightthickness=0,
                 command=start_button)
button3.grid(column=0, row=2)

window.mainloop()
