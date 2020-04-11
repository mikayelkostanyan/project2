from sympy import *

class Pos:
    a1 = 0
    F1 = 0
    T = 0
    a2 = 0
    a3x = 0
    a3y = 0

    def init(self, t, M1, M2, M3, distanceBetweenM1_M3, Myu1, Myu2, Myu3, function, startingXPositionM1,
             startingXPositionM2, v0=0):
        self.M1 = M1
        self.M2 = M2
        self.M3 = M3
        self.Myu1 = Myu1
        self.Myu2 = Myu2
        self.Myu3 = Myu3
        self.v0 = v0
        self.g = 10
        self.t = t
        self.startingXPositionM1 = startingXPositionM1
        self.startingXPositionM2 = startingXPositionM2
        self.startingXPositionM3 = distanceBetweenM1_M3 + startingXPositionM1
        self.distanceBetweenM1_M3 = distanceBetweenM1_M3
        self.F = function(t)

    def findVariables(self):
        a1 = symbols('a1')
        a2 = symbols('a2')
        T = symbols('T')
        F1 = symbols('F1')

        f1k = self.Myu1 * (T + self.M1 * self.g + self.Myu3 * F1 + self.M2 * self.g)
        f2k = self.Myu2 * self.M2 * self.g
        f3k = self.Myu3 * F1

        x = f3k + f2k
        y = -1 * self.F + f1k
        z = self.M1 * self.M2 + 2 * self.M2 * self.M3 + self.M1 * self.M3 + self.M3

        eq1 = -(((self.M3 * (y + self.M2 * self.g)) - self.M2 * (x - y)) / z) - a1
        eq2 = f2k + self.M2 * a2 - T
        eq3 = -1 * self.M3 * a1 - F1
        eq4 = ((y + (self.M1 + self.M3) * a1) / -1 * self.M2) - a2
        equations = solve([eq1, eq2, eq3, eq4])

        self.a1 = equations.get(a1)
        self.a2 = equations.get(a2)
        self.a3x = equations.get(a1)
        self.a3y = equations.get(a1) - equations.get(a2)
        self.F1 = equations.get(F1)
        self.T = equations.get(T)

    def calculatePosition(self):
        self.findVariables()
        XPositionM1 = 1 / 2 * (self.a1 * self.t  2) + self.v0 * self.t + self.startingXPositionM1
        XPositionM2 = 1 / 2 * (self.a2 * self.t  2) + self.v0 * self.t + self.startingXPositionM2
        XPositionM3 = 1 / 2 * (self.a3x * self.t  2) + self.v0 * self.t + self.startingXPositionM3
        YPositionM3 = 1 / 2 * (self.a3y * self.t ** 2) + self.v0 * self.t + 0

        print("XPositionM1 = ", XPositionM1, ". XPositionM2 = ", XPositionM2, ". XPositionM3 = ", XPositionM3,
              ". YPositionM3 = ", YPositionM3)


timeIntervals = [0, 5, 10, 15, 20, 25]

for t in timeIntervals:
    pos = Pos(t, 0.8, 0.1, 0.6, 10, 6, 1, 9, lambda t: 3 * t - 11, 0, 0, 0)
    print("Example 1")
    pos.calculatePosition()
    pos2 = Pos(t, 4, 6, 0.9, 10, 9, 11, 0, lambda t: 5 * t - 7, 1, 1, 0)
    print("Example 2")
    pos.calculatePosition()
    pos3 = Pos(t, 0.7, 0.5, 11, 1000, 90, 11, 8, lambda t: 8 * t - 1, 0, 0, 0)
    print("Example 3")
    pos.calculatePosition()