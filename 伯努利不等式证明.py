from manimlib import *


class Try(Scene):
    def construct(self):
        title = Text("伯努利不等式的证明", font="KaiTi", font_size=90)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.move_to(1.5*UP))

        bonuli = Tex(r"""
            \begin{cases}
                (1 + x)^a \ge 1 + ax & \text{if } x > -1, a > 1 \\
                (1 + x)^a \le 1 + ax & \text{if } x > -1, 0 < a < 1
            \end{cases}
        """).set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)

        bonuli.move_to(DOWN)
        self.play(Write(bonuli))
        self.wait(1)

        bonuli2 = Tex(r"(1 + x)^a \le 1 + ax \quad \text{if } x > -1, 0 < a < 1")
        bonuli2.set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        bonuli2.move_to(bonuli)
        self.play(bonuli.animate.become(bonuli2))

        self.wait(1)
        self.play(title.animate.scale(0.45).to_corner(UL), bonuli.animate.scale(0.9).move_to(UP * 2))
        self.wait(1)

        zhengming = VGroup(
            Tex(r"f(x)=(1 + x)^a-1-ax"),
            Tex(r"f'(x)=a(1+x)^{a-1}-a"),
            Tex(r"f'(x)=a\left[ (1+x)^{a-1}-1 \right]"),
            Tex(r"f(x)_{max}=f(0)=0"),
            Tex(r"(1 + x)^a-1-ax \le 0"),
            Tex(r"(1 + x)^a \le 1+ax"),
            Tex(r"(1 + x)^a \le 1+ax \quad (x > -1, 0 < a < 1)")
        ).set_color(BLUE)

        self.play(Write(zhengming[0]))
        self.wait(1)

        for i in range(1, len(zhengming)):
            self.play(TransformMatchingTex(zhengming[i-1], zhengming[i]))
            self.wait(1)

        rect = SurroundingRectangle(zhengming[-1], color=YELLOW, buff=0.1)
        self.play(Write(rect))
        self.play(FadeOut(rect))
        self.remove(bonuli)

        xiexie = Text("谢谢观看", font="KaiTi", font_size=140).set_color_by_gradient(BLUE, YELLOW, RED)
        self.play(
            Transform(zhengming[-1], xiexie),
            FadeOut(title)
        )




