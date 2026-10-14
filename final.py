# KP, AM, DL, JR,  Build the Game Final

# (W.D.B = Work Done By)

# W.D.B Jake
import random

with open('dice.txt', "r") as file:
    number_list = [number.strip() for number in file.readlines()]

# W.D.B Kristian
lives = 1


def hangman():

    secret_word = "jeep"

    wrong_guesses = 0
    guessed_letters = []

    guessed_letters.append(input("What is your guess? "))

    def show_hangman(wrong_guesses): 
        if wrong_guesses == 0:
            print("""
    ______
    |    |
    |   
    |   
    |   
    |________
    """)

        elif wrong_guesses == 1:
            print("""
    ______
    |    |
    |    O
    |   
    |   
    |________
    """)

        elif wrong_guesses == 2:
                print("""
        ______
        |    |
        |    O
        |    |
        |   
        |________
        """)

        elif wrong_guesses == 3:
            print("""
        ______
        |    |
        |    O
        |   /|
        |   
        |________
        """)

        elif wrong_guesses == 4:
            print("""
        ______
        |    |
        |    O
        |   /|\\
        |   
        |________
        """)

        elif wrong_guesses == 5:
            print("""
        ______
        |    |
        |    O
        |   /|\\
        |   /
        |________
        """)

        elif wrong_guesses == 6:
            print("""
        ______
        |    |
        |    O
        |   /|\\
        |   / \\
        |________
        """)


    def show_word(secret_word, guessed_letters):
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        return display_word


    while True:

        show_hangman(wrong_guesses)

        print("Word:", show_word(secret_word, guessed_letters))
        print("Guessed letters:", guessed_letters)
        print("Wrong guesses remaining:", 6 - wrong_guesses)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            wrong_guesses += 1
            print("Sorry,", guess.upper(), "is not in the word.")
        else:
            print("Nice!", guess.upper(), "is in the word!")

        if "_" not in show_word(secret_word, guessed_letters):
            print("Congratulations! You guessed the word:", secret_word.upper())
            return True
    

            #break

        if wrong_guesses == 6:
            print("You lost!")
            print("The word was:", secret_word.upper())
            return False

            #break

def cabin():
    print("You two eventually make it to the cabin. You find an old man sitting in a rocking chair.")
    print("'Hey!' You shout. 'We're stranded and have no way home. Can you help us?' You ask the old man. He looks at you and pulls out a whiteboard. What's enscribed on it is a game of hangman.\n 'Beat me at this game, and that is yours to use.' He gestures to his white jeep.")
    print("'But if I win, Ol' girl here will show you to the heavens.'")
    decide = input("What is your decision?: (Y)es or (N)o?: ").upper()
    if decide == "N":
        print(f"'Well that's bad news.'\nThe old man takes out Ol' girl and shoots you in the head. I guess he really wanted to play a game.\nYou died. Your score was '{score}'")
        lives -= 1
        if lives == 0:
            print("Game Over!")
    elif decide == "Y":
        score += 1
        did_they_win = hangman()
        if did_they_win:
            print("'Well, I'll be. Never seen anyone guess my word.' The old man says.\n'Well, I doubt you meet a lot of people living here.'You reply.\nEmphasis on living.'\nYep, that old man's creepy. But hey, now you got the car keys!\nYou get into the car with Gabe in the passenger seat. There's an engraving on the steering wheel that reads the word 'Artemis'\nYou turn the ignition and... it works! You drive on the dirt road until you read a sign that says, 'Pebble Woods Town' and points West.\nYou head in that direction, and live happily ever after with Gabe.\nThe End.")
            print(play_again)
        else:
            print(f"'Welp, that'd be it fer you. Say hi to my wife for me, Kay?' He points the gun at you and shoots.\nYou died. your score was '{score}'")

