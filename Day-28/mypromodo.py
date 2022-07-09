import math
from tkinter import *

# ------------------------------CONSTANT--------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ------------------------------TIMER RESET--------------------#
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0


# ------------------------------TIMER MECHANISM--------------------#
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="work", fg=GREEN)


# ------------------------------COUNTDOWN MECHANISM--------------------#
def count_down(count):
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            check_mark +="✔"
        check_label.config(text=check_mark)

# ------------------------------UI SETUP--------------------#
window = Tk()
window.title("My Promodoro Program")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_image)
canvas.grid(row=1, column=1)

timer_text = canvas.create_text(102, 130, text=f"00:00", fill="white", font=(FONT_NAME, 30, "bold"))

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, bg=YELLOW, font=(FONT_NAME, 24, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, bg=YELLOW, font=(FONT_NAME, 24, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
check_label.grid(row=3, column=1)

window.mainloop()
