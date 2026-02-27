from manimlib import *

class Wallis(Scene):
    def construct(self):
        title = Text("Wallis 公式", font="KaiTi")
        title.set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL).scale(2)
        wallis_formula = Tex(
            r"""\int_{0}^{\frac{\pi}{2}} \sin ^{n} x dx=\int_{0}^{\frac{\pi}{2}} \cos ^{n} x dx=
            \left\{\begin{array}{l}
            \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{3}{4} \cdot \frac{1}{2} \cdot \frac{\pi}{2} \quad \text {n is even} \\
            \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{4}{5} \cdot \frac{2}{3} \cdot 1 \quad \text {n is odd}
            \end{array}\right."""
        ).set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.shift(UP*2))
        wallis_formula.shift(DOWN * 0.7)
        self.play(Write(wallis_formula))
        self.wait(1)

        xianzheng = Tex(r"\int_{0}^{\frac{\pi}{2}} \sin ^{n} x dx=\int_{0}^{\frac{\pi}{2}} \cos ^{n} x dx")
        xianzheng.set_color(BLUE)
        self.play(
            Transform(wallis_formula, xianzheng),
            title.animate.scale(0.43).to_edge(UL),
            run_time=1.5
        )
        self.wait(0.5)
        self.remove(wallis_formula)
        self.play(xianzheng.animate.shift(2 * UP))

        buzhou1_group = VGroup(
            Tex(r"\int_{0}^{\frac{\pi}{2}} \sin ^{n} x dx=\int_{0}^{\frac{\pi}{2}} \sin ^{n} x dx").set_color(BLUE),
            Tex(r"\int_{0}^{\frac{\pi}{2}} \sin ^{n} x dx=\int_{\frac{\pi}{2}}^{0} \sin ^{n}\left(\frac{\pi}{2}-t\right) d\left(\frac{\pi}{2}-t\right)").set_color(BLUE),
            Tex(r"\int_{0}^{\frac{\pi}{2}} \sin ^{n} x dx=-\int_{\frac{\pi}{2}}^{0} \cos ^{n} t d t").set_color(BLUE),
            Tex(r"\int_{0}^{\frac{\pi}{2}} \sin ^{n} x dx=\int_{0}^{\frac{\pi}{2}} \cos ^{n} t d t").set_color(BLUE),
        )

        huanyuan = Tex(r"x=\frac{\pi}{2}-t").set_color(BLUE)
        self.play(Write(buzhou1_group[0]))
        huanyuan.shift(2 * DOWN)
        self.wait(1)
        self.play(Write(huanyuan))

        for i in range(1, 4):
            self.play(TransformMatchingTex(buzhou1_group[i-1], buzhou1_group[i]))
            self.wait(1)

        rect1 = SurroundingRectangle(buzhou1_group[3], buff=0.2, color=YELLOW)
        rect2 = SurroundingRectangle(xianzheng, buff=0.2, color=YELLOW)
        self.play(FadeOut(huanyuan, shift=DOWN), Write(rect1), Write(rect2))
        self.wait(1)
        self.play(FadeOut(rect1), FadeOut(rect2), FadeOut(buzhou1_group[3]), FadeOut(xianzheng))

        buzhou2_group = VGroup(
            Tex(r"I_{n}=\int_{0}^{\frac{\pi}{2}} \cos ^{n} x d x").set_color(BLUE),
            Tex(r"I_{n}=\int_{0}^{\frac{\pi}{2}} \cos ^{n-1} x d(\sin x)").set_color(BLUE),
            Tex(r"I_{n}=\left.\cos ^{n-1} x \sin x\right|_{0} ^{\frac{\pi}{2}}-\int_{0}^{\frac{\pi}{2}} \sin x d\left(\cos ^{n-1} x\right)").set_color(BLUE),
            Tex(r"I_{n}=(n-1) \int_{0}^{\frac{\pi}{2}} \sin ^{2} x \cos ^{n-2} x d x").set_color(BLUE),
            Tex(r"I_{n}=(n-1) \int_{0}^{\frac{\pi}{2}}\left(1-\cos ^{2} x\right) \cos ^{n-2} x d x").set_color(BLUE),
            Tex(r"I_{n}=(n-1) \int_{0}^{\frac{\pi}{2}} \cos ^{n-2} x d x - (n-1) \int_{0}^{\frac{\pi}{2}} \cos ^{n} x d x").set_color(BLUE),
            Tex(r"I_{n}=(n-1) I_{n-2}-(n-1) I_{n}").set_color(BLUE),
            Tex(r"I_{n}=\frac{n-1}{n}\cdot{I_{n-2}}").set_color(BLUE),
            # n is odd
            Tex(r"I_{n}=\frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdot {I_{n-4}}").set_color(BLUE),
            Tex(r"I_{n}=\frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{2}{3}\cdot {I_{1}}").set_color(BLUE),
            Tex(r"I_{n}=\frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{2}{3}\cdot \int_{0}^{\frac{\pi}{2}} \cos ^{1} x d x").set_color(BLUE),
            Tex(r"I_{n}=\frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{2}{3}\cdot 1").set_color(BLUE),
            # n is even
            Tex(r"I_{n}=\frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{3}{4} \cdot \frac{1}{2} \cdot {I_{0}}").set_color(BLUE),
            Tex(r"I_{n}=\frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{3}{4} \cdot \frac{1}{2} \cdot \int_{0}^{\frac{\pi}{2}} \cos ^{0} x d x").set_color(BLUE),
            Tex(r"I_{n}=\frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{3}{4} \cdot \frac{1}{2} \cdot \frac{\pi}{2}").set_color(BLUE)
        )

        self.play(Write(buzhou2_group[0]))
        for i in range(0, 14):
            self.play(TransformMatchingTex(buzhou2_group[i], buzhou2_group[i+1]))
            self.wait(1)
            if i == 7 or i == 12:
                self.wait(1)

        wallis_formula = Tex(
            r"""\int_{0}^{\frac{\pi}{2}} \sin ^{n} x dx=\int_{0}^{\frac{\pi}{2}} \cos ^{n} x dx=
            \left\{\begin{array}{l}
            \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{3}{4} \cdot \frac{1}{2} \cdot \frac{\pi}{2} \quad \text {n is even} \\
            \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{4}{5} \cdot \frac{2}{3} \cdot 1 \quad \text {n is odd}
            \end{array}\right."""
        ).set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        self.play(FadeOut(buzhou2_group[14]), Write(wallis_formula))

        self.wait(1)
        self.play(FadeOut(title))

        xiexie = Text("感谢观看", font="KaiTi", font_size=140).set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        self.play(Transform(wallis_formula, xiexie))
        self.wait(2)