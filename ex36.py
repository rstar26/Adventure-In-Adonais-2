import sys
import random
import time
import os
start_puzzle = False
cabin_puzzle = False
cabin_basket_searched = False
cabin_mantle_box_searched = False
cabin_locked_chest_searched = False
forest_grove_puzzle = False
pickles_clearing_puzzle = False
everton_ruins_solved = False
everton_ruins_barracks_warg_dead = False
everton_ruins_kitchen_goblin_dead = False
everton_ruins_lords_chamber_searched =False
everton_ruins_ogre_dead = False
everton_ruins_bed_chamber_searched = False
everton_ruins_footlocker_key = False
cappadocia_basilisk_dead = False
black_hollow_camp_battle_won = False
crowly_met = False
bruenor_met = False
monster = None
player = None

class Player_character():
    def __init__(self):        
        self.name = None
        self.armor_bonus = 0
        self.hit_points = 15
        self.armor = []
        self.home = None
        self.weapons = []
        self.current_weapon = None   
        self.gold = 0
        self.wand_charges = None
        self.acorns = None
        self.items = []

    def player_inventory_count(self):
        if "Wand" in self.weapons:
            print(f"\nYour Wand has {self.wand_charges} charges remaining.")
        if "Acorn"in self.weapons:
            print(f"\nYou have {self.acorns} Acorns remaining")
        else:
            return
    
    def player_armor_bonus_calc(self):
        if not self.armor:
            self.armor_bonus = 0
        elif "travelling cloak" in self.armor and not "chain mail" in self.armor:
            self.armor_bonus = 5
        elif "travelling cloak" in self.armor and "chain mail" in self.armor:
            self.armor_bonus = 15
        elif "chain mail" in self.armor and not "travelling cloak" in self.armor:
            self.armor_bonus = 10
        elif "travelling cloak" not in self.armor and "chain mail" not in self.armor:
            self.armor_bonus = 0
        else:
            self.armor_bonus = 0

    
    def player_hit_points(self):
        
        hit_points = self.hit_points + self.armor_bonus
        return hit_points
    
    def to_hit(self):
        crit_chance = random.randint(1, 100)
        if crit_chance in range(70, 100):
            print("\nA Critical Hit!")
            return crit_chance
        else:
            print("\nA Regular Hit!")
            return crit_chance
    
    def player_weapon_choice(self):
        print("\nPlease select a weapon to attack with:")
        for i, item in enumerate(self.weapons, 1):
            print(i, '. ' + item, ' ', sep=' ', end='')
        #print(f"{self.weapons}")
        self.player_inventory_count()
        player_weapon_choice = str.lower(input("\n> "))
        #self.current_weapon = player_weapon_choice
        if "1" in player_weapon_choice and "Fist" in self.weapons or "fist" in player_weapon_choice and "Fist" in self.weapons:
            self.current_weapon = "Fist"
            crit_chance = self.to_hit()
            if crit_chance in range(70, 100):
                player_damage = random.randint(2, 4)
                return player_damage
            else:
                player_damage = random.randint(1, 2)
                return player_damage    
        elif "1" in player_weapon_choice and "Dagger" in self.weapons or "dagger" in player_weapon_choice and "Dagger" in self.weapons:
            self.current_weapon = "Dagger"
            crit_chance = self.to_hit()
            if crit_chance in range(70, 100):
                player_damage = random.randint(6, 10)
                return player_damage
            else:
                player_damage = random.randint(1, 5)
                return player_damage   
        elif "1" in player_weapon_choice and "Broad Sword" in self.weapons or "broad sword" in player_weapon_choice and "Broad Sword" in self.weapons:
            self.current_weapon = "Broad Sword"
            crit_chance = self.to_hit()
            if crit_chance in range(70,100):
                player_damage = random.randint(10, 15)
                return player_damage
            else:
                player_damage = random.randint(5, 10)
                return player_damage
        elif "3" in player_weapon_choice and "Wand" in self.weapons or "wand" in player_weapon_choice and "Wand" in self.weapons:
            wand_charges = self.wand_charges
            self.current_weapon = "Magic Wand"
            if wand_charges > 0:
                crit_chance = self.to_hit()
                if crit_chance in range(70, 100):
                    player_damage = random.randint(15, 20)
                    self.wand_charges = self.wand_charges - 1
                    return player_damage
                else:
                    player_damage = random.randint(10, 15)
                    self.wand_charges = self.wand_charges - 1
                    return player_damage
            else:
                print("You are out of charges.")
                player_damage = self.player_weapon_choice()
                return player_damage
        elif "2" in player_weapon_choice and "Acorn" in self.weapons or "acorn" in player_weapon_choice and "Acorn" in self.weapons:
            self.current_weapon = "Magic Acorn"
            acorns_in_inv = self.acorns
            if acorns_in_inv > 0:
                crit_chance = self.to_hit()
                if crit_chance in range(70, 100):
                    player_damage = random.randint(20, 30)
                    self.acorns = self.acorns - 1
                    return player_damage
                else:
                    player_damage = random.randint(15, 20)
                    self.acorns = self.acorns - 1
                    return player_damage
            else:
                print("\nYou are out of Acorns.")
                player_damage = self.player_weapon_choice()
                return player_damage
        else:
            print("\nI do not understand that.")
            player_damage = self.player_weapon_choice()
            return player_damage

class Item(object):
    def __init__(self, name, dmg, crt, health_bonus, price):
        self.name = name
        self.dmg = dmg
        self.crt = crt
        self.health_bonus = health_bonus
        self.price = price

class Store_Inventory(object):
    def __init__(self):
        self.items = {}

    def add_items(self, item):
        self.items[item.name] = item

    def print_items(self):
        print("\t".join(["Name         ", "Dmg", "Crt", "+HP", "Val"]))
        for item in self.items.values():
            print("\t".join([str(x) for x in [item.name, item.dmg, item.crt, item.health_bonus, item.price]]))


class Giant_rat():
    def __init__(self):
        self.name = "Giant Rat"
        self.hit_points = 10
        self.crit = "teeth"
    def regular_hit(self):
        monster_damage = random.randint(1, 3)
        return monster_damage

    def critical_hit(self):
        monster_damage = random.randint(3, 7)
        return monster_damage
    def monster_gold(self):
        monster_gold = random.randint(5, 10)
        player.gold = player.gold + monster_gold
        return monster_gold

class Orc():
    def __init__(self):
        self.name = "Orc"
        self.crit = "powerful slash"
        self.hit_points = 12

    def regular_hit(self):
        monster_damage = random.randint(2, 6)
        return monster_damage

    def critical_hit(self):
        monster_damage = random.randint(4, 8)
        return monster_damage
    def monster_gold(self):
        monster_gold = random.randint(12, 18)
        player.gold = player.gold + monster_gold
        return monster_gold

class Wild_dog():
    def __init__(self):
        self.name = "Wild Dog"
        self.crit = "viscious bite"
        self.hit_points = 11

    def regular_hit(self):
        monster_damage = random.randint(2, 4)
        return monster_damage

    def critical_hit(self):
        monster_damage = random.randint(3, 6)
        return monster_damage
    def monster_gold(self):
        monster_gold = random.randint(3, 13)
        player.gold = player.gold + monster_gold
        return monster_gold

class Small_spider():
    def __init__(self):
        self.name = "Small Spider"
        self.hit_points = 5
        self.crit = "venom bite"
    def regular_hit(self):
        monster_damage = random.randint(1, 2)
        return monster_damage

    def critical_hit(self):
        monster_damage = random.randint(2, 5)
        return monster_damage
    def monster_gold(self):
        monster_gold = random.randint(3, 7)
        player.gold = player.gold + monster_gold
        return monster_gold

class Warg():
    def __init__(self):
        self.name = "Warg"
        self.hit_points = 13
        self.crit = "rabbid bite"
        self.gold = ()
    def regular_hit(self):
        monster_damage = random.randint(2, 5)
        return monster_damage

    def critical_hit(self):
        monster_damage = random.randint(6,8)
        return monster_damage

    def monster_gold(self):
        monster_gold = random.randint(10, 15)
        player.gold = player.gold + monster_gold
        return monster_gold

class Goblin():
    def __init__(self):
        self.name = "Goblin"
        self.hit_points = 13
        self.crit = "axe slash"
        self.gold = ()

    def regular_hit(self):
        monster_damage = random.randint(2, 4)
        return monster_damage

    def critical_hit(self):
        monster_damage = random.randint(5, 8)
        return monster_damage
    def monster_gold(self):
        monster_gold = random.randint(13, 18)
        player.gold = player.gold + monster_gold
        return monster_gold

class Mountain_Ogre():
    def __init__(self):
        self.name = "Mountain Ogre"
        self.hit_points = 22
        self.crit = "Club Smash"
    def regular_hit(self):
        monster_damage = random.randint(5, 8)
        return monster_damage
    def critical_hit(self):
        monster_damage = random.randint(9, 11)
        return monster_damage
    def monster_gold(self):
        monster_gold = random.randint(15, 22)
        player.gold = player.gold + monster_gold
        return monster_gold

