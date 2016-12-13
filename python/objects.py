import time
import random

class Person(object):
    alive=True
    innocent=True
    onTheRun=False
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.mname = ""

    def greet(self,person):
        print "%s is saying hi to %s" % (self.longname(),person.longname())
    # def sayHi
    def kill(self,person):
        person.alive=False
        self.innocent=False
        self.onTheRun=True
        print "%s just killed %s" % (self.longname(),person.longname())

    def longname(self):
        return self.fname + " " + self.lname

    def birthdate(self,format=""):
        return self.fname + " " + self.lname

janice = Person("Janice","Smith")
# janice.greet()

bob = Person("Bob","Jones")
bob.kill(janice)

if janice.alive:
    print "Janice is alive"
else:
    print "Janice is dead"

while bob.onTheRun:
    print "%s says 'Can't catch me'" % bob.fname


people = []
people.append(bob)
people.append(janice)
print people
