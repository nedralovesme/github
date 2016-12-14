"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

from characters import *

def main():
    hero = Hero()
    goblin = Goblin()
    zombie = Zombie()

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        zombie.print_status()
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. fight zombie"
        print "3. do nothing"
        print "4. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            if goblin.alive():
                # Goblin attacks hero
                goblin.attack(hero)
        elif input == "2":
            # Hero attacks zombie
            hero.attack(zombie)
            if zombie.alive():
                # Goblin attacks hero
                zombie.attack(hero)
        elif input == "3":
            pass
        elif input == "4":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input


main()
