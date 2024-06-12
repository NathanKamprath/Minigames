import random
from replit import clear

word_bank = [
    "sphynx", "onyx", "butterfly", "sapphire", "vaccuum",
    "aardvark", "aardwolf", "sword", "castle", "anvil", "glyph", 
    "onomatopoeia", "banjo", "velvet", "xylophone", "saxophone", 
    "abyss", "affix", "askew", "avenue", "azure", "blizzard", 
    "crypt", "espionage", "fjord", "galaxy", "ivy", "jazzy", 
    "luxury", "nymph", "mnemonic", "oxygen", "waltz"
    ]

logo = r''' 
 _   _                                         
| | | |                                        ||
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  ||
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ||
| | | | (_| | | | | (_| | | | | | | (_| | | | |||
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|()
                    __/ |                      
                   |___/ 
'''

hang_stage = [
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
r'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]


playing = True

while playing:
    chosen_word = random.choice(word_bank)
    word_bank.remove(chosen_word)
    word_len = len(chosen_word)
    count = 0

    print(logo)

    display = []
    for letter in chosen_word:
        display.append("_")
    print(f"{" ".join(display)}")

    #while not game_end (set var game_end = False)
    while "_" in display and count < 6:
        
        print(hang_stage[-1])
        guess = str(input("Guess a letter: ").lower())

        for position in range(word_len):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
            else:
                pass


        if guess not in chosen_word:
            hang_stage.pop()
            count += 1

        print(f"{" ".join(display)}")

        if "_" not in display:
            print("You win!")
        elif count >= 6:
            print("You lose :(")
            break

    print("Would you like to play again? Y/N")
    continue_play = input().lower()
    if continue_play == "y":
        playing = True
        clear()
        if word_bank == []:
            print("There are no more words!\nThank you for playing!")
            playing = False
    else:
        playing = False
