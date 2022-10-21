from tkinter import *
import random
import time

attempts = 20
limit = random.randint(0,999)
answer = random.randint(0, limit)


def check_answer():
    global attempts
    global text

    attempts -= 1

    guess = int(my_entry.get())

    if attempts == 0:
        text.set("Awww! You are out of attempts")
        check_btn.pack_forget()

    elif guess > answer:
        time.sleep(0.5)
        if guess > limit:
            time.sleep(0.5)
            text.set("Hmmm.....Your guess is out of bound, guess again. you have " + str(attempts) + " attempts left.")
        else:
            text.set("Incorrect! You have " + str(attempts) + " attempts left. Your guess is too high!!")

    elif guess < answer:
        time.sleep(0.5)
        text.set("Incorrect! You have " + str(attempts) + " attempts left. Your guess is too low!!")

    elif answer == guess:
        time.sleep(0.5)
        text.set("Right guess!")
        check_btn.pack_forget()

    return


root = Tk()
root.geometry("650x400")
root.title("Number Guessing Game")
root.configure(bg="sky blue")

label_head = Label(root, text="JUST HOW GOOD ARE YOU AT GUESSING?", font=("arial", 18, "bold"), bg="sky blue")
label_head.pack(pady=20, padx=50)

label = Label(root, text=f"Guess a number between 0 and {limit}", font=("arial", 15, "bold"), bg="sky blue")
label.pack(pady=50, padx=10)

my_entry = Entry(root, width=40)
my_entry.pack(pady=20)

check_btn = Button(root, text="Check", command=check_answer, width=20)
check_btn.pack(pady=15)

text = StringVar()
text.set("You have 20 attempts! Good luck!")

guess_attempts = Label(root, textvariable=text, bg="sky blue")
guess_attempts.pack()

root.mainloop()