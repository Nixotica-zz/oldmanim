from manimlib.imports import *

class S3Complete(GraphScene):
    def construct(self):
        dots = []
        dot1 = Dot(point = ORIGIN + 3*UP)
        dot2 = Dot(point = ORIGIN + 3*LEFT + 3*DOWN)
        dot3 = Dot(point = ORIGIN + 3*RIGHT + 3*DOWN)
        dots.append(dot1)
        dots.append(dot2)
        dots.append(dot3)
        for i in range(len(dots)):
            self.play(ShowCreation(dots[i]))
        for i in range(len(dots)):
            for j in range(i + 1, len(dots)):
                arrow = DoubleArrow(dots[i].get_center(), dots[j].get_center())
                self.play(GrowArrow(arrow))

class S5Complete(GraphScene):
    def construct(self):
        dots = []
        dot1 = Dot(point = ORIGIN + 3*UP)
        dot2 = Dot(point = ORIGIN + 0.5*UP + 3*LEFT)
        dot3 = Dot(point = ORIGIN + 3*DOWN + 2*LEFT)
        dot4 = Dot(point = ORIGIN + 3*DOWN + 2*RIGHT)
        dot5 = Dot(point = ORIGIN + 0.5*UP + 3*RIGHT)
        dots.append(dot1)
        dots.append(dot2)
        dots.append(dot3)
        dots.append(dot4)
        dots.append(dot5)
        for i in range(len(dots)):
            self.play(ShowCreation(dots[i]))
        for i in range(len(dots)):
            for j in range(i + 1, len(dots)):
                arrow = DoubleArrow(dots[i].get_center(), dots[j].get_center(), stroke_width = 3, preserve_tip_size_when_scaling = False)
                self.play(GrowArrow(arrow))

class SnComplete(GraphScene):
    def construct(self):
        dots = []
        for i in range(10):
            x = random.uniform(-4, 4)
            y = random.uniform(-3, 3)
            dot = Dot(point = ORIGIN + x*RIGHT + y*UP)
            dots.append(dot)
            self.play(ShowCreation(dots[i]))
        
        for i in range(len(dots)):
            for j in range(i + 1, len(dots)):
                arrow = DoubleArrow(dots[i].get_center(), dots[j].get_center(), stroke_width = 3, preserve_tip_size_when_scaling = False)
                self.play(GrowArrow(arrow))