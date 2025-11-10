#herança
class clawfish(object):
    pass
nemo = clawfish()
print(type(clawfish()))
print(type(nemo))

print(isinstance(nemo, clawfish))

#relação filho e pai
class Animal(object):
    pass

class Vertebrate(Animal):
    pass

class Fish(Vertebrate):
    pass

class ClownFish(Fish):
    pass

class TangFish(Fish):
    pass

nemo = ClownFish()
print(isinstance(nemo, ClownFish))
print(isinstance(nemo, TangFish))
print(isinstance(nemo, Animal))

#metodos herdados
class Fish(Animal):
    def speak(self):
        return "Blub"

class ClownFish(Fish):
    pass

class TangFish(Fish):
    pass
dory = TangFish()
print(dory.speak())
