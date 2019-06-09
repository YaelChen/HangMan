HANGMAN_PHOTOS = {
    0: """x-------x 
| 
| 
|
|
|\n""",
    1: """x-------x 
|       | 
|       0 
|
|
|\n""",
    2: """x-------x 
|       | 
|       0 
|       |
|
|\n""",
    3: """x-------x 
|       | 
|       0 
|      /|
| 
|\n""",
    4: """x-------x 
|       | 
|       0 
|      /|\ 
|
|\n""",
    5: """x-------x 
|       | 
|       0 
|      /|\ 
|      /
|\n""",
    6: """x-------x 
|       | 
|       0 
|      /|\ 
|      / \ 
|\n"""
}
try_no = 0
MAX_TRIES = 6


def headline():
    print("""      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/""")
    print(MAX_TRIES)


def choose_word(file_path, index):
    words_list = []
    read_words_file = open(file_path, "r")
    read_file = read_words_file.read()
        # print(read_file)
    all_words_list = read_file.split(" ")

    for word in all_words_list:
        if word not in words_list:
            words_list.append(word)
    num_words = len(words_list)
        # print(words_list)

    if index > num_words:
        index = index % num_words
        if index == 0:
            index = num_words

    index_word = words_list[index-1]
    read_words_file.close()

    return index_word


def check_valid(letter):
    if not letter.isalpha() and len(letter) > 1:
        check = False
        print("X\nError3 (Please print only ONE LETTER)")
    elif len(letter) > 1:
        check = False
        print("X\nError1 (Please print only ONE letter)")
    elif not letter.isalpha():
        check = False
        print("X\nError2 (Please print only LETTERS)")
    else:
        check = True

    return check


def try_update_letter_guessed(letter_guessed, old_letter_list):
    check = check_valid(letter_guessed)
    if check is False:
        return False
    else:
        if letter_guessed in old_letter_list:
            print(f"X\nletter was already guessed")
            return False
        else:
            old_letter_list.append(letter_guessed)
            return True


def show_hidden_word(guess, secret_word, old_letters_guessed):
    global new_guessed
    global try_no
    x = 0
    for letter in secret_word:
        if letter == guess:
            new_guessed = list(new_guessed)
            new_guessed[x] = letter
        x += 1
    if guess not in secret_word:
        try_no += 1
        if try_no <= MAX_TRIES:
            print(HANGMAN_PHOTOS[try_no])
            print(f"{try_no} out of {MAX_TRIES}")

    return old_letters_guessed, new_guessed


def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter in old_letters_guessed:
            continue
        else:
            return False
    return True


def main():
    headline()
    global new_guessed
    global old_letter_guessed
    global try_no
    file_location = input("Where is the wanted file? ")
    index_word = int(input("Choose a number: "))
    secret_word = choose_word(file_location, index_word)
    new_guessed = ("_" * len(secret_word))
    old_letter_guessed = []

    print("Let's start!")

    win = check_win(secret_word, old_letter_guessed)
    print(HANGMAN_PHOTOS[try_no])
    print(" ".join(new_guessed) + "\n")
    while win is False:
        if try_no >= MAX_TRIES:
            print(f"Game Over :(\nThe word was {secret_word.upper()}.")
            break
        check = False
        while check is False:
            letter = input("Guess a letter: ").lower()
            check = try_update_letter_guessed(letter, old_letter_guessed)
            if check is True:
                old_letter_guessed, word = show_hidden_word(letter, secret_word, old_letter_guessed)
            word = " ".join(new_guessed)
            print(f"\n{word}")
            sorted_olg = " -> ".join(sorted(old_letter_guessed))
            print("\n"+sorted_olg)
            win = check_win(secret_word, old_letter_guessed)
            if win is True:
                print("You Win!")

    old_letter_guessed, new_guessed = show_hidden_word(letter, secret_word, old_letter_guessed)


if __name__ == '__main__':
    main()