class Desert_scorpian():
    def __init__(self):
        self.name = "Desert Scorpian"
        self.hit_points = 10
        self.crit = "Venom Barb"

    def regular_hit(self):
        monster_damage = random.randint(3, 6)
        return monster_damage

    def critical_hit(self):
        monster_damage = random.randint(6, 8)
        return monster_damage

    def monster_gold(self):
        monster_gold = random.randint(7, 12)
        player.gold = player.gold + monster_gold
        return monster_gold

class Desert_mummy():
    def __init__(self):
        self.name = "Decayed Mummy"
        self.crit = "Ancient Curse"
        self.hit_points = 14

    def regular_hit(self):
        monster_damage = random.randint(3, 5)
        return monster_damage

    def critical_hit(self):
        monster_damage = random.randint(6, 10)
        return monster_damage

    def monster_gold(self):
        monster_gold = random.randint(10, 15)
        player.gold = player.gold + monster_gold
        return monster_gold

class Desert_deathworm():
    def __init__(self):
        self.name = "Death Worm"
        self.crit = "Venomous Skin"
        self.hit_points = 9

    def regular_hit(self):
        monster_damage = random.randint(2, 4)
        return monster_damage

    def critical_hit(self):
        monster_damage = random.randint(8, 12)
        return monster_damage
    
    def monster_gold(self):
        monster_gold = random.randint(5, 8)
        player.gold = player.gold + monster_gold
        return monster_gold

class Desert_scarab():
    def __init__(self):
        self.name = "Scarab Beetle"
        self.crit = "Gnawing Bite"
        self.hit_points = 8

    def regular_hit(self):
        monster_damage = random.randint(2, 4)
        return monster_damage

    def critical_hit(self):
        monster_damage = random.randint(5, 8)
        return monster_damage

    def monster_gold(self):
        monster_gold = random.randint(2, 4)
        player.gold = player.gold + monster_gold
        return monster_gold

class Desert_sandspider():
    def __init__(self):
        self.name = "Sand Spider"
        self.crit = "Choking Web"
        self.hit_points = 15

    def regular_hit(self):
        monster_damage = random.randint(5, 8)
        return monster_damage

    def critical_hit(self):
        monster_damage = random.randint(9, 11)
        return monster_damage

    def monster_gold(self):
        monster_gold = random.randint(15, 20)
        player.gold = player.gold + monster_gold
        return monster_gold

class Desert_basilisk():
    def __init__(self):
        self.name = "Desert Basilisk"
        self.crit = "Venemous Fang"
        self.hit_points = 20

    def regular_hit(self):
        monster_damage = random.randint(4, 8)
        return monster_damage

    def critical_hit(self):
        monster_damage = random.randint(9, 13)
        return monster_damage

    def monster_gold(self):
        monster_gold = random.randint(20, 25)
        player.gold = player.gold + monster_gold
        return monster_gold

class Hobgoblin_bandit():
    def __init__(self):
        self.name = "Hobgoblin Bandit"
        self.crit = "poison dagger"
        self. hit_points = 10

    def regular_hit(self):
        monster_damage = random.randint(3, 6)
        return monster_damage

    def critical_hit(self):
        monster_damage = random.randint(5, 7)
        return monster_damage

    def monster_gold(self):
        monster_gold = random.randint(5, 10)
        player.gold = player.gold + monster_gold
        return monster_gold

class Hobgoblin_boss():
    def __init__(self):
        self.name = "Hobgoblin Captain"
        self.crit = "axe strike"
        self.hit_points = 15

    def regular_hit(self):
        monster_damage = random.randint(5, 9)
        return monster_damage

    def critical_hit(self):
        monster_damage = random.randint(9, 12)
        return monster_damage

    def monster_gold(self):
        monster_gold = random.randint(20, 25)
        player.gold = player.gold + monster_gold
        return monster_gold

def character_creator():
    print("\nBefore we get started, let's create your character!")
    player.name = input("\nEnter your name:\n> ")
    player.home = input("\nWhere are you from:\n> ")

def battler():
    global monster
    global player
    monster_hp = monster.hit_points
    player.player_armor_bonus_calc()
    player_hp = player.player_hit_points()
    monster_dead = False
    while monster_hp > 0 and player_hp > 0:
        print(f"\nThe {monster.name} has {monster_hp} HP.")
        print(f"You have {player_hp} HP.")
        print(f"\nYou attack the {monster.name}!")
        equation_solved = battler_function()
        if equation_solved == True:
            damage = player.player_weapon_choice()
            time.sleep(1)
            os.system("cls")
            print(f"\nYou hit the {monster.name} with your {player.current_weapon.capitalize()} for {damage} damage.")
            monster_hp = monster_hp - damage          
            if monster_hp < 1:
                print(f"\nYou have slain the {monster.name}")
                monster_dead = True
                monster_loot = monster.monster_gold()
                print(f"\nYou have found {monster_loot} gold coins!")
                print(f"\nYou have {player.gold} gold coins!")
                clr_screen()
                return monster_dead
            elif monster_hp > 1:          
                monster_damage = monster.regular_hit()
                time.sleep(1)
                print(f"The {monster.name} counter attacks and hits you for {monster_damage} damage!")
                player_hp = player_hp - monster_damage
                    
        elif equation_solved == False:
            monster_damage = monster.critical_hit()
            time.sleep(1)
            print(f"\nYou miss, the {monster.name} attacks with it's {monster.crit} for {monster_damage} damage.")
            player_hp = player_hp - monster_damage
            
    while monster_hp < 1:
        time.sleep(1)
        print(f"\nYou have slain the {monster.name}!")
        monster_dead = True
        monster_loot = monster.monster_gold()
        print(f"\nYou have found {monster_loot} gold coins!")
        print(f"\nYou have {player.gold} gold coins!")
        clr_screen()
        return monster_dead
    while player_hp < 1:
        print("\nYou have died.\nGame Over.")
        exit()

def battler_1():
    solved = False
    operations = ['+', '-']
    ops = random.choice(operations)
    num_list = []
    a = random.randint(0, 20)
    b = random.randint(0,20)
    num_list.extend([a, b])
    num_list.sort(reverse = True)
    user_solution = int(input(f"\nSolve for: {num_list[0]} {ops} {num_list[1]} = "))
    solution = eval(str(num_list[0]) + ops + str(num_list[1]))
    while not solved:    
        if user_solution == solution:
            print("\nCorrect!")
            solved = True
            return solved
        elif user_solution != solution:
            print(f"\nIncorrect!")
            solved = False
            return solved

def battler_2():
    solved = False
    operations = ['*', '/']
    ops = random.choice(operations)
    num_list = []
    if ops == '*':
        num_list = []
        a = random.randint(0, 20)
        b = random.randint(0, 20)
        num_list.extend([a, b])
        num_list.sort(reverse = True)
        user_solution = int(input(f"\nSolve for: {num_list[0]} {ops} {num_list[1]} = "))
        solution = eval(str(num_list[0]) + ops + str(num_list[1]))
        while not solved:
            if user_solution == solution:
                print("\nCorrect!")
                solved = True
                return solved
            elif user_solution != solution:
                print(f"\nIncorrect!")
                solved = False
                return solved
        
    else:
        num_list = []
        num1_div = [4, 6, 8, 10, 12, 14, 16, 18, 20]
        num2_div20 = [2, 4, 5, 10, 20]
        num2_div18 = [2, 6, 9, 18]
        num2_div16 = [2, 4, 8, 16]
        num2_div14 = [2, 7, 14]
        num2_div12 = [2, 3, 4, 6, 12]
        num2_div10 = [2, 5, 10]
        num2_div8 = [2, 4, 8]
        num2_div6 = [2, 3, 6]
        num2_div4 = [2, 4]
        num2_div2 = [2]
        a = random.choice(num1_div)
        if a == 20:
            b = random.choice(num2_div20)
        elif a == 18:
            b = random.choice(num2_div18)
        elif a == 16:
            b = random.choice(num2_div16)
        elif a == 14:
            b = random.choice(num2_div14)
        elif a == 12:
            b = random.choice(num2_div12)
        elif a == 10:
            b = random.choice(num2_div10)
        elif a == 8:
            b = random.choice(num2_div8)
        elif a == 6:
            b = random.choice(num2_div6)
        elif a == 4:
            b = random.choice(num2_div4)
        elif a == 2:
            b = random.choice(num2_div2)
        num_list.extend([a, b])
        user_solution = int(input(f"\nSolve for: {num_list[0]} {ops} {num_list[1]} = "))
        solution = eval(str(num_list[0]) + ops + str(num_list[1]))
        while not solved:
            if user_solution == solution:
                print("\nCorrect!")
                solved = True
                return solved
            elif user_solution != solution:                
                print(f"\nIncorrect!")
                solved = False
                return solved

def math_battle1():
    solved = False
    operations = ['+', '-']
    ops = random.choice(operations)
    num_list = []
    tries = 3
    a = random.randint(0, 20)
    b = random.randint(0,20)
    num_list.extend([a, b])
    num_list.sort(reverse = True)
    user_solution = int(input(f"\nSolve for: {num_list[0]} {ops} {num_list[1]} = "))
    solution = eval(str(num_list[0]) + ops + str(num_list[1]))
    while tries > 1:    
        if user_solution == solution:
            print("\nCorrect!")
            solved = True
            return solved
        elif user_solution != solution:
            tries = tries - 1
            print(f"\nIncorrect! You have {tries} more attempts.")
            user_solution = int(input(f"\nSolve for: {num_list[0]} {ops} {num_list[1]} = "))
    else:
        if tries <= 1 and user_solution != solution:
            tries = tries -1
            print(f"\nThe correct solution is: {num_list[0]} {ops} {num_list[1]} = {solution}")
            print("\nGame Over.")
            return None
        else:
            print("\nCorrect!")
            solved = True
            return solved

