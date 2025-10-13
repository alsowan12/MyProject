import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_lyrics(line, delay=1.5):
    print(line)
    time.sleep(delay)

def main():
    clear_screen()
    print("🎶 Fall Out Boy - Centuries 🎶\n")
    time.sleep(2)
    print_lyrics("Some legends are told")
    print_lyrics("Some turn to dust or to gold")
    print_lyrics("But you will remember me")

if __name__ == "_main_":
    main()