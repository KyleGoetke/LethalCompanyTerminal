from datetime import datetime
import os
import random
import sys
import textwrap
from time import sleep


def startscreen():
    os.system("cls" if os.name == "nt" else "clear")

    print("╔═══════════════════════════════════════════════════╗\n║  BG IG, A System-Act Ally                         ║\n║  Copyright(C) 2084-2108, Halden Electronics Inc.  ║\n╚═══════════════════════════════════════════════════╝", end="\r")
    sleep(1.5)
    print("╠═══════════════════════════════════════════════════╣\n║  CPU Type      :   BORSON 300 CPU at 2500 MHz     ║\n║  Memory Test   :   45421586K OK                   ║\n║                                                   ║\n║  Boot Distribitioner Application v0.04            ║\n║  Copyright(C) 2107 Distribitioner                 ║\n╚═══════════════════════════════════════════════════╝", end="\r")
    sleep(0.75)
    print("║     Detecting String X ROM                        ║\n╚═══════════════════════════════════════════════════╝", end="\r")
    sleep(0.75)
    print("║     Detecting Web LNV Extender                    ║\n╚═══════════════════════════════════════════════════╝", end="\r")
    sleep(2)
    print("║     Detecting Heartbeats OK                       ║\n╚═══════════════════════════════════════════════════╝\n")
    sleep(1)
    print("\nUTGF Device Listening...\n")

    animation = "|/-\\"
    for i in range(50):
        sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\rBody    ID     Neural     Device Class\n---------------------------------------")
    sleep(0.5)
    print("2       52     Jo152      H515")
    sleep(0.75)
    print("2       52     Sa5155     H515")
    sleep(0.75)
    print("2       52     Bo75       H515")
    sleep(0.5)
    print("2       52     Eri510     H515")
    sleep(0.75)
    print("1       36     Ell567     H515")
    sleep(0.5)
    print("1       36     Jos912     H515")
    sleep(0.75)
    print("0")
    sleep(1)
    print("\nOS Loaded\n")
    sleep(3)


# global variables
balance = 60
route_cost = 0
purchased_items = 0
current_location = ""
experimentation_weather = random.choice(["mild", "rain", "flood", "eclipse", "fog"])
assurance_weather = random.choice(["mild", "rain", "flood", "eclipse", "fog"])
vow_weather = random.choice(["mild", "rain", "flood", "eclipse", "fog"])
offense_weather = random.choice(["mild", "rain", "flood", "eclipse", "fog"])
march_weather = random.choice(["mild", "rain", "flood", "eclipse", "fog"])
rend_weather = random.choice(["mild", "rain", "flood", "eclipse", "fog"])
dine_weather = random.choice(["mild", "rain", "flood", "eclipse", "fog"])
titan_weather = random.choice(["mild", "rain", "flood", "eclipse", "fog"])
company_rate = 0.3
terminal_max_width = 160

known_creatures = {
    "baboon hawks": "Unknown",
    "brakens": "Unknown",
    "bunker spiders": "Unknown",
    "circuit bees": "Unknown",
    "coil-heads": "Unknown",
    "earth leviathans": "Unknown",
    "eyeless dogs": "Unknown",
    "forest keepers": "Unknown",
    "hoarding bugs": "Unknown",
    "hygroderes": "Unknown",
    "jesters": "Unknown",
    "lasso man": "Unknown",
    "manticoils": "Unknown",
    "roaming locusts": "Unknown",
    "snare fleas": "Unknown",
    "spore lizards": "Unknown",
    "thumpers": "Unknown"
}

stored_items = []

radar_boosters = []

current_players = {
    "player": "alive",
    "username1": "alive",
    "Individual2": "alive",
    "Company_Intern": "dead",
    "VIP": "alive"
}

price_list = {
    "walkie-talkie": 12,
    "flashlight": 15,
    "shovel": 30,
    "lockpicker": 20,
    "pro-flashlight": 25,
    "stun grenade": 40,
    "boombox": 60,
    "tzp-inhalant": 120,
    "zap gun": 400,
    "jetpack": 700,
    "extension ladder": 60,
    "radar-booster": 50,
    "loud horn": 150,
    "teleporter": 375,
    "inverse teleporter": 425,
    "romantic table": 120,
    "pajama suit": 900,
    "television": 130,
    "shower": 180,
    "cozy lights": 140
}


