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
            title.animate.scale(0.6).to_edge(UL),
            agm_formula.animate.scale(0.65).shift(UP*3.2),
            run_time=1.5
        )
        self.wait(1)

        step1 = VGroup(
            Tex(r"e^x \ge x + 1"),
            Tex(r"e^{x - 1} \ge x"),
            Tex(r"e^{\frac{a_1}{A_n} - 1} \ge \frac{a_1}{A_n}")
        ).set_color(BLUE).shift(DOWN * 0.5)

        self.play(Write(step1[0]))
        self.wait(1)

        for i in range(1, len(step1)):
            self.play(TransformMatchingTex(step1[i-1], step1[i]))
            self.wait(1)

        step2 = Tex(
            r"""
            \begin{array}{c}
            e^{\frac{a_1}{A_n} - 1} \ge \frac{a_1}{A_n} \\
            e^{\frac{a_2}{A_n} - 1} \ge \frac{a_2}{A_n} \\
            \cdots \\
            e^{\frac{a_{n - 1}}{A_n} - 1} \ge \frac{a_{n - 1}}{A_n} \\
            e^{\frac{a_n}{A_n} - 1} \ge \frac{a_n}{A_n} \\
            \end{array}
            """
        ).set_color(BLUE).shift(DOWN * 0.5)
        self.play(TransformMatchingTex(step1[-1], step2))
        self.wait(1)

        step3 = VGroup(
            Tex(r"\left( e^{\frac{a_1}{A_n} - 1} \right )\left( e^{\frac{a_2}{A_n} - 1} \right ) \cdots \left( e^{\frac{a_n}{A_n} - 1} \right ) \ge \left( \frac{a_1}{A_n} \right )\left( \frac{a_2}{A_n} \right )\cdots\left( \frac{a_n}{A_n} \right)"),
            Tex(r"e^{\frac{a_1+a_2+\cdots+a_n}{A_n}-n} \ge \frac{a_1a_2\cdots a_n}{{\left( A_n \right)}^n}"),
            Tex(r"e^{n-n} \ge \frac{a_1a_2\cdots a_n}{{\left( A_n \right)}^n}"),
            Tex(r"1 \ge \frac{a_1a_2\cdots a_n}{{\left( A_n \right)}^n}"),
            Tex(r"{{\left( A_n \right)}^n} \ge a_1a_2\cdots a_n"),
            Tex(r"A_n \ge \sqrt[n] {a_1a_2\cdots a_n}"),
            Tex(r"\frac{a_1+a_2+\cdots+a_n}{n}\geq\sqrt[n]{a_1a_2\cdots{a_n}}")
        ).set_color(BLUE)

        self.play(TransformMatchingTex(step2, step3[0]))
        self.wait(1)

        for i in range(1, len(step3)):
            self.play(TransformMatchingTex(step3[i-1], step3[i]))
            self.wait(1)

        rect = SurroundingRectangle(step3[-1], buff=0.1).set_color(YELLOW)
        self.play(ShowCreation(rect))

        self.wait(0.5)
        self.play(
            FadeOut(agm_formula),
            rect.animate.scale(1.8),
            FadeOut(title),
            step3[-1].animate.scale(1.8).set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL),
            run_time=1.5
        )

        self.wait(1)
        thank_you = Text("感谢观看", font="KaiTi", font_size=140).set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        self.play(Write(thank_you), FadeOut(rect), FadeOut(step3[-1]))
        self.wait(3)