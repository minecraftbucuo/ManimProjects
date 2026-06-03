from manim import *


class ExponentialLineMaximumProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        cover_text_1 = Text("已知对任意", font="KaiTi", font_size=30)
        cover_math_1 = MathTex(r"x\in\mathbb{R}", font_size=36).set_color(BLUE)
        cover_text_2 = Text("，有", font="KaiTi", font_size=30)
        cover_line_1 = VGroup(cover_text_1, cover_math_1, cover_text_2).arrange(RIGHT, buff=0.1)

        cover_line_2 = MathTex(r"e^x\geq ax+b", font_size=58).set_color(BLUE)

        cover_text_3 = Text("求", font="KaiTi", font_size=30)
        cover_math_2 = MathTex(r"a+b", font_size=38).set_color(YELLOW)
        cover_text_4 = Text("的最大值。", font="KaiTi", font_size=30)
        cover_line_3 = VGroup(cover_text_3, cover_math_2, cover_text_4).arrange(RIGHT, buff=0.1)

        cover = VGroup(cover_line_1, cover_line_2, cover_line_3).arrange(DOWN, buff=0.42)
        self.play(FadeIn(cover_line_1, shift=UP))
        self.play(FadeIn(cover_line_2, shift=UP))
        self.play(FadeIn(cover_line_3, shift=UP))

        # ==================== 3秒倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=180)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.move_to(ORIGIN)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：看清所求量 ====================
        desc_1 = Text("先把所求量和题设中的直线联系起来。", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_orig = MathTex(r"e^x\geq ax+b", font_size=52).set_color(BLUE).next_to(desc_1, DOWN, buff=0.45)
        self.play(Write(eq_orig))
        self.wait(1)

        desc_2_text_1 = Text("当", font="KaiTi", font_size=28)
        desc_2_math_1 = MathTex(r"x=1", font_size=34).set_color(YELLOW)
        desc_2_text_2 = Text("时，直线的值就是", font="KaiTi", font_size=28)
        desc_2_math_2 = MathTex(r"a+b", font_size=34).set_color(YELLOW)
        desc_2 = VGroup(desc_2_text_1, desc_2_math_1, desc_2_text_2, desc_2_math_2).arrange(RIGHT, buff=0.08)
        desc_2.next_to(eq_orig, DOWN, buff=0.55)
        self.play(Write(desc_2))

        eq_value = MathTex(r"ax+b\big|_{x=1}=a+b", font_size=44).set_color(GREEN).next_to(desc_2, DOWN, buff=0.32)
        self.play(Write(eq_value))
        self.wait(1.5)

        self.play(FadeOut(desc_1), FadeOut(desc_2))
        self.play(VGroup(eq_orig, eq_value).animate.to_edge(UP, buff=0.75))

        # ==================== 第二幕：先求出上界 ====================
        desc_3_text_1 = Text("由于不等式对任意", font="KaiTi", font_size=28)
        desc_3_math_1 = MathTex(r"x", font_size=34).set_color(YELLOW)
        desc_3_text_2 = Text("都成立，所以可以取", font="KaiTi", font_size=28)
        desc_3_math_2 = MathTex(r"x=1", font_size=34).set_color(YELLOW)
        desc_3 = VGroup(desc_3_text_1, desc_3_math_1, desc_3_text_2, desc_3_math_2).arrange(RIGHT, buff=0.08)
        desc_3.next_to(eq_value, DOWN, buff=0.6)
        self.play(Write(desc_3))

        eq_upper_1 = MathTex(r"e=e^1\geq a+b", font_size=44).set_color(YELLOW).next_to(desc_3, DOWN, buff=0.32)
        self.play(Write(eq_upper_1))
        self.wait(1.2)

        desc_4 = Text("因此立刻得到上界。", font="KaiTi", font_size=28).next_to(eq_upper_1, DOWN, buff=0.5)
        self.play(Write(desc_4))

        eq_upper_2 = MathTex(r"a+b\leq e", font_size=48).set_color(GREEN).next_to(desc_4, DOWN, buff=0.32)
        rect_upper = SurroundingRectangle(eq_upper_2, color=GREEN, buff=0.16)
        self.play(Write(eq_upper_2))
        self.play(Create(rect_upper))
        self.wait(2)

        self.play(
            FadeOut(eq_orig), FadeOut(eq_value), FadeOut(desc_3), FadeOut(eq_upper_1), FadeOut(desc_4)
        )
        upper_group = VGroup(eq_upper_2, rect_upper)
        self.play(upper_group.animate.to_edge(UP, buff=0.8))

        # ==================== 第三幕：讨论怎样取到上界 ====================
        desc_5 = Text("下面讨论这个上界能否取到。", font="KaiTi", font_size=30).next_to(upper_group, DOWN, buff=0.55)
        self.play(Write(desc_5))

        desc_6_text_1 = Text("若要", font="KaiTi", font_size=28)
        desc_6_math_1 = MathTex(r"a+b=e", font_size=34).set_color(YELLOW)
        desc_6_text_2 = Text("，则直线必须经过点", font="KaiTi", font_size=28)
        desc_6_math_2 = MathTex(r"(1,e)", font_size=34).set_color(YELLOW)
        desc_6 = VGroup(desc_6_text_1, desc_6_math_1, desc_6_text_2, desc_6_math_2).arrange(RIGHT, buff=0.08)
        desc_6.next_to(desc_5, DOWN, buff=0.32)
        self.play(Write(desc_6))
        self.wait(1.2)

        self.play(FadeOut(desc_5))
        self.play(desc_6.animate.next_to(upper_group, DOWN, buff=0.5))

        desc_7_text_1 = Text("同时还要满足", font="KaiTi", font_size=28)
        desc_7_math_1 = MathTex(r"ax+b\leq e^x", font_size=34).set_color(BLUE)
        desc_7_text_2 = Text("对任意", font="KaiTi", font_size=28)
        desc_7_math_2 = MathTex(r"x", font_size=34).set_color(BLUE)
        desc_7_text_3 = Text("成立。", font="KaiTi", font_size=28)
        desc_7 = VGroup(desc_7_text_1, desc_7_math_1, desc_7_text_2, desc_7_math_2, desc_7_text_3).arrange(
            RIGHT, buff=0.08
        )
        desc_7.next_to(desc_6, DOWN, buff=0.38)
        self.play(Write(desc_7))
        self.wait(1.5)

        desc_8 = Text("因此最自然的选择是取曲线在该点处的切线。", font="KaiTi", font_size=28).next_to(
            desc_7, DOWN, buff=0.4
        )
        self.play(Write(desc_8))
        self.wait(1.8)

        self.play(FadeOut(desc_6), FadeOut(desc_7), FadeOut(desc_8))

        # ==================== 第四幕：求出切线 ====================
        desc_9_text_1 = Text("考虑函数", font="KaiTi", font_size=30)
        desc_9_math_1 = MathTex(r"y=e^x", font_size=38).set_color(BLUE)
        desc_9_text_2 = Text("在", font="KaiTi", font_size=30)
        desc_9_math_2 = MathTex(r"x=1", font_size=38).set_color(YELLOW)
        desc_9_text_3 = Text("处的切线。", font="KaiTi", font_size=30)
        desc_9 = VGroup(desc_9_text_1, desc_9_math_1, desc_9_text_2, desc_9_math_2, desc_9_text_3).arrange(
            RIGHT, buff=0.08
        )
        desc_9.next_to(upper_group, DOWN, buff=0.55)
        self.play(Write(desc_9))

        eq_derivative = MathTex(r"(e^x)'=e^x,\qquad (e^x)'|_{x=1}=e", font_size=38).next_to(desc_9, DOWN, buff=0.3)
        self.play(Write(eq_derivative))
        self.wait(1.2)

        self.play(FadeOut(desc_9))
        self.play(eq_derivative.animate.next_to(upper_group, DOWN, buff=0.5))

        desc_10 = Text("所以切线的斜率是 e 。", font="KaiTi", font_size=28).next_to(eq_derivative, DOWN, buff=0.38)
        self.play(Write(desc_10))

        eq_tangent = MathTex(r"y=e(x-1)+e=ex", font_size=40).set_color(GREEN).next_to(desc_10, DOWN, buff=0.28)
        self.play(Write(eq_tangent))
        self.wait(2)

        self.play(FadeOut(eq_derivative), FadeOut(desc_10))
        self.play(eq_tangent.animate.next_to(upper_group, DOWN, buff=0.55))

        # ==================== 第五幕：得到 a 和 b ====================
        desc_11 = Text("这条切线就是符合条件的最佳直线。", font="KaiTi", font_size=28).next_to(
            eq_tangent, DOWN, buff=0.45
        )
        self.play(Write(desc_11))

        eq_ab = MathTex(r"ax+b=ex", font_size=38).next_to(desc_11, DOWN, buff=0.28)
        self.play(Write(eq_ab))
        self.wait(1.2)

        self.play(FadeOut(desc_11))
        self.play(eq_ab.animate.next_to(eq_tangent, DOWN, buff=0.38))

        desc_12 = Text("对比系数可得：", font="KaiTi", font_size=26).next_to(eq_ab, DOWN, buff=0.35)
        self.play(Write(desc_12))

        eq_coeff = MathTex(r"a=e,\qquad b=0", font_size=40).set_color(YELLOW).next_to(desc_12, DOWN, buff=0.28)
        self.play(Write(eq_coeff))
        self.wait(2)

        self.play(FadeOut(upper_group), FadeOut(eq_tangent), FadeOut(eq_ab), FadeOut(desc_12))

        # ==================== 第六幕：验证并总结 ====================
        desc_13 = Text("下面验证原不等式确实成立。", font="KaiTi", font_size=30)
        desc_13.to_edge(UP, buff=0.8)
        self.play(Write(desc_13))

        eq_check_1 = MathTex(r"\varphi(x)=e^x-ex", font_size=40).next_to(desc_13, DOWN, buff=0.35)
        self.play(Write(eq_check_1))
        self.wait(1)

        eq_check_2 = MathTex(r"\varphi'(x)=e^x-e", font_size=40).next_to(eq_check_1, DOWN, buff=0.28)
        self.play(Write(eq_check_2))
        self.wait(1)

        self.play(FadeOut(desc_13), FadeOut(eq_check_1))
        self.play(eq_check_2.animate.to_edge(UP, buff=0.8))

        desc_14 = Text("由导数符号可知：", font="KaiTi", font_size=28)
        desc_14.next_to(eq_check_2, DOWN, buff=0.45)
        self.play(Write(desc_14))

        eq_check_3 = MathTex(
            r"x<1\Rightarrow \varphi'(x)<0,\qquad x>1\Rightarrow \varphi'(x)>0",
            font_size=32
        ).next_to(desc_14, DOWN, buff=0.32)
        self.play(Write(eq_check_3))
        self.wait(1.5)

        self.play(FadeOut(desc_14))
        self.play(eq_check_3.animate.next_to(eq_check_2, DOWN, buff=0.4))

        desc_15_text_1 = Text("所以", font="KaiTi", font_size=28)
        desc_15_math_1 = MathTex(r"\varphi(x)", font_size=34).set_color(YELLOW)
        desc_15_text_2 = Text("在", font="KaiTi", font_size=28)
        desc_15_math_2 = MathTex(r"x=1", font_size=34).set_color(YELLOW)
        desc_15_text_3 = Text("处取最小值。", font="KaiTi", font_size=28)
        desc_15 = VGroup(
            desc_15_text_1, desc_15_math_1, desc_15_text_2, desc_15_math_2, desc_15_text_3
        ).arrange(RIGHT, buff=0.08)
        desc_15.next_to(eq_check_3, DOWN, buff=0.38)
        self.play(Write(desc_15))

        eq_check_4 = MathTex(r"\varphi(1)=e-e=0", font_size=38).set_color(GREEN).next_to(desc_15, DOWN, buff=0.28)
        self.play(Write(eq_check_4))
        self.wait(1.2)

        self.play(FadeOut(eq_check_2), FadeOut(eq_check_3), FadeOut(desc_15))
        self.play(eq_check_4.animate.to_edge(UP, buff=0.8))

        desc_16 = Text("因此", font="KaiTi", font_size=28)
        eq_check_5 = MathTex(r"\varphi(x)\geq 0", font_size=36).set_color(GREEN)
        desc_17 = Text("，也就是", font="KaiTi", font_size=28)
        eq_check_6 = MathTex(r"e^x\geq ex", font_size=36).set_color(GREEN)
        line_result = VGroup(desc_16, eq_check_5, desc_17, eq_check_6).arrange(RIGHT, buff=0.08)
        line_result.next_to(eq_check_4, DOWN, buff=0.42)
        self.play(Write(line_result))
        self.wait(2)

        self.play(
            FadeOut(eq_coeff), FadeOut(eq_check_4), FadeOut(line_result)
        )

        # ==================== 第七幕：最终结论 ====================
        desc_18 = Text("上界能够取到，因此最大值就是 e 。", font="KaiTi", font_size=30)
        desc_18.to_edge(UP, buff=0.9)
        self.play(Write(desc_18))

        final_cond = MathTex(r"a=e,\qquad b=0", font_size=44).set_color(GREEN).next_to(desc_18, DOWN, buff=0.4)
        self.play(Write(final_cond))

        final_ans = MathTex(r"\boxed{\max(a+b)=e}", font_size=50).set_color(YELLOW).next_to(final_cond, DOWN, buff=0.45)
        self.play(FadeIn(final_ans, shift=UP))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)
