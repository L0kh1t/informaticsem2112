class Vector:
    def __init__(self, x, y, z):
        try:
            self.x = int(x)
            self.y = int(y)
            self.z = int(z)
        except ValueError:
            pass

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def summ(self, other):
        print(self.x + other.x, self.y + other.y, self.z + other.z)

    def min(self, other):
        print(self.x - other.x, self.y - other.y, self.z - other.z)

    def compvectors(self, other):
        print(self.x*other.x, self.y*other.y, self.z*other.z)

    def compnum(self, other):
        print(self.x*other, self.y*other, self.z*other)
