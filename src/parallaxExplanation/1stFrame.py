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

        
        self.add(axes1, observer_arc1, observer_arc_label1, observer_point_label1, observer_point, smaller_arc1, bigger_arc1)
        


        
