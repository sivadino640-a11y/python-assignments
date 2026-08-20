class bird:
    def move(self):
        return "Flying sky"
class dog:
    def move(self):
        return "Running ground"
class fish:
    def move(self):
        return "Swimming water"
bird = bird()
dog = dog()
fish = fish()
print(bird.move())
print(dog.move())
print(fish.move())
