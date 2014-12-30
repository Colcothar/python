class Animal(object):
    

    isalive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print self.name
        print self.age
hippo = Animal("Hank", 3)
sloth = Animal("Soli", 4)
ocelot = Animal("Ocoso", 7)
hippo.description()
print hippo.health
print sloth.health
print ocelot.health