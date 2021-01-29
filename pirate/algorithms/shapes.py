import math

class Point():
    def __init__(self,x,y):
      self.x = x
      self.y = y

    def to_string(self):
      return self.__str__()

    def __str__(self):
        return f"({self.x}, {self.y})"

class Line():
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def to_string(self):
        return self.__str__()

    def __str__(self):
        pxstr = self.p1.to_string()
        pystr = self.p2.to_string()

        return f"{pxstr} {pystr}"

    def length(self):
        rise = math.pow(self.p1.y - self.p2.y,2)
        run = math.pow(self.p1.x - self.p2.x, 2)
        return math.sqrt(rise + run)

class Shape():
    def __init__(self,*lines):
        self.lines = lines

    def __str__(self):
        str = []
        for i in self.lines:
           str.append(i.to_string())
        return ", ".join(str)

if __name__ == "__main__":
    p = Point(1,2)
    print(p)

    l = Line(Point(1,1), Point(2,2))
    print(l)
    print(l.length())

    l2 = Line(Point(2,2), Point(2,4))

    l3 = Line(Point(2, 4), Point(1, 1))
    s = Shape(l,l2, l3)
    print(s)
