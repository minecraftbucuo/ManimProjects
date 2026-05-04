from manim import *


class CompositeNumberProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("如何证明这个数是合数？", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"10^{100} + 1",
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

        # ==================== 第一幕：寻找灵感 ====================
        desc_1_text1 = Text("遇到次方加", font="KaiTi", font_size=30)
        desc_1_math = MathTex(r"1", font_size=32).set_color(YELLOW)
        desc_1_text2 = Text("，本能想到因式分解：", font="KaiTi", font_size=30)
        desc_1 = VGroup(desc_1_text1, desc_1_math, desc_1_text2).arrange(RIGHT, buff=0.05)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_cubic = MathTex(r"a^3 + 1 = (a+1)(a^2 - a + 1)").set_color(GREEN).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(eq_cubic))
        self.wait(1)

        desc_2_text1 = Text("推广到奇数次方，都能提取出", font="KaiTi", font_size=28)
        desc_2_math = MathTex(r"(a+1)", font_size=30).set_color(YELLOW)
        desc_2 = VGroup(desc_2_text1, desc_2_math).arrange(RIGHT, buff=0.05).next_to(eq_cubic, DOWN, buff=0.5)
        self.play(Write(desc_2))

        eq_odd = MathTex(r"a^n + 1 = (a+1)(a^{n-1} - a^{n-2} + \dots - a + 1)").set_color(GREEN).next_to(desc_2, DOWN,
                                                                                                         buff=0.3)
        self.play(Write(eq_odd))
        self.wait(1)

        desc_3_text1 = Text("只要指数", font="KaiTi", font_size=28)
        desc_3_math1 = MathTex(r"n", font_size=30).set_color(RED)
        desc_3_text2 = Text("是奇数，它就必为合数！", font="KaiTi", font_size=28)
        desc_3 = VGroup(desc_3_text1, desc_3_math1, desc_3_text2).arrange(RIGHT, buff=0.05).next_to(eq_odd, DOWN,
                                                                                                    buff=0.5)
        self.play(Write(desc_3))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(desc_1), FadeOut(eq_cubic), FadeOut(desc_2), FadeOut(eq_odd)
        )
        self.play(desc_3.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：转化偶数次方 ====================
        desc_4_text1 = Text("回到原题，指数", font="KaiTi", font_size=30)
        desc_4_math1 = MathTex(r"100", font_size=32).set_color(RED)
        desc_4_text2 = Text("是偶数，怎么办？", font="KaiTi", font_size=30)
        desc_4 = VGroup(desc_4_text1, desc_4_math1, desc_4_text2).arrange(RIGHT, buff=0.05).next_to(desc_3, DOWN,
                                                                                                    buff=0.8)
        self.play(Write(desc_4))

        eq_orig = MathTex(r"10^{100} + 1").set_color(BLUE).next_to(desc_4, DOWN, buff=0.5)
        self.play(Write(eq_orig))
        self.wait(1.5)

        desc_5_text1 = Text("整体偶数，那就拆出奇数因子！让新的指数变奇数：", font="KaiTi", font_size=28).next_to(eq_orig,
                                                                                                               DOWN,
                                                                                                               buff=0.5)
        self.play(Write(desc_5_text1))

        eq_split = MathTex(r"100 = 4 \times 25").set_color(YELLOW).next_to(desc_5_text1, DOWN, buff=0.3)
        self.play(Write(eq_split))
        self.wait(1)

        desc_6_text1 = Text("把底数包进去，强行构造奇数次方：", font="KaiTi", font_size=28).next_to(eq_split, DOWN,
                                                                                                  buff=0.4)
        self.play(Write(desc_6_text1))

        eq_transform = MathTex(r"10^{100} + 1 = (10^4)^{25} + 1").set_color(YELLOW).next_to(desc_6_text1, DOWN,
                                                                                            buff=0.3)
        self.play(TransformMatchingTex(eq_orig.copy(), eq_transform))
        self.wait(2)

        # 再次整理屏幕
        self.play(
            FadeOut(desc_3), FadeOut(desc_4), FadeOut(eq_orig), FadeOut(desc_5_text1),
            FadeOut(eq_split), FadeOut(desc_6_text1)
        )
        self.play(eq_transform.animate.to_edge(UP, buff=0.8))

        # ==================== 第三幕：换元与核心 ====================
        desc_7_text1 = Text("为了看清结构，令", font="KaiTi", font_size=30)
        desc_7_math1 = MathTex(r"x = 10^4", font_size=32).set_color(GREEN)
        desc_7 = VGroup(desc_7_text1, desc_7_math1).arrange(RIGHT, buff=0.1).next_to(eq_transform, DOWN, buff=0.8)
        self.play(Write(desc_7))

        eq_sub = MathTex(r"x^{25} + 1").scale(1.2).set_color(GREEN).next_to(desc_7, DOWN, buff=0.6)
        self.play(ReplacementTransform(eq_transform.copy(), eq_sub))
        self.wait(1.5)

        desc_8_text1 = Text("完美契合奇数次方公式，直接因式分解：", font="KaiTi", font_size=28).next_to(eq_sub, DOWN,
                                                                                                      buff=0.5)
        self.play(Write(desc_8_text1))

        eq_factor = MathTex(r"x^{25} + 1 = (x+1)(x^{24} - x^{23} + \dots - x + 1)").set_color(GREEN).next_to(
            desc_8_text1, DOWN, buff=0.3)
        self.play(Write(eq_factor))
        self.wait(2)

        # 大清场
        self.play(
            FadeOut(eq_transform), FadeOut(desc_7), FadeOut(eq_sub), FadeOut(desc_8_text1)
        )
        self.play(eq_factor.animate.move_to(UP * 1.5))

        # ==================== 第四幕：回代与结论 ====================
        desc_9_text1 = Text("把", font="KaiTi", font_size=30)
        desc_9_math1 = MathTex(r"x = 10^4", font_size=32).set_color(GREEN)
        desc_9_text2 = Text("代回分解式：", font="KaiTi", font_size=30)
        desc_9 = VGroup(desc_9_text1, desc_9_math1, desc_9_text2).arrange(RIGHT, buff=0.05).next_to(eq_factor, DOWN,
                                                                                                    buff=0.8)
        self.play(Write(desc_9))

        eq_final_1 = MathTex(r"10^{100} + 1 = (10^4 + 1)").set_color(BLUE).next_to(desc_9, DOWN, buff=0.5)
        eq_final_2 = MathTex(r"\times [(10^4)^{24} - (10^4)^{23} + \dots - 10^4 + 1]").set_color(BLUE).next_to(
            eq_final_1, DOWN, buff=0.2)
        self.play(Write(eq_final_1), Write(eq_final_2))
        self.wait(1.5)

        desc_10_text1 = Text("第一项", font="KaiTi", font_size=28)
        desc_10_math1 = MathTex(r"10^4 + 1 = 10001", font_size=30).set_color(YELLOW)
        desc_10_text2 = Text("，第二项也是正整数。", font="KaiTi", font_size=28)
        desc_10 = VGroup(desc_10_text1, desc_10_math1, desc_10_text2).arrange(RIGHT, buff=0.05).next_to(eq_final_2,
                                                                                                        DOWN, buff=0.5)
        self.play(Write(desc_10))
        self.wait(1)

        desc_11_text1 = Text("存在非", font="KaiTi", font_size=28)
        desc_11_math1 = MathTex(r"1", font_size=30).set_color(RED)
        desc_11_text2 = Text("和自身的因子，故必为合数！", font="KaiTi", font_size=28)
        desc_11 = VGroup(desc_11_text1, desc_11_math1, desc_11_text2).arrange(RIGHT, buff=0.05).next_to(desc_10, DOWN,
                                                                                                        buff=0.3)
        self.play(Write(desc_11))
        self.wait(2)

        # 全屏暴力清场
        self.play(
            FadeOut(eq_factor), FadeOut(desc_9), FadeOut(eq_final_1), FadeOut(eq_final_2),
            FadeOut(desc_10), FadeOut(desc_11)
        )

        # ==================== 散场 ====================
        outro_1_text1 = Text("证毕", font="KaiTi", font_size=60).set_color_by_gradient(RED, YELLOW).move_to(UP * 0.5)
        self.play(Write(outro_1_text1))
        self.wait(1.5)

        outro_2_text1 = Text("换个角度看，只要指数含有奇数因子", font="KaiTi", font_size=30).next_to(outro_1_text1, DOWN,
                                                                                                    buff=0.8)
        self.play(Write(outro_2_text1))

        outro_3_math1 = MathTex(r"a^n + 1", font_size=40).set_color(BLUE).next_to(outro_2_text1, DOWN, buff=0.4)
        self.play(FadeIn(outro_3_math1, shift=UP))
        self.wait(1)

        outro_4_text1 = Text("就注定是合数", font="KaiTi", font_size=45).set_color(GREEN).next_to(outro_3_math1, DOWN,
                                                                                                  buff=0.6)
        self.play(Write(outro_4_text1))
        self.wait(4)

        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)