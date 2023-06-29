import time
import contextlib
with contextlib.redirect_stdout(None):
    import pygame


# Audio play configuration
pygame.mixer.init()
pygame.mixer.set_num_channels(1)
audio_channel = pygame.mixer.Channel(0)

# Dot and dash duration in seconds
DOTS_DURATION = 0.1
SPACE_BETWEEN_SYMBOLS = 0.15
SPACE_BETWEEN_WORDS = 0.6


# Function to play dot sound
def play_dot():
    pygame.mixer.Sound("sounds/dot.wav").play()
    time.sleep(DOTS_DURATION + 0.02)


# Function to play dash sound
def play_dash():
    pygame.mixer.Sound("sounds/dash.wav").play()
    time.sleep(0.2)


# Function to play silences between words
def play_silence():
    time.sleep(SPACE_BETWEEN_WORDS)


# Plays sounds for each element
def play_morse_sound(codex_text):
    for element in codex_text:
        for symbol in element:
            if symbol == ".":
                play_dot()
            elif symbol == "-":
                play_dash()
            elif symbol == " ":
                time.sleep(SPACE_BETWEEN_WORDS)
        time.sleep(SPACE_BETWEEN_SYMBOLS)
