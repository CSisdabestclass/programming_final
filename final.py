# KP, AM, DL, JR,  Build the Game Final

score = 0
lives = 1
play_start = input(f"Would you like to play the game? 'Y' if yes, 'N' if no: " ).upper

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
        print("Somehow, you survive the crash. However, your buddy is not doing so well. He's \n been pierced by a large machete. These were some dangerous passengers. he'll \n survive with the proper care and utilities. But he's got a deadline. Literally. There could possibly be things to help on the plane. But heres the bad news. The plane is on fire, so searching for resources could be very risky.")
        print("\nGameplay:")    

        #Beginning:

        # Variables:
    
        # Room Two (After plane Crash)


        # Gameplay:
        username = input("Enter your name: ").strip().title()

        if username.isnumeric():
            print("Sorry, that is a number. Please enter your name: ")

        while True:
            choice_1 = input("You find yourself on the floor next to the burning plane. You have two options: \n 1: You go inside the plane to get resources. \n 2: You leave the plane and drag your buddy to find a place to stay the night.\nIf you go into the plane, there is a chance you or Fred could be burned alive. \nPut '1' for option 1 or put '2' for option 2: ").lower()
            if choice_1 == "1":
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
                print("You notice a cabin in the map. If you get to the cabin, you will be safe.")
                print("You run out of the plane and you find out that the flames from the plane got to your friend and he died. Just as your grieving your friends death, you hear a\n growl behind you.")
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
                
                choice_1_1 = input("You have three options:\n'1' You throw your dead friend at the wolf and book it.\n'2' Get the machete from Freds body and try to kill the wolf.\n'3' Approach the wolf slowly and carefully to try to befriend it.")
                if choice_1_1 == 1:
                    print(f"The wolf had no interest in your burning friend, and instead went after you. You were defensless and died. Your score was '{score}'")
                    lives - 1
                if choice_1_1 == 2:
                    input(f"You enter into a battle with the wolf.\nIt's your move first. What will you do?\n Action:'A'    Pass Action:'O'\n input your move: ")
                    lives - 1
                if choice_1_1 == 3:
                    print("You ")
            if choice_1 =="2":
                score += 1
                choice_2 = input("You grab Fred by the armpits and drag him through the forest. You search for hours. The sun is going down. After about 4 hours of searching, you come across a small and welcoming cave right by a river. You set Fred down in the cave. You're safe for now, but what do you do?\n(A): Start working on a campfire.\n(B): Grab some water for Fred.")
                if choice_2 == "A" or "a":
                    print("You gather sticks, stones, and dry leaves. You begin on your campfire, but by the time it's finished, Fred is already dead. You later die due to demotivation and greif. You died. Your score was {score}.")
                
            if choice_1.isalpha():
                print("That's not an option...")
            else:
                 break
elif: 
    play_start == "N"
    print("No worries. Bye Bye!")

with open("highscore.txt", "r") as file:
    high_score = int(file.read())

if score > high
