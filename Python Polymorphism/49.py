class Temperature:
    def __init__(self, temp):
        self.temp = temp
    def __gt__(self, t):
        return self.temp > t.temp
t1 = Temperature(40)
t2 = Temperature(30)
print(t1 > t2)