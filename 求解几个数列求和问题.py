# 2025.7.30
from manimlib import *


class LimitDerivation(Scene):
    def show_title(self, title_text):
        self.title = Text(title_text, font="KaiTi", font_size=90)
        self.title.set_color_by_gradient(GREEN, BLUE, YELLOW)
        self.play(Write(self.title))
        self.wait(1)

        self.play(self.title.animate.scale(0.45).to_corner(UL))
        self.wait(1)

    def show_end(self, last):
        xiexie = Text("谢谢观看", font="KaiTi", font_size=140).set_color_by_gradient(BLUE, YELLOW, RED)
        self.play(
            FadeOut(self.title),
            ReplacementTransform(last, xiexie),
        )

    def construct(self):
        self.show_title("求解几个求和问题")

        problem1 = Tex(r"\sum_{i=1}^{n} {1}")
        problem1.set_color_by_gradient(BLUE, YELLOW, GREEN)
        self.play(Write(problem1))
        self.wait(1)

        ans1 = Tex(r"\sum_{i=1}^{n} {1} = n")
        ans1.set_color_by_gradient(BLUE, YELLOW, GREEN)
        self.play(TransformMatchingTex(problem1, ans1))
        self.wait(1)

        problem2 = VGroup(
            Tex(r"\sum_{i=1}^{n}{i}"),
            Tex(r"2\sum_{i=1}^{n}{i}=\sum_{i=1}^{n}{i} + \sum_{i=1}^{n}{i}"),
            Tex(r"2\sum_{i=1}^{n}{i}=\sum_{i=1}^{n}{i} + \sum_{i=1}^{n}{(n - i + 1)}"),
            Tex(r"2\sum_{i=1}^{n}{i}=\sum_{i=1}^{n}{(i + n - i + 1)}"),
            Tex(r"2\sum_{i=1}^{n}{i}=\sum_{i=1}^{n}{(n + 1)}"),
            Tex(r"2\sum_{i=1}^{n}{i}=(n + 1)\sum_{i=1}^{n}{1}"),
            Tex(r"2\sum_{i=1}^{n}{i}=n(n + 1)"),
            Tex(r"\sum_{i=1}^{n}{i} = \frac{n(n+1)}{2}"),
        )
        problem2.set_color_by_gradient(BLUE, YELLOW, GREEN)
        self.play(TransformMatchingTex(ans1, problem2[0]))
        self.wait(1)
        for i in range(1, len(problem2)):
            self.play(TransformMatchingTex(problem2[i - 1], problem2[i]))
            self.wait(1)

        self.wait(1)
        problem3 = VGroup(
            Tex(r"\sum_{i = 1}^{n}{\frac{i(i+1)}{2}}"),
            Tex(r"\sum_{i = 1}^{n}{\frac{i^2}{2}} + \sum_{i = 1}^{n}{\frac{i}{2}}"),
            Tex(r"\sum_{i = 1}^{n}{\frac{i(i+1)}{2}} + \sum_{i = 1}^{n}{\frac{i(i+1)}{2}} + \sum_{i = 1}^{n}{\frac{i(i+1)}{2}}"),
        )
        problem3.set_color_by_gradient(BLUE, YELLOW, GREEN)
        self.play(TransformMatchingTex(problem2[-1], problem3[0]))
        self.wait(1)
        for i in range(1, len(problem3)):
            self.play(TransformMatchingTex(problem3[i-1], problem3[i]))
            self.wait(1)
        self.wait(1)

        self.show_end(problem3)













