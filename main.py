from tkinter import *
from cards import Cards

BACKGROUND_COLOR = "#B1DDC6"


# -------------------- GENERATE NEW CARDS -------------------- #
def generate_card():
    # Uses ID flip to cancel flip timer
    global flip
    canvas.after_cancel(flip)
    try:
        flash_cards.new_card()
    except IndexError:
        canvas.itemconfig(language, text="You've completed the deck.", fill="black")
        canvas.itemconfig(word, text="Delete './data/words_to_learn.csv' to restart progress", fill="black", font=20)
    else:
        canvas.itemconfig(word, text=f"{flash_cards.french_word}", fill="black")
        canvas.itemconfig(language, text="French", fill="black")
        canvas.itemconfig(card_face, image=flash_cards.card_front)
        canvas.itemconfig(word, text=flash_cards.french_word)
        flip = canvas.after(3000, flip_card)


# -------------------------- FLIP CARD -------------------------- #
def flip_card():
    canvas.itemconfig(word, text=f"{flash_cards.english_word}", fill="white")
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(card_face, image=flash_cards.card_back)


# -------------------------- REMOVE CARD -------------------------- #
def remove_card():
    generate_card()
    try:
        flash_cards.remove_card()
    except ValueError:
        pass


# -------------------------- UI SETUP -------------------------- #
# Window
app = Tk()
app.title("Flashy")
app.minsize(width=900, height=726)
app.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Create cards object, generate card
flash_cards = Cards()

# Flash Card
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_face = canvas.create_image(400, 263, image=flash_cards.card_front)
language = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text=flash_cards.french_word, fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Sets ID for after_cancel
flip = canvas.after(3000, flip_card)

# Wrong button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(command=generate_card, image=wrong_img, highlightthickness=0, padx=0, pady=0)
wrong_button.grid(row=1, column=0)

# Right button
right_img = PhotoImage(file="images/right.png")
right_button = Button(command=remove_card, image=right_img, highlightthickness=0, padx=0, pady=0)
right_button.grid(row=1, column=1)

generate_card()
app.mainloop()