def math_battle2():
    solved = False
    operations = ['*', '/']
    ops = random.choice(operations)
    num_list = []
    tries = 3
    if ops == '*':
        num_list = []
        a = random.randint(0, 20)
        b = random.randint(0, 20)
        num_list.extend([a, b])
        num_list.sort(reverse = True)
        user_solution = int(input(f"\nSolve for: {num_list[0]} {ops} {num_list[1]} = "))
        solution = eval(str(num_list[0]) + ops + str(num_list[1]))
        while tries > 1:
            if user_solution == solution:
                print("\nCorrect!")
                solved = True
                return solved
            elif user_solution != solution:
                tries = tries - 1
                print(f"\nIncorrect! You have {tries} more attempts.")
                user_solution = int(input(f"\nSolve for: {num_list[0]} {ops} {num_list[1]} = "))
        else:
            if tries <= 1 and user_solution != solution:
                tries = tries - 1
                print(f"\nThe correct solution is: {num_list[0]} {ops} {num_list[1]} = {solution}")
                print("\nGame Over.")
                return None
            else: 
                print("\nCorrect!")
                solved = True
                return solved
    else:
        num_list = []
        num1_div = [4, 6, 8, 10, 12, 14, 16, 18, 20]
        num2_div20 = [2, 4, 5, 10, 20]
        num2_div18 = [2, 6, 9, 18]
        num2_div16 = [2, 4, 8, 16]
        num2_div14 = [2, 7, 14]
        num2_div12 = [2, 3, 4, 6, 12]
        num2_div10 = [2, 5, 10]
        num2_div8 = [2, 4, 8]
        num2_div6 = [2, 3, 6]
        num2_div4 = [2, 4]
        num2_div2 = [2]
        a = random.choice(num1_div)
        if a == 20:
            b = random.choice(num2_div20)
        elif a == 18:
            b = random.choice(num2_div18)
        elif a == 16:
            b = random.choice(num2_div16)
        elif a == 14:
            b = random.choice(num2_div14)
        elif a == 12:
            b = random.choice(num2_div12)
        elif a == 10:
            b = random.choice(num2_div10)
        elif a == 8:
            b = random.choice(num2_div8)
        elif a == 6:
            b = random.choice(num2_div6)
        elif a == 4:
            b = random.choice(num2_div4)
        elif a == 2:
            b = random.choice(num2_div2)
        num_list.extend([a, b])
        user_solution = int(input(f"\nSolve for: {num_list[0]} {ops} {num_list[1]} = "))
        solution = eval(str(num_list[0]) + ops + str(num_list[1]))
        while tries > 1:
            if user_solution == solution:
                print("\nCorrect!")
                solved = True
                return solved
            elif user_solution != solution:
                tries = tries - 1
                print(f"\nIncorrect! You have {tries} more attempts.")
                user_solution = int(input(f"\nSolve for: {num_list[0]} {ops} {num_list[1]} = "))
        else:
            if tries <= 1 and user_solution != solution:
                tries = tries - 1
                print(f"\nThe correct solution is: {num_list[0]} {ops} {num_list[1]} = {solution}")
                print("\nGame Over.")
                return None
            else:
                print("\nCorrect!")
                solved = True
                return solved

def r_desert_encounter():
    global desert_monster_list
    global monster
    r_encounter = random.randint(1, 100)
    if r_encounter in range(65, 100):
        monster_choice = random.choice(desert_monster_list)
        monster = monster_choice()
        print("\nRandom Encounter!")
        time.sleep(2)
        print(f"\nA {monster.name} appears!")
        battler()
    else:
        return

def r_encounter():
    global monster_list
    global monster
    r_encounter = random.randint(1, 100)
    if r_encounter in range(65, 100):
        monster_choice = random.choice(monster_list)
        monster = monster_choice()
        print("\nRandom Encounter!")
        time.sleep(2)
        print(f"\nA {monster.name} appears!")
        battler()
    else:
        return

def title_screen():
    title = "**        ADVENTURE IN ADONAIS       **"             
    print('*' * len(title))
    print('*' * len(title))
    print("**                                   **") 
    print(title)
    print("**          by Ryan Starosta         **")
    print("**                                   **")  
    print('*' * len(title))
    print('*' * len(title))

def main_menu():
    menu_list = ["1. Skill Level 1 (Addition & Subtraction)", "2. Skill Level 2 (Multiplication & Division)", "3. Exit"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])

def get_user_input():
    user_input = int(input("Enter your choice:\n> "))
    while user_input > 3 or user_input <= 0:
        print("Invalid choice.")
        user_input = int(input("Please choose again:\n\t> "))
    else:
        return user_input 

def make_choice():
    print("\nWhat do you do?")
    user_input = str.lower(input("\n> "))
    os.system("cls")
    return user_input

def time_delay():
    print("\n.")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)

def clr_screen():
    input("\nPress ENTER to continue...")
    os.system("cls")

def introduction():
    print("\nIt's a lazy Saturday afternoon.")
    time.sleep(2)
    print("\nYou are in your bedroom reading a book.")
    time.sleep(2)
    print("\nYou yawn and your eyes begin to close.")
    time.sleep(2)
    print("\nYou feel like you are falling.")
    time_delay()
    print("\nAs the ground comes closer you are startled awake.")
    time.sleep(2)
    print("\nYour eyes snap open and you find yourself in a clearing next to a tree.")
    time.sleep(2)
    start_room()
    
def start_room():
    global start_puzzle 
    print("\nYou take a look around the clearing, you see a path leading north and a note nailed to the tree.")
    print("\nmove 'north' or 'read' note")
    choice = make_choice()
    while not start_puzzle:
        if "read" in choice and not start_puzzle:
            print("\nYou move in and read the note nailed to the tree. It reads:")
            print("""\n\t\tWelcome to Adonais! In this world you will use math to unlock
            \tnew areas to explore, as well as when fighting the various monsters that inhabit Adonais.
            \tAny action you can take will have '' around them and be presented as a verb or direction
            \tsuch as 'north' or 'search'. 
            \n\t\tLets's try an equation!""")
            start_puzzle = math_battle_function()
            print("\nYou can now move on to the next area.")
            print("\nMove 'north' or 'read' note")
            choice = make_choice()
        elif "north" in choice and not start_puzzle:
            print("\nYou must complete this part of the tutorial first.")
            print("\nMove 'north' or 'read' note")
            choice = make_choice()
        else:
            while "north" or "read" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'north' or 'read' note")
                choice = make_choice()
                break
    while start_puzzle:
        if "north" in choice:
                print("\nYou make your way down an overgrown forest trail.")
                time_delay()
                cabin_room()
        elif "read" in choice:
            print("\nYou have already completed this part of the tutorial.")
            print("\nmove 'north' or 'read' note")
            choice = make_choice()    
        else:
            while "read" or "north" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'north' or 'read' note")
                choice = make_choice()
                break     
    
def cabin_room():
    global cabin_puzzle
    print("\nYou enter a clearing, and see a small log cabin and a trail leading to the east")
    print("\nMove 'east' or 'approach' cabin?")
    choice = make_choice()
    while not cabin_puzzle:
        if "east" in choice:
            print("\nMaybe you should check the cabin out first.")
            print("\nMove 'east' or 'approach' cabin?")
            choice = make_choice()
        elif "approach" in choice:
            print("\nYou approach the cabin, the smell of cedar fills your senses.")
            time_delay()
            print("\nThere is a sign above the door that reads: 'Pickles Place', and a hastily written note nailed to the old door.")
            print("\nYou read the note:")
            print(f"\n\tDear {player.name}, I just knew we would get you back from {player.home}!")
            print("\tI would like to help you prepare for your journey this time.")
            print("\tLet yourself into my cabin, inside there is an item that will help you on your way!")
            print("\tI won't tell you what it is, but see if you can find it!")
            print("\nmove 'back' from the cabin or 'enter' cabin?")
            choice = make_choice()
            if "back" in choice:
                print("\nYou step away from the cabin.")
                time_delay()
                cabin_room()                
            elif "enter" in choice:
                print("\nYou open the door to the cabin, its groans as it swings open with a thud. You enter the Cabin.")
                time_delay()
                cabin_kitchen()                
            else:
                while "back" or "enter" not in choice:
                    print("\nI do not understand that.")
                    print("\nmove 'back' from the cabin, or 'enter' cabin?")
                    choice = make_choice()
                    break
        else:
            while "east" or "approach" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'east' or 'approach' cabin?")
                choice = make_choice()
                break
    while cabin_puzzle:
        if "east" in choice:
            print("\nYou make your way down the path to the east.")
            time_delay()
            forest_grove()
        elif "cabin" in choice:
            print("\nYou could enter the cabin again, but you would be wasting your time.")
            cabin_room()
        else:
            while "east" or "approach" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'east' or 'approach' cabin?")
                choice = make_choice()
                break
    
