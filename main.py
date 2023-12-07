import random

def choose_word():
    # List of words for the game
    words = ["python", "hangman", "programming", "challenge", "developer", "learning"]
    return random.choice(words).upper()

def display_word(word, guessed_letters):
    # Display the word with guessed letters
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # Number of allowed attempts

    while attempts > 0:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"Word: {current_display}")
        print(f"Guessed Letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")

        guess = input("Enter a letter: ").upper()

        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts -= 1

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the player has guessed all letters
        if set(word_to_guess).issubset(set(guessed_letters)):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
