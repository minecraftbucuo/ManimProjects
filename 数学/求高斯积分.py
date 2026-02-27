from manimlib import *

class GaussIntegral(Scene):
    def construct(self):
        gauss_int = Tex(r"\int_0^{+\infty} e^{-x^2}dx", font_size=60)
        gauss_int.set_color_by_gradient(GREEN, BLUE, YELLOW)
        title = Text("求 解 高 斯 积 分", font="KaiTi", font_size=90)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW)

        cover = VGroup(title, gauss_int).arrange(DOWN)
        title.shift(UP)
        self.play(Write(title))
        gauss_int.move_to(DOWN)

        self.play(Write(gauss_int))
        self.wait(1)

        self.play(
            title.animate.scale(0.45).to_corner(UL),
            gauss_int.animate.scale(0.6).to_corner(UR),
        )
        self.wait(1)

        group1 = VGroup(
            VGroup(
                Text("令", font="KaiTi", font_size=32),
                Tex(r"F(t)=\left[\int_{0}^{t} e^{-x^{2}} d x\right]^{2}")
            ).arrange(RIGHT),
            VGroup(
                Text("则", font="KaiTi", font_size=32),
                Tex(r"F(0)=0")
            ).arrange(RIGHT)
        )
        group1.arrange(RIGHT).set_color(BLUE)
        group1[0].shift(LEFT*0.25)
        group1[1].shift(RIGHT*0.25)
        # 纠正位置
        group1[1].shift(DOWN * 0.1)

        self.play(Write(group1[0]))
        self.wait(1)
        self.play(Write(group1[1]))
        self.wait(1)

        # 考虑求出F(t)的其他表达式
        self.play(group1.animate.scale(0.7).shift(UP * 2))
        self.wait(1)

        group2 = VGroup(
            # 0
            VGroup(Tex(r"\frac{d F(t)}{d t}"), Tex(r"=")).arrange(RIGHT),
            # 1
            Tex(r"\frac{d}{d t} \left[\int_{0}^{t} e^{-x^{2}} d x\right] ^ 2"),
            # 2
            Tex(r"2 \left( \int_{0}^{t} e^{-x^{2}} d x \right) ", r"\frac{d}{d t} \int_{0}^{t} e^{-x^{2}} d x"),
            # 3
            Tex(r"2 \left( \int_{0}^{t} e^{-x^{2}} d x \right)", r"e^{-t^{2}}"),
            # 4
            Tex(r"2 \int_{0}^{t} e^{-x^{2} - t^{2}} d x"),
            # 5
            Tex(r"2 \int_{0}^{1} t e^{-(t y)^{2}-t^{2}} d y"),
            # 6
            Tex(r"2 \int_{0}^{1} t e^{-t^{2}\left(y^{2}+1\right)} d y"),
            # 7
            Tex(r"\frac{d}{d t} \int_{0}^{1}-\frac{e^{-t^{2}\left(y^{2}+1\right)}}{y^{2}+1} d y")
        ).set_color(BLUE).arrange(RIGHT)

        for i in group2:
            i.move_to(ORIGIN)

        self.play(Write(group2[0]))
        self.wait(0.6)

        group2_00_copy = group2[0][0].copy()

        self.play(group2_00_copy.animate.shift(5 * LEFT), group2[0][1].animate.shift(5 * LEFT))
        self.play(TransformMatchingTex(group2[0][0], group2[1]))
        self.wait(1)

        for i in range(2, 5):
            self.play(TransformMatchingTex(group2[i-1], group2[i]))
            self.wait(1)

        group3 = VGroup(
            VGroup(Text("令", font="KaiTi", font_size=32), Tex(r"x=ty")).arrange(RIGHT),
            VGroup(Text("则", font="KaiTi", font_size=32), Tex(r"d x=t d y")).arrange(RIGHT)
        ).arrange(RIGHT).set_color(BLUE)

        group3[0].shift(LEFT*0.25)
        group3[1].shift(RIGHT*0.25)
        group3.shift(DOWN * 2)

        self.play(Write(group3))
        self.wait(0.5)
        self.play(group1.animate.to_edge(LEFT), group3.animate.scale(0.7).move_to(group1[1].get_right() + RIGHT*1.5 + DOWN*0.01))

        for i in range(5, 8):
            self.play(TransformMatchingTex(group2[i-1], group2[i]))
            self.wait(1)

        group4 = VGroup(
            group2_00_copy,
            group2[0][1],
            group2[7]
        )
        self.play(group4.animate.arrange(RIGHT))

        rect1 = SurroundingRectangle(group2_00_copy[1:5], buff=0.05, color=YELLOW)
        rect2 = SurroundingRectangle(group2[7][4:], buff=0.05, color=YELLOW)
        self.play(Write(rect1), Write(rect2))
        self.play(FadeOut(rect1), FadeOut(rect2))

        f_t = VGroup(
            Tex(r"F(t)"),
            Tex("="),
            Tex(r"-\int_{0}^{1} \frac{e^{-t^2\left(y^{2}+1\right)}}{y^{2}+1} d y+c \,")
        ).set_color(BLUE).arrange(RIGHT)

        self.play(
            TransformMatchingTex(group4[0], f_t[0]),
            TransformMatchingTex(group4[1], f_t[1]),
            TransformMatchingTex(group4[2], f_t[2])
        )

        qiu_c = VGroup(
            Tex(r"F(0)"),
            Tex("="),
            Tex(r"-\int_{0}^{1} \frac{d y}{y^{2}+1}+c")
        ).set_color(BLUE).arrange(RIGHT)

        qiu_c2 = VGroup(
            Tex(r"0"),
            Tex("="),
            Tex(r"-\frac{\pi}{4}+c")
        ).set_color(BLUE).arrange(RIGHT)

        f_t_copy = f_t.copy()
        self.play(f_t_copy.animate.next_to(f_t, 2*DOWN))
        qiu_c.next_to(f_t, 2*DOWN)
        qiu_c2.next_to(f_t, 2*DOWN)
        self.play(
            TransformMatchingTex(f_t_copy[0], qiu_c[0]),
            TransformMatchingTex(f_t_copy[1], qiu_c[1]),
            TransformMatchingTex(f_t_copy[2], qiu_c[2])
        )

        self.wait(1)

        self.play(
            TransformMatchingTex(qiu_c[0], qiu_c2[0]),
            TransformMatchingTex(qiu_c[1], qiu_c2[1]),
            TransformMatchingTex(qiu_c[2], qiu_c2[2])
        )
        self.wait(1)

        new_f_t2 = Tex(r"-\int_{0}^{1} \frac{e^{-t^2\left(y^{2}+1\right)}}{y^{2}+1} d y+\frac{\pi}{4}")
        new_f_t2.move_to(f_t[2].get_center()).set_color(BLUE)

        self.play(FadeOut(qiu_c2), TransformMatchingTex(f_t[2], new_f_t2))
        self.wait(1)

        f_t_group = VGroup(
            f_t[0],
            f_t[1],
            new_f_t2
        )

        self.play(FadeOut(group1[1]), FadeOut(group3), FadeOut(group1[0][0]))

        f_inf_group = VGroup(
            Tex(
                r"\lim_{t\to+\infty} {F(t)}", "=",
                r"-\lim_{t\to+\infty} \int_{0}^{1} \frac{e^{-t^2\left(y^{2}+1\right)}}{y^{2}+1} d y+\frac{\pi}{4}"
            ),
            Tex(
                r"\lim_{t\to+\infty} {F(t)}", "=",
                r"-\int_{0}^{1} \frac{0}{y^{2}+1} d y+\frac{\pi}{4}"
            ),
            Tex(
                r"\lim_{t\to+\infty} {F(t)}", "=",
                r"0+\frac{\pi}{4}"
            ),
            Tex(
                r"\lim_{t\to+\infty} {F(t)}", "=",
                r"\frac{\pi}{4}"
            ),
            Tex(
                r"\left[\int_{0}^{+\infty} e^{-x^{2}} d x\right]^{2}",
                "=",
                r"\frac{\pi}{4}"
            ),
            Tex(
                r"\int_{0}^{+\infty} e^{-x^{2}} d x",
                "=",
                r"\sqrt{\frac{\pi}{4}}"
            ),
            Tex(
                r"\int_{0}^{+\infty} e^{-x^{2}} d x",
                "=",
                r"\frac {\sqrt{\pi}} {2}"
            )
        ).set_color(BLUE)

        self.play(TransformMatchingShapes(f_t_group, f_inf_group[0]))
        self.wait(1)

        for i in range(1, 7):
            self.play(TransformMatchingTex(f_inf_group[i-1], f_inf_group[i]))
            if i == 4:
                self.play(FadeOut(group1[0][1]))
            self.wait(1)

        rect = SurroundingRectangle(f_inf_group[6], buff=0.05, color=YELLOW)
        self.play(Write(rect))
        self.play(
            f_inf_group[6].animate.scale(2).set_color_by_gradient(BLUE, YELLOW, RED),
            rect.animate.scale(2),
            FadeOut(gauss_int),
            FadeOut(title)
        )
        self.wait(1)

        xiexie = Text("谢谢观看", font="KaiTi", font_size=140).set_color_by_gradient(BLUE, YELLOW, RED)
        self.play(
            ReplacementTransform(f_inf_group[6], xiexie),
            FadeOut(rect)
        )
