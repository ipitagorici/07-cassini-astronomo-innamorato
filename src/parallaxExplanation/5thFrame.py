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
        observer_arc1 = Arc(
            1, 
            angle=PI/2,
            arc_center=axes2.get_origin()
        )

        observer_point = Dot(observer_arc1.get_end())\
            .set_color(YELLOW)
        
        K_star2 = Star(outer_radius=0.1).set_color(WHITE)\
            .move_to([bigger_arc2.get_center()[0]+1.8, bigger_arc2.get_center()[1]+0.1, 0])
        K_label1 = Tex("K")\
            .next_to(K_star2, UR*0.3)
        L1 = Dot([2.3, observer_arc1.get_end()[1]+0.6, 0])
        L_label1 = Tex("L")\
            .next_to(L1, RIGHT)

        BL1 = Line(observer_arc1.get_end(),
                   L1)
        
        KL = Line(K_star2, L1,
                  stroke_width=6)\
            .set_color(GREEN)

        comet_position2v2 = Dot([1.5, observer_arc1.get_end()[1]+0.5, 0])\
            .set_color(RED)
        G_label1 = Tex("F")\
            .next_to(comet_position2v2, DR)\
            .shift(LEFT*0.6)

        possibility1 = VGroup(
            axes2, observer_arc1, observer_point, smaller_arc2, bigger_arc2,
            K_star2, K_label1, L1, L_label1, BL1, comet_position2v2, G_label1, KL
        ).shift(LEFT*3)

        self.add(possibility1)
        
        
        
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

        observer_point = Dot(observer_arc2.get_end())\
            .set_color(YELLOW)
        
        K_star2 = Star(outer_radius=0.1).set_color(WHITE)\
            .move_to([bigger_arc2.get_center()[0]+1.8, bigger_arc2.get_center()[1]+0.1, 0])
        K_label2 = Tex("K")\
            .next_to(K_star2, UR*0.3)
        L2 = Dot([2.3, observer_arc2.get_end()[1]+0.6, 0])
        L_label2 = Tex("L")\
            .next_to(L2, RIGHT)
        M_label1 = Tex("M")\
            .next_to(L_label2, UP)\
            .shift(LEFT*0.2)
        M1 = Dot(M_label1.get_center())\
            .shift(LEFT*0.55)
        
        BL2 = Line(observer_arc2.get_end(),
                   L2)

        ML = Line(M1.get_center(), L2,
                  stroke_width=6)\
            .set_color(PINK)

        comet_position2v2 = Dot([1.5, observer_arc2.get_end()[1]+0.5, 0])\
            .set_color(RED)
        G_label2 = Tex("F")\
            .next_to(comet_position2v2, DR)\
            .shift(LEFT*0.6)

        possibility2 = VGroup(
            axes2, observer_arc2, observer_point, smaller_arc2, bigger_arc2,
            K_star2, K_label2, L2, L_label2, M1, M_label1, BL2, comet_position2v2, G_label2, ML
        ).shift(RIGHT*3)

        self.add(possibility2)