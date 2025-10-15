from manim import *

class Test(Scene):
    def construct(self):
        axes2 = Axes(
            (0, 5, 5), (0, 5, 5),
            5, 5,
            tips=False
        )
        bigger_arc2 = Arc(5,
                  angle=PI/2,
                  arc_center=axes2.get_origin()
        )
        smaller_arc2 = Arc(
            4.25,
            angle=PI/2,
            arc_center=axes2.get_origin()
        )
        observer_arc2 = Arc(
            1, 
            angle=PI/2,
            arc_center=axes2.get_origin()
        )
        
        BG2 = Line(observer_arc2.get_end(),
            [bigger_arc2.get_center()[0]+0.8, bigger_arc2.get_center()[1]+1.25, 0])
        E2 = Star(outer_radius=0.1).set_color(WHITE)\
            .move_to([bigger_arc2.get_end()[0]+0.5, bigger_arc2.get_end()[1], 0])
        K2 = Star(outer_radius=0.1).set_color(WHITE)\
            .move_to([bigger_arc2.get_center()[0]+1.35, bigger_arc2.get_center()[1]+0.7, 0])
        CG2 = Line([observer_arc2.get_start()[0]-0.15, observer_arc2.get_start()[1]+0.5, 0],
                  BG2.get_end())
        BK2 = Line(observer_arc2.get_end(),
                  K2.get_center())
        
        B_label2 = Tex("B")\
            .next_to(observer_arc2.get_end(), LEFT)
        C_label2 = Tex("C")\
            .next_to(CG2.get_start(), RIGHT)
        D_label2 = Tex("D")\
            .next_to(bigger_arc2.get_end(), LEFT)
        E_label2 = Tex("E")\
            .next_to(E2, UR)
        H_label2 = Tex("H")\
            .next_to(K2, DL*2)
        K_label2 = Tex("K")\
            .next_to(K2, UR*0.3)
        G_label2 = Tex("G")\
            .next_to(BG2.get_end(), UR*0.5)

        self.add(axes2, bigger_arc2, smaller_arc2, observer_arc2, BG2, E2, K2, CG2, BK2, B_label2, C_label2, D_label2, E_label2, H_label2, K_label2, G_label2)