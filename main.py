import random
import PySimpleGUI as sg

def get_guess():
    """Отримати вгадане число від користувача"""
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Вихід':
            return None
        guess = int(values[0])
        if guess < number_to_guess:
            sg.popup("Завелике! Спробуйте ще раз.")
        elif guess > number_to_guess:
            sg.popup("Замале! Спробуйте ще раз.")
        else:
            return guess

def guess_the_number():
    """Головна функція програми"""
    number_to_guess = random.randint(1, 100)

    layout = [[sg.Text("Введіть число від 1 до 100:")],
              [sg.Input()],
              [sg.Button('Перевірити'), sg.Button('Вихід')]]

    window = sg.Window('Вгадай число', layout)

    guess = get_guess()
    while guess is not None and guess != number_to_guess:
        guess = get_guess()

    if guess == number_to_guess:
        sg.popup("Вітаємо! Ви вгадали число.")

    window.close()

if __name__ == "__main__":
    guess_the_number()
