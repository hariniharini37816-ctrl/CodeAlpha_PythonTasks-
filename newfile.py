# hangman.py
import random

WORDS = ["apple", "banana", "orange", "mango", "peach"]

def choose_word():
    return random.choice(WORDS)

def display_progress(secret, correct_guesses):
    return " ".join([c if c in correct_guesses else "_" for c in secret])

def play():
    secret = choose_word()
    correct = set()
    wrong = set()
    max_wrong = 6

    print("Welcome to Hangman!")
    while True:
        print("\nWord:", display_progress(secret, correct))
        print(f"Wrong guesses ({len(wrong)}/{max_wrong}):", " ".join(sorted(wrong)))
        guess = input("Enter one letter: ").strip().lower()
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in correct or guess in wrong:
            print("You already guessed that letter.")
            continue
        if guess in secret:
            correct.add(guess)
            print("Good!")
        else:
            wrong.add(guess)
            print("Wrong!")
        # win check
        if all(c in correct for c in secret):
            print("\nCongratulations! The word was:", secret)
            break
        if len(wrong) >= max_wrong:
            print("\nGame over. The word was:", secret)
            break

if __name__ == "__main__":
    play()