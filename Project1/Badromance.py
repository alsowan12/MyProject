# Badromance.py
import sys
import time
import random
import os

LYRICS = [
    
    "You know that I want you",
    "And you know that I need you",
    "I want it bad, your bad romance",
    
    "I want your love and",
    "I want your revenge",
    "You and me could write a bad romance",
    "(Oh-oh-oh--oh-oh!)",
    "I want your love and",
    "All your lovers' revenge",
    "You and me could write a bad romance",
    
    "Oh-oh-oh-oh-oh-oh-oh-oh-oh-oh-oh-oh!",
    "Caught in a bad romance",
    "Oh-oh-oh-oh-oh-oh-oh-oh-oh-oh-oh-oh!",
    "Caught in a bad romance",
    
    "Rah-rah-ah-ah-ah-ah!",
    "Roma-roma-mamaa!",
    "Ga-ga-ooh-la-la!",
    "Want your bad romance",
    
    "I want your horror",
    "I want your design",
    "Cause you're a criminal",
    "As long as your mine",
    "I want your love",
    "(Love-love-love I want your love-uuhh)",
 
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_print(text, base_delay=1.5, jitter=0.5, newline=True):
    """
    Print text like typing on keyboard.
    base_delay: average delay between keystrokes (seconds)
    jitter: random variation added/subtracted from base_delay
    """
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
    
        # simulate human typing variability
        delay = max(0.001, base_delay + random.uniform(-jitter, jitter))
        time.sleep(delay)
    if newline:
        sys.stdout.write("\n")
        sys.stdout.flush()

def slow_print_line_by_line(lines, line_pause=0.8, char_delay=0.03):
    for line in lines:
        # small chance to simulate a short pause mid-line (thinking)
        type_print(line, base_delay=char_delay, jitter=char_delay/2)
        time.sleep(line_pause)

def interactive_mode():
    """
    Let user step through lines by pressing Enter.
    """
    clear_screen()
    print("Interactive typing mode. Tekan Enter untuk menampilkan baris berikutnya, Ctrl+C untuk keluar.\n")
    for line in LYRICS:
        input()  # wait for Enter
        type_print(line, base_delay=1.5, jitter=0.5)

def main():
    clear_screen()
    print("🔤 Simulasi Ketikan Lirik — Original Song (inspired theme)\n")
    print("Pilihan mode:")
    print("1) Otomatis (typing effect, baris demi baris)")
    print("2) Interaktif (tekan Enter untuk setiap baris)")
    print("3) Cepat (lebih cepat)")
    print("Pilih 1/2/3 atau tekan Enter untuk default (1).")
    choice = input("Mode: ").strip()
    print()

    try:
        if choice == "2":
            interactive_mode()
        else:
            if choice == "3":
                # cepat
                slow_print_line_by_line(LYRICS, line_pause=1.5, char_delay=0.5)
            else:
                # default otomatis
                slow_print_line_by_line(LYRICS, line_pause=0.1, char_delay=0.1)

        print("\n— Selesai —")
    except KeyboardInterrupt:
        print("\n(Proses dihentikan oleh pengguna.)")
    except Exception as e:
        print("\nTerjadi error:", e)

if __name__ == "__main__":
    main()
