# -*- coding: utf-8 -*-
# @Time    : 2026/3/29 23:18
# @Author  : MINEC
# @File    : 含参积分求解1.py
# @Software: PyCharm
from manimlib import *


class FrullaniIntegral(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("费 曼 积 分 法", font="KaiTi", font_size=90)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW)

        integral = Tex(r"\int_0^1 \frac{x^b - x^a}{\ln x} dx \,=\, ?", font_size=60)
        integral.set_color_by_gradient(GREEN, BLUE, YELLOW)

        cover = VGroup(title, integral).arrange(DOWN)
        title.shift(UP)
        self.play(Write(title))
        integral.move_to(DOWN)
        self.play(Write(integral))
        self.wait(1)

        self.play(
            title.animate.scale(0.45).to_corner(UL),
            integral.animate.scale(0.6).to_corner(UR),
        )
        self.wait(1)

        # ==================== 第一步：定义含参积分 ====================
        group1 = VGroup(
            VGroup(
                Text("令", font="KaiTi", font_size=50),
                Tex(r"I(t)=\int_0^1 \frac{x^t - 1}{\ln x} dx")
            ).arrange(RIGHT),
            VGroup(
                Text("则", font="KaiTi", font_size=50),
                Tex(r"? \, = \, I(b)-I(a)")
            ).arrange(RIGHT)
        )
        group1.arrange(RIGHT).set_color(BLUE)
        group1[0].shift(LEFT * 0.25)
        group1[1].shift(RIGHT * 0.25)
        group1[1].shift(DOWN * 0.1)

        self.play(Write(group1[0]))
        self.wait(1)
        self.play(Write(group1[1]))
        self.wait(1)

        self.play(group1.animate.scale(0.7).shift(UP * 2))
        self.wait(1)

        # ==================== 第二步：对 I(t) 求导 ====================
        group2 = VGroup(
            VGroup(Tex(r"I'(t)"), Tex(r"=")).arrange(RIGHT),
            Tex(r"\frac{d}{dt} \int_0^1 \frac{x^t - 1}{\ln x} dx"),
            Tex(r"\int_0^1 \frac{\partial}{\partial t} \left( \frac{x^t - 1}{\ln x} \right) dx"),
            Tex(r"\int_0^1 \frac{x^t \ln x}{\ln x} dx"),
            Tex(r"\int_0^1 x^t dx"),
            Tex(r"\frac{1}{t+1}")
        ).set_color(BLUE)

        for i in group2:
            i.move_to(ORIGIN)

        self.play(Write(group2[0]))
        self.wait(0.6)

        group2_00_copy = group2[0][0].copy()

        self.play(
            group2_00_copy.animate.shift(5 * LEFT),
            group2[0][1].animate.shift(5 * LEFT)
        )
        self.play(TransformMatchingTex(group2[0][0], group2[1]))
        self.wait(1)

        for i in range(2, 4):
            self.play(TransformMatchingTex(group2[i - 1], group2[i]))
            self.wait(1)

        self.play(TransformMatchingTex(group2[3], group2[4]))
        self.wait(1)

        self.play(TransformMatchingShapes(group2[4], group2[5]))
        self.wait(1)

        # 组装 I'(t) = 1/(t+1)
        group3 = VGroup(group2_00_copy, group2[0][1], group2[5])
        self.play(group3.animate.arrange(RIGHT))

        # ==================== 第三步：积分求 I(t) ====================
        i_t_with_c = VGroup(
            Tex(r"I(t)"),
            Tex(r"="),
            Tex(r"\ln(t+1) + C")
        ).set_color(BLUE).arrange(RIGHT)

        self.play(
            TransformMatchingTex(group3[0], i_t_with_c[0]),
            TransformMatchingTex(group3[1], i_t_with_c[1]),
            TransformMatchingTex(group3[2], i_t_with_c[2])
        )
        self.wait(1)

        # ==================== 第四步：由 I(0)=0 求 C ====================
        qiu_c1 = VGroup(
            Tex(r"I(0)"), Tex(r"="), Tex(r"\ln(1) + C")
        ).set_color(BLUE).arrange(RIGHT)

        qiu_c2 = VGroup(
            Tex(r"0"), Tex(r"="), Tex(r"0 + C")
        ).set_color(BLUE).arrange(RIGHT)

        qiu_c3 = VGroup(
            Tex(r"C"), Tex(r"="), Tex(r"0")
        ).set_color(BLUE).arrange(RIGHT)

        i_t_copy = i_t_with_c.copy()
        self.play(i_t_copy.animate.next_to(i_t_with_c, 2 * DOWN))
        qiu_c1.next_to(i_t_with_c, 2 * DOWN)
        qiu_c2.next_to(i_t_with_c, 2 * DOWN)
        qiu_c3.next_to(i_t_with_c, 2 * DOWN)

        self.play(
            TransformMatchingTex(i_t_copy[0], qiu_c1[0]),
            TransformMatchingTex(i_t_copy[1], qiu_c1[1]),
            TransformMatchingTex(i_t_copy[2], qiu_c1[2])
        )
        self.wait(1)

        self.play(
            TransformMatchingTex(qiu_c1[0], qiu_c2[0]),
            TransformMatchingTex(qiu_c1[1], qiu_c2[1]),
            TransformMatchingTex(qiu_c1[2], qiu_c2[2])
        )
        self.wait(1)

        self.play(
            TransformMatchingTex(qiu_c2[0], qiu_c3[0]),
            TransformMatchingTex(qiu_c2[1], qiu_c3[1]),
            TransformMatchingTex(qiu_c2[2], qiu_c3[2])
        )
        self.wait(1)

        # 更新 I(t)，去掉 +C
        new_i_t_rhs = Tex(r"\ln(t+1)")
        new_i_t_rhs.move_to(i_t_with_c[2].get_center()).set_color(BLUE)

        self.play(FadeOut(qiu_c3), TransformMatchingTex(i_t_with_c[2], new_i_t_rhs))
        self.wait(1)

        i_t_final = VGroup(i_t_with_c[0], i_t_with_c[1], new_i_t_rhs)

        # ==================== 第五步：回代得最终结果 ====================
        self.play(FadeOut(group1[1]))

        sub_title = Text("回 代 ：", font="KaiTi", font_size=50).set_color(BLUE)
        sub_title.next_to(i_t_final, DOWN, buff=0.6).align_to(i_t_final, LEFT)
        self.play(Write(sub_title))
        self.wait(0.5)

        sub1 = Tex(r"I(b) - I(a) = \ln(b+1) - \ln(a+1)").set_color(BLUE)
        sub1.next_to(sub_title, RIGHT, buff=0.3)

        sub2 = Tex(r"I(b) - I(a) = \ln\left(\frac{b+1}{a+1}\right)").set_color(BLUE)
        sub2.move_to(sub1.get_center())

        self.play(Write(sub1))
        self.wait(1)
        self.play(TransformMatchingShapes(sub1, sub2))
        self.wait(1)

        # 清理并显示最终结果
        self.play(
            FadeOut(sub2),
            FadeOut(sub_title),
            FadeOut(group1[0]),
            FadeOut(i_t_final)
        )

        final = Tex(
            r"\int_0^1 \frac{x^b - x^a}{\ln x} dx = \ln\left(\frac{b+1}{a+1}\right)"
        ).set_color(BLUE)

        self.play(Write(final))
        self.wait(1)

        # 高亮放大
        rect = SurroundingRectangle(final, buff=0.05, color=YELLOW)
        self.play(Write(rect))
        self.play(
            final.animate.scale(2).set_color_by_gradient(BLUE, YELLOW, RED),
            rect.animate.scale(2),
            FadeOut(integral),
            FadeOut(title)
        )
        self.wait(1)

        xiexie = Text("谢谢观看", font="KaiTi", font_size=140).set_color_by_gradient(BLUE, YELLOW, RED)
        self.play(
            ReplacementTransform(final, xiexie),
            FadeOut(rect)
        )