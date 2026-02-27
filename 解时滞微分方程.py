# 2025.8.19
from manimlib import *


class Solution(Scene):
    def show_end(self, last):
        xiexie = Text("谢谢观看", font="KaiTi", font_size=140).set_color_by_gradient(BLUE, YELLOW, RED)
        self.play(
            FadeOut(self.title),
            ReplacementTransform(last, xiexie),
        )
        self.wait(2)

    def construct(self):
        self.title = Tex(r"f'(x)=f(x+1)", font_size=100)
        self.title.set_color_by_gradient(BLUE, YELLOW, RED)
        self.play(Write(self.title))
        self.wait(1)
        self.play(self.title.animate.scale(0.6).to_edge(UP))
        self.wait(1)

        sol = VGroup(
            Tex(r"f(x)=e^{rx}"),
            Tex(r"r e^{r x} = e^{r(x+1)}"),
            Tex(r"r = e^{r}"),

            Tex(r"re^{-r}=1"),
            Tex(r"-re^{-r}=-1"),
            Tex(r"-r=W(-1)"),
            Tex(r"r=-W(-1)"),

            Tex(r"f(x) = \sum_{k} c_k e^{r_k x}"),
        )
        for i in sol:
            i.set_color_by_gradient(BLUE, YELLOW, RED)
            i.scale(1.3)

        W = Tex(r"W(z)e^{W(z)}=z").set_color_by_gradient(BLUE, YELLOW, RED)

        self.play(Write(sol[0]))
        self.wait(1)
        for i in range(1, len(sol)):
            self.play(TransformMatchingTex(sol[i - 1], sol[i]))
            self.wait(1)
            if i == 2:
                W.shift(UP * 1.5)
                self.play(Write(W))
                self.wait(1)

            if i == 5:
                self.play(FadeOut(W, shift=DOWN))

            if i == 6:
                self.r = sol[i].copy()
                self.play(self.r.animate.shift(DOWN * 1.5))

        v = VGroup(sol[-1], self.r)
        self.play(v.animate.move_to(ORIGIN))
        rect = SurroundingRectangle(v, buff=0.1, color=YELLOW)
        self.play(ShowCreation(rect))
        self.wait(1)
        self.play(
            v.animate.scale(1.8),
            rect.animate.scale(1.8),
        )
        self.wait(1)
        self.show_end(v)











