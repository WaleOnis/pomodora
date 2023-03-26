from tkinter import *
import math

# ---------------------------- MY CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
laps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_the_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_id_label.config(text="Timer")
    check_marks.config(text="")
    global laps
    laps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global laps
    laps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if laps % 8 == 0:
        count_down(long_break_sec)
        timer_id_label.config(text="Long Break", fg=RED)
    elif laps % 2 == 0:
        count_down(short_break_sec)
        timer_id_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_id_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        c_marks = ""
        working_sessions = math.floor(laps/2)
        for _ in range(working_sessions):
            c_marks += "✔"
        check_marks.config(text=c_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodora")
window.config(padx=105, pady=50, bg=YELLOW)

# create label

timer_id_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
timer_id_label.grid(row=0, column=1)

# create a canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

# create start button widget
start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

# create reset button widget
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_the_time)
reset_button.grid(row=2, column=2)

# create a check mark
check_marks = Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)

window.mainloop()