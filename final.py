# KP, AM, DL, JR,  Build the Game Final

import random

score = 0
lives = 1
play_start = input(f"Would you like to play the game? 'Y' if yes, 'N' if no: " ).upper
high_score = high_score.txt
if play_start == "Y":
    def main():
        
    
            
    
    
        print("""
                        ___( |___                            ~ (`    _ )
                        `--- \---'                         (_ (    )    `)                         
                            | \                          (_   (_ .  _) _)
                            \  \\
        __________________\  \___________________
        \                    \                   \\
            ------------------    \-------------------
                        (\)   \   \ (\)
                            \ ' \\
                                :`(.)-'
                                ` ; `,
        """)
        print("You were on your way to the best vacation spot on the planet. Machu Picchu, Peru. Ok, it may not be the best in the \n world, but still a decent place.")
        print("So you both are on your way after a long weeks worth of homework in hopes to get some time off of school. However, \n things don't go as planned. ")
        print("Your friend Fred told you that there are llamas there which got you motivated to try to ride one. Don't know what you were \n thinking, llamas are the spawn of Satan but whatever.")
        print("'Attention passengers.' The pilot says over the intercome. 'I've got good news \n and bad news. The good news is we'll be landing immediately. The bad news is...\n we're crash landing.")
        print("Somehow, you survive the crash. However, your buddy is not doing so well. He's \n been pierced by a large machete. These were some dangerous passengers. He'll \n survive with the proper care and utilities. But he's got a deadline. Literally. There could possibly be things to help on the plane. But heres the bad news. The plane is on fire, so searching for resources could be very risky.")
        print("\nGameplay:")    

        #Beginning:

        # Variables:
    
        # Room Two (After plane Crash)


        # Gameplay:
        username = input("Enter your name: ").strip().title()

        if username.isnumeric():
            print("Sorry, that is a number. Please enter your name: ")

        while True:
            choice_1 = input(f"{username} finds themself on the floor next to the burning plane. You have two options: \n 1: You go inside the plane to get resources. \n 2: You leave the plane and drag your buddy to find a place to stay the night.\nIf you go into the plane, there is a chance you or Fred could be burned alive. \nPut '1' for option 1 or put '2' for option 2: ").lower()
            if choice_1 == "1":
                score += 1
                print("You run into the burning plane and through the smoke, you find a piece of paper on the ground. \n It's a map!")
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
                print(f"{username} notices a cabin on the map. If they get to the cabin, they will be safe.")
                print(f"{username} runs out of the plane and finds out that the flames from the plane got to Fred and he died. Just as {username} is grieving their friends death, they hear a\n growl behind them.")
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
                
                choice_1_1 = input(f"{username} has three options:\n'1' Throw your dead friend at the wolf and book it.\n'2' Get the machete from Freds body and try to kill the wolf.\n'3' Approach the wolf slowly and carefully to try to befriend it.")
                if choice_1_1 == 1:
                    print(f"The wolf had no interest in your burning friend, and instead went after you. You were defensless and died.\nYour score was '{score}'")
                    lives - 1
                if choice_1_1 == 2:
                    choice_1_2 = input(f"{username} enters into a battle with the wolf.\nIt's {username}'s move first. What will you do?\n Action:'A'    Pass Action:'P'\n input your move: ").upper()
                    if choice_1_2 == "A":
                        score += 1
                        print("You decide to assert your dominance. You run at the wolf with nothing but your bare hands, thinking that you're Hercules. You're about to throw a punch, but the wolf is too quick. It bites and sweeps your legs. You expect to fall over but your insane relfexes catch you, rolling you back onto your feet. The wolf lunges at you. With your uninjured leg, you kick the wolf straight in the throat. It falls over, and you pin it from the top, asserting your dominance. You have won. The wolf has submitted to you and is now your pet. You decide to name him Gabe. Gabe the Babe. You and Gabe head off to the cabin.")
                        print("As you make your way to the cabin, Gabe assists you in getting food and defending you from predators.\nYou two eventually make it to the cabin. You find an old man sitting in a rocking chair. You ")...
                    if choice_1_2 == "P":
                        score += 1
                        print(f"You decide to be a pacifist and not attack the wolf. He's still hungry so he eats you anyway.\nYou died. Your score was {score}")
                if choice_1_1 == 3:
                    print(f"The wolf is not easy to be befriended. To win him over, you must be more dominant than him. Which you are not. So he eats you.\nYou died. Your score was '{score}'")
                    lives - 1
            if choice_1 =="2":
                score += 1
                choice_2 = input(f"{username} grabs Fred by the armpits and drags him through the forest. {username} searches for hours. The sun is going down. After about 4 hours of searching, {username} comes across a small and welcoming cave right by a river. {username} sets Fred down in the cave. You're safe for now, but what do you do?\n'A': Start working on a campfire.\n'B': Grab some water for Fred.").upper()
                if choice_2 == "A":
                    print("You gather sticks, stones, and dry leaves. You begin on your campfire, but by the time it's finished, Fred is already dead.")
                    choice_2_1 = input(f"A couple hours pass by, and {username}'s stomach begins to growl. You have to make a decision.\n'1' Search for food in the dark and likely get mauled by a bear.\n'2' Eat Fred. He may be dead, but he also may be tasty.")
                    if choice_2_1 == 1:
                        print(f"You decide to go out and search for berries and bunnies to catch. You accidentally bump into something hard, but furry. You turn to see that it was a very hungry bear. You died. Your final score was '{score}'")
                    if choice_2_1 == 2:
                        print("You prepare Fred to be eaten when you realize, you can't bring yourself to do it, seeing that it is your friend. So you decide not to eat him. Instead, you choose to go out and look for food.")
                        print(f"You decide to go out and search for berries and bunnies to catch. You accidentally bump into something hard, but furry. You turn to see that it was a very hungry bear. You died. Your final score was '{score}'")
                if choice_2 == "B":
                    score += 1
                    print("You pull out your water bottle and gather some water from the creek for Fred. However, it isn't the best water, so there is a likely chance of him dying of dysentery.")
                    print("Click 'R' to roll the die of chance. if it is a 4-6, he lives. If it is a 1-3, he dies.")...
            if choice_1.isalpha():
                print("That's not an option...")
            else:
                 break
elif: 
    play_start == "N"
    print("No worries. Bye Bye!")

with open("highscore.txt", "r") as file:
    high_score = int(file.read())

if score > high_score:
    high_score = score

    with open("highscore.txt", "w") as file:
        file.write(str(high_score))


if score > high
