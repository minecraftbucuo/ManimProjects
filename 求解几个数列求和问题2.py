# 2025.7.30
from manimlib import *


class SummationProblems2(Scene):
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
        self.wait(2)

    def construct(self):
        self.show_title("求解几个求和问题 2")

        problem = VGroup(
            Tex(r"\sum_{i = 1}^{n}{\frac{i(i+1)}{2}} + \sum_{i = 1}^{n}{\frac{i(i+1)}{2}} + \sum_{i = 1}^{n}{\frac{i(i+1)}{2}}"),
            Tex(r"\sum_{i = 1}^{n}{\frac{i(i+1)}{2}}"),
            Tex(r"\sum_{i = 1}^{n}{\frac{(n - i + 1)(n - i + 2)}{2}}"),
            Tex(r"\sum_{i = 1}^{n}{\frac{n^2-2ni+3n+i^2-3i+2}{2}}"),
            Tex(r"\sum_{i = 1}^{n}{\frac{i(i+1)}{2}}"),
            Tex(r"\sum_{i = 1}^{n}{\sum_{j = 1}^{i}{j}}"),
            Tex(r"\sum_{j = 1}^{n}{j\sum_{i = j}^{n}{1}}"),
            Tex(r"\sum_{j = 1}^{n}{j(n - j + 1)}"),
            Tex(r"\sum_{i = 1}^{n}{(ni - i^2 + i)}"),
            Tex(r"\sum_{i = 1}^{n}{\frac{i(i+1)}{2}} + \sum_{i = 1}^{n}{\frac{i(i+1)}{2}} + \sum_{i = 1}^{n}{\frac{i(i+1)}{2}}"),
            Tex(r"\sum_{i = 1}^{n}{\frac{i(i+1)}{2}} + \sum_{i = 1}^{n}{\frac{n^2-2ni+3n+i^2-3i+2}{2}} + \sum_{i = 1}^{n}{(ni - i^2 + i)}"),
            Tex(r"\sum_{i = 1}^{n}{\frac{n^2+3n+2}{2}}"),
            Tex(r"\sum_{i = 1}^{n}{\frac{(n+1)(n+2)}{2}}"),
            Tex(r"\frac{n(n+1)(n+2)}{2}"),
            Tex(r"3\sum_{i = 1}^{n}{\frac{i(i+1)}{2}} = \frac{n(n+1)(n+2)}{2}"),
            Tex(r"\sum_{i = 1}^{n}{\frac{i(i+1)}{2}} = \frac{n(n+1)(n+2)}{6}"),
        )
        for i in range(len(problem)):
            problem[i].set_color_by_gradient(GREEN, BLUE, YELLOW)

        self.play(Write(problem[0]))
        self.wait(1)
        for i in range(1, 4):
            self.play(TransformMatchingTex(problem[i - 1], problem[i]))
            self.wait(1)

        problem3_copy = problem[3].copy()
        self.play(problem3_copy.animate.scale(0.7).next_to(self.title, DOWN))
        self.wait(1)

        for i in range(4, 9):
            self.play(TransformMatchingTex(problem[i - 1], problem[i]))
            self.wait(1)

        problem8_copy = problem[8].copy()
        problem8_copy_ = problem8_copy.copy()
        problem8_copy_.to_corner(UR).shift(DOWN * self.title.get_height())
        self.play(problem8_copy.animate.scale(0.7).move_to(problem8_copy_))
        self.wait(1)

        for i in range(9, len(problem)):
            if i == 10:
                self.play(
                    FadeOut(problem3_copy),
                    FadeOut(problem8_copy)
                )
            self.play(TransformMatchingTex(problem[i - 1], problem[i]))
            self.wait(1)

        rect = SurroundingRectangle(problem[-1], buff=0.05, color=YELLOW)
        self.play(ShowCreation(rect))
        self.play(FadeOut(rect))

        problem2 = VGroup(
            Tex(r"\sum_{i=1}^{n}{1}=n"),
            Tex(r"\sum_{i=1}^{n}{i}=\frac{n(n+1)}{2}"),
            Tex(r"\sum_{i=1}^{n}{\frac{i(i+1)}{2}}=\frac{n(n+1)(n+2)}{6}"),
        ).arrange(DOWN)
        for i in range(len(problem2)):
            problem2[i].set_color_by_gradient(GREEN, BLUE, YELLOW)

        self.play(TransformMatchingShapes(problem[-1], problem2))
        self.wait(2)

        problem3 = VGroup(
            Tex(r"\sum_{i=1}^{n}{1}=\frac{n}{1!}"),
            Tex(r"\sum_{i=1}^{n}{i}=\frac{n(n+1)}{2!}"),
            Tex(r"\sum_{i=1}^{n}{\frac{i(i+1)}{2}}=\frac{n(n+1)(n+2)}{3!}"),
        ).arrange(DOWN)
        for i in range(len(problem3)):
            problem3[i].set_color_by_gradient(GREEN, BLUE, YELLOW)

        self.play(TransformMatchingShapes(problem2, problem3))
        self.wait(2)

        guess1 = Tex(r"\sum_{i=1}^{n}{\frac{i(i+1)(i+2)}{3!}}=\frac{n(n+1)(n+2)(n+3)}{4!}")
        guess1.set_color_by_gradient(GREEN, BLUE, YELLOW)
        self.play(TransformMatchingShapes(problem3, guess1))
        self.wait(2)

        guess2 = Tex(r"\underbrace{\sum \sum \cdots \sum}_{\text{m terms}} \space1=\frac{(n+m-1)!}{m! \space (n-1)!}")
        guess2.set_color_by_gradient(GREEN, BLUE, YELLOW)
        self.play(TransformMatchingShapes(guess1, guess2))
        self.wait(2)

        self.show_end(guess2)





