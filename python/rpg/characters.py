class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
    def alive(self):
        return self.health>0
    def print_status(self):
        print "%s has %d health and %d power" % ((self.name).capitalize(),self.health,self.power)
    def attack(self,opponent):
        opponent.health -= self.power
        print "The %s does %d damage to the %s." % (self.name,self.power,opponent.name)
        if not opponent.alive():
            print "The %s is dead." % opponent.name

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 0
        self.power = 1

    def alive(self):
        #undead, always alive
        self.health=0
        return True
