import time
import random
import Lists


# testing githubs commit changes


def print_pause(string):
    print(string)
    time.sleep(2)


def valid_input_3choice(prompt, option1, option2, option3):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        elif option3 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def valid_input_2choice(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def intro():
    print_pause("You're standing over a mutilated body")
    print_pause("You can smell the rotting corpse...")
    print_pause("You can taste the blood in your mouth...")
    print_pause("You can feel the fear they had...")
    print_pause("A drop of blood suddenly splatters on the floor "
                "beside your foot...")
    print_pause("You look up to see where it came from and "
                "spot a shimmer in the rafters...")
    print_pause("Something rushes towards you with astounding quickness,"
                "consuming all the light around you, "
                "just as it is about to reach you...")
    print_pause("You wake up, drenched in a cold sweat")
    print_pause("You look around and recognize the room as your own")
    print_pause("A sense of relief comes over you...when all of a "
                "sudden you hear a crash come from your closet")


def grab_weapon(visits, weapon, enemy, location, enemy_weapon):
    if "1" in visits:
        print_pause("You've already grabbed what you need here "
                    "but you feel around...")
        print_pause("and come up with nothing but dust")
        wake_up_decision(visits, weapon, enemy, location, enemy_weapon)
    else:
        visits.append("1")
        print_pause(f"You reach under your bed and pull out {weapon}!")
        wake_up_decision(visits, weapon, enemy, location, enemy_weapon)


def investigate_crash(visits, weapon, enemy, location, enemy_weapon):
    if "2" in visits:
        print_pause("You take another look in the closet and "
                    "still see the portal there")
        print_pause("Do you decide to...")
        print_pause("1. Walk in and see where the portal takes you")
        print_pause("2. Run out of your room... "
                    "you're not dealing with this today")
        portal = valid_input_2choice("Please enter '1' or '2' "
                                     "to make your choice: \n", "1", "2")
        if portal == "1":
            walk_in_portal(visits, weapon, enemy, location, enemy_weapon)
        elif portal == "2":
            walk_away_from_portal(visits, weapon, enemy,
                                  location, enemy_weapon)
    else:
        visits.append("2")
        print_pause("You go investigate what the crash was in your closet")
        print_pause("You open the door slowly...")
        print_pause("You see a silver gleaming portal floating "
                    " in the middle of your closet!")
        print_pause("Do you decide to...")
        print_pause("1. Walk in and see where the portal takes you")
        print_pause("2. Run out of your room... "
                    "you're not dealing with this today")
        portal = valid_input_2choice("Please enter '1' or '2' "
                                     "to make your choice: \n", "1", "2")
        if portal == "1":
            walk_in_portal(visits, weapon, enemy, location, enemy_weapon)
        elif portal == "2":
            walk_away_from_portal(visits, weapon, enemy,
                                  location, enemy_weapon)


def walk_in_portal(visits, weapon, enemy, location, enemy_weapon):
    if "1" in visits:
        print_pause(f"With {weapon} in your hand you feel "
                    "ready to handle whatever comes your way")
        print_pause(f"You walk into the portal and immediately "
                    f"get transported to {location}!")
        print_pause(f"You take a look around {location} and "
                    "wonder what in the world is going on")
        print_pause("You suddenly hear a noise from your right "
                    "and turn to look...")
        print_pause(f"You see {enemy} charging at you full speed..")
        print_pause(f"You go to bring up {weapon} to defend yourself "
                    "but you realize you can't wield it properly")
        print_pause(f"{enemy} strikes you down with {enemy_weapon} "
                    "until everything eventually turns black...")
        print_pause("Sometimes its best not to be curious...")
    else:
        print_pause("You decide to walk into the portal with "
                    "nothing but your bare fists to defend yourself")
        print_pause(f"You are immediately transported to {location}!")
        print_pause(f"You take a look around {location} and "
                    "wonder what in the world is going on")
        print_pause("You suddenly hear a noise from your right "
                    "and turn to look...")
        print_pause(f"You see {enemy} charging at you full speed..")
        print_pause(f"You go to shield yourself with your arms, "
                    f"cowering down as {enemy} closes in on you")
        print_pause(f"{enemy} strikes you down with {enemy_weapon} "
                    "until everything eventually turns black...")
        print_pause("Sometimes it might help to not "
                    "be so confident in yourself...")


def walk_away_from_portal(visits, weapon, enemy, location, enemy_weapon):
    if "1" in visits:
        print_pause(f"With {weapon} in your hand you feel "
                    "ready to handle whatever comes your way")
        print_pause("You begin to walk towards the portal...")
        print_pause(f"A wave of regret comes over you and you do a 180, "
                    f"throw {weapon} back onto your bed and run out of "
                    "your room")
        print_pause("You decide that only the pub will cure this ailment "
                    "and call up your best buds for a few pints")
        print_pause("Sometimes its better to just spend the day with "
                    "the ones you love rather than be a hero...")
    else:
        print_pause("You immediately turn around with nothing "
                    "but your phone in your hand and walk out the door")
        print_pause("You're not sure what you will do today "
                    "but at least the world is still your oyster")
        print_pause("Sometimes its best to not limit yourself...")


def run_away(visits, weapon, enemy, location, enemy_weapon):
    if "1" in visits:
        print_pause(f"You throw {weapon} and decide 'screw it', "
                    "today is not going to start like this..")
        print_pause("You grab your keys and decide your going to check-in "
                    "to a hotel for a few weeks.. maybe the portal "
                    "will disappear")
    else:
        print_pause("You put your head up for a second and look over..")
        print_pause("You're too tired to even bother.. although "
                    "the dream rattled you.. "
                    "you shake it off and decide that you're never "
                    "smoking 'that stuff' again")


def wake_up_decision(visits, weapon, enemy, location, enemy_weapon):
    print_pause("You decide you have three choices...")
    print_pause("1. Grab for whatever you can find to defend yourself")
    print_pause("2. Go investigate the crash in your closet")
    print_pause("3. Run out of your room screaming")
    decision = valid_input_3choice("Please enter '1', '2', or '3' to "
                                   "make your choice:\n ", "1", "2", "3")
    if decision == "1":
        grab_weapon(visits, weapon, enemy, location, enemy_weapon)
    elif decision == "2":
        investigate_crash(visits, weapon, enemy, location, enemy_weapon)
    elif decision == "3":
        run_away(visits, weapon, enemy, location, enemy_weapon)


def play_game():
    visits = []
    weapons = Lists.weapons
    enemies = Lists.enemies
    locations = Lists.locations
    weapon = random.choice(weapons)
    enemy_weapon = random.choice(weapons)
    enemy = random.choice(enemies)
    location = random.choice(locations)
    intro()
    wake_up_decision(visits, weapon, enemy, location, enemy_weapon)
    play_again()


def play_again():
    print_pause("Would you like to play again?")
    play_again = valid_input_2choice("Please enter 'y' or 'n':\n", "y", "n")
    if play_again == "y":
        print_pause("Nice! Enjoy!")
        play_game()
    elif play_again == "n":
        print_pause("Good game!")


play_game()
