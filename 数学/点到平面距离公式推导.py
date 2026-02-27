# 2025.5.10
from manimlib import *

class MovingPointOnPlane(Scene):
    def construct(self):
        title = Text("点到平面距离公式的推导", font="KaiTi", font_size=80)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.5).to_corner(UL))


        gongshi = Tex(r"Ax+By+Cz+D=0 \quad \quad E(x_0,y_0,z_0)").move_to(UP * 2).set_color(BLUE).scale(0.8)
        self.play(Write(gongshi))
        group1 = VGroup(
            Tex(r"\sqrt {(x-x_0)^2+(y-y_0)^2+(z-z_0)^2}"),
            Tex(r"(x-x_0)^2+(y-y_0)^2+(z-z_0)^2"),
            Tex(r"\left[ (x-x_0)^2+(y-y_0)^2+(z-z_0)^2 \right] (A^2+B^2+C^2)"),
            Tex(r"\left[ (x-x_0)^2+(y-y_0)^2+(z-z_0)^2 \right] (A^2+B^2+C^2) \ge \left[ A(x-x_0)+B(y-y_0)+C(z-z_0) \right]^2"),
            Tex(r"\left[ (x-x_0)^2+(y-y_0)^2+(z-z_0)^2 \right] (A^2+B^2+C^2) \ge \left[Ax+By+Cz-(Ax_0+By_0+Cz_0) \right]^2"),
            Tex(r"\left[ (x-x_0)^2+(y-y_0)^2+(z-z_0)^2 \right] (A^2+B^2+C^2) \ge \left[-D-(Ax_0+By_0+Cz_0) \right]^2"),
            Tex(r"\left[ (x-x_0)^2+(y-y_0)^2+(z-z_0)^2 \right] (A^2+B^2+C^2) \ge \left[Ax_0+By_0+Cz_0+D \right]^2"),
            Tex(r"\left[ (x-x_0)^2+(y-y_0)^2+(z-z_0)^2 \right] \ge \frac{\left[Ax_0+By_0+Cz_0+D \right]^2} {A^2+B^2+C^2}"),
            Tex(r"\sqrt {(x-x_0)^2+(y-y_0)^2+(z-z_0)^2} \ge \frac{\left | Ax_0+By_0+Cz_0+D \right | } {\sqrt {A^2+B^2+C^2}}"),
        ).set_color(BLUE).scale(0.73)

        self.play(Write(group1[0]))
        self.wait(1)
        for i in range(1, len(group1)):
            self.play(TransformMatchingTex(group1[i - 1], group1[i]))
            self.wait(1)

        rect = SurroundingRectangle(group1[-1], buff=0.05, color=YELLOW)
        self.play(Write(rect))

        self.wait(2)

        xiexie = Text("谢谢观看", font="KaiTi", font_size=140).set_color_by_gradient(BLUE, YELLOW, RED)
        self.play(
            ReplacementTransform(group1[-1], xiexie),
            FadeOut(rect),
            FadeOut(title),
            FadeOut(gongshi)
        )

