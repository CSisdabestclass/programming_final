# KP, AM, DL, JR - Build the Game Final

import random

score = 0
lives = 1
high_score = 0
inventory = []

try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read().strip())
except
    high_score = 0


def show_map():
    print(r"""
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

def show_inventory():
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for item in inventory:
            print("-", item)


def cabin_and_puzzle(username, gabe_is_friend, fred_alive):
    global score

    print("\nYou continue through the forest toward the cabin.")
    print("You find a walking stick and a bottle of water along the path.")

    for item in ["walking stick", "water"]:
        if item not in inventory:
            inventory.append(item)
            print("You picked up the", item + ".")
            score += 1

    print("\nYou reach the log cabin. An old man is sitting in a rocking chair.")
    print("He says, 'I can help you leave this island, but first solve my cipher.'")
    print("Each letter in the secret word has been moved forward by one letter.")
    print("Move each letter backward by one letter to solve it.")
    print("Secret word: DBS")
    print("Hint: It is a vehicle you can travel in.")

    answer = input("What is the decoded word? ").strip().upper()

    if answer == "CAR":
        print("'Correct!' the old man says, handing you the car keys.")
        inventory.append("car keys")
        score += 5
        print("You follow his directions: W, S, W, W, N, E, E, N, S, S, W, N, E, E, S.")

        if gabe_is_friend:
            print("Gabe follows you to the vehicle and jumps in beside you.")

        if fred_alive:
            print("You help Fred into the vehicle.")

        print("You use the keys and escape the island. You won!")
        return True
    else:
        print("The answer is incorrect. The old man cannot help you escape.")
        print("Your adventure ends on the island.")
        return False


def wolf_scene(username):
    global score

    show_wolf()
    print("It's a wolf! And he looks hungry.")

    while True:
        choice = input(
            f"{username}, you have three options:\n"
            "1: Throw your dead friend at the wolf and run.\n"
            "2: Take the machete from Fred's body and fight the wolf.\n"
            "3: Approach the wolf slowly and try to befriend it.\n"
            "Choose 1, 2, or 3: "
        ).strip()

        if choice == "1":
            print("The wolf ignores your distraction and chases you. You died.")
            return False

        elif choice == "2":
            if "machete" not in inventory:
                inventory.append("machete")

            while True:
                move = input("Choose A to attack or P to pass: ").strip().upper()

                if move == "A":
                    score += 1
                    print("You charge at the wolf, dodge its lunge, and manage to scare it away.")
                    print("You have won the encounter. You name the wolf Gabe the Babe.")
                    print("Gabe follows you toward the cabin and helps you find food and avoid danger.")
                    return cabin_and_puzzle(username, True, False)

                elif move == "P":
                    print("You decide not to fight. The hungry wolf attacks. You died.")
                    return False

                else:
                    print("That's not an option. Enter A or P.")

        elif choice == "3":
            print("The wolf is wary of you, but you give it space and offer some food.")
            print("After a tense moment, it begins to trust you. You name him Gabe the Babe.")
            score += 2
            return cabin_and_puzzle(username, True, False)

        else:
            print("That's not an option. Enter 1, 2, or 3.")


def main():

    score = 0
    lives = 1
    inventory = []

    print(r"""
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

    print("You were on your way to the best vacation spot on the planet: Machu Picchu, Peru.")
    print("Okay, it may not be the best in the world, but still a decent place.")
    print("You and your friend Fred are going after a long week of homework, hoping to get some time off school.")
    print("Fred told you there are llamas there, which motivated you to try to ride one.")
    print("Llamas are the spawn of Satan, but whatever.")
    print("'Attention passengers,' the pilot says. 'The good news is we'll be landing immediately.")
    print("The bad news is... we're crash landing.'")
    print("Somehow, you survive the crash. Fred has been pierced by a large machete.")
    print("He might survive with proper care and supplies, but he needs help soon.")
    print("There could be things on the plane that would help, but the plane is on fire.")

    while True:
        username = input("Enter your name: ").strip().title()

        if username == "" or username.isnumeric():
            print("Please enter a name, not a number or blank answer.")
        else:
            break

    print("\nWelcome,", username + "!")
    print("Your inventory starts empty.")

    while True:
        choice = input(
            "\nYou are next to the burning plane. Choose:\n"
            "1: Enter the plane to get resources.\n"
            "2: Leave the plane and drag Fred to find shelter.\n"
            "Type 1 or 2: "
        ).strip()

        if choice == "1":
            won = plane_route(username)
            break

        elif choice == "2":
            won = cave_route(username)
            break

        else:
            print("That's not an option. Please enter 1 or 2.")

    print("\nYour final score was:", score)

    if won:
        print("Result: WIN")
    else:
        print("Result: LOSS")

    if score > high_score:
        high_score = score

        with open("highscore.txt", "w") as file:
            file.write(str(high_score))

        print("New high score!")

    print("High score:", high_score)
    show_inventory()


while True:
    play_start = input(
        "Would you like to play the game? Enter Y for yes or N for no: "
    ).strip().upper()

    if play_start == "Y":
        main()

        play_again = input("Would you like to play again? Enter Y or N: ").strip().upper()

        if play_again != "Y":
            print("Thanks for playing! Bye bye!")
            break

    elif play_start == "N":
        print("No worries. Bye bye!")
        break

    else:
        print("That's not an option. Enter Y or N.")
