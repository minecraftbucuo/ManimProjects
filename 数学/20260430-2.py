from manim import *


class FactorialModuloProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("如何计算这个巨大的数的余数？", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"2026! \pmod{2027}",
            font_size=60
        ).set_color(BLUE)

        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))
        # ==================== 3秒高燃倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=180)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.move_to(ORIGIN)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：观察数字关系 ====================
        desc_1_text1 = Text("观察这两个数，暗藏玄坤：", font="KaiTi", font_size=30)
        desc_1_math1 = MathTex(r"2026", font_size=32).set_color(YELLOW)
        desc_1_math2 = MathTex(r"=", font_size=32)
        desc_1_math3 = MathTex(r"2027", font_size=32).set_color(YELLOW)
        desc_1_math4 = MathTex(r"- 1", font_size=32)
        desc_1 = VGroup(desc_1_text1, desc_1_math1, desc_1_math2, desc_1_math3, desc_1_math4).arrange(RIGHT, buff=0.05)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_orig = MathTex(r"2026! \pmod{2027}").set_color(BLUE).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(eq_orig))
        self.wait(1)

        desc_2 = Text("把关系代入，结构瞬间浮现：", font="KaiTi", font_size=28).next_to(eq_orig, DOWN, buff=0.5)
        self.play(Write(desc_2))

        eq_struct_1 = MathTex(r"(2027 - 1)! \pmod{2027}").set_color(GREEN).next_to(desc_2, DOWN, buff=0.3)
        self.play(ReplacementTransform(eq_orig.copy(), eq_struct_1))
        self.wait(1.5)

        desc_3_text1 = Text("抽象出一般形式，令", font="KaiTi", font_size=28)
        desc_3_math1 = MathTex(r"p = 2027", font_size=30).set_color(RED)
        desc_3 = VGroup(desc_3_text1, desc_3_math1).arrange(RIGHT, buff=0.1).next_to(eq_struct_1, DOWN, buff=0.5)
        self.play(Write(desc_3))

        eq_struct_2 = MathTex(r"(p-1)! \pmod p").scale(1.1).set_color(RED).next_to(desc_3, DOWN, buff=0.3)
        self.play(TransformMatchingTex(eq_struct_1.copy(), eq_struct_2))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(desc_1), FadeOut(eq_orig), FadeOut(desc_2), FadeOut(eq_struct_1), FadeOut(desc_3)
        )
        self.play(eq_struct_2.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：素数与威尔逊定理 ====================
        desc_4_text1 = Text("这种结构，指向数论中最优雅的定理", font="KaiTi", font_size=30)
        desc_4 = VGroup(desc_4_text1).arrange(RIGHT, buff=0.1).next_to(eq_struct_2, DOWN, buff=0.8)
        self.play(Write(desc_4))

        desc_5_text1 = Text("前提是", font="KaiTi", font_size=28)
        desc_5_math1 = MathTex(r"p", font_size=30).set_color(RED)
        desc_5_text2 = Text("必须为素数", font="KaiTi", font_size=28)
        desc_5 = VGroup(desc_5_text1, desc_5_math1, desc_5_text2).arrange(RIGHT, buff=0.05).next_to(desc_4, DOWN, buff=0.3)
        self.play(Write(desc_5))

        desc_6_text1 = Text("验证可知", font="KaiTi", font_size=28)
        desc_6_math1 = MathTex(r"2027", font_size=30).set_color(YELLOW)
        desc_6_text2 = Text("正是素数", font="KaiTi", font_size=28)
        desc_6 = VGroup(desc_6_text1, desc_6_math1, desc_6_text2).arrange(RIGHT, buff=0.05).next_to(desc_5, DOWN, buff=0.3)
        self.play(Write(desc_6))
        self.wait(1)

        desc_7 = Text("有请威尔逊定理（Wilson's Theorem）登场：", font="KaiTi", font_size=28).next_to(desc_6, DOWN, buff=0.5)
        self.play(Write(desc_7))

        eq_wilson = MathTex(r"(p-1)! \equiv -1 \pmod p").scale(1.2).set_color(YELLOW).next_to(desc_7, DOWN, buff=0.4)
        self.play(Write(eq_wilson))

        rect_wilson = SurroundingRectangle(eq_wilson, color=YELLOW, buff=0.15)
        self.play(Create(rect_wilson))
        self.wait(2)

        # 再次整理屏幕
        self.play(
            FadeOut(desc_4), FadeOut(desc_5), FadeOut(desc_6), FadeOut(desc_7)
        )
        wilson_group = VGroup(eq_wilson, rect_wilson)
        self.play(wilson_group.animate.move_to(UP * 2))
        self.play(eq_struct_2.animate.next_to(wilson_group, UP, buff=0.5))

        # ==================== 第三幕：代入与余数转化 ====================
        desc_8_text1 = Text("将", font="KaiTi", font_size=30)
        desc_8_math1 = MathTex(r"p = 2027", font_size=32).set_color(RED)
        desc_8_text2 = Text("直接代入定理：", font="KaiTi", font_size=30)
        desc_8 = VGroup(desc_8_text1, desc_8_math1, desc_8_text2).arrange(RIGHT, buff=0.05).next_to(wilson_group, DOWN, buff=0.8)
        self.play(Write(desc_8))

        eq_calc_1 = MathTex(r"2026! \equiv -1 \pmod{2027}").set_color(BLUE).next_to(desc_8, DOWN, buff=0.5)
        self.play(Write(eq_calc_1))
        self.wait(1.5)

        desc_9_text1 = Text("余数通常要求非负，只需加上模数", font="KaiTi", font_size=28)
        desc_9_math1 = MathTex(r"2027", font_size=30).set_color(GREEN)
        desc_9 = VGroup(desc_9_text1, desc_9_math1).arrange(RIGHT, buff=0.05).next_to(eq_calc_1, DOWN, buff=0.5)
        self.play(Write(desc_9))

        eq_calc_2 = MathTex(r"-1 + 2027 = 2026").set_color(GREEN).next_to(desc_9, DOWN, buff=0.3)
        self.play(Write(eq_calc_2))
        self.wait(1)

        desc_10_text1 = Text("所以余数为", font="KaiTi", font_size=35)
        desc_10_math1 = MathTex(r"2026", font_size=40).set_color(RED)
        desc_10 = VGroup(desc_10_text1, desc_10_math1).arrange(RIGHT, buff=0.1).next_to(eq_calc_2, DOWN, buff=0.6)
        self.play(Write(desc_10))
        self.wait(2)

        # 全屏暴力清场，绝对不往下叠加了
        self.play(
            FadeOut(eq_struct_2), FadeOut(wilson_group), FadeOut(desc_8), FadeOut(eq_calc_1),
            FadeOut(desc_9), FadeOut(eq_calc_2), FadeOut(desc_10)
        )

        # ==================== 第四幕：揭秘威尔逊定理 ====================
        desc_11 = Text("为什么威尔逊定理成立？直觉是：配对消元", font="KaiTi", font_size=35).to_edge(UP, buff=1)
        self.play(Write(desc_11))
        self.wait(1.5)

        desc_12_text1 = Text("在模", font="KaiTi", font_size=28)
        desc_12_math1 = MathTex(r"2027", font_size=30).set_color(YELLOW)
        desc_12_text2 = Text("的世界里，中间项两两配对互为逆元，例如", font="KaiTi", font_size=28)
        desc_12 = VGroup(desc_12_text1, desc_12_math1, desc_12_text2).arrange(RIGHT, buff=0.05).next_to(desc_11, DOWN, buff=0.8)
        self.play(Write(desc_12))

        eq_pair = MathTex(r"2 \times 1014 \equiv 1 \pmod{2027}").set_color(GREEN).next_to(desc_12, DOWN, buff=0.4)
        self.play(Write(eq_pair))
        self.wait(1)

        desc_13 = Text("所有中间对相乘全消成 1，只剩首尾两项：", font="KaiTi", font_size=28).next_to(eq_pair, DOWN, buff=0.5)
        self.play(Write(desc_13))

        eq_final_logic = MathTex(r"2026! \equiv 1 \times 2026 \equiv -1 \pmod{2027}").set_color(YELLOW).next_to(desc_13, DOWN, buff=0.3)
        self.play(Write(eq_final_logic))

        self.wait(3)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)