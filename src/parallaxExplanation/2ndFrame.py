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
        
        E_star1 = Star(outer_radius=0.1).set_color(WHITE)\
            .move_to([bigger_arc1.get_end()[0]+0.5, bigger_arc1.get_end()[1] - 0.03, 0])
        E_label1 = Tex("E")\
            .next_to(E_star1, UP)
        H1 = Dot([-1, 2.3, 0])
        H_label1 = Tex("H")\
            .next_to(H1, UP)

        BH1 = Line(observer_arc1.get_end(),
                  H1)
        
        EH = Line(E_star1, H1,
                  stroke_width=6)\
            .set_color(GREEN)

        comet_position1v1 = Dot([-1.25, 1.6, 0])\
            .set_color(RED)
        F_label1 = Tex("F")\
            .next_to(comet_position1v1, DR)\
            .shift(LEFT*0.3)

        self.add(axes1, observer_arc1, observer_arc_label1, observer_point_label1, observer_point, smaller_arc1, bigger_arc1)
        self.add(E_star1, E_label1, H1, H_label1, BH1, comet_position1v1, F_label1, EH)