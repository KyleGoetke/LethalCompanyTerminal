from threading import Thread
from itertools import cycle
from time import sleep
from datetime import datetime
from sys import stdout
import os

box = """
╔═══════════════════════════════════════════════════╗
║  BG IG, A System-Act Ally                         ║
║  Copyright(C) 2084-2108, Halden Electronics Inc.  ║
╚═══════════════════════════════════════════════════╝"""

box2 = """╠═══════════════════════════════════════════════════╣
║  CPU Type      :   BORSON 300 CPU at 2500 MHz     ║
║  Memory Test   :   45421586K OK                   ║
║                                                   ║
║  Boot Distribitioner Application v0.04            ║
║  Copyright(C) 2107 Distribitioner                 ║
╚═══════════════════════════════════════════════════╝"""

box3 = """║     Detecting String X ROM                        ║
╚═══════════════════════════════════════════════════╝"""

box4 = """║     Detecting Web LNV Extender                    ║
╚═══════════════════════════════════════════════════╝"""

box5 = """║     Detecting Heartbeats OK                       ║
╚═══════════════════════════════════════════════════╝
"""

listening = "UTGF Device Listening...\n"

tblh = """Body    ID     Neural     Device Class
- - - - - - - - - - - - - - - - - - - -"""
tbl1 = "2       52     Jo152      H515"
tbl2 = "2       52     Sa5155     H515"
tbl3 = "2       52     Bo75       H515"
tbl4 = "2       52     Eri510     H515"
tbl5 = "1       36     Ell567     H515"
tbl6 = "1       36     Jos912     H515"
tbl7 = "0"

print(box, end="\r")
sleep(1.5)
print(box2, end="\r")
sleep(0.75)
print(box3, end="\r")
sleep(0.75)
print(box4, end="\r")
sleep(2)
print(box5)
sleep(1)
print

done = False

print(listening)

def animate():
    for c in cycle(['|', '/', '-', '\\']):
        if done:
            break
        stdout.write("\r" + c)
        stdout.flush()
        sleep(0.1)

t = Thread(target=animate)
t.start()
sleep(4)
done = True

print(f"\r{tblh}")
sleep(0.5)
print(tbl1)
sleep(0.75)
print(tbl2)
sleep(0.75)
print(tbl3)
sleep(0.5)
print(tbl4)
sleep(0.75)
print(tbl5)
sleep(0.5)
print(tbl6)
sleep(0.75)
print(tbl7)
sleep(1)

print("\nDATABASE LOADED\n")
sleep(3)

balance = 60
route_cost = 0
current_location = ""
experimentation_weather = "mild"
assurance_weather = "rain"
vow_weather = "mild"
offense_weather = "flood"
march_weather = "flood"
rend_weather = "eclipse"
dine_weather = "eclipse"
titan_weather = "fog"
company_rate = "30%"

known_creatures = {
    "Locusts": "Unknown",
    "Manticoil": "New",
    "Flowerman": "Known"
}

stored_items = []

radar_boosters = []

current_players = ["player", "Cyan_Republic", "TrashBoat", "Scr333ch", "Larry"]

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

def get_weather(weather):
    match weather:
        case "mild":
            return ["", "mild weather"]
        case "rain":
            return ["(Rainy)", "rainy"]
        case "flood":
            return ["(Flooded)", "flooded"]
        case "eclipse":
            return["(Eclipsed)", "eclipsed"]
        case "fog":
            return["(Foggy)", "foggy"]

