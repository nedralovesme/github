"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time


class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)


class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evadePoints = 0

    def attack(self, enemy):
        # store orig power
        origPower = self.power
        # 20% chance to double the power
        if random.random() <= .2:
            # temporarily double the power
            print "%s does double damage!" % self.name
            self.power *= 2
        # do the orig attack
        super(Hero, self).attack(enemy)
        # restore original power
        self.power = origPower

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        if (self.coins >= item.cost):
            self.coins -= item.cost
            item.apply(self)
        else:
            print "Insufficient funds"

    def receive_damage(self, points):
        # try to evade
        if self.evadePoints > 0:
            # 5% points for every 2 evade points starting at 10%, max of 100%
            evadePerc = max(.1 + .05 * (self.evadePoints - 2) / 2.0, 1)
            if random.random <= evadePerc:
                print "The %s has evaded the attack!" % self.name
                return
        # if we have armor, damage that first
        if self.armor > 0:
            origArmor = self.armor
            if points >= self.armor:
                damageArmor = self.armor
                points = points - self.armor
            else:
                damageArmor = points
                points = 0
            self.armor -= damageArmor
            print "%s armor has beed reduced from %d to %d." % (origArmor, self.armor)
        if points:
            super(Hero, self).receive_damage(points)


class Medic(Hero):
    def __init__(self):
        super(Medic, self).__init__()
        self.name = 'medic'
        self.health = 4

    def receive_damage(self, points):
        super(Medic, self).receive_damage(self, points)
        if random.random() <= .2:
            # 20% chance of health regain
            self.health += 2


class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.coins = random.randint(0, 5)


class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.coins = random.randint(3, 8)

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power


class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 2
        self.coins = random.randint(5, 12)

    def receive_damage(self, points):
        # only receive damage 10% of the time
        if random.random() <= .1:
            super(Shadow, self).receive_damage(points)


class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            print "Enemy dropped %d coins" % enemy.coins
            hero.coins += enemy.coins
            return True
        else:
            print "YOU LOSE!"
            return False


class Tonic(object):
    cost = 5
    name = 'tonic'

    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)


class SuperTonic(object):
    cost = 9
    name = 'supertonic'

    def apply(self, character):
        #don't reduce to 10 if higher than 10
        character.health = max(10,character.power)
        print "%s's health increased to %d." % (character.name, character.health)


class Sword(object):
    cost = 10
    name = 'sword'

    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)


class Armor(object):
    cost = 10
    name = 'armor'

    def apply(self, hero):
        hero.armor += 2
        print "%s's armor increased to %d." % (hero.name, hero.armor)


class Evade(object):
    cost = 10
    name = 'evade'

    def apply(self, hero):
        hero.evadePoints += 2
        print "%s's evade points increased to %d." % (hero.name, hero.evadePoints)


class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, SuperTonic, Sword, Evade, Armor]

    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                if input <= len(Store.items):
                    ItemToBuy = Store.items[input - 1]
                    item = ItemToBuy()
                    hero.buy(item)
                else:
                    print "Invalid option, please select again"


hero = Hero()
enemies = [Goblin(), Wizard()]
if random.random <= .25:
    enemies.append(Shadow())

battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
