from tkinter import *
import pandas
import random

# Stała definiująca kolor tła okna
BACKGROUND_COLOR = "#B1DDC6"
# Słownik przechowujący aktualną kartę i słowa do nauki
current_card = {}
to_learn = {}

# Próba wczytania pliku CSV z danymi do nauki, jeśli plik nie istnieje, używane są dane oryginalne
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/spain_words.csv")
    to_learn = original_data.to_dict("records")
else:
    to_learn = data.to_dict(orient='records')

# Funkcja wyświetlająca następną kartę
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Hiszpański", fill="black")
    canvas.itemconfig(card_word, text=current_card["Hiszpański"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

# Funkcja odwracająca kartę
def flip_card():
    canvas.itemconfig(card_title, text="Polski", fill="white")
    canvas.itemconfig(card_word, text=current_card["Polski"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

# Funkcja usuwająca wyraz z listy "do nauki" i przechowująca zmiany w pliku CSV
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv", index=False)
    next_card()

# Inicjalizacja okna Tkinter
window = Tk()
window.title("Fiszki")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Ustawienie timera do automatycznego odwracania karty po 3 sekundach
flip_timer = window.after(3000, func=flip_card)

# Inicjalizacja płótna dla kart
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Inicjalizacja przycisku "Nieznane"
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# Inicjalizacja przycisku "Znane"
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0,  command=is_known)
known_button.grid(row=1, column=1)

# Wyświetlenie pierwszej karty
next_card()

# Rozpoczęcie głównej pętli Tkinter
window.mainloop()