def info(choice):
    #! MOONS
    if "company".startswith(choice):
        print(f"The Company is buying your goods at {company_rate}\n")
        print("Go here to drop off any valuable scrap you've collected while on the job. The rate of return updates hourly and fluctuates over the course of several days.")
    elif "experimentation".startswith(choice):
        print("41-Experimentation\n----------------------\n")
        print("CONDITIONS: Arid. Low habitability, worsened by industrial artifacts.\n")
        print("HISTORY: Not discovered for quite some time due to its close orbit around gas giant Big Grin. However it appears to have been used in secret.\n")
        print("FAUNA: Unknown\n")
    elif "assurance".startswith(choice):
        print("220-Assurance\n----------------------\n")
        print("CONDITIONS: Similar to its twin moon, 41-Experimentation, featuring far more jagged and weathered terrain.\n")
        print("HISTORY: 220-Assurance is far younger than its counterpart. Discovered not long before 41-Experimentation.\n")
        print("FAUNA: Unknown\n")
    elif "vow".startswith(choice):
        print("56-Vow\n----------------------\n")
        print("CONDITIONS: Humid\n")
        print("HISTORY: Vow appears to have been inhabited by several colonies across its continents, but there is now no sign of life, and they have become a mystery.\n")
        print("FAUNA: Diverse, teeming with plant-life.\n")
    elif "offense".startswith(choice):
        print("21-Offense\n----------------------\n")
        print("CONDITIONS: Believed to have splintered of from its cousin Assurance, Offense features similar jagged and dry conditions but differs in its ecosystem.\n")
        print("HISTORY: 21-Offense is categorized as an asteroid moon and seems to have not existed on its own for more than several hundred years. The industrial artifacts here have suffered damage; it's believed they were built long before 21-Offense was splintered off.\n")
        print("FAUNA: A competitive and toughened ecosystem supports aggressive lifeforms. Travellers to 21-Offense should know it's not for the faint of heart.\n")
    elif "march".startswith(choice):
        print("61-March\n----------------------\n")
        print("CONDITIONS: March undergoes constant drizzling weather. Its terrain is more expansive.\n")
        print("HISTORY: This moon is overlooked due to its twin moon, Vow.\n")
        print("FAUNA: Unknown\n")
    elif "rend".startswith(choice):
        print("85-Rend\n----------------------\n")
        print("CONDITIONS: Its planet orbits a white dwarf star, making for inhospitale, cold conditions. Constant blizzards decrease visibility.\n")
        print("HISTORY: Several famous travelers went missing here, giving it some reputation. Their bodies are unlikely to be found due to the planet's conditions.\n")
        print("FAUNA: It's highly unlikely for complex life to exist here.\n")
    elif "dine".startswith(choice):
        print("7-Dine\n----------------------\n")
        print("CONDITIONS: Its planet orbits a white dwarf star, making for inhospitale, cold conditions. Constant blizzards decrease visibility.\n")
        print("HISTORY: Several famous travelers went missing here, giving it some reputation. Their bodies are unlikely to be found due to the planet's conditions.\n")
        print("FAUNA: It's highly unlikely for complex life to exist here.\n")
    elif "titan".startswith(choice):
        print("8-Titan\n----------------------\n")
        print("CONDITIONS: A frozen, flat landscape.\n")
        print("HISTORY: It looks like this moon was mined for resources. It's easy to get lost within the giant industrial complex. There are many entrances to it littered about the landscape.\n")
        print("FAUNA: Dangerous entities have been rumored to take residence in the vast network of tunnels.\n")
    #! STORE ITEMS
    elif "walkie-talkie".startswith(choice):
            print("Useful for keeping in touch! Hear other players when the walkie talkie is in your inventory. Must be in your hand and pressed down to transmit voice.")
    elif "flashlight".startswith(choice):
            print("The most affordable light source. It's even waterproof!")
    elif "shovel".startswith(choice):
            print("For self-defense!")
    elif "lockpicker".startswith(choice):
            print("Lock-pickers will unlock your limitless potential for efficiency on the job. Powered by proprietary AI software, they will get you access through any locked door.")
    elif "pro-flashlight".startswith(choice):
            print("With an extra battery life and even brighter bulb, your colleagues can never leave you in the dark again!")
    elif "stun grenade".startswith(choice):
            error()
    elif "boombox".startswith(choice):
            print("These jammong tunes are great for a morale boost on your crew!")
    elif "tzp-inhalant".startswith(choice):
            print("This safe and legal medicine can be administered to see great benefits to your performance on the job! Your ability to move LONG distances while carrying HEFTY objects will be second to none. Warning: TZP gas may impact the brain with extended exposure. Follow instructions manual provided with the canister.\nDon't forge to share!")
    elif "zap gun".startswith(choice):
            print("The most specialized self-protective equipment, capable of sending upwards of 80,000 volts!\n")
            print("To keep it targeted as long as possible, pull the gun side-to-side to counter the bend and fight against the pull of the electric beam. It can only stun for as long as you keep the current flowing.")
    elif "jetpack".startswith(choice):
            print("This device will get you around anywhere! Just use it responsibly!")
    elif "extension ladder".startswith(choice):
            print("This extension ladder can reach as high as nine meter! Use it to scale any cliff and reach for the stars. To save batteries the extension ladder automatically stores itself after 18 seconds.")
    elif "radar-booster".startswith(choice):
            print("Radar boosters come with many uses!\n")
            print("""Use the "SWITCH" command before the radar booster's name to view it on the main monitor. It must be activated.""")
            print("""Use the "PING" command before the radar booster's name to play a special sound from the device. """)
    elif "loud horn".startswith(choice):
            print("Used to communicate with any crew member from any distance, no walkie talkie required! The horn can be heard from anywhere. But what does it mean? That's up to you!")
    elif "teleporter".startswith(choice):
            print("Press the button to activate the teleporter. It will teleport whoever is currently being monitored on the ship's radar. They will not be able to keep any of their held items through the teleport. It takes about ten seconds to recharge.")
    elif "inverse teleporter".startswith(choice):
            print("The inverse teleporter is a modified teleporter which will teleport you to a random position outside the ship. All your items will be dropped at the teleporter before your transport. The inverse teleporter can be used by everyone at once andhas a 3.5 minute cooldown.\n")
            print("DISCLAIMER: The inverse teleporter can only transport you out, not in, and you may become trapped. The Company is not responsible for injury or replacement of heads and limbs induced by quantum entanglement and bad luck.")
    #! Creatures
    elif "manticoils".startswith(choice):
            print("Manticoils\n")
            print("Sigurd's danger level: 0%\n")
            print("Scientific name Quadrupes-manta\nMantacoils are a passerine bird of the family corvidae. Their bodies are quite large compared to their early descendants, and their wingspan ranges from 55 to 64 inches. Their most defining characteristic is their set of four wings. Their back wings are mostly used to stabilize when at low speed, while their front two wings create the majority of lift. Their round bodies are a striking yellow but with black outlines or stripes along their primary (rear) feathers.\n")
            print("Manticoils mostly feed on small insects but can also feed on small rodents. They are highly intelligent and social. They pose little threat and have a generally passive temperament towards humans, although they are capable of transmitting Rabies, Rubenchloria, and Pitt Virus.\n")
    elif "x".startswith(choice):
        print("x")
    else:
        error()

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
    for item in price_list:
        if item.startswith(choice):
            price = int(price_list[item]) * int(quantity)
            if price > balance:
                print(f"You could not afford these items!\nYour balance is ▘{balance}. Total cost of these items is ▘{price}.\n")
            else:
                print(f"You have requested to order {item}. Amount: {quantity}.")
                print(f"Total cost of items: ▘{price}.\n")
                option = input("Please CONFIRM or DENY.\n\n").lower()
                if "confirm".startswith(option):
                    balance = int(balance) - int(price)
                    clear_screen()
                    print(f"Ordered {quantity} {item}s. Your new balance is ▘{balance}.\n")
                    print("Our contractors enjoy fast, free shipping while on the job! Any purchased items will arrive hourly at your approximate location.\n")
                elif "deny".startswith(option):
                    print("\nCancelled order.\n\n")
                else:
                    buy(choice, quantity)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"▘{balance}\n\n")

