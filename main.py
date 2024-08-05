from tkinter import *
import tkinter
import tkinter.font as tkFont
from PIL import ImageFont
import random
import ctypes


def key_press(event=None):
    try:
        if event.char.lower() == label_right.cget('text')[0].lower():  # check the key pressed with the current letter
            # delete the current letter from the right side
            label_right.configure(text=label_right.cget("text")[1:])

            # add the current letter to the left side
            label_left.configure(text=label_left.cget('text') + event.char.lower())

            # set the next current letter
            current_letter.configure(text=label_right.cget('text')[0])

    except tkinter.TclError:
        pass


def add_second():
    # subtract a second from the timer
    global timer
    timer += 1
    time_left.configure(text=f"{timer} seconds")

    if writeable:
        window.after(1000, add_second)


def restart():
    # destroy all widgets
    for widgets in window.winfo_children():
        widgets.destroy()

    # reset the window
    reset_window()


def stop_app():
    global writeable
    writeable = False

    # get the amount of words typed
    amount_of_words = len(label_left.cget('text').split(" "))

    # destroy unnecessary widgets
    for widgets in window.winfo_children():
        widgets.destroy()

    # display typing speed (wpm)
    global speed
    speed = Label(window, text=f"{amount_of_words} WPM!", fg="black")
    speed.place(relx=0.5, rely=0.4, anchor=CENTER)

    global reset_button
    restart_button = Button(window, text="Restart", command=restart)
    restart_button.place(relx=0.5, rely=0.6, anchor=CENTER)


def reset_window():
    # List of Text
    possible_text = [
        'For writers, a random sentence can help them get their creative juices flowing. Since the topic of the sentence is completely unknown, it forces the writer to be creative when the sentence appears. There are a number of different ways a writer can use the random sentence for creativity. The most common way to use the sentence is to begin a story. Another option is to include it somewhere in the story. A much more difficult challenge is to use it to end a story. In any of these cases, it forces the writer to think creatively since they have no idea what sentence will appear from the tool.',
        'The goal of Python Code is to provide Python tutorials, recipes, problem fixes and articles to beginner and intermediate Python programmers, as well as sharing knowledge to the world. Python Code aims for making everyone in the world be able to learn how to code for free. Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.',
        'As always, we start with the imports. Because we make the UI with tkinter, we need to import it. We also import the font module from tkinter to change the fonts on our elements later. We continue by getting the partial function from functools, it is a genius function that excepts another function as a first argument and some args and kwargs and it will return a reference to this function with those arguments. This is especially useful when we want to insert one of our functions to a command argument of a button or a key binding.'
    ]

    # Choose random text from text list
    text = random.choice(possible_text).lower()

    # text split point
    split_point = 0

    # The left label will have the already typed text
    global label_left
    label_left = Label(window, text=text[0:split_point], fg="grey")
    label_left.place(relx=0.5, rely=0.5, anchor=E)

    # The right label will have the text to be typed next
    global label_right
    label_right = Label(window, text=text[split_point:])
    label_right.place(relx=0.5, rely=0.5, anchor=W)

    # Display current letter to be typed
    global current_letter
    current_letter = Label(window, text=text[split_point], fg="grey")
    current_letter.place(relx=0.5, rely=0.6, anchor=N)

    # display time remaining
    global time_left
    time_left = Label(window, text=f"0 seconds", fg="grey")
    time_left.place(relx=0.5, rely=0.4, anchor=S)

    global writeable
    writeable = True
    window.bind("<Key>", key_press)

    global timer
    timer = 0

    # binding calls to function after a certain amount of time
    window.after(60000, stop_app)
    window.after(1000, add_second)


ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Create window
window = Tk()
window.geometry('700x700')
window.title("Typing Speed Test")

# Load custom font's path
font_path = "ThaleahFat.ttf"

# Use PIL to load the custom font
custom_font = ImageFont.truetype(font_path, size=30)

# Register the custom font with Tkinter
font = tkFont.Font(family=custom_font.getname()[0], size=30)

# set custom font
window.option_add("*Font", font)

reset_window()

window.mainloop()