def getweather(weather):
    match weather:
        case "mild":
            return ["", "mild weather"]
        case "rain":
            return ["(Rainy)", "rainy"]
        case "flood":
            return ["(Flooded)", "flooded"]
        case "eclipse":
            return ["(Eclipsed)", "eclipsed"]
        case "fog":
            return ["(Foggy)", "foggy"]


def info(choice):
    global terminal_max_width
    #! MOONS
    if "assurance".startswith(choice):
        with open("moons/assurance.txt", "r") as f:
            file_contents = f.readlines()
    elif "company".startswith(choice):
        print(f"The Company is buying your goods at {int(company_rate * 100)}%\n")
        print("Go here to drop off any valuable scrap you've collected while on the job. The rate of return updates hourly and fluctuates over the course of several days.")
    elif "dine".startswith(choice):
        with open("moons/dine.txt", "r") as f:
            file_contents = f.readlines()
    elif "experimentation".startswith(choice):
        with open("moons/experimentation.txt", "r") as f:
            file_contents = f.readlines()
    elif "march".startswith(choice):
        with open("moons/march.txt", "r") as f:
            file_contents = f.readlines()
    elif "offense".startswith(choice):
        with open("moons/offense.txt", "r") as f:
            file_contents = f.readlines()
    elif "rend".startswith(choice):
        with open("moons/rend.txt", "r") as f:
            file_contents = f.readlines()
    elif "titan".startswith(choice):
        with open("moons/titan.txt", "r") as f:
            file_contents = f.readlines()
    elif "vow".startswith(choice):
        with open("moons/vow.txt", "r") as f:
            file_contents = f.readlines()
    #! STORE ITEMS
    elif "boombox".startswith(choice):
        with open("items/boombox.txt", "r") as f:
            file_contents = f.readlines()
    elif "extension ladder".startswith(choice):
        with open("items/extension_ladder.txt", "r") as f:
            file_contents = f.readlines()
    elif "flashlight".startswith(choice):
        with open("items/flashlight.txt", "r") as f:
            file_contents = f.readlines()
    elif "inverse teleporter".startswith(choice):
        with open("items/inverse_teleporter.txt", "r") as f:
            file_contents = f.readlines()
    elif "jetpack".startswith(choice):
        with open("items/jetpack.txt", "r") as f:
            file_contents = f.readlines()
    elif "lockpicker".startswith(choice):
        with open("items/lockpicker.txt", "r") as f:
            file_contents = f.readlines()
    elif "loud horn".startswith(choice):
        with open("items/loud_horn.txt", "r") as f:
            file_contents = f.readlines()
    elif "pro-flashlight".startswith(choice):
        with open("items/pro_flashlight.txt", "r") as f:
            file_contents = f.readlines()
    elif "radar-booster".startswith(choice):
        with open("items/radar_booster.txt", "r") as f:
            file_contents = f.readlines()
    elif "shovel".startswith(choice):
        with open("items/shovel.txt", "r") as f:
            file_contents = f.readlines()
    elif "stun grenade".startswith(choice):
        try:
            with open("items/stun_grenade.txt", "r") as f:
                file_contents = f.readlines()
        except FileNotFoundError:
            file_contents = ""
            error()
    elif "teleporter".startswith(choice):
        with open("items/teleporter.txt", "r") as f:
            file_contents = f.readlines()
    elif "tzp-inhalant".startswith(choice):
        with open("items/tzp_inhalant.txt", "r") as f:
            file_contents = f.readlines()
    elif "walkie-talkie".startswith(choice):
        with open("items/walkie_talkie.txt", "r") as f:
            file_contents = f.readlines()
    elif "zap gun".startswith(choice):
        with open("items/zap_gun.txt", "r") as f:
            file_contents = f.readlines()
    #! Creatures
    elif "baboon hawks".startswith(choice):
        with open("creatures/baboon_hawks.txt", "r") as f:
            file_contents = f.readlines()
    elif "brakens".startswith(choice):
        with open("creatures/brakens.txt", "r") as f:
            file_contents = f.readlines()
    elif "bunker spiders".startswith(choice):
        with open("creatures/bunker_spiders.txt", "r") as f:
            file_contents = f.readlines()
    elif "circuit bees".startswith(choice):
        with open("creatures/circuit_bees.txt", "r") as f:
            file_contents = f.readlines()
    elif "coil heads".startswith(choice):
        with open("creatures/coil_heads.txt", "r") as f:
            file_contents = f.readlines()
    elif "earth leviathans".startswith(choice):
        with open("creatures/earth_leviathans.txt", "r") as f:
            file_contents = f.readlines()
    elif "eyeless dogs".startswith(choice):
        with open("creatures/eyeless_dogs.txt", "r") as f:
            file_contents = f.readlines()
    elif "forest keepers".startswith(choice):
        with open("creatures/forest_keepers.txt", "r") as f:
            file_contents = f.readlines()
    elif "hoarding bugs".startswith(choice):
        with open("creatures/hoarding_bugs.txt", "r") as f:
            file_contents = f.readlines()
    elif "hygroderes".startswith(choice):
        with open("creatures/hygroderes.txt", "r") as f:
            file_contents = f.readlines()
    elif "jesters".startswith(choice):
        with open("creatures/jesters.txt", "r") as f:
            file_contents = f.readlines()
    elif "lasso man".startswith(choice) or "lasso men".startswith(choice):
        with open("creatures/lasso_man.txt", "r") as f:
            file_contents = f.readlines()
    elif "manticoils".startswith(choice):
        with open("creatures/manticoils.txt", "r") as f:
            file_contents = f.readlines()
    elif "roaming locusts".startswith(choice):
        with open("creatures/roaming_locusts.txt", "r") as f:
            file_contents = f.readlines()
    elif "snare fleas".startswith(choice):
        with open("creatures/snare_fleas.txt", "r") as f:
            file_contents = f.readlines()
    elif "spore lizards".startswith(choice):
        with open("creatures/spore_lizards.txt", "r") as f:
            file_contents = f.readlines()
    elif "thumpers".startswith(choice):
        with open("creatures/thumpers.txt", "r") as f:
            file_contents = f.readlines()
    else:
        error()
        return
    for line in file_contents:
        print(textwrap.fill(line, terminal_max_width))
    if not file_contents == "":
        print("")


