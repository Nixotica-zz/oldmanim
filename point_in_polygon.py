from manimlib.imports import *

class PIP_Arrow(GraphScene):
    def construct(self):
        testBorder = [(-3.25, -3.25, 0),
                      (-3.25, 3.25, 0),
                      (3.25, 3.25, 0),
                      (3.25, -3.25, 0)]
        visBorder = Polygon(*testBorder, color = WHITE)

        self.play(ShowCreation(visBorder))

        poly = [(-2.5, 0, 0),
                (0, 2.5, 0),
                (2.5, 0, 0),
                (1, 0, 0),
                (1, -2.5, 0),
                (-1, -2.5, 0),
                (-1, 0, 0)]

        visPoly = Polygon(*poly, color = GREEN, fill_color = GREEN, fill_opacity = 0.2)
        
        self.play(ShowCreation(visPoly))

        def makeDot(num, col, x, y):
            dot = Dot(point = ORIGIN, color = col)
            dot.shift(x*RIGHT + y*UP)
            points[i] = dot

        points = []
        for i in range(10):
            x = random.uniform(-3, 3)
            y = random.uniform(-3, 3)
            dot = Dot()
            points.append(dot)
            if (visPoly.is_inside(x, y) < 0):
                makeDot(i, WHITE, x, y)
            else:
                makeDot(i, GREEN, x, y)
            self.play(ShowCreation(points[i]))