def cabin_kitchen():
    global cabin_basket_searched
    print("\nYou are in the Kitchen, the smell of dust and mildew overwhelms you.")
    while not cabin_basket_searched:
        print("\nYou see a basket covered in dust on the counter, a hallway leading to the living room and the door leading out of the cabin.")
        print("\n'search' basket, move 'forward' or 'exit' cabin?")
        choice = make_choice()
        if "search" in choice:
            print("\nYou open the basket and find 10 gold coins.")
            player.gold = player.gold + 10
            print(f"\nYou now have {player.gold} gold coins!")
            cabin_basket_searched = True
            cabin_kitchen()
        elif "exit" in choice:
            print("\nYou exit the cabin.")
            time_delay()
            cabin_room()
        elif "forward" in choice:
            print("\nYou make your way down the hallway")
            time_delay()
            cabin_livingroom()
        else:
            while "search" or "forward" or "exit" not in choice:
                print("\nI do not understand that.")
                print("\n'search' basket, move 'forward' or 'exit' cabin?")
                choice = make_choice()
                break
    while cabin_basket_searched:
        print("\nYou see a hallway leading to the living room and the door leading to the exit.")
        print("\nmove 'forward' or 'exit' cabin?")
        choice = make_choice()
        if "forward" in choice:
            print("\nYou make your way down the hallway.")
            time_delay()
            cabin_livingroom()
        elif "exit" in choice:
            print("\nYou exit the cabin.")
            time_delay()
            cabin_room()
        else:
            while "forward" or "exit" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'forward' or 'exit' cabin?")
                choice = make_choice()
                break
        
def cabin_livingroom():
    global cabin_mantle_box_searched
    global cabin_puzzle
    print("\nYou are in the living room.  A thick layer of dust covers the furniture.")
    while not cabin_mantle_box_searched:
        print("\nYou see an ornate box on the fireplace mantle, and a ladder leading to a loft.")
        print("\n'search' ornate box, 'climb' ladder, or move 'back' to kitchen?")
        choice = make_choice()
        if "back" in choice:
            print("\nYou make your way back to the kitchen.")
            time_delay()
            cabin_kitchen()
        elif "search" in choice:
            print("\nYou open the ornate box. ")
            time_delay()
            print("\nIt contains an old iron Dagger.")
            print("\nYou take the dagger and clip it to your belt.")
            print("\nThis must be the item Pickle told you to find.")
            print("\nYou can now move on to the next area, or keep searching the cabin, you never know what you might find!")
            player.weapons.remove("Fist")
            player.weapons.append("Dagger")
            cabin_mantle_box_searched = True
            cabin_puzzle = True
            cabin_livingroom()
        elif "climb" in choice:
            print("You climb the ladder to the loft, it creaks under your weight.")
            time_delay()
            cabin_loft()
        else:
            while "back" or "search" or "climb" not in choice:
                print("\nI do not understand that.")
                print("\n'search' ornate box, 'climb' ladder, or move 'back' to kitchen?")
                choice = make_choice()
                break
    while cabin_mantle_box_searched:
        print("\n'climb' ladder or move 'back' to kitchen?")
        choice = make_choice()
        if "climb" in choice:
            print("\nYou climb the ladder, it creaks under your weight.")
            time_delay()
            cabin_loft()
        elif "back" in choice:
            print("\nYou make your way back to the kitchen.")
            time_delay()
            cabin_kitchen()
        else:
            while "climb" or "back" not in choice:
                print("\nI do not understand that.")
                print("\n'climb' ladder or move 'back' to kitchen?")
                choice = make_choice()
                break

def cabin_loft():
    global cabin_locked_chest_searched
    global monster
    print("\nYou are in the loft, it smells of musty clothes.")
    while not cabin_locked_chest_searched:
        box_unlocked = False
        print("\nAt the end of the loft you see a small lock box.")
        print("\n'open' box or 'back' to living room?")
        choice = make_choice()
        if "open" in choice:
            monster = Small_spider()
            print(f"\nA {monster.name} drops from the ceiling!")
            battler()
            print("\nThe box has a magic lock on it, solve to open:")
            box_unlocked = math_battle_function()
            if box_unlocked == True:
                print("\nYou unlock the box, inside you find 15 gold coins!")
                player.gold = player.gold + 15
                cabin_locked_chest_searched = True
                cabin_loft()
            else:
                print("\nThe lock shatters.")
                cabin_locked_chest_searched == True
                cabin_loft()
        elif "back" in choice:
            print("\nYou back down the ladder.")
            time_delay()
            cabin_livingroom()
        else:
            while "open" or "back" not in choice:
                print("\nI do not understand that.")
                print("\n'open' or 'back' down ladder?")
                choice = make_choice()
                break
    while cabin_locked_chest_searched:
        print("\nmove 'back' to living room?")
        choice = make_choice()
        if 'back' in choice:
            print("\nYou climb back down the ladder.")
            time_delay()
            cabin_livingroom()
        else:
            while 'back' not in choice:
                print("\nI do not understand that.")
                print("\nmove 'back' to living room?")
                choice = make_choice()
                break

def forest_grove():
    global forest_grove_puzzle
    global monster
    print("\nThere is the remnants of a camp. There is a sign which reads:")
    print("\n\tNorth: Wallowdale Crossroads\n\tEast: Everton Ruins")
    print("\n'search' camp, move 'north', move 'east' or move 'west'(Back to Pickles Place)?")
    choice = make_choice()
    while not forest_grove_puzzle:
        if "west" in choice:
            print("\nYou make your way west back to the cabin.")
            time_delay()
            cabin_room()
            break
        elif "search" in choice:
            monster = Giant_rat()
            print("\nYou begin to search the remnants of the camp.")
            print(f"\nThe noise of your search attracts a {monster.name}!")
            print("\nYou draw your sword: FIGHT!")
            forest_grove_puzzle = battler()
            print("\nIn the rubble of the camp you find a note, and 3 magic acorns!\nThe note reads:\n")
            print("\n\tThis concludes the tutorial. You will now be able to")
            print("\tmove freely throughout the game world, you will try and")
            print("\tfind your way home, you will need to find various items")
            print("\tto move on. These acorns will explode when thrown, use them wisely!")
            print("\tIt's dangerous out there, be careful.")
            player.weapons.append("Acorn")
            player.acorns = 3
            forest_grove()
        elif "north" in choice:
            print("\nYou cannot move there yet.")
            print("\n'search' camp?")
            choice = make_choice()
        elif "east" in choice:
            print("\nYou cannot move there yet.")
            print("\n'search' camp?")
            choice = make_choice()
        else:
            while "north" or "east" or "west" or "search" not in choice:
                print("\nI do not understand that.")
                print("\n'search' camp, move 'north', move 'east' or move 'west'?")
                choice = make_choice()
                break
    while forest_grove_puzzle:
        if "west" in choice:
            print("\nYou make your way west back to the cabin.")
            time_delay()
            cabin_room()
            break
        elif "north" in choice:
            print("\nYou make your way north.")
            time_delay()
            print("8 minutes later...")
            crossroad()
        elif "east" in choice:
            print("\nYou make your way east.")
            time_delay()
            print("25 minutes later you come to the edge of the forest.")
            pickles_clearing()
        elif "search" in choice:
            print("\nYou rummage through the debris of the camp.")
            print("\nYou find nothing.")
            print("\n'search' camp, move 'north', move 'east' or move 'west'?")
            choice = make_choice()
        else:
            while "search" or "north" or "east" or "west" not in choice:
                print("\nI do not understand that.")
                print("\n'search' camp, move 'north', move 'east' or move 'west'?")
                choice = make_choice()
                break

def crossroad():
    r_encounter()
    cross_road_loop = True
    while cross_road_loop:
        print("\nYou come to a crossroad.")
        print("\nThere is a sign which reads:")
        print("\n\tNorth: Mount Holmfirth")
        print("\tSouth: Everton Ruins")
        print("\tWest: Duncaster Beach")
        print("\tEast: Black Hollow Camp")
        print("\nmove 'north', 'south', 'east' or 'west'")
        choice = make_choice()
        if "north" in choice:
            print("\nYou make your way north.")
            time_delay()
            print("\nThe road opens up at the base of Mount Holmfirth.")
            mount_holmfirth()
        elif "south" in choice:
            print("\nYou make your way south")
            time_delay()
            forest_grove()
        elif "west" in choice:
            print("\nYou make your way west.")
            time_delay()
            print("\nThe canopy of trees closes around you, you are filled with a sense of foreboding.")
            spider_cavern()
        elif "east" in choice:
            print("\nYou make your way east.")
            time_delay()
            print("\nIn the distance you can see a bustling camp")
            black_hollow_camp()
        else:
            while "north" or "south" or "east" or "west" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'north', 'south', 'east', 'west'")
                choice = make_choice()
                break

