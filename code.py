``` py

import random

class HangmanGame:
    def _init_(self, words, max_incorrect_guesses=6):
        self.words = words
        self.word = random.choice(words).lower()
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = max_incorrect_guesses

    def display_word(self):
        display = [letter if letter in self.guessed_letters else '_' for letter in self.word]
        return " ".join(display)

    def display_game_status(self):
        print("\nCurrent word:", self.display_word())
        print("Incorrect guesses:", self.incorrect_guesses)
        print("Guessed letters:", ", ".join(self.guessed_letters))
        print(f"Guesses left: {self.max_incorrect_guesses - self.incorrect_guesses}")

    def make_guess(self, guess):
        if guess in self.guessed_letters:
            print("You have already guessed that letter. Try again.")
        elif guess in self.word:
            self.guessed_letters.add(guess)
        else:
            self.incorrect_guesses += 1
            print(f"Incorrect guess. You have {self.max_incorrect_guesses - self.incorrect_guesses} guesses left.")

    def play(self):
        print("Welcome to Hangman!")
        while True:
            self.display_game_status()

            if set(self.word) == self.guessed_letters:
                print("Congratulations! You guessed the word correctly!")
                break

            if self.incorrect_guesses >= self.max_incorrect_guesses:
                print("Game Over! You have reached the maximum number of incorrect guesses.")
                print("The word was:", self.word)
                break

            guess = input("Guess a letter: ").lower()

            if self.is_valid_guess(guess):
                self.make_guess(guess)
            else:
                print("Invalid input. Please enter a single letter.")

    def is_valid_guess(self, guess):
        return guess.isalpha() and len(guess) == 1

if _name_ == "_main_":
    words_to_guess = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    hangman_game = HangmanGame(words_to_guess)
    hangman_game.play()
```
