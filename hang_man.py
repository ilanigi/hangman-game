MAX_TRIES = 6

HANGMAN_ASCII_ART = """  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_  \\
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/""" "\n \n" + str(MAX_TRIES)

YOU_WIN_ASCII_ART = """
 __     __          __          ___       _ _
 \ \   / /          \ \        / (_)     | | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| | |
    | | (_) | |_| |    \  /\  /  | | | | |_|_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_|_)
                                              """

YOU_LOSE_ASCII_ART = """
 __      __                          __
|  \    /  \                        |  \\
 \$$\  /  $$______   __    __       | $$       ______    _______   ______
  \$$\/  $$/      \ |  \  |  \      | $$      /      \  /       \ /      \\
   \$$  $$|  $$$$$$\| $$  | $$      | $$     |  $$$$$$\|  $$$$$$$|  $$$$$$\\
    \$$$$ | $$  | $$| $$  | $$      | $$     | $$  | $$ \$$    \ | $$    $$
    | $$  | $$__/ $$| $$__/ $$      | $$_____| $$__/ $$ _\$$$$$$\| $$$$$$$$ __  __  __
    | $$   \$$    $$ \$$    $$      | $$     \\\\$$    $$|       $$ \$$     \|  \|  \|  \\
     \$$    \$$$$$$   \$$$$$$        \$$$$$$$$ \$$$$$$  \$$$$$$$   \$$$$$$$ \$$ \$$ \$$


                                                                                       """


HANGMAN_PHOTOS = {
1: """      x-------x\n""",
2: """
    x-------x
    |
    |
    |
    |
    |\n""",

3: """
    x-------x
    |       |
    |       0
    |
    |
    |\n""",

4: """
    x-------x
    |       |
    |       0
    |       |
    |
    |\n""",

5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |\n""",

6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |\n""",

7: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |\n"""
}

def print_welcome_screen():
    """
    prints the welcome screen of the game.
    :return: nothing
    """
    print(HANGMAN_ASCII_ART)

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    checks if a given str is a valid letter to guess.
    valid means one letter, alphabetic and wasn't in use
    :param letter_guessed: the word to be checked
    :type letter_guessed: str
    :return: true if is valid, else false
    """
    letter_guessed = letter_guessed.lower()
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and not letter_guessed in old_letters_guessed

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    checks if the user's gussed letter is vaild.
    if the word is not vaild, it prints 'x' and the letters already gussed.
    :param letter_guessed: the new letter that the user is gussed
    :param old_letters_guessed: the list of gussed letters
    :return:True if valid, False if not

    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True

    print('X')
    arrow = ' -> '
    print(arrow.join(sorted(old_letters_guessed))+"\n")
    return False

def show_hidden_word(secret_word, old_letters_guessed):
    """
    shows the game board
    :param secret_word:
    :param old_letters_guessed:
    :return: the hidden word as a sequence of the gussed letters
     and "_" for that none-guessed letters, by the word letters order.
    """
    to_print = ""
    for letter in secret_word:

        if letter == " ":
            to_print = to_print + "  "

        if letter in old_letters_guessed:
            to_print = to_print + letter + " "

        else:
            to_print = to_print + "_ "
    print (to_print+"\n")

def check_win(secret_word, old_letters_guessed):
    """
    checks if every letter in the secret word exists in the list of the guessed letters.
    :param secret_word: the word to guess
    :param old_letters_guessed: list of guessed letters
    :return:
    """
    for letter in secret_word:
        if not letter in old_letters_guessed:
            return False
    return True

def print_hangman(num_of_tries):
    """
    prints a photos of the hangman by the number of the gussed wrong letters
    :param num_of_tries: the number of time the user try to guss a letter and
    was worng.
    :return:
    """
    print(HANGMAN_PHOTOS.get(num_of_tries))

def choose_word(file_path, index):
    """
    choose a word from a txt file og words.
    :param file_path: a txt file with words to be choosen from.
    :param index: place in the file of a choosen letter.
    :return: a tuple of the number of words available to gussed in the file,
    and the word that is in the index that was given.
    """

    word_file = open(file_path, "r")
    all_words_list = word_file.read().split(" ")

    if index == 0:
        index = 1

    word_dict = {}

    for word in all_words_list:
        if word not in word_dict:
            word_dict[word] = word

    word_file.close()

    return len(word_dict), all_words_list[(int(index) - 1) % len(all_words_list)]

def input_word_file():
    print("Welcome to hangman game!")
    file_path = input("please enter file path for words txt file:\n")
    index = input("please enter index of word in the txt file:\n ")

    return choose_word(file_path, index)

# ----------------------------main------------------------------------------#

def main():

    old_letters_guessed = []
    print_welcome_screen()
    secret_word = input_word_file()[1]
    num_of_tries = 1

    print("secret word has been choosen!\n"
          "Let's play!\n")
    print_hangman(num_of_tries)
    while num_of_tries <= MAX_TRIES:
        show_hidden_word(secret_word,old_letters_guessed)
        letter_guessed = input("Enter a letter to guess:\n")

        while not try_update_letter_guessed(letter_guessed,old_letters_guessed):
            "invalid letter enterd. try again."
            letter_guessed = input("Enter a letter to guess:\n")

        if letter_guessed in secret_word:
            print("Correct!\n")

        else:
            print("letter not in secret word...  :(\n")
            num_of_tries += 1
            print_hangman(num_of_tries)

        if check_win(secret_word, old_letters_guessed):
            show_hidden_word(secret_word, old_letters_guessed)
            print(YOU_WIN_ASCII_ART)
            break

    if not check_win(secret_word, old_letters_guessed):
        print(YOU_LOSE_ASCII_ART)
        print("the word was: "+ secret_word)
       
       smile = ""
       
       if true:
        smile = ":)"
         
if __name__ == '__main__':
    main()# hangman-game