def pickles_clearing():
    global pickles_clearing_puzzle
    r_encounter()
    while not pickles_clearing_puzzle:
        print("\nYou are on a hill overlooking a plain, the wind blows through the grass. You can hear the sound of birds chirping in the distance")
        print("\nA road leads east and a road leads west back to the forest.")
        print("\nYou can see a what appears to be a small person covered in purple fur crossing the plain. It's Pickle!")
        print("\n'approach' Pickle, move 'east' or move 'west'?")
        choice = make_choice()
        if "approach" in choice:
            print("\nYou cross the plain and approach Pickle.")
            time_delay()
            print(f"\n\"{player.name}, I just knew you would make it back to Adonais!\" says Pickle ")
            print("\n\"It's great to see you Pickle!\" you reply.")
            print("\n\"I see you have found my old Sword! If you want to make it home, you will need to get to Duncaster Beach\nIn order to do that you will have to get through the spider cave! You will need a torch to\n get in there. I think I seen one on Mount Dunforth. It's north of the crossroads.\"")
            print("\nYou thank Pickle.")
            print("\n\"Oh, once more thing...If you want to get up Mount Holmfirth you will need something to protect yourself from\nthe cold up there, there is a ruin south east of here, you might find what you are looking for\nthere.\"adds Pickle.")
            print("\nYou thank Pickle and he throws a glowing stone on the ground and disappears in a puff of smoke.")
            pickles_clearing_puzzle = True
            pickles_clearing()
        elif "east" in choice:
            print("You cross the plain and take the road east.")
            time_delay()
            everton_ruins_fork()
        elif "west" in choice:
            print("\nYou make your way back into the forest to the west.")
            time_delay
            forest_grove()
        else:
            while "approach" or "east" or "west" not in choice:
                print("\nI do not understand that.")
                print("\n'aproach', move 'east' or move 'west'?")
                choice = make_choice()
                break
    while pickles_clearing_puzzle:
        print("\nYou are on a hill overlooking a plain, the wind blows through the grass. You can hear the sound of birds chirping in the distance")
        print("\nA road leads east and a road leads west back to the forest.")
        print("\nmove 'east' or move 'west'?")
        choice = make_choice()
        if "east" in choice:
            print("\nYou cross the plain and take the road east.")
            time_delay()
            everton_ruins_fork()
        elif "west" in choice:
            print("\nYou make your way back into the forest to the west.")
            time_delay()
            forest_grove()
        else:
            while "east" or "west" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'east' or move 'west'?")
                choice = make_choice()
                break
    
def mount_holmfirth():
    print("Place holder for Mount Holmfirth")
    crossroad()

def spider_cavern():
    print("Place holder for spider cavern")
    crossroad()

def black_hollow_camp():
    global black_hollow_camp_battle_won
    global monster
    while not black_hollow_camp_battle_won:
        print("\nAs you approach the camp, can see a plume of smoke and hear the sound of battle.")
        time.sleep(1)
        print("\nBlack Hollow Camp is under attack by Hobgoblins!")
        time.sleep(1)
        print("\nYou rush in to lend a hand!")
        time.sleep(1)
        print("\nFight!")
        monster = Hobgoblin_bandit()
        battler()
        print("\nYou rush over to the next bandit, ready to fight!")
        monster = Hobgoblin_bandit()
        battler()
        print("\nYou finish off this bandit and see a much larger goblin about to strike down a halfling. You move in to fight it.")
        monster = Hobgoblin_boss()
        battler()
        print("\nWhen you strike down the Captain, the remaining bandits flee the camp.")
        time.sleep(1)
        print("\nThe halfling you saved stands up.")
        time.sleep(1)
        print("\nShe has bright blue hair, and pointy ears, covered in gold earings. She has tattoo's on her face.")
        time.sleep(1)
        print(f"""\n\"Thank you for saving me, those bandits won't give up. I'm Sapphire by the way, the quartermaster of Black Hollow Camp.
        
You give her your name, and tell her you are trying to find your way home.
        
\"Well {player.name} It's nice to meet you, if you need to buy any supplies, please come talk to me again, also, talk to some of the
other guards stationed here, they might be able to offer you some advice on how to get home.""")
        black_hollow_camp_battle_won = True
        clr_screen()
        black_hollow_camp()
    while black_hollow_camp:
        print("\nYou approach the bustling camp.")
        print("\nTalk to 'Sapphire', talk to 'Crowly', talk to 'Bruenor' or 'leave' camp?")
        choice = make_choice()
        if "sapphire" in choice:
            print("\nYou approach Sapphires shop front and greet her.")
            time_delay()
            black_hollow_camp_sapphire_shop()
        elif "crowly" in choice:
            print("\nYou approach battle hardened Wood Elf.")
            time_delay()
            black_hollow_camp_crowly()
        elif "bruenor" in choice:
            print("\nYou approach A dwarf, wearing stained and dented plate armor.")
            time_delay()
            black_hollow_camp_bruenor()
        elif "leave" in choice:
            print("\nYou leave the camp and head towards Wallowdale Crossroads.")
            time_delay()
            crossroad()
        else:
            while "sapphire" or "crowly" or "bruenor" or "leave" not in choice:
                print("\nI do not understand that.")
                print("\nTalk to 'Sapphire', talk to 'Crowly', talk to 'Bruenor' or 'leave' camp?")
                choice = make_choice()
                break

def black_hollow_camp_sapphire_shop():
    global st_inventory
    print(f"\nWelcome to my shop {player.name}.\n")
    st_inventory.print_items()
    print(f"\nYou have {player.gold} gold.")
    item_choice = str.lower(input("\nWhat can I get for you?(Type 'leave', 'back', or 'exit' anytime to exit)\n>"))
    if "broad sword" in item_choice: 
        if player.gold >= 100:
            print("\n\"The Broad Sword, nice choice!\"")
            player.gold = player.gold - 100
            player.weapons.remove("Dagger")
            player.weapons.insert(0, "Broad Sword")
            st_inventory.items.pop("Broad Sword")
            clr_screen()
            black_hollow_camp_sapphire_shop()
        else:
            print(f"\n\"Sorry {player.name}, you don't have enough gold.\"")
            print("\n\"Can I get you anything else?\"")
            item_choice = str.lower(input("\n>"))
    elif "acorns" or "acorn" or "acorn[x3]" in item_choice: 
        if player.gold >= 150:
            print("\n\"I love Magic Acorns.\"")
            player.acorns = player.acorns + 3
            print(f"\nYou now have {player.acorns} magic Acorns.")
            player.gold = player.gold - 150
            print("\n\"Can I get you anything else?\"")
            item_choice = str.lower(input("\n>"))
            return item_choice
        else:
            print(f"\n\"Sorry {player.name}, you don't have enough gold.\"")
            print("\n\"Can I get you anything else?\"")
            item_choice = str.lower(input("\n>"))
            return item_choice
    elif "wand charges" or "wand" or "wand charges[x3]" in item_choice:
        if player.gold >= 75:
            print(f"\nYou hand Sapphire your wand, she drops it in a vat of swirling multi-colored liquid.")
            time_delay()
            print(f"\"Here you go {player.name}, 3 more charges for your wand.\"")
            player.gold = player.gold - 75
            player.wand_charges = player.wand_charges + 3
            print(f"\nYour Wand now has {player.wand_charges} charges.")
            print("\n\"Can I get you anything else?\"")
            item_choice = str.lower(input("\n>"))
            return item_choice
        else:
            print(f"\n\"Sorry {player.name}, you don't have enough gold.\"")
            print("\n\"Can I get you anything else?\"")
            item_choice = str.lower(input("\n>"))
            return item_choice
    elif "chain" or "chain mail" or "armor" in item_choice:
        if player.gold >= 250:
            print("\n\"A fine choice, this will keep you protected.\"")
            player.gold = player.gold - 250
            player.armor.append("chain mail")
            st_inventory.items.pop("chain mail")
            player.player_hit_points()
            print(f"\nYou now have {player.hit_points} HP.")
            print("\n\"Can I get you anything else?\"")
            item_choice = str.lower(input("\n>"))
            return item_choice
        else:
            print("\n\"Can I get you anything else?\"")
            item_choice = str.lower(input("\n>"))
            return item_choice
    elif "leave" in item_choice or "back" in item_choice or "exit" in item_choice or "nothing" in item_choice:
        print(f"\nThanks for coming {player.name}, come back if you need anything else!")
        clr_screen()
        black_hollow_camp()
    else:
        print("\nI do not understand that.")
        item_choice = str.lower(input("\nWhat can I get for you?\n>"))
        return item_choice

