from manim import *

class Test(Scene):
    def construct(self):
        axes1 = Axes(
            (0, 5, 5), (0, 5, 5),
            5, 5,
            tips=False
        )
        bigger_arc1 = Arc(5,
                  angle=PI/2,
                  arc_center=axes1.get_origin()
        )
        smaller_arc1 = Arc(
            4.25,
            angle=PI/2,
            arc_center=axes1.get_origin()
        )
        observer_arc1 = Arc(
            1, 
            angle=PI/2,
            arc_center=axes1.get_origin()
        )

        observer_arc_label1 = Tex("Terra")\
            .next_to(observer_arc1.get_start(), DOWN)\
            .shift(LEFT*1.5)
        observer_point_label1 = Tex("Punto d'osservazione", font_size=40)\
            .next_to(observer_arc1.get_end(), LEFT)
        observer_point = Dot(observer_arc1.get_end())\
            .set_color(YELLOW)
        
        K_star1 = Star(outer_radius=0.1).set_color(WHITE)\
            .move_to([bigger_arc1.get_center()[0]+1.8, bigger_arc1.get_center()[1]+0.1, 0])
        K_label1 = Tex("K")\
            .next_to(K_star1, UR*0.3)
        L1 = Dot([2.3, observer_arc1.get_end()[1]+0.6, 0])
        L_label1 = Tex("L")\
            .next_to(L1, RIGHT)

        BL1 = Line(observer_arc1.get_end(),
                   L1)
        
        KL = Line(K_star1, L1,
                  stroke_width=6)\
            .set_color(GREEN)

        comet_position1v2 = Dot([1.5, observer_arc1.get_end()[1]+0.5, 0])\
            .set_color(RED)
        G_label1 = Tex("F")\
            .next_to(comet_position1v2, DR)\
            .shift(LEFT*0.6)

        comet_movement_arrow = CurvedArrow([-1.25, 1.6, 0], comet_position1v2.get_center(), angle=PI/4)
        star_movement_arrow = CurvedArrow([bigger_arc1.get_end()[0]+0.5, bigger_arc1.get_end()[1] - 0.03, 0], K_star1.get_center(), angle=-PI/2)

        self.add(axes1, observer_arc1, observer_arc_label1, observer_point_label1, observer_point, smaller_arc1, bigger_arc1)
        self.add(K_star1, K_label1, L1, L_label1, BL1, comet_position1v2, G_label1, KL, comet_movement_arrow, star_movement_arrow)
