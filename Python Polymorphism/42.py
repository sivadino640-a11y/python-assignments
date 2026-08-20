class Distance:
    def __init__(self, feet):
        self.feet = feet
    def __add__(self, d):
        return Distance(self.feet + d.feet)
d1 = Distance(10)
d2 = Distance(20)
d3 = d1 + d2
print(d3.feet)