def black_hollow_camp_crowly():
    global crowly_met
    while not crowly_met:
        print("\nYou approach Crowly and introduce yourself.")
        time.sleep(1)
        print(f"\n\"Well met then {player.name}, not many humans in Adonais!")
        time.sleep(1)
        if "travelling cloak" in player.armor:
            print("""\n\"I see you have a travelling cloak, if you're looking to get home, you will need to head up Mount Holmfirth.
There you will need to find the torch, you'll need it to get through the cavern west of here. Make sure you are well prepared
because the monsters there are quite a bit stronger than the ones around here.\"""")
            time.sleep(3)
            print("\nYou thank Crowly for the advice and return to the main camp.")
            crowly_met = True
            clr_screen()
            black_hollow_camp()
        elif "travelling cloak" not in player.armor:
            print("""\n\"I heard from Sapphire that you were looking to get home, you need a to head up Mount Holmfirth, in order to do that
you will need something to keep you warm. I heard you might be able to find something over at Everton Ruins, it's to the south east.\"""")
            time.sleep(3)
            print("\nYou thank Crowly for the advice and return to the main camp.")
            crowly_met = True
            clr_screen()
            black_hollow_camp()
    while crowly_met:
        print(f"\nGood to see you again {player.name}, how fare thee?")
        time.sleep(1)
        if "travelling cloak" in player.armor:
            print("""\n\"I see you have a travelling cloak, if you're looking to get home, you will need to head up Mount Holmfirth.
There you will need to find the torch, you'll need it to get through the cavern west of here. Make sure you are well prepared
because the monsters there are quite a bit stronger than the ones around here.\"""")
            time.sleep(3)
            print("\nYou thank Crowly for the advice and return to the main camp.")
            clr_screen()
            black_hollow_camp()
        elif "travelling cloak" not in player.armor:
            print("""\n\"I heard from Sapphire that you were looking to get home, you need a to head up Mount Holmfirth, in order to do that
you will need something to keep you warm. I heard you might be able to find something over at Everton Ruins, it's to the south east.\"""")
            time.sleep(2)
            print("\nYou thank Crowly for the advice and return to the main camp.")
            clr_screen()
            black_hollow_camp()
   
def black_hollow_camp_bruenor():
    global bruenor_met
    while not bruenor_met:
        if "torch" not in player.items:
            print("\nYou approach the Dwarf in battered plate armor and introduce yourself.")
            time.sleep(1)
            print(f"\n\"Well then {player.name}, It's good ta meet ya!\"")
            time.sleep(1)
            print("\nYou tell Bruenor you are trying to make your way home.")
            time.sleep(1)
            print("\nAfter some thought he responds.")
            time.sleep(1)
            print("""\n\"Well then let me tell ye. If yet be wanting to get home, ye need to head through the spider cavern. I order ta do that
        ye be needing a torch ta clear tha webs! Climb Mouth Holmfirth to find that!""")
            time.sleep(2)
            print("\nYou thank Bruenor and return to the main camp")
            bruenor_met = True
            clr_screen()
            black_hollow_camp()
        elif "torch" in player.items:
            print("\nYou approach the Dwarf in battered plate armor and introduce yourself.")
            time.sleep(1)
            print(f"\n\"Well then {player.name}, It's good ta meet ya!\"")
            time.sleep(1)
            print("\nYou tell Bruenor you are trying to make your way home.")
            time.sleep(1)
            print("\nHe glances at the torch belted to you waist and says.")
            time.sleep(1)
            print("\n\"Seems yer half way there, head to the spider cave west of here, yer way home is through there!")
            time.sleep(1)
            print("\nYou thank Bruenor and return to the main camp")
            bruenor_met = True
            clr_screen()
            black_hollow_camp()
    while bruenor_met:
        if "torch" not in player.items:
            print("\nYou greet Bruenor and ask him again how to get home.")
            time.sleep(1)
            print(f"\n\"Good to see ye again {player.name} seems ye haven't found that Torch yet! Head up Mouth Holfirth ta find it!")
            time.sleep(1)
            print("\nYou thank Bruenor and return to the main camp.")
            time.sleep(1)
            clr_screen()
            black_hollow_camp()
        elif "torch" in player.items:
            print("\nYou greet Bruenor and ask him again how to get home.")
            time.sleep(1)
            print(f"\n\"Well met {player.name}, seems ye found that torch! Good on ye. Best be headed west to that spider cave if ye want to get home!\"")
            time.sleep(1)
            print("\nYou thank Bruenor and return to the main camp.")
            time.sleep(1)
            clr_screen()
            black_hollow_camp()


                    

def everton_ruins_fork():
    everton_ruins_fork_loop = True
    r_encounter()
    print("\nThe road comes to an end, the air is hot and arid. A sign reads:")
    print("\n\tNorth: Cappadocia Desert")
    print("\tSouth: Everton Ruins")
    print("\tWest: Wallowdale Crossroads")
    print("\nmove 'north', move 'south' or move 'west'?")
    choice = make_choice()
    while everton_ruins_fork_loop:
        if "north" in choice:
            print("\nYou make your way north, the air grows hot.")
            time_delay()
            cappadocia_desert_entrance()
        elif "south" in choice:
            print("\nYou make your way south, you can barely see the ruin of a castle in the distance.")
            time_delay()
            everton_ruins()
        elif "west" in choice:
            print("\nYou make your way west towards the plains.")
            time_delay()
            pickles_clearing()
        else:
            while "north" or "west" or "south" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'north', move 'south' or move 'west'?")
                choice = make_choice()
                break

def everton_ruins():
    everton_ruins_courtyard_loop = True
    print("\nYou are in the courtyard of a derelict castle. You sense danger near.")
    print("\nTo the north you see a door leading to the barracks, to the south a door to the kitchen, and to the east the great hall.")
    print("\nmove 'north', move 'south', move 'east' or 'leave' Everton Ruins?")
    choice = make_choice()
    while everton_ruins_courtyard_loop:
        if "north" in choice:
            print("\nYou climb through the rubble of an old door into the barracks.")
            time_delay()
            everton_ruins_barracks()
        elif "south" in choice:
            print("\nYou cross the courtyard into the kitchen.")
            time_delay()
            everton_ruins_kitchen()
        elif "east" in choice:
            print("\nYou climb the whithered stair up to the great hall.")
            time_delay()
            everton_ruins_great_hall()
        elif "leave" in choice:
            print("\nYou head west away from the ruin.")
            time_delay()
            everton_ruins_fork()
        else:
            while "north" or "south" or "east" or "leave" not in choice:
                print("\nI do not unsertand that.")
                print("\nmove 'north', move 'south', move 'east' or 'leave' ruin?")
                choice = make_choice()
                break

def everton_ruins_barracks():
    global everton_ruins_barracks_warg_dead
    global monster
    print("\nYou are in the barracks, there is debris scattered across the room, there is blood in one corner.")
    print("\n'search' room or 'leave' room?")
    choice = make_choice()
    while not everton_ruins_barracks_warg_dead:
        if "search" in choice:
            print("\nYou search the room, it's been pillaged before.")
            time_delay()
            print("\nYou move in to investigate the blood on the floor, it's fresh.")
            time_delay()
            print("\nA Warg appears!")
            monster = Warg()
            everton_ruins_barracks_warg_dead = battler()
            print("\nYou find a scroll, when you unroll it words begin to appear. It reads:")
            time.sleep(1)
            print("\n\tSometimes I am a gentle breeze,")
            time.sleep(1)
            print("\tAnd other times I am a strong gust,")
            time.sleep(1)
            print("\tOn the water I blow sailing ships,")
            time.sleep(1)
            print("\tAnd in the desert I blow dust")
            time.sleep(1)
            riddle_choice = str.lower(input("\n\tWhat am I? >"))
            if "wind" in riddle_choice:
                os.system("cls")
                print("\nAs you speak the words, the writing fades away, and is replaced.")
                time.sleep(1)
                print("\n\tWhere the Wind blows the dust,")
                time.sleep(1)
                print("\tThe path to the treasure is,")
                time.sleep(1)
                print("\n\tN - E - S - E")
                time.sleep(1)
                print("\nThe scroll burns to ash in your hands.")
                print("\nMaybe You should jot N - E - S - E down, it might come in handy.")
                clr_screen()
                everton_ruins_barracks()
            else:
                if "wind" not in riddle_choice:
                    print("\nThe Scroll burns you ash in your hands.")
                    clr_screen()
                    everton_ruins_barracks()
        elif "leave" in choice:
            print("You make your way back to the courtyard.")
            time_delay()
            everton_ruins()
        else:
            while "search" or "leave" not in choice:
                print("\nI do not understand that.")
                print("\n'search' or 'leave'?")
                choice = make_choice()
                break
    while everton_ruins_barracks_warg_dead:
        if "search" in choice:
            print("\nYou have already searched here, there is nothing left")
            everton_ruins_barracks()
        elif "leave" in choice:
            print("\nYou make your way back to the courtyard.")
            time_delay()
            everton_ruins()
        else:
            while "search" or "leave" not in choice:
                print("\nI do not understand that.")
                print("\n'search' or 'leave'?")
                choice = make_choice()
                break

def everton_ruins_kitchen():
    global everton_ruins_kitchen_goblin_dead
    global monster
    print("\nYou enter the what used to be a kitchen, there is debris everywhere.")
    print("\n'search' room or 'leave' room?")
    choice = make_choice()
    while not everton_ruins_kitchen_goblin_dead:
        if "search" in choice:
            time_delay()
            print("\nYou search the room and find 5 gold coins in an old earthen jar!")
            player.gold = player.gold + 5
            print(f"\nYou have {player.gold} gold coins!")
            print("The sound of your searching attracts the attention of a Goblin!")
            monster = Goblin()
            everton_ruins_kitchen_goblin_dead = battler()            
            everton_ruins_kitchen()
        elif "leave" in choice:
            print("\nYou make your way back to the courtyard.")
            time_delay()
            everton_ruins()
        else:
            while "search" or "leave" not in choice:
                print("\nI do not understand that.")
                print("\n'search' room or 'leave' room?")
                choice = make_choice()
                break
    while everton_ruins_kitchen_goblin_dead:
        if "search" in choice:
            print("\nYou search the room.")
            time_delay()
            print("\nThere is nothing left here.")
            everton_ruins_kitchen()
        elif "leave" in choice:
            print("\nYou make your way back to the courtyard.")
            time_delay()
            everton_ruins()
        else:
            while "search" or "leave" not in choice:
                print("\nI do not understand that.")
                print("\n'search' room or 'leave' room?")
                choice = make_choice()
                break