def bestiary():
    global known_creatures
    print("BESTIARY\n")
    print('To access a creature file, type "INFO" after its name.\n---------------------------------\n')
    if all(value == "Unknown" for value in known_creatures.values()):
        print("No data collected on wildlife. Scans are required.\n")
    else:
        for creature in known_creatures:
            if known_creatures[creature] == "New":
                print(f"{creature} (New)")
                known_creatures[creature] = "Known"
            elif known_creatures[creature] == "Known":
                print(creature)
        print()

def route(destination):
    if "company".startswith(destination):
        print(f"The Company is buying at {company_rate}.\n")
        print("Do you want to route the autopilot to the Company building?\n\n")
        confirm_route(destination, "the Company building", 0)
        return
    elif "experimentation".startswith(destination):
        moon_id = "41-Experimentation"
        moon_weather = get_weather(experimentation_weather)[1]
    elif "assurance".startswith(destination):
        moon_id = "220-Assurance"
        moon_weather = get_weather(assurance_weather)[1]
    elif "vow".startswith(destination):
        moon_id = "56-Vow"
        moon_weather = get_weather(vow_weather)[1]
    elif "offense".startswith(destination):
        moon_id = "21-Offense"
        moon_weather = get_weather(offense_weather)[1]
    elif "march".startswith(destination):
        moon_id = "61-March"
        moon_weather = get_weather(march_weather)[1]
    elif "rend".startswith(destination):
        moon_id = "85-Rend"
        moon_weather = get_weather(rend_weather)[1]
    elif "dine".startswith(destination):
        moon_id = "7-Dine"
        moon_weather = get_weather(dine_weather)[1]
    elif "titan".startswith(destination):
        moon_id = "8-Titan"
        moon_weather = get_weather(titan_weather)[1]
    else:
        error()
        return

    print(f"The cost to route to {moon_id} is ▘{route_cost}.\n")
    print(f"It is currently {moon_weather} on this moon.\n\n")
    confirm_route(destination, moon_id, 1)

