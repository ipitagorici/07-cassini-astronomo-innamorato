from manim import *

class Test(Scene):
    def construct(self):
        circle = Circle(radius=2).set_color(WHITE)\
            .shift(UP)
        F = Dot(circle.get_center())
        FP = Line(F,
            [F.get_x(), F.get_y()+circle.radius, 0])
        
        FC = Line(F,
            [F.get_x(), F.get_y()-circle.radius, 0])
        FB = Line(F,
            [F.get_x()-1.5, F.get_y()-circle.radius+0.7, 0])
        FG = Line(F,
            [F.get_x()-0.7, F.get_y()-circle.radius+0.3, 0])
        FH = Line(F,
            [F.get_x()+0.7, F.get_y()-circle.radius+0.3, 0])
        FE = Line(F,
            [F.get_x()+1.5, F.get_y()-circle.radius+0.7, 0])
        
        BC = Line(FB.get_end(), FC.get_end())
        EC = Line(FE.get_end(), FC.get_end())
        
        M = Dot([FC.get_end()[0], FC.get_end()[1]-1.25, 0])
        CM = Line(M.get_center(), FC.get_end())
        BM = Line(M.get_center(), FB.get_end())
        EM = Line(M.get_center(), FE.get_end())
        
        IK = Line([FC.get_end()[0]-circle.radius, FC.get_end()[1], 0],
            [FC.get_end()[0]+circle.radius, FC.get_end()[1], 0])
        CI = Line(FC.get_end(),
            [IK.get_start()[0], IK.get_start()[1]-circle.radius/2, 0])
        CK = Line(FC.get_end(),
            [IK.get_end()[0], IK.get_end()[1]-circle.radius/2, 0])
        
        MD = Line(M.get_center(),
            [FC.get_end()[0]-0.45, FC.get_end()[1]-0.2, 0])
        MA = Line(M.get_center(),
            [FC.get_end()[0]+0.45, FC.get_end()[1]-0.2, 0])
        
        self.add(circle, F,
                 FP, FC, FB, FG, FH, FE,
                 BC, EC,
                 M, CM, BM, EM,
                 IK, CI, CK,
                 MD, MA)