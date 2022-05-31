from tkinter import *
import customtkinter
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

reps = 0
time = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    app.after_cancel(time)
    canvas.itemconfig(timer_text, text='00:00')
    timer.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps = reps + 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", text_color=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", text_color=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global time
        time = app.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check.config(text="✓")


# ---------------------------- UI SETUP ------------------------------- #
customtkinter.set_appearance_mode("default")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.title("Pomodoro Timer")
app.config(padx=100, pady=50, bg=YELLOW)
timer = customtkinter.CTkLabel(master=app, text="Timer", text_color=GREEN, text_font=(FONT_NAME, 45, 'bold'))
canvas = Canvas(width=300, height=300, bg=YELLOW, border=0, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=photo)
timer_text = canvas.create_text(150, 170, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)
button = customtkinter.CTkButton(master=app, text="Start", command=start_timer)
button.grid(row=2, column=0)
button = customtkinter.CTkButton(master=app, text="Reset", command=reset_timer)
button.grid(row=2, column=2)
timer.grid(row=0, column=1)
check = customtkinter.CTkLabel(master=app, text="", text_color=GREEN, text_font=(FONT_NAME, 25, 'bold'))
check.grid(row=3, column=1)

app.mainloop()
