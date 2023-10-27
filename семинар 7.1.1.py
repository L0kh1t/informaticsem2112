import copy

N = ['0'] + list(map(int, input().split(',')))
# Это если ввод таков, что пишут координаты x y z точки, а после её массу


class Vector:
    def __init__(self, x, y, z):
        try:
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
        except ValueError:
            pass

    def summ(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def div(self, other):
        return Vector(self.x//other, self.y//other, self.z//other)


m = 0
n = [0]*(((len(N) - 1)//4)+1)
for i in range(1, len(N)):
    if i % 4 == 0:
        n[i//4] = Vector(N[i-3]*N[i], N[i-2]*N[i], N[i-1]*N[i])
        m += N[i]
n.remove(n[0])
a = copy.copy(n[0])
n.remove(n[0])
while len(n) > 0:
    a = a.summ(n[0])
    n.remove(n[0])
print(a.x/m, a.y/m, a.z/m)

