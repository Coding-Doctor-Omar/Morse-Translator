from dictionary import translate
import time
import os

TITLE = """
┳┳┓         ┏┓   ┓    ┏┳┓       ┓       
┃┃┃┏┓┏┓┏┏┓  ┃ ┏┓┏┫┏┓   ┃ ┏┓┏┓┏┓┏┃┏┓╋┏┓┏┓
┛ ┗┗┛┛ ┛┗   ┗┛┗┛┗┻┗    ┻ ┛ ┗┻┛┗┛┗┗┻┗┗┛┛ 
                                        
"""

OPTIONS = """
*******************
1) Text To Morse
2) Morse To Text
3) Exit
*******************
"""

MORSE_TO_TEXT = """
┳┳┓         ┏┳┓    ┏┳┓     
┃┃┃┏┓┏┓┏┏┓   ┃ ┏┓   ┃ ┏┓┓┏╋
┛ ┗┗┛┛ ┛┗    ┻ ┗┛   ┻ ┗ ┛┗┗
                           
"""

TEXT_TO_MORSE = """
┏┳┓       ┏┳┓    ┳┳┓       
 ┃ ┏┓┓┏╋   ┃ ┏┓  ┃┃┃┏┓┏┓┏┏┓
 ┻ ┗ ┛┗┗   ┻ ┗┛  ┛ ┗┗┛┛ ┛┗ 
                           
"""
def clear_screen():
    """Clears the screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')




def greet_user():
    clear_screen()
    print(TITLE)
    print("\n")
    print(OPTIONS)
    print("\n")

    return input("Choose an option: ").lower()

def text_to_morse():
    """Displays the Text To Morse screen."""

    clear_screen()
    print(TEXT_TO_MORSE)
    print("\n")
    print("Note: The translator only accepts English letters, numbers, and normal punctuation.\nSome symbols such as '%' are not supported.")
    print("\n")

    return input("Enter Text: ").lower()

def morse_to_text():
    """Displays the Morse To Text screen."""

    clear_screen()
    print(MORSE_TO_TEXT)
    print("\n")
    print("Morse Format: Separate letters with space and words with a 'space + slash + space' (' / '). Use '.' for dots and '-' for dashes.")
    print("\n")

    return input("Enter Morse Code: ").lower()



running = True
response = greet_user()

while running:

    if response == "1":
        user_input = text_to_morse()
        result = translate(string=user_input, to="morse")

        if result:
            print(f"\nMorse Code:\n{result}\n")
        else:
            input("Invalid text. Please try again! Press ENTER to retry...")
            continue

        new_response = input("Do you want to translate something else? (y/n): ").lower()

        if new_response == "y":
            response = greet_user()
        else:
            running = False

    elif response == "2":
        user_input = morse_to_text()
        result = translate(string=user_input, to="text")

        if result:
            print(f"\nTranslated Text:\n{result}\n")
        else:
            input("Invalid morse code. Please try again! Press ENTER to retry...")
            continue

        new_response = input("Do you want to translate something else? (y/n): ").lower()

        if new_response == "y":
            response = greet_user()
        else:
            running = False
    elif response == "3":
        running = False

    else:
        input("Invalid option. Press ENTER to try again.")
        clear_screen()
        response = greet_user()
        continue

clear_screen()
print("Bye!")
time.sleep(1)