def store():
    global price_list
    print("Welcome to the Company store.\nUse words BUY and INFO on any item.\nOrder tools in bulk by typing a number.")
    print("----------------------------\n\n")
    print(f"Walkie-talkie  //  Price: ▘{price_list['walkie-talkie']}")
    print(f"Flashlight  //  Price: ▘{price_list['flashlight']}")
    print(f"Shovel  //  Price: ▘{price_list['shovel']}")
    print(f"Lockpicker  //  Price: ▘{price_list['lockpicker']}")
    print(f"Pro-flashlight  //  Price: ▘{price_list['pro-flashlight']}")
    print(f"Stun grenade  //  Price: ▘{price_list['stun grenade']}")
    print(f"Boombox  //  Price: ▘{price_list['boombox']}")
    print(f"TZP-Inhalant  //  Price: ▘{price_list['tzp-inhalant']}")
    print(f"Zap gun  //  Price: ▘{price_list['zap gun']}")
    print(f"Jetpack  //  Price: ▘{price_list['jetpack']}")
    print(f"Extension ladder  //  Price: ▘{price_list['extension ladder']}")
    print(f"Radar-booster  //  Price: ▘{price_list['radar-booster']}")
    print("\nSHIP UPGRADES")
    print(f"Loud horn  //  Price: ▘{price_list['loud horn']}")
    print(f"Teleporter  //  Price: ▘{price_list['teleporter']}")
    print(f"Inverse Teleporter  //  Price: ▘{price_list['inverse teleporter']}")
    print("\nThe selection of ship decor rotates per-quote. Be sure to check back next week:\n----------------------------\n")
    print(f"Romantic table  //  ▘{price_list['romantic table']}")
    print(f"Pajama suit  //  ▘{price_list['pajama suit']}")
    print(f"Television  //  ▘{price_list['television']}")
    print(f"Shower  //  ▘{price_list['shower']}")
    print(f"Cozy lights  //  ▘{price_list['cozy lights']}\n")


