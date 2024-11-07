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
REPS = 1
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global TIMER
    global REPS
    REPS = 1
    window.after_cancel(TIMER)
    check_l.config(text="")
    timer_l.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        countdown(work_sec)
        timer_l.config(text="Work", fg=GREEN)
    elif REPS == 2 or REPS == 4 or REPS == 6:
        countdown(short_break)
        timer_l.config(text="Break", fg=PINK)
    else:
        countdown(long_break)
        timer_l.config(text="Break", fg=RED)
    REPS += 1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)

    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif len(str(count_sec)) < 2:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count - 1)
    elif count == 0:
        start_timer()
        if REPS / 2 == 1:
            check_l.config(text="✔")
        elif REPS / 2 == 2:
            check_l.config(text="✔ ✔")
        elif REPS / 2 == 3:
            check_l.config(text="✔ ✔ ✔")
        elif REPS / 2 == 4:
            check_l.config(text="✔ ✔ ✔ ✔")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Label

timer_l = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
timer_l.grid(column=1, row=0)

check_l = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_l.grid(column=1, row=4)

#Buttons

start_b = Button(text="Start", command=start_timer)
start_b.grid(column=0, row=3)

reset_b = Button(text="Reset", command=reset_timer)
reset_b.grid(column=3, row=3)

window.mainloop()
