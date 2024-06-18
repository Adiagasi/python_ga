letters_list = []  # List to store guessed letters
WORD = ""  # Variable to store the secret word
#C:\Users\adiag\Downloads\hangMan.txt
# Function to display the game's title
def display_title():
    print("""
    Welcome to the best game-
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |
                       |___/
    """)

# Function to retrieve the secret word from a file at a specified index
def word_hangMan(file, index):
    global WORD
    print("Let’s start!" )
    print_hangman(0)
    with open(file, 'r') as file1:
        words = file1.read().split()
        if 0 <= index - 1 < len(words):
            WORD = words[index - 1]
            num = len(WORD)
            print("_ " * num)
        else:
            print("Index out of range or file not found.")


# Function to display the hidden word with guessed letters
def show_hidden_word(secret_word, old_letters_guessed):
    displayed_word = ""
    for letter in secret_word:
        if letter.lower() in old_letters_guessed:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

# Function to validate the input for a guessed letter
def check_valid_input(letter_guessed, old_letters_guessed):
    if not letter_guessed.isalpha() or len(letter_guessed) > 1 or letter_guessed.lower() in old_letters_guessed or letter_guessed.upper() in old_letters_guessed:
        return False
    else:
        return True

# Function to update the guessed letters and check if the guessed letter is correct
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        letters_list.append(letter_guessed.lower())  # Append lowercase version to maintain uniformity
        if letter_guessed not in WORD.lower():
            if len(old_letters_guessed)>1:
               print(":(\n" + " -> ".join(sorted(old_letters_guessed)))
            return True
        else:
            return False
    else:
        print("X")
        return False


# Function to check if the player has won
def check_win(secret_word, old_letters_guessed):
    return '_' not in show_hidden_word(secret_word, old_letters_guessed)

# Function to print the hangman based on the number of tries
def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {
        "picture 1:": " x-------x",
        "picture 2:": """
        x-------x
        |
        |
        |
        |
        | """, "picture 3: " : """
    x-------x
    |       |
    |       0
    |
    |
    | """, "picture 4:" : """
    x-------x
    |       |
    |       0
    |       |
    |
    | """, "picture 5: ": """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    | """ , "picture 6: ": """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |  """ , "picture 7:" : """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |  """ }

    for key in HANGMAN_PHOTOS.keys():
        if num_of_tries == int(key[8]):
            return HANGMAN_PHOTOS[key]

# Main game function
def main():
    num_of_tries = 1
    display_title()
    file = input("Please enter file path: ")
    index = int(input("Please enter index 1-40: "))  # Convert input to an integer
    word_hangMan(file, index)

    while num_of_tries < 6:
        letter = input("Guess a letter: ")
        if try_update_letter_guessed(letter, letters_list):
            print(print_hangman(num_of_tries+1))
            print("Attempts left:", 5 - num_of_tries)
            num_of_tries += 1
        print(show_hidden_word(WORD, letters_list))
        if check_win(WORD, letters_list):
            print("WIN")
            break
        if num_of_tries == 6:
            print("LOSE\nThe word is "+WORD)

if __name__ == "__main__":
    main()
