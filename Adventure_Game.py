import time
import random


def print_pause(content):
    print(content)
    time.sleep(2)


def intro(details, beasts):
    print_pause("You are on a short walk, suddenly you find yourself on an island, filled with bones, tall reeds and Totem poles.")
    print_pause("History has it that a " + beasts + " is living on the island terrorising other creatures around the Island.")
    print_pause("In front of you is an abandoned temple.")
    print_pause("To your right is a thick jungle.")
    print_pause("In your hand is a very blunt kitchen knife")


def jungle(details, beasts):
    if "confused" in details:
        print_pause("You thread a path into the thick jungle.")
        print_pause("You noticed you've walked through this jungle before and gotten the deadly weapon there with you. There is nothing here again.")
        print_pause("You went back to the Island.")
    else:
        print_pause("You thread a path into the thick jungle.")
        print_pause("Getting into the the thick jungle, the only thing you can see are tall trees and coconut trees.")
        print_pause("Turning to your right in the jungle, you see a deadly weapon hung on a tree.")
        print_pause("You have found an excape weapon in the island.")
        print_pause("You threw away your blunt kitchen knife and take the deadly weapon.")
        print_pause("You thread out to the island.")
        details.append("confused")
    island(details, beasts)


def temple(details, beasts):
    print_pause("You walk towards the gate of the temple.")
    print_pause("You open the gate and walk about 10 meters into the temple and from no where steps out a " + beasts + ".")
    print_pause("Yay! This is the " + beasts + "'s hideout")
    print_pause("The " + beasts + " move towards you and try to jump on you!")
    if "confused" not in details:
        print_pause("You feel so nervous and afraid beacuse you are unaware of this, with you is just a kitchen knife")
    while True:
        preference = input("Would you like to (1) fight or (2) "
                        "run away?")
        if preference == "1":
            if "confused" in details:
                print_pause("As the " + beasts + " jumps on you to attack, you grab your deadly weapon from your side.")
                print_pause("The deadly weapon can cut off the head of a bull at once.")
                print_pause("But the " + beasts + "takes one look at your weapon and runs away!")
                print_pause("You have made the Island safe from the threat of the  " + beasts + ". You are victorious!")
            else:
                print_pause("You try your best in fighting...")
                print_pause("but your kitchen knife can not defeat the " + beasts + ".")
                print_pause("You have been defeated!")
            play_again()
            break
        if preference == "2":
            print_pause("You run back into the Island. Luckily, you don't seem to have been followed.")
            island(details, beasts)
            break


def island(details, beasts):
    print_pause("Enter 1 to open the gate of the temple.")
    print_pause("Enter 2 to thread into the thick jungle.")
    print_pause("What would you like to do?")
    while True:
        preference1 = input("(Please enter 1 or 2.)\n")
        if preference1 == "1":
            temple(details, beasts)
            break
        elif preference1 == "2":
            jungle(details, beasts)
            break


def play_again():
    repeat = input("Would you like to play again? (y/n)").lower()
    if repeat == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        start_game()
    elif repeat == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def start_game():
    details = []
    beasts = random.choice(["Giant Crab", "Dinosaur", "Sand Monster", "Cockroach Whale",
                            "Giant Ape"])
    intro(details, beasts)
    island(details, beasts)


start_game()







