print("hello world" * 3)

for i in range (1, 5, 2):
    print(i)

def findMax():
    return print(max(5, 7))

list_ages = [2, 5, 10, 9, 5, 10, 22,1]
set_ages = set(list_ages)
print(set_ages)

class ClownFish():
    pass

fish = ClownFish()

print(isinstance(fish, ClownFish))

class Fish():
    pass
class ClownFish(Fish):
    pass

fish = ClownFish()
print(isinstance(f
