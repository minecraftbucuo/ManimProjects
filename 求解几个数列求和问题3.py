# 2025.8.4
from manimlib import *


class SummationProblems3(Scene):
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
            ReplacementTransform(last, xiexie),
        )
        self.wait(2)

    def construct(self):
        self.show_title("求解几个求和问题 3")

        tex1 = VGroup(
            Tex(r"\underbrace{\sum \sum \cdots \sum}_{\text{m terms}} \space1=\frac{(n+m-1)!}{m! \space (n-1)!}"),
            Tex(r"\sum_{i_1 = 1}^{n}\sum_{i_2 = 1}^{i_1} \cdots \sum_{i_m=1}^{i_{m-1}} \space 1 = \frac{(n+m-1)!}{m! \space (n-1)!}"),
            Tex(r"\sum_{i_1 = 1}^{n}\sum_{i_2 = 1}^{i_1} \cdots \sum_{i_m=1}^{i_{m-1}} \space 1 = C_{n+m-1}^{m}"),

            Tex(r"C_n^m=C_{n-1}^{m}+C_{n-1}^{m-1}"),
            Tex(r"C_{n-1}^{m-1}=C_n^m-C_{n - 1}^{m}"),
            Tex(r"C_{n-1}^{m-1}=C_n^m-C_{n - 1}^{m}"),
            Tex(r"C_i^{m-1}=C_{i+1}^m-C_i^m"),
            Tex(r"\sum_{i_1=m-1}^{n+m-2}{C_{i_1}^{m-1}}=\sum_{i_1=m-1}^{n+m-2}{(C_{i_1+1}^m-C_{i_1}^m)}"),
            Tex(r"\sum_{i_1=m-1}^{n+m-2}{C_{i_1}^{m-1}}=C_{n+m-1}^m"),

            Tex(r"\sum_{i_1=1}^{n}{C_{i_1 + (m-1) -1}^{m-1}}=C_{n+m-1}^m"),
            Tex(r"\sum_{i_1=1}^{n}{\sum_{i_2=1}^{i_1}{C_{i_2+(m-2)-1}^{m-2}}}=C_{n+m-1}^m"),
            Tex(r"\sum_{i_1=1}^{n}{\sum_{i_2=1}^{i_1}{\cdots \sum_{i_m=1}^{i_{m-1}} {C_{i_m+(m-m)-1}^{m-m}} }}=C_{n+m-1}^m"),
            Tex(r"\sum_{i_1=1}^{n}{\sum_{i_2=1}^{i_1}{\cdots \sum_{i_m=1}^{i_{m-1}} {\space 1} }}=C_{n+m-1}^m"),
        )
        for i in range(len(tex1)):
            tex1[i].set_color_by_gradient(GREEN, BLUE, YELLOW)

        self.play(Write(tex1[0]))
        self.wait(2)

        for i in range(1, 3):
            self.play(TransformMatchingTex(tex1[i - 1], tex1[i]))
            self.wait(2)

        tex1_2copy = tex1[2].copy()
        self.play(tex1_2copy.animate.scale(0.8).shift(UP * 2))
        self.wait(2)

        for i in range(3, len(tex1)):
            self.play(TransformMatchingTex(tex1[i - 1], tex1[i]))
            self.wait(2)
            if i == 9:
                rect = SurroundingRectangle(tex1[9][6:20], buff=0.05, color=YELLOW)
                rect2 = SurroundingRectangle(tex1[9][21:], buff=0.05, color=YELLOW)
                self.play(ShowCreation(rect), ShowCreation(rect2))
                self.wait(1)
                self.play(FadeOut(rect), FadeOut(rect2))
                self.wait(1)

        self.play(FadeOut(tex1_2copy))
        rect = SurroundingRectangle(tex1[-1], buff=0.05, color=YELLOW)
        self.play(ShowCreation(rect))
        self.wait(1)
        self.play(
            FadeOut(self.title),
            tex1[-1].animate.scale(2),
            rect.animate.scale(2),
        )
        self.wait(1)
        self.show_end(tex1[-1])