def everton_ruins_great_hall():
    global everton_ruins_lords_chamber_searched
    global everton_ruins_ogre_dead
    global monster
    print("\nYou see the remains of a throne room, and to the left a stair case leading to the upper keep.")
    while not everton_ruins_lords_chamber_searched and not everton_ruins_ogre_dead:
        print("\n'search' Great Hall, 'climb' stairs, or 'leave' room?")
        choice = make_choice()
        if "search" in choice:
            print("\nYou search the great hall.")
            time_delay()
            print("\nIt is empty.")
            everton_ruins_great_hall()
        elif "climb" in choice:
            print("\nYou climb the staircase to the upper keep.")
            time_delay()
            everton_ruins_upper_hallway()
        elif "leave" in choice:
            print("\nYou return to the courtyard.")
            time_delay()
            everton_ruins()
        else:
            while "search" or "climb" or "leave" not in choice:
                print("\nI do not understand that.")
                print("\n'search' great hall, 'climb' stairs, or 'leave' room.")
                choice = make_choice()
                break

    while everton_ruins_lords_chamber_searched and not everton_ruins_ogre_dead:
        print("\nA mountain Ogre is in the great hall!")
        monster = Mountain_Ogre()
        everton_ruins_ogre_dead = battler()
        everton_ruins_great_hall()
    while everton_ruins_lords_chamber_searched and everton_ruins_ogre_dead:
        print("\n'search' Great Hall, 'climb' stairs, or 'leave' room?")
        choice = make_choice()
        if "search" in choice:
            time_delay()
            print("\nYou find nothing.")
            everton_ruins_great_hall()
        elif "leave" in choice:
            print("You return to the courtyard.")
            time_delay()
            everton_ruins()
        elif "climb" in choice:
            print("\nYou climb the staircase to the upper keep.")
            time_delay()
            everton_ruins_upper_hallway()
        else:
            while "search" or "climb" or "leave" not in choice:
                print("\nI do not understand that.")
                print("\n'search' great hall, 'climb' stairs, or 'leave' room?")
                choice = make_choice()
                break

def everton_ruins_upper_hallway():
    everton_ruins_upper_hallway_loop = True
    while everton_ruins_upper_hallway_loop:
        print("\nYou are in a hall way in the upper keep, you see a door to the north and another door to the south.")
        print("\nmove 'north' move 'south', or 'leave' back to great hall?")
        choice = make_choice()
        if "north" in choice:
            print("\nYou enter the North Chamber.")
            time_delay()
            everton_ruins_bed_chamber()
        elif "south" in choice:
            print("\nYou enter the South Chamber.")
            time_delay()
            everton_ruins_lords_chamber()
        elif "leave" in choice:
            print("\nYou return to the Great Hall.")
            time_delay()
            everton_ruins_great_hall()
        else:
            if "north" or "south" or "leave" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'north', 'south' or 'leave'?")
                choice = make_choice()
                break

def everton_ruins_bed_chamber():
    global everton_ruins_bed_chamber_searched
    global everton_ruins_footlocker_key
    while not everton_ruins_bed_chamber_searched:
        print("\nYou are in the remains of the servants quarters.")
        print("\n'search' room, or 'leave' room?")
        choice = make_choice()
        if "search" in choice:
            print("\nYou search the room.")
            time_delay()
            print("\nUnder a pillow you find 5 gold coins, and a gold key!")
            player.gold = player.gold + 5
            print(f"\nYou now have {player.gold} gold coins!")
            everton_ruins_footlocker_key = True
            everton_ruins_bed_chamber_searched = True
            everton_ruins_bed_chamber()
        elif "leave" in choice:
            print("\nYou leave the room.")
            time_delay()
            everton_ruins_upper_hallway()
        else:
            while "search" or "leave" not in choice:
                print("\nI do not understand that.")
                print("\n'search' room, or 'leave' room?")
                choice = make_choice()
                break
    while everton_ruins_bed_chamber_searched:
        print("\nYou are in the remains of the servants quarters.")
        print("\n'search' room, or 'leave' room?")
        choice = make_choice()
        if "search" in choice:
            print("\nYou search the room.")
            time_delay()
            print("\nYou find nothing.")
            everton_ruins_bed_chamber()
        elif "leave" in choice:
            print("\nYou leave the room.")
            time_delay()
            everton_ruins_upper_hallway()
        else:
            while "search" or "leave" not in choice:
                print("\nI do not understand that.")
                print("\n'search' room, or 'leave' room?")
                choice = make_choice()
                break

def everton_ruins_lords_chamber():
    global everton_ruins_lords_chamber_searched
    global everton_ruins_footlocker_key
    print("\nYou are in an elegant room, lavishly decorated, this must be the Lords Chamber.")
    print("\nYou see a footlocker at the foot of the bed.")
    print("\n'search' footlocker, or 'leave' room?")
    choice = make_choice()
    while not everton_ruins_lords_chamber_searched and not everton_ruins_footlocker_key:
        if "search" in choice:
            print("\nYou attempt to open the footlocker.")
            time_delay()
            print("\nIt's locked, you need to find the key!")
            everton_ruins_lords_chamber()
        elif "leave" in choice:
            print("\nYou leave the room.")
            time_delay()
            everton_ruins_upper_hallway()
        else:
            while "leave" or "search" not in choice:
                print("\nI do not understand that.")
                print("\n'search' room, or 'leave' room?")
                choice = make_choice()
                break 
    while not everton_ruins_lords_chamber_searched and everton_ruins_footlocker_key:
        if "search" in choice:
            print("\nYou try the gold key you found.")
            time_delay()
            print("\nYou hear a loud click, the footlocker is unlocked.")
            print("\nInside you find an Enchanted Travelers Cloak, you put it on.")
            
            player.armor.append("travelling cloak")
            print("\nThe enchantment on the cloak envelopes you, you feel stronger.")
            player.player_armor_bonus_calc()
            print(f"\nYou now have {player.player_hit_points()} HP, and have protection from the elements.")
            everton_ruins_lords_chamber_searched = True
            everton_ruins_lords_chamber()
        elif "leave" in choice:
            print("\nYou leave the room.")
            time_delay()
            everton_ruins_upper_hallway()
        else:
            if "leave" or "search" not in choice:
                print("\nI do not understand that.")
                print("\n'search' room, or 'leave' room?")
                choice = make_choice()
                break
    while everton_ruins_lords_chamber_searched:
        if "search" in choice:
            print("\nThe footlocker is empty.")
            time_delay()
            everton_ruins_lords_chamber()
        elif "leave" in choice:
            print("\nYou leave the room.")
            time_delay()
            everton_ruins_upper_hallway()
        else:
            while "search" or "leave" not in choice:
                print("\nI do not understand that.")
                print("\n'search' room, or 'leave' room?")
                choice = make_choice()
                break
            
def cappadocia_desert_entrance():
    print("\nThe land withers away into a searing desert. The wind blows sand into your eyes, and the heat of the sun causes you to sweat.")
    while "travelling cloak" not in player.armor:
        print("\nYou will require protection from the elements to go any further.")
        print("\n'leave' desert and return to the fork in the road?")
        choice = make_choice()
        if "leave" in choice:
            print("\nYou walk south to the fork in the road.")
            time_delay()
            everton_ruins_fork()
        else:
            while "leave" not in choice:
                print("\nI do not understand that.")
                print("\n'leave' desert?")
                choice = make_choice()
                break
    while "travelling cloak" in player.armor:
        print("\nYou can feel the enchantment on your cloak cools you down. You can proceed into the desert.")        
        print("\nmove 'north', move 'east', move 'west' or 'leave' desert?")
        choice = make_choice()
        if "north" in choice:
            print("\nYou move north. The sand dunes surround you, the wind howls.")
            time_delay()
            cappadocia_desert_n1()
        elif "east" in choice:
            print("\nYou move east, the sand dunes surround you, the wind howls.")
            time_delay()
            cappadocia_desert_e1()
        elif "west" in choice:
            print("\nYou move west, the sand dunes surround you, the wind howls.")
            time_delay()
            cappadocia_desert_w1()
        elif "leave" in choice:
            print("\nYou walk south to the fork in the road.")
            time_delay()
            everton_ruins_fork()
        else:
            while "north" or "east" or "west" or "leave" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'north', 'east', 'west' or 'leave'?")
                choice = make_choice()
                break

def cappadocia_desert_w1():
    cappadocia_desert_w1_loop = True
    r_desert_encounter()
    while cappadocia_desert_w1_loop:
        print("\nThe sand in the air blocks all you can see.")
        print("\nmove 'north', move 'east', move 'south' or move 'west'?")
        choice = make_choice()
        if "north" or "west" or "south" in choice:
            print("\nYou make your way through the desert, everything seems to look the same.")
            time_delay()
            cappadocia_desert_w1()
        elif "east" in choice:
            print("\nAfter some time you manage to find your way back to where you started.")
            time_delay()
            cappadocia_desert_entrance()
        else:
            if "north" or "east" or "south" or "west" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'north', move 'east', move 'south' or move 'west'?")
                choice = make_choice()
                break

