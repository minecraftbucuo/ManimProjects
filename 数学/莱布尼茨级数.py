from manimlib import *

class Leibniz(Scene):
    def construct(self):
        title = Text("莱布尼茨级数的推导", font="KaiTi")
        title.set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL).scale(1.8)
        title.move_to(1.3*UP)

        leibniz = Tex(r"\sum_{i=0}^{\infty} \frac{(-1)^{i}}{2 i+1}=\frac{\pi}{4}")
        leibniz.set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)

        leibniz.move_to(1.2*DOWN)
        self.play(Write(title))
        self.wait(1)
        self.play(Write(leibniz))
        self.wait(1)

        self.play(title.animate.scale(0.5).to_corner(UL), FadeOut(leibniz, shift=DOWN))
        self.wait(1)

        F_x = Tex(r"F(x)=\sum_{i=0}^{\infty} \frac{(-1)^{i}}{2 i+1} x^{2 i+1} \quad F(0)=0")
        F_x.set_color(BLUE)
        self.play(Write(F_x))
        self.wait(1)
        self.play(F_x.animate.move_to(1.7 * UP))

        dF_x_group = VGroup(
            Tex(r"\frac{d F(x)}{d x}=\sum_{i=0}^{\infty}(-1)^{i} x^{2 i}"),
            Tex(r"\frac{d F(x)}{d x}=1-x^{2}+x^{4}-x^{6}+\cdots"),
            Tex(r"\frac{d F(x)}{d x}=\frac{1}{1+x^{2}}"),
            Tex(r"F(x)=\arctan x+c"),
            Tex(r"F(x)=\arctan x"),
            Tex(r"F(1)=\arctan 1"),
            Tex(r"F(1)=\frac{\pi}{4}"),
            Tex(r"\sum_{i=0}^{\infty} \frac{(-1)^{i}}{2 i+1}=\frac{\pi}{4}")
        ).set_color(BLUE)

        self.play(Write(dF_x_group[0]))
        for i in range(1, 4):
            self.play(TransformMatchingTex(dF_x_group[i-1], dF_x_group[i]))
            self.wait(1)

        F_0 = dF_x_group[3].copy()
        self.play(F_0.animate.move_to(1.7 * DOWN))
        self.wait(1)

        F_0_1 = Tex(r"F(0)=c").set_color(BLUE)
        F_0_1.move_to(1.7 * DOWN)
        self.play(TransformMatchingTex(F_0, F_0_1))
        self.wait(1)

        self.play(FadeOut(F_0_1), TransformMatchingTex(dF_x_group[3], dF_x_group[4]))
        self.wait(1)
        self.play(TransformMatchingTex(dF_x_group[4], dF_x_group[5]))
        self.wait(1)
        self.play(TransformMatchingTex(dF_x_group[5], dF_x_group[6]))
        self.wait(1)
        self.play(TransformMatchingTex(dF_x_group[6], dF_x_group[7]))
        self.play(FadeOut(F_x))
        self.wait(1)

        rect = SurroundingRectangle(dF_x_group[7], buff=0.2)
        self.play(Write(rect))

        self.play(
            dF_x_group[7].animate.scale(2).set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL),
            rect.animate.scale(2),
            FadeOut(title)
        )
        self.wait(1)

        xiexie = Text("感谢观看", font="KaiTi", font_size=140)
        xiexie.set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        self.play(
            ReplacementTransform(dF_x_group[7], xiexie),
            FadeOut(rect)
        )
        self.wait(2)