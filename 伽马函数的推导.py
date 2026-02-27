from manimlib import *

class Try(Scene):
    def construct(self):
        self.wait(1)
        gamma = Tex(r"\Gamma(x) = \int_{0}^{\infty} t^{x-1} e^{-t} \, dt", font_size=100).set_color(RED)
        title = Text("伽马函数的推导", font="KaiTi", font_size=100).set_color(RED)
        self.play(Write(gamma))
        self.wait(1)
        self.play(ReplacementTransform(gamma, title))
        self.wait(1)
        self.play(title.animate.scale(0.4).to_corner(UL))
        self.wait(1)
        math_text1 = Tex(r"\sum_{n = 0}^{+\infty} x^n = ").set_color(BLUE)
        self.play(Write(math_text1))
        self.play(math_text1.animate.to_edge(LEFT))
        math_text2 = Tex(r"1 + x + x^2 + x^3 + \cdots").set_color(BLUE)
        self.play(Write(math_text2))
        self.wait(1)
        math_text3 = Tex(r"\frac 1 {1 - x}").set_color(BLUE)
        self.play(ReplacementTransform(math_text2, math_text3))
        self.wait(1)
        math_text4 = Tex(r"\int_0^{+\infty} e^{-t(1-x)}dt").set_color(BLUE)
        # self.play(ReplacementTransform(math_text3, math_text4))
        self.play(TransformMatchingTex(math_text3, math_text4))
        self.wait(1)
        math_text5 = Tex(r"\int_0^{+\infty} e^{-t} \cdot e^{tx}dt").set_color(BLUE)
        # self.play(ReplacementTransform(math_text4, math_text5))
        self.play(TransformMatchingTex(math_text4, math_text5))
        self.wait(1)
        math_text6 = Tex(r"\int_0^{+\infty} e^{-t} \sum_{n = 0}^{+\infty} {\frac {x^nt^n} {n!}} dt")
        math_text6.set_color(BLUE)
        # self.play(ReplacementTransform(math_text5, math_text6))

        # 效果更佳
        self.play(TransformMatchingTex(math_text5, math_text6, key_map={
            r"\cdot e^{tx}" : r"\sum_{n = 0}^{+\infty} {\frac {x^nt^n} {n!}}"
        }))

        # self.play(TransformMatchingTex(math_text5, math_text6))

        self.wait(1)
        math_text7 = Tex(r"\sum_{n = 0}^{+\infty} {x^n \int_0^{+\infty} {\frac{e^{-t}t^n} {n!}}dt}").set_color(BLUE)
        # self.play(ReplacementTransform(math_text6, math_text7))
        self.play(TransformMatchingTex(math_text6, math_text7))
        self.wait(1)
        group1 = VGroup(math_text1, math_text7)
        self.play(group1.animate.arrange(RIGHT))
        self.wait(1)
        math_text8 = Tex(r"1 = \int_0^{+\infty} {\frac{e^{-t}t^n}{n!}}dt").set_color(BLUE)
        # self.play(ReplacementTransform(group1, math_text8))
        self.play(TransformMatchingShapes(group1, math_text8))
        self.wait(1)
        math_text9 = Tex(r"n!=\int_0^{+\infty}t^ne^{-t}dt").set_color(BLUE)
        # self.play(ReplacementTransform(math_text8, math_text9))
        self.play(TransformMatchingTex(math_text8, math_text9))
        self.wait(1)
        math_text10 = Tex(r"\Gamma(x) = \int_{0}^{+\infty} t^{x-1} e^{-t} \, dt").set_color(BLUE)
        # self.play(ReplacementTransform(math_text9, math_text10))
        self.play(TransformMatchingTex(math_text9, math_text10))

        # 创建矩形包裹住 math_text10
        rect = SurroundingRectangle(math_text10, buff=0.1, color=YELLOW)
        self.play(Write(rect))
        self.play(FadeOut(rect))

        self.wait(1.5)
        text = Text("感谢观看", color=RED, font_size=100, font="KaiTi").set_color(RED)
        # self.remove(title)
        # self.remove(math_text10)
        self.play(FadeOut(title), FadeOut(math_text10, shift=DOWN))
        self.play(Write(text))
        self.wait(2)