def cappadocia_desert_e1():
    cappadocia_desert_e1_loop = True
    r_desert_encounter()
    while cappadocia_desert_e1_loop:
        print("\nThe great dunes of sand surround you, you only see desert all around you.")
        print("\nmove 'north', move 'east', move 'south' or move 'west'?")
        choice = make_choice()
        if "north" or "east" or "south" in choice:
            print("\nYou make your way through the desert, everything seems to look the same.")
            time_delay()
            cappadocia_desert_e1()
        elif "west" in choice:
            print("\nAfter some time you manage to make your way back to where you started.")
            time_delay()
            cappadocia_desert_entrance
        else:
            if "north" or "east" or "south" or "west" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'north', move 'east', move 'south' or move 'west'?")
                choice = make_choice()
                break

def cappadocia_desert_n1():
    cappadocia_desert_n1_loop = True
    r_desert_encounter()
    while cappadocia_desert_n1_loop:
        print("\nYou are in a valley of sand.")
        print("\nmove 'north', move 'east', move 'south' or move 'west'?")
        choice = make_choice()
        if "north" in choice:
            print("You proceed onward through the desert.")
            time_delay()
            cappadocia_desert_n2()
        elif "west" in choice:
            print("\nYou proceed onward through the desert, everything seems familiar.")
            time_delay()
            cappadocia_desert_w1()
        elif "south" in choice:
            print("\nYou proceed onward through the desert.")
            time_delay()
            cappadocia_desert_entrance()
        elif "east" in choice:
            print("\nYou proceed onward through the desert, everything seems familiar.")
            time_delay()
            cappadocia_desert_n_e()
        else:
            if "north" or "east" or "south" or "west" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'north', move 'south', move 'east', or move 'west'?")
                choice = make_choice()
                break

def cappadocia_desert_n2():
    cappadocia_desert_n2_loop = True
    r_desert_encounter()
    while cappadocia_desert_n2_loop:
        print("\nAn ancient obelisk, covered in heirogliphs stands before you.")
        print("\nmove 'north', move 'east', move 'west', move 'south', or 'inspect' obelisk?")
        choice = make_choice()
        if "north" in choice:
            print("\nYou proceed passed the obelisk.")
            time_delay()
            cappadocia_desert_n1()
        elif "east" in choice:
            print("\nYou proceed passed the obelisk.")
            time_delay()
            cappadocia_desert_e1()
        elif "south" in choice:
            print("You proceed passed the obelisk.")
            time_delay()
            cappadocia_desert_n1()
        elif "west" in choice:
            print("\nYou proceed passed the obelisk.")
            time_delay()
            cappadocia_desert_w1()
        elif "inspect" in choice:
            print("\nYou reach out and touch the obelisk")
            time_delay()
            print("\nEverything fades to black.")
            time_delay()
            print("\nYou open your eyes, you are back at the entrance to the desert.")
            cappadocia_desert_entrance()
        else:
            if "north" or "east" or "south" or "west" or "inspect" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'north', move 'east', move 'south', move 'west', or 'inspect' obelisk?")
                choice = make_choice()
                break

def cappadocia_desert_n_e():
    cappadocia_desert_n_e_loop = True
    r_desert_encounter()
    while cappadocia_desert_n_e_loop:
        print("\nYou are in a valley of sand.")
        print("\nmove 'north', move 'east', move 'south' or move 'west'?")
        choice = make_choice()
        if "north" in choice:
            print("You proceed onward through the desert.")
            time_delay()
            cappadocia_desert_n2()
        elif "west" in choice:
            print("\nYou proceed onward through the desert, everything seems familiar.")
            time_delay()
            cappadocia_desert_n1()
        elif "south" in choice:
            print("\nYou proceed onward through the desert.")
            time_delay()
            cappadocia_desert_n_e_s()
        elif "east" in choice:
            print("\nYou proceed onward through the desert, everything seems familiar.")
            time_delay()
            cappadocia_desert_e1()
        else:
            if "north" or "east" or "south" or "west" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'north', move 'south', move 'east', or move 'west'?")
                choice = make_choice()
                break

def cappadocia_desert_n_e_s():
    cappadocia_desert_n_e_s_loop = True
    r_desert_encounter()
    while cappadocia_desert_n_e_s_loop:
        print("\nYou are on a great sand dune, the desert stretches in every direction before you.")
        print("\nmove 'north', move 'east', move 'south' or move 'west'?")
        choice = make_choice()
        if "north" in choice:
            print("You proceed onward through the desert.")
            time_delay()
            cappadocia_desert_n_e()
        elif "west" in choice:
            print("\nYou proceed onward through the desert, everything seems familiar.")
            time_delay()
            cappadocia_desert_w1()
        elif "south" in choice:
            print("\nYou proceed onward through the desert.")
            time_delay()
            cappadocia_desert_n2()
        elif "east" in choice:
            print("\nYou proceed onward through the desert, everything seems familiar.")
            time_delay()
            cappadocia_desert_n_e_s_e()
        else:
            if "north" or "east" or "south" or "west" not in choice:
                print("\nI do not understand that.")
                print("\nmove 'north', move 'south', move 'east', or move 'west'?")
                choice = make_choice()
                break

def cappadocia_desert_n_e_s_e():
    global cappadocia_basilisk_dead
    global monster
    global st_inventory
    print("\nYou come to a depression in the desert, in the center you find the long dead corpse of a human, like you.")
    print("\n'search' corpse, move 'north', move 'east', move 'south', or move 'west'?")
    choice = make_choice()
    while not cappadocia_basilisk_dead:
        if "search" in choice:
            print("\nYou search the corpse.")
            time_delay()
            print("\nBurried in the sand beneath the corpse you find a Magic Wand!")
            player.weapons.append("Wand")
            player.wand_charges = 2
            st_inventory.add_items(Item("Wand Charge[x3]", 15, 20, 0, 75))
            print(f"\nYou will now be better able to defeat your enemies.")
            print("\nDisturbing the corpse summons a horror from the deep!")
            time_delay()
            monster = Desert_basilisk()
            cappadocia_basilisk_dead = battler()
            print("\nThe Basilisk's corpse fades away and reveals a gem, you reach out and grab it.")
            time_delay()
            print("\nEverything fades to black, you got what you came for.")
            time_delay()
            cappadocia_desert_entrance()
        elif "north" in choice:
            print("You proceed onward through the desert.")
            time_delay()
            cappadocia_desert_e1()
        elif "west" in choice:
            print("\nYou proceed onward through the desert, everything seems familiar.")
            time_delay()
            cappadocia_desert_n_e_s()
        elif "south" in choice:
            print("\nYou proceed onward through the desert.")
            time_delay()
            cappadocia_desert_n1()
        elif "east" in choice:
            print("\nYou proceed onward through the desert, everything seems familiar.")
            time_delay()
            cappadocia_desert_w1()
        else:
            if "north" or "east" or "south" or "west" or "search" not in choice:
                print("\nI do not understand that.")
                print("\n'search' corpse, move 'north', move 'south', move 'east', or move 'west'?")
                choice = make_choice()
                break
    while cappadocia_basilisk_dead:
        if "search" in choice:
            time_delay()
            print("\nNothing remains.")
            cappadocia_desert_n_e_s_e()
        elif "north" in choice:
            print("You proceed onward through the desert.")
            time_delay()
            cappadocia_desert_e1()
        elif "west" in choice:
            print("\nYou proceed onward through the desert, everything seems familiar.")
            time_delay()
            cappadocia_desert_n_e_s()
        elif "south" in choice:
            print("\nYou proceed onward through the desert.")
            time_delay()
            cappadocia_desert_n1()
        elif "east" in choice:
            print("\nYou proceed onward through the desert, everything seems familiar.")
            time_delay()
            cappadocia_desert_w1()
        else:
            if "north" or "east" or "south" or "west" or "search" not in choice:
                print("\nI do not understand that.")
                print("\n'search' corpse, move 'north', move 'south', move 'east', or move 'west'?")
                choice = make_choice()
                break
                  




    
monster_list = (Orc, Giant_rat, Wild_dog) # populate monster_list
desert_monster_list = (Desert_deathworm, Desert_mummy, Desert_sandspider, Desert_scarab, Desert_scorpian) #biome specific monster list.
title_screen()
main_menu()
option = get_user_input() 
if option == 1:
    math_battle_function = math_battle1  
    battler_function = battler_1  
elif option == 2:
    math_battle_function = math_battle2
    battler_function = battler_2
player = Player_character() # initialize Player_Character
player.weapons.append("Fist")
st_inventory = Store_Inventory() # initialize the shop
st_inventory.add_items(Item('Broad Sword', 10, 15, 0, 100))
st_inventory.add_items(Item("Acorn[x3]", 20, 30, 0, 150))
st_inventory.add_items(Item("Chain Mail", 0, 0, 10, 250))
character_creator()
introduction()




    