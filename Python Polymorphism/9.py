class bird:
    def move(self):
        return "Flying in the sky"
class dog:
    def move(self):
        return "Running on the ground"
class fish:
    def move(self):
        return "Swimming in the water"
bird = bird()
dog = dog()
fish = fish()
print(bird.move())
print(dog.move())
print(fish.move())
