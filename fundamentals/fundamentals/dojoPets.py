class Pet:

    def __init__(self,name,type,tricks,health,energy,noise):
        self.name = name
        self.type = type 
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 5
        return self
        def eat(self):
            self.energy+= 10
        def play(self):
            self.energy = self.health - 15
            # self.health = self.health + 5
            self.health= self.health + 5
            return self
        def eat (self):
            self.energy+= 5
            self.health+= 15
        def noise (self):
            print(self.noise)
# implement __init__( name , type , tricks ):
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound

class Ninja:
#     # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self,first_name, last_name,pet,treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        print ("ninja is walking pet")
        return self

        def feed(self):
            pass

            def bathe(self):
                pass


# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method
ninja1 = Ninja ('adrian','vences','bear','milkbone','purina')
bear = Pet ('bear','rottweiler','sit',100,100)


ninja1.walk()
bear.play()