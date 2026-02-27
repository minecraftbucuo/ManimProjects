from manimlib import *

class ArithmeticGeometricMean(Scene):
    def construct(self):
        title = Text("算术几何平均不等式的证明", font="KaiTi").scale(1.5)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        agm_formula = Tex(
            r"""A_n=\frac{a_1+a_2+\cdots+a_n}{n}\geq\sqrt[n]{a_1a_2\cdots{a_n}}=G_n"""
        ).set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        agm_formula.shift(DOWN)

        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.shift(UP*2))

        self.play(Write(agm_formula))
        self.wait(1)

        self.play(
            title.animate.scale(0.6).to_edge(UL).shift(UP * 0.4),
            FadeOut(agm_formula, shift=DOWN),
            run_time=1.5
        )
        self.wait(2)

        step1 = VGroup(
            VGroup(
                Text("当", font="KaiTi"),
                Tex(r"n = 2"), Text("时", font="KaiTi")
            ).arrange(RIGHT).set_color(BLUE),
            Tex(r"\frac {a_1 + a_2} {2} \ge \sqrt {a_1 a_2} ").set_color(BLUE),
        ).set_color(BLUE).arrange(DOWN)

        self.play(Write(step1))
        self.wait(1)
        self.play(FadeOut(step1, shift=DOWN))
        self.wait(1)

        step2 = VGroup(
            VGroup(
                Text("假设", font="KaiTi"),
                Tex(r"n = k(k \ge 2)"), Text("时命题成立,即", font="KaiTi")
            ).arrange(RIGHT).set_color(BLUE),
            Tex(r"\frac{a_1+a_2+\cdots+a_k}{k}\geq\sqrt[k]{a_1a_2\cdots{a_k}}").set_color(BLUE),
        ).set_color(BLUE).arrange(DOWN)

        self.play(Write(step2))
        self.wait(1)
        self.play(FadeOut(step2, shift=DOWN))
        self.wait(2)

        step3 = VGroup(
            Tex(r"(k+1)A_{k+1}=a_{1}+a_{2}+\cdots+a_{k}+a_{k+1}"),
            Tex(r"=a_{1}+a_{2}+\cdots+a_{k}+\left[a_{k+1}+(k-1)G_{k+1}\right]-(k-1) G_{k+1}"),
            Tex(r"\geqslant k \sqrt[k]{a_{1} a_{2} \cdots a_{k}}+k \sqrt[k]{a_{k+1} G_{k+1}^{k-1}}-(k-1) G_{k+1}"),
            Tex(r"\geqslant 2 k \sqrt{\sqrt[k]{a_{1} a_{2} \cdots a_{k}} \sqrt[k]{a_{k+1} G_{k+1}^{k-1}}}-(k-1) G_{k+1}"),
            Tex(r"= 2 k \sqrt[2 k]{a_{1} a_{2} \cdots a_{k+1} G_{k+1}^{k-1}}-(k-1) G_{k+1}"),
            Tex(r"= 2 k \sqrt[2 k]{G_{k+1}^{k+1} G_{k+1}^{k-1}}-(k-1) G_{k+1}"),
            Tex(r"= (k+1) G_{k+1}"),
            Tex(r"\Rightarrow  A_{k + 1} \ge G_{k + 1}")
        ).set_color(BLUE).arrange(DOWN).scale(0.8)

        for i in range(len(step3)):
            self.play(Write(step3[i]))
            if i == 1:
                rect1 = SurroundingRectangle(step3[i][1:13], buff=0.1)
                rect2 = SurroundingRectangle(step3[i][14:30], buff=0.1)
                self.wait(1)
                self.play(ShowCreation(rect1), ShowCreation(rect2))
                self.wait(1)
                self.play(FadeOut(rect1), FadeOut(rect2))
            if i == 2:
                rect1 = SurroundingRectangle(step3[i][1:30], buff=0.1)
                self.wait(1)
                self.play(ShowCreation(rect1))
                self.wait(1)
                self.play(FadeOut(rect1))
            self.wait(1)

        # 将摄像头往上移动
        self.play(self.camera.frame.animate.rotate(0.4 * PI, axis=RIGHT), run_time=2)

        self.wait(1)
        thank_you = Text("感谢观看", font="KaiTi", font_size=140).set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        thank_you.rotate(0.4 * PI, axis=RIGHT)
        self.play(Write(thank_you), FadeOut(title), FadeOut(step3, shift=DOWN))
        self.wait(3)