# W.D.B Jake, Kristian, Dara, Ainsley
def main():
    
    score = 0
        

    # Lines 19-37 details the storyline. Each print statement is giving a piece of information for the story and typing it out for the reader.
    print("""
               { }'.
            __/\__}`
           `==/\==`
 ____________/__\____________
/____________________________\\
  __||__||__/.--.\__||__||__
 /__|___|___( >< )___|___|__\\
           _/`--`\_
          (/------\)
    """)
    print("You were on your way to the best vacation spot on the planet. Machu Picchu, Peru. Ok, it may not be the best in the \n world, but still a decent place.")
    print("Your friend Fred told you that there are llamas there which got you motivated to try to ride one. Don't know what you were \n thinking, llamas are the spawn of Satan but whatever.")
    print("So you both are on your way after a long weeks worth of homework in hopes to get some time off of school. However, \n things don't go as planned.")
    print("'Attention passengers.' The pilot says over the intercome. 'I've got good news \n and bad news. The good news is we'll be landing immediately. The bad news is...\n we're crash landing.")
    print("Somehow, you survive the crash. However, your buddy is not doing so well. He's \n been pierced by a large machete. These were some dangerous passengers. He'll \n survive with the proper care and utilities. But he's got a deadline. Literally. There could possibly be things to help on the plane. But heres the bad news. The plane is on fire, so searching for resources could be very risky.")
    print("\nGameplay:")

    # Gameplay (lines 40-193):

    # This will get the username from the user and later on and makes it so later on we will be able to retreive that username that was typed in for the game.
    username = input("Enter your name: ").strip().title()
    

    if username.isnumeric():
        print("Sorry, that is a number. Please enter your name: ")

    # This is the users first choice. The variable choice_1 is an input that the user writes which determintes which path of the gameplay they will take.
    choice_1 = input(f"{username} finds themself on the floor next to the burning plane. You have two options: \n 1: You go inside the plane to get resources. \n 2: You leave the plane and drag your buddy to find a place to stay the night.\nIf you go into the plane, there is a chance you or Fred could be burned alive. \nPut '1' for option 1 or put '2' for option 2: ").lower()

    # If the user chooses this input (1), their story goes down a certain pathway different from if they chose the other input (2).
    if choice_1 == "1":
        score += 1
        print("You run into the burning plane and through the smoke, you find a piece of paper on the ground. \n It's a map!")
        # This prints out the map for the user to read and understand where they need to go.
        print("""
____________________________________________________________________________________________________________________________
|                                                                                                                          |
|   .------------------------------------------------------------------------------------------------------------------.   |
|   |  [N]                               ISLAND OF THE FORGOTTEN PILOT                                                 |   |
|   |   |                                                                                                              |   |
|   | [W]+[E]  /\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\      |   |
|   |   |     /  DEAD MAN'S PEAKS                                                                               \      |   |
|   |  [S]   '---------------------------------------------------------------------------------------------------'     |   |
|   |                                                      ||                                                          |   |
|   |                                                 \ \  ||  / /                                                     |   |
|   |                                              =====> (XX) <=====  <-- CRASH SITE (Flight 404 Wreckage)            |   |
|   |                                                 / /  ||  \ \                                                     |   |
|   |                                                      ||                                                          |   |
|   |  . . . . . . . . . . . . . . . . . . . . . . . . . . :: . . . . . . . . . . . . . . . . . . . . . . . . . . . .  |   |
|   |  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ :: ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^  |   |
|   |  /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\  ::  /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\   |   |
|   | /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \ :: /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  / \|   |
|   |  ||    ||    ||    ||    ||    ||    ||    ||    ||  ::  ||    ||    ||    ||    ||    ||    ||    ||    ||   || |   |
|   |  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ :: ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^  |   |
|   |  /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\  ::  /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\   |   |
|   | /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \ :: /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  / \|   |
|   |  ||    ||    ||    ||    ||    ||    ||    ||    ||  ::  ||    ||    ||    ||    ||    ||    ||    ||    ||   || |   |
|   |  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ :: ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^  |   |
|   |  /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\  ::  /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\   |   |
|   | /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \ :: /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  / \|   |
|   |  ||    ||    ||    ||    ||    ||    ||    ||    ||  ::  ||    ||    ||    ||    ||    ||    ||    ||    ||   || |   |
|   |  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ BLACKWOOD PINE FOREST ^ ^ ^ :: ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^  |   |
|   |  /\ /\ /\ /\ /\ /\ /\ /\ /\  (ALL FORESTS)  /\ /\ /\ :: /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\    |   |
|   | /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \ :: /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  / \|   |
|   |  ||    ||    ||    ||    ||    ||    ||    ||    ||  ::  ||    ||    ||    ||    ||    ||    ||    ||    ||   || |   |
|   |  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ :: ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^  |   |
|   |  /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\  ::- - - - - - .  /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\  |   |
|   | /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \ ::            | /  \  /  \  /_/\_/\_/\_/\_/\_/\             |   |
|   |  ||    ||    ||    ||    ||    ||    ||    ||    ||  ::            |   /  _ \ /                    \             |   |
|   |  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ :: (Fork East)`->|  / \ V /   (STALACTITES)   |             |   |
|   |  /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\  ::               | |  /   \                   | <-- CAVE    |   |
|   | /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \ ::                | | (  .  )  [===] CHEST    |             |   |
|   |  ||    ||    ||    ||    ||    ||    ||    ||    ||  ::                |  \ /^\ /   /|/|\ STALAG   |             |   |
|   |  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ::                 \__\_/\_/___________________/            |   |
|   |  /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\  ::                      ||                                  |   |
|   | /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \ ::                    ~~~~ (Underground River)              |   |
|   |  ||    ||    ||    ||    ||    ||    ||    ||    ||  ::                                                          |   |
|   |  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ :: ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^  |   |
|   |  /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\  ::  /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\   |   |
|   | /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \ :: /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  / \|   |
|   |  ||    ||    ||    ||    ||    ||    ||    ||    ||  ::  ||    ||    ||    ||    ||    ||    ||    ||    ||   || |   |
|   |  . . . . . . . . . . . . . . . . . . . . . . . . . . :: . . . . . . . . . . . . . . . . . . . . . . . . . . . .  |   |
|   |                                                      ::                                                          |   |
|   |                                               (SMOKE) ~  ~                                                       |   |
|   |                                                      ||                                                          |   |
|   |                                             .-- .---[||]---.                                                     |   |
|   |                                            /   /  ________  \                                                    |   |
|   |                                           /   /  /        \  \  <-- ROOF SHINGLES                                |   |
|   |                                          /   /  '----------'  \                                                  |   |
|   |                                         (===(==================)                                                 |   |
|   |                                         |   | [=] [=]  [=] [=] | <-- LOG WALLS                                   |   |
|   |                                         |   | [=]  ____    [=] |                                                 |   |
|   |                                         |   | [=] |    |   [=] | <-- DESTINATION: LOG CABIN                      |   |
|   |                                         |   | [=] | [] |   [=] |     (X Marks the Spot)                          |   |
|   |                                         \__ |_____|____|_______|                                                 |   |
|   |                                                                                                                  |   |
|   '------------------------------------------------------------------------------------------------------------------'   |
|__________________________________________________________________________________________________________________________|
""")
# by using ("""      """), this makes a map that the user can see our map withought it not showing the format incorrectly. THis also means we can use the map later by just typing in the name that we called our map.
        print(f"{username} notices a cabin on the map. If they get to the cabin, they will be safe.")
        print(f"{username} runs out of the plane and finds out that the flames from the plane got to Fred and he died. Just as {username} is grieving their friends death, they hear a\n growl behind them.")
        # This prints out a picture of a wolf just to give the user some visuals. For fun :D
        print("""
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠃⠀⠀⠀⠘⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢹⣏⡿⢿⣿⡦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⣴⣴⡀⠘⢻⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢻⣇⡀⠙⢿⣮⡈⠳⣦⣤⣀⠀⠀⠀⠀⠀⣿⠀⠀⢰⣿⣿⣿⡀⠈⢻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⣿⡆⠀⠀⠻⡿⣦⠀⠉⢽⣿⣶⠶⢦⣶⣿⠀⠀⢸⣿⣿⣿⡇⠀⠘⢿⣿⣷⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣧⣄⣀⡀⠘⠽⣷⣤⣾⡟⠀⠀⠀⣿⣿⣦⡀⠈⢿⣿⣿⠇⠀⠀⠸⣿⣿⡇⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⢀⣼⠿⠃⠀⠀⢀⣤⠟⠻⠿⣿⣄⢸⣿⠏⠀⠀⠀⠀⠻⢿⣷⠀⠈⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⡄⢀⡶⠛⠁⠀⠀⢀⣴⣿⠋⠀⠀⠀⠀⠉⠻⠋⠀⠀⠀⠀⠀⠀⠀⣿⡄⠀⠀⠙⣿⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⠟⢀⡴⢀⡇⢀⣿⠿⠛⠂⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠈⢦⡙⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣶⠟⠀⢸⡁⣾⠀⠀⠀⠀⠀⠀⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠑⢿⣿⣷⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⠏⠀⢀⣿⠀⣿⣠⠖⠓⣦⠀⠀⠀⠈⠳⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⡀⠀⠀⠀⠀⢹⣾⣿⠛⠶⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⡀⠀⢸⡇⠠⣿⡏⠀⠀⣟⣀⡀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠙⣿⠀⠀⠀⠀⡀
⠀⠀⠀⠀⠀⠀⢈⣿⣿⣶⣾⠃⠀⣿⠀⠐⢋⣽⠿⢿⢾⡿⢷⣦⡀⠀⠉⠒⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠈⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⠃⠀⠀⠘⢷⣴⣿⣿⣶⠶⠟⠁⠀⠈⣿⣷⣦⣤⣀⡀⠀⠀⠀⠀⠀⠈⢻⡆⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣼⠃⠀⠀⠀⢀⢾⠟⠉⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⠉⠉⠛⣷⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠠⢻⣦⣴⣄⣀⣙⣷⡦⣶⣦⣿⣷⡀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⠀⢀⡠⠒⠉⠉⠉⠉⠉⠛⠛⠀⠀⢿⣿⣿⣷⡀⢀⣾⣿⠀⠀⠀⠀⠀⠀⣉⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀
⠀⠀⠀⢀⡼⠅⢀⣴⠆⠀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠙⠛⣿⣿⠃⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀
⠀⠀⣠⠾⠀⣠⣿⣋⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣇⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⢸⡃⠀⠀⠀⠀
⠀⡼⠁⠀⣴⣻⣿⣧⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠖⠁⠘⢿⣷⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠾⠁⠀⠀⠀⠀
⠈⣷⣾⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⣠⣾⠿⠋⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢿⣿⣿⣽⡟⠀⠀⠀⠀⠀⠀⢀⣠⣞⣩⣤⠴⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠻⢧⣀⣠⣄⣀⣤⡶⣞⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⣿⡟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠃⠀⠀
""")
        print("It's a wolf! And he looks hungry.")

        # The variable choice_1_1 opens lots of other pathways for the player to go down. Their pathway depends on their input. Each of the pathways has their own storyline that either allows the player to win or lose.
        choice_1_1 = input(f"{username} has three options:\n'1' Throw your dead friend at the wolf and book it.\n'2' Try to kill the wolf.\n'3' Approach the wolf slowly and carefully to try to befriend it.\nInput your response here: ")
        # This choice is saying that if the user puts the input 1, a print statement will show up, telling them that the wolf goes after you. This pathway makes the player die, causing them to lose.
        if choice_1_1 == "1":
            print(f"The wolf had no interest in your burning friend, and instead went after you. You were defensless and died.\nYour score was '{score}'")
            lives -= 1
            if lives == 0:
                    print("Game Over!")
        elif choice_1_1 == "2":
            choice_1_2 = input(f"{username} enters into a battle with the wolf.\nIt's {username}'s move first. What will you do?\n Action:'A'    Pass Action:'P'\n input your move: ").upper()
            # This choice will allow the player to fight the wolf.
            if choice_1_2 == "A":
                score += 1
                print("You decide to assert your dominance. You run at the wolf with nothing but your bare hands, thinking that you're Hercules. You're about to throw a punch, but the wolf is too quick. It bites and sweeps your legs. You expect to fall over but your insane relfexes catch you, rolling you back onto your feet. The wolf lunges at you. With your uninjured leg, you kick\nthe wolf straight in the throat. It falls over, and you pin it from the top, asserting your dominance. You have won. The wolf has submitted to you and is now your pet. You decide to\nname him Gabe. Gabe the Babe. You and Gabe head off to the cabin.")
                print("As you make your way to the cabin, Gabe assists you in getting food and defending you from predators.")
                cabin()

            # This choice will allow the player to try to make peace with the wolf. You end up dead.
            elif choice_1_2 == "P":
                score += 1
                print(f"You decide to be a pacifist and not attack the wolf. He's still hungry so he eats you anyway.\nYou died. Your score was {score}")
                # This choice is a wrong choice and you end up dead.
        elif choice_1_1 == "3":
            print(f"The wolf is not easy to be befriended. To win him over, you must be more dominant than him. Which you are not. So he eats you.\nYou died. Your score was '{score}'")
            lives -= 1
            if lives == 0:
                    print("Game Over!")
    elif choice_1 =="2":
        score += 1
        choice_2 = input(f"{username} grabs Fred by the armpits and drags him through the forest. {username} searches for hours. The sun is going down. After about 4 hours of searching, {username} comes across a small and welcoming cave right by a river. {username} sets Fred down in the cave. You're safe for now, but what do you do?\n'A': Start working on a campfire.\n'B': Grab some water for Fred: ").upper()
        if choice_2 == "A":
            print("You gather sticks, stones, and dry leaves. You begin on your campfire, but by the time it's finished, Fred is already dead.")
            choice_2_1 = input(f"A couple hours pass by, and {username}'s stomach begins to growl. You have to make a decision.\n'1' Search for food in the dark and likely get mauled by a bear.\n'2' Eat Fred. He may be dead, but he also may be tasty.")
            if choice_2_1 == 1:
                print(f"You decide to go out and search for berries and bunnies to catch. You accidentally bump into something hard, but furry. You turn to see that it was a very hungry bear. You died. Your final score was '{score}'")
                lives -= 1
                if lives == 0:
                        print("Game Over!")
            elif choice_2_1 == 2:
                print("You prepare Fred to be eaten when you realize, you can't bring yourself to do it, seeing that it is your friend. So you decide not to eat him. Instead, you choose to go out and look for food.")
                print(f"You decide to go out and search for berries and bunnies to catch. You accidentally bump into something hard, but furry. You turn to see that it was a very hungry bear. You died. Your final score was '{score}'")
                lives -= 1
                if lives == 0:
                        print("Game Over!")
        elif choice_2 == "B":
            score += 1
            print("You pull out your water bottle and gather some water from the creek for Fred. However, it isn't the best water, so there is a likely chance of him dying of dysentery.")
            print("Click 'R' to roll the die of chance. if it is a 4-6, he lives. If it is a 1-3, he dies.")
            dice_roll_active = True
            while(dice_roll_active):
                roll_dice = input("Type the letter R: ").upper().strip()
                if roll_dice == "R":
                    rand_int = random.randint(1,6)
                    print(rand_int)
                    dice_roll_active = False
                else:
                    print("Roll the dice with 'R'!")
            if rand_int in [1,2,3]:
                print("It was contaminated water. Fred dies.")
            else:
                print("Good news! Fred gets to live to see another day. After a couple of hours, Fred gets better and you two continue moving on throughout the woods.")
                cabin()
            

    elif choice_1.isalpha():
        print("That's not an option...")
    #else:
            #break


# W.D.B Ainsley
play_start = input(f"Would you like to play the game? 'Y' if yes, 'N' if no: " ).upper()

# W.D.B Ainsley, Jake
while play_start == "Y":
    main()

    # **** this should be at the end of main **** #


    play_again = input("Do you want to play again?: ").lower()



if play_again == "yes":
    lives == 1
elif play_again == "no":
    print("Thanks for playing!")

with open("high_score.txt", "r") as file:
    high_score = int(file.read())

if score > high_score:
    high_score = score

    with open("high_score.txt", "w") as file:
        file.write(str(high_score))










if score > high
