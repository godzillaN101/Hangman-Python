import random

def get_word():
    words = ["python", "java", "javascript", "godfather", "hangman", "scarlet"]
    word = random.choice(words)
    return word

def play(word):
    word_completion = "_" * len(word)
    gussed = False
    gussed_letters = []
    gussed_words = []
    tries = 7

    print("Let's Play Hangman")
    print_hangman(tries)
    print(word_completion)

    while(tries and not gussed):
        guess = input("Enter a word or character:")
        if len(guess) == 1 and guess.isalpha():
            if guess in gussed_letters:
                print("You have already used this letter, please try another one.")
            elif guess not in word:
                print(guess, " is not in word")
                tries -= 1
                gussed_letters.append(guess)
                print_hangman(tries)
                print(word_completion)
            else:
                print("Good job ", guess, " is in the word")
                word_as_list = list(word_completion)
                for i in range(len(word)):
                    if guess == word[i]:
                        word_as_list[i] = guess
                word_completion = ''.join(word_as_list)
                print_hangman(tries)
                print(word_completion)
                gussed_letters.append(guess)

        elif len(guess) == len(word):
            if(guess == word):
                print("Good job. You have guessed the correct word.")
                word_completion = word
            elif guess in gussed_words:
                print("You have already guessed that word. Please try again.")
            else:
                tries -= 1
                print_hangman(tries)
                print("Oops. Wrong guess.")
                gussed_words.append(guess)

        else:
            print("not a valid guess")

        if "_" not in word_completion:
            gussed = True
    if(tries == 0):
        print("Sorry but you lost.")
    else:
        print("Congratulations!! You have gussed correctly.")

    
def print_hangman(tries):
    stages = [
        # stage 7
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # stage 6
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # stage 5
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
        # stage 4
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |
                   |
                   -
                """,
        # stage 3
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |
                   |
                   -
                """,
        # stage 2
        """
                   --------
                   |      |
                   |      O
                   |     \\
                   |
                   |
                   -
                """,
        # stage 1
        """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
        # stage 0
        """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """,
    ]
    print(stages[tries])
    

word = get_word()
play(word)