def buy(choice, quantity):
    global balance
    global purchased_items
    if not quantity.isdigit():
        quantity = 1
    quantity = int(quantity)
    for item in price_list:
        if item.startswith(choice):
            price = price_list[item] * quantity
            if price > balance:
                print(f"You could not afford these items!\nYour balance is ▘{balance}. Total cost of these items is ▘{price}.\n")
            else:
                print(f"You have requested to order {item}. Amount: {quantity}.")
                print(f"Total cost of items: ▘{price}.\n")
                option = input("Please CONFIRM or DENY.\n\n").lower()
                if "confirm".startswith(option):
                    balance = balance - price
                    clearscreen()
                    print(f"Ordered {quantity} {item}s. Your new balance is ▘{balance}.\n")
                    purchased_items += quantity
                    print("Our contractors enjoy fast, free shipping while on the job! Any purchased items will arrive hourly at your approximate location.\n")
                elif "deny".startswith(option):
                    print("\nCancelled order.\n\n")
                else:
                    buy(choice, quantity)


def clearscreen():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"▘{balance}\n\n")


def bestiary():
    global known_creatures
    print("BESTIARY\n")
    print("To access a creature file, type \"INFO\" after its name.\n---------------------------------\n")
    if all(value == "Unknown" for value in known_creatures.values()):
        print("No data collected on wildlife. Scans are required.\n")
    else:
        for creature in known_creatures:
            if known_creatures[creature] == "New":
                print(f"{creature} (New)")
                known_creatures[creature] = "Known"
            elif known_creatures[creature] == "Known":
                print(creature)
        print("")


def route(destination):
    if "company".startswith(destination):
        print(f"The Company is buying at {int(company_rate * 100)}%.\n")
        print("Do you want to route the autopilot to the Company building?\n\n")
        confirmroute(destination, "the Company building", 0)
        return
    elif "experimentation".startswith(destination):
        moon_id = "41-Experimentation"
        moon_weather = getweather(experimentation_weather)[1]
    elif "assurance".startswith(destination):
        moon_id = "220-Assurance"
        moon_weather = getweather(assurance_weather)[1]
    elif "vow".startswith(destination):
        moon_id = "56-Vow"
        moon_weather = getweather(vow_weather)[1]
    elif "offense".startswith(destination):
        moon_id = "21-Offense"
        moon_weather = getweather(offense_weather)[1]
    elif "march".startswith(destination):
        moon_id = "61-March"
        moon_weather = getweather(march_weather)[1]
    elif "rend".startswith(destination):
        moon_id = "85-Rend"
        moon_weather = getweather(rend_weather)[1]
    elif "dine".startswith(destination):
        moon_id = "7-Dine"
        moon_weather = getweather(dine_weather)[1]
    elif "titan".startswith(destination):
        moon_id = "8-Titan"
        moon_weather = getweather(titan_weather)[1]
    else:
        error()
        return

    print(f"The cost to route to {moon_id} is ▘{route_cost}.\n")
    print(f"It is currently {moon_weather} on this moon.\n\n")
    confirmroute(destination, moon_id, 1)


def confirmroute(destination, moon_id, bal_check):
    global current_location
    global balance
    option = input("Please CONFIRM or DENY.\n\n").lower()
    if "confirm".startswith(option):
        if current_location.startswith(destination):
            clearscreen()
            print("The autopilot ship is already orbiting this moon!\n")
            return
        elif not current_location.startswith(destination):
            current_location = destination
            clearscreen()
            print(f"Routing autopilot to {moon_id}.")
            if bal_check == 1:
                print(f"Your new balance is {balance}.")
            print("\nPlease enjoy your flight.\n")
    elif "deny".startswith(option):
        print("\nYou have cancelled the order.\n\n")
    else:
        route(destination)


def storage():
    global stored_items
    print("While moving furniture with [B], you an pres [X] to send it to storage. You can call it back from storage here.\n")
    print("These are the items in storage:\n")
    if stored_items == []:
        print("[No items stored. While moving and object with [B], press [X] to store it.]\n")
    else:
        for item in stored_items:
            print(item)


