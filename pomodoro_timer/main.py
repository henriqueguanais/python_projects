#Pomodoro timer
import os 
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
LONG_BREAK_MIN = 15
reps = 0
timer = None
marks = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, marks
    window.after_cancel(timer)
    reps = 0
    marks = ""
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text=marks)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        title_label.config(text="Descanse!", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Relaxe\num pouco", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Trabalhe💪", fg=GREEN)
        count_down(work_sec)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps

    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global marks
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(107, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

button_start = Button(text="Start", bd=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", bd=0, command=reset_timer)
button_reset.grid(column=2, row=2)

checkmark = Label(bg=YELLOW,fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmark.grid(column=1, row=3)

window.mainloop()
