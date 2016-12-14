class Animal(object):
    def __init__(self):
        self.type="animal"
    def breed(self):
        return Animal()
    def makeNoise(self):
        print "I am %s, I am an animal" % self.type

class Dog(Animal):
    def __init__(self,numlegs):
        self.type="dog"
        self.eager=False
        self.numlegs=numlegs
    def woof(self):
        print "Woof!!!!"

class Cat(Animal):
    def __init__(self):
        self.type="cat"
    def meow(self):
        print "Meow"

class ThreeLeggedEagerDog(Dog):
    def __init__(self,myWoof):
        super(ThreeLeggedEagerDog,self).__init__(3)
        self.woof()
        self.eager=True
        self.myWoof = myWoof
    def woof(self):
        super(ThreeLeggedEagerDog,self).makeNoise()
        print self.myWoof



# d = ThreeLeggedEagerDog("wooof woooof")
# print d.numlegs
# d.woof()

odie = Dog(4)
Dog.woof(odie)
odie.woof()
