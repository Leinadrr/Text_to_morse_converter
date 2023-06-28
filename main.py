from morse_to_sounds import *
from source_sound import Signals
from dict import morse_dict


# Asking for text to transform and making it lower case
normal_text = input("Please, write down the text you want to transform in morse code: \n").lower()
coded_text = []
signals = Signals()


# Logic for conversion
for letter in normal_text:
    if letter in morse_dict.keys():
        coded_text.append(morse_dict[letter])
    elif letter == " ":
        coded_text.append(" ")
    else:
        print(f"Sorry {letter} is not a valid character. Please input only normal letters.")
        break


print(f"Your message coded in morse: {' '.join(i for i in coded_text)}")
print("Sounds like this (listen): ♪ ♫ ♪")

play_morse_sound(coded_text)