def error():
    clearscreen()
    print("[There was no action supplied with the word]\n")


# Main execution loop
try:
    startscreen()
except KeyboardInterrupt:
    pass
clearscreen()
print("Welcome to the FORTUNE-9 OS")
print("          Courtesy of the Company\n")
print(f"Happy {datetime.today().strftime('%A')}.\n")
print("Type \"Help\" for a list of commands.\n\n\n")

while True:
    choice = input("").lower()
    match choice.split():
        case ["moons"]:
            clearscreen()
            print("Wecome to the exomoons catalogue.")
            print("To route the autopilot to a moon, use the word ROUTE.")
            print("To learn about any moon, use the word INFO.")
            print("----------------------------\n")
            print(f"* The Company building   //   Buying at {int(company_rate * 100)}%.\n")
            print(f"* Experimentation {getweather(experimentation_weather)[0]}")
            print(f"* Assurance {getweather(assurance_weather)[0]}")
            print(f"* Vow {getweather(vow_weather)[0]}\n")
            print(f"* Offense {getweather(offense_weather)[0]}")
            print(f"* March {getweather(march_weather)[0]}\n")
            print(f"* Rend {getweather(rend_weather)[0]}")
            print(f"* Dine {getweather(dine_weather)[0]}")
            print(f"* Titan {getweather(titan_weather)[0]}\n")

        case ["info", item] | [item, "info"]:
            clearscreen()
            info(item)

        case ["route", destination]:
            clearscreen()
            route(destination)

        case ["store"]:
            clearscreen()
            store()

        case ["buy", item]:
            clearscreen()
            buy(item, 1)

        case ["buy", item, quantity]:
            clearscreen()
            buy(item, quantity)

        case ["bestiary"]:
            clearscreen()
            bestiary()

        case ["storage"]:
            clearscreen()
            storage()

        case ["other"]:
            clearscreen()
            print(">VIEW MONITOR\nTo togle on AND off the main monitor's map cam.\n")
            print(">SWITCH [Player name]\nTo switch view to a player on the main monitor.\n")
            print(">PING [Radar booster name]\nTo make a radar booster play a noise.\n")
            print(">SCAN\nTo scan for the number of items left on the current planet.\n")

        case ["view", "monitor"]:
            clearscreen()
            print("Toggling radar cam\n\n")

        case ["switch", switch_target]:
            valid_name = False
            for name in current_players:
                if name.lower().startswith(switch_target.lower()):
                    clearscreen()
                    print(f"Switched radar to {name}.\n")
                    valid_name = True
            for name in radar_boosters:
                if name.lower().startswith(switch_target.lower()):
                    clearscreen()
                    print(f"Switched radar to {name}.\n")
                    valid_name = True
            if valid_name == False:
                error()

        case ["ping", booster_name]:
            if booster_name in radar_boosters:
                print(f"{booster_name}")
                # TODO, NO CLUE ABOUT FUNCTIONALITY
            else:
                error()

        case ["scan"]:
            clearscreen()
            left_behind_value = 0
            left_behind_objects = []
            for each in left_behind_objects:
                left_behind_value += each * price_list[item]
            print(f"There are {len(left_behind_objects)} objects outside the ship, totalling at approximate value of ▘{left_behind_value}.\n")

        case ["help"]:
            clearscreen()
            print(">MOONS\nTo see the list of moons the autopilt can route to.\n")
            print(">STORE\nTo see the company store's selection of useful products.\n")
            print(">BESTIARY\nTo see the list of wildlife on record.\n")
            print(">STORAGE\nTo access objects placed into storage.\n")
            print(">OTHER\nTo see the list of other commands\n")
            if purchased_items > 1:
                print(f"{purchased_items} purchased items on route.\n")
                purchased_items = 0
            elif purchased_items > 0:
                print(f"{purchased_items} purchased item on route.\n")
                purchased_items = 0

        case ["exit"] | ["q"]:
            print("")
            exit()

        case ["add", value]:
            balance += int(value)
            print(f"\nNew balance is ▘{balance}.\n")

        case _:
            error()