def confirm_route(destination, moon_id, bal_check):
    global current_location
    global balance
    option = input("Please CONFIRM or DENY.\n\n").lower()
    if "confirm".startswith(option):
        if current_location.startswith(destination):
            clear_screen()
            print("The autopilot ship is already orbiting this moon!\n")
            return
        elif not current_location.startswith(destination):
            current_location = destination
            clear_screen()
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
    clear_screen()
    print("[There was no action supplied with the word]\n")

clear_screen()
print("Welcome to the FORTUNE-9 OS")
print("          Courtesy of the Company\n")
print(f"Happy {datetime.today().strftime('%A')}.\n")
print('Type "Help" for a list of commands.\n')

while True:
    choice = input("").lower()
    match choice.split():
        case ["moons"]:
            clear_screen()
            print("Wecome to the exomoons catalogue.")
            print("To route the autopilot to a moon, use the word ROUTE.")
            print("To learn about any moon, use the word INFO.")
            print("----------------------------\n")
            print(f"* The Company building   //   Buying at {company_rate}.\n")
            print(f"* Experimentation {get_weather(experimentation_weather)[0]}")
            print(f"* Assurance {get_weather(assurance_weather)[0]}")
            print(f"* Vow {get_weather(vow_weather)[0]}\n")
            print(f"* Offense {get_weather(offense_weather)[0]}")
            print(f"* March {get_weather(march_weather)[0]}\n")
            print(f"* Rend {get_weather(rend_weather)[0]}")
            print(f"* Dine {get_weather(dine_weather)[0]}")
            print(f"* Titan {get_weather(titan_weather)[0]}\n")

        case ["info", item] | [item, "info"]:
            clear_screen()
            info(item)

        case ["route", destination]:
            clear_screen()
            route(destination)

        case ["store"]:
            clear_screen()
            store()

        case ["buy", item]:
            clear_screen()
            buy(item, 1)

        case ["buy", item, quantity]:
            clear_screen()
            buy(item, quantity)

        case ["bestiary"]:
            clear_screen()
            bestiary()

        case ["storage"]:
            clear_screen()
            storage()

        case ["other"]:
            clear_screen()
            print(">VIEW MONITOR\nTo togle on AND off the main monitor's map cam.\n")
            print(">SWITCH [Player name]\nTo switch view to a player on the main monitor.\n")
            print(">PING [Radar booster name]\nTo make a radar booster play a noise.\n")
            print(">SCAN\nTo scan for the number of items left on the current planet.\n")

        case ["view", "monitor"]:
            clear_screen()
            print("Toggling radar cam\n\n")

        case ["switch", switch_target]:
            for name in current_players:
                if name.lower().startswith(switch_target.lower()):
                    clear_screen()
                    print(f"Switched radar to {name}.\n")
                #TODO else:
                #TODO     error()

        case ["ping", booster_name]:
            if booster_name in radar_boosters:
                print(f"{booster_name}")
                #TODO NO CLUE ABOUT FUNCTIONALITY
            else:
                error()

        case ["scan"]:
            clear_screen()
            left_behind_value = 0
            left_behind_objects = []
            for each in left_behind_objects:
                left_behind_value += each * price_list[item]
            print(f"There are {len(left_behind_objects)} objects outside the ship, totalling at approximate value of ▘{left_behind_value}.\n")

        case ["help"]:
            clear_screen()
            print(">MOONS\nTo see the list of moons the autopilt can route to.\n")
            print(">STORE\nTo see the company store's selection of useful products.\n")
            print(">BESTIARY\nTo see the list of wildlife on record.\n")
            print(">STORAGE\nTo access objects placed into storage.\n")
            print(">OTHER\nTo see the list of other commands\n")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if "xyz" == "xyz":
                print(f"{'1'} purchased items on route.\n")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        case ["exit"] | ["q"]:
            print("")
            exit()

        case ["add", value]:
            balance += int(value)
            # clear_screen()
            print(f"\nNew balance is ▘{balance}.\n")

        case _:
            error()
