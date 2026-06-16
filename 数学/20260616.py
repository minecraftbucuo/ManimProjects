from manim import *

class CauchyInequalityProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("条件极值求解：柯西不等式的应用", font="KaiTi", font_size=45)
        title.set_color(BLUE)

        cover_cond_text = Text("已知条件：", font="KaiTi", font_size=35)
        cover_cond_math = MathTex(r"a^2 + b^2 = 4", font_size=40).set_color(GREEN)
        cover_cond = VGroup(cover_cond_text, cover_cond_math).arrange(RIGHT, buff=0.2)

        cover_obj_text = Text("求代数式的最小值：", font="KaiTi", font_size=35)
        cover_obj_math = MathTex(r"\sqrt{20 - 8a} + \sqrt{8 + 4b}", font_size=40).set_color(YELLOW)
        cover_obj = VGroup(cover_obj_text, cover_obj_math).arrange(RIGHT, buff=0.2)

        cover = VGroup(title, cover_cond, cover_obj).arrange(DOWN, buff=0.8)
        cover.move_to(UP * 1)

        self.play(Write(title))
        self.play(FadeIn(cover_cond, shift=UP), FadeIn(cover_obj, shift=UP))

        # ==================== 3秒倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=120)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.next_to(cover, DOWN, buff=1.0)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：代数式配方 ====================
        desc_1 = Text("首先，利用已知条件对根号内部进行完全平方式的构造：", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        known_eq = MathTex(r"a^2 + b^2 = 4", font_size=36).set_color(GREEN).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(known_eq))
        self.wait(1)

        desc_2_text = Text("对于第一项", font="KaiTi", font_size=28)
        desc_2_math = MathTex(r"20 - 8a", font_size=30).set_color(YELLOW)
        desc_2_text2 = Text("，进行常数拆分并代入已知条件：", font="KaiTi", font_size=28)
        desc_2 = VGroup(desc_2_text, desc_2_math, desc_2_text2).arrange(RIGHT, buff=0.1).next_to(known_eq, DOWN, buff=0.5)
        self.play(Write(desc_2))

        eq_term1 = MathTex(r"20 - 8a = 16 - 8a + (a^2+b^2) = (4-a)^2 + (-b)^2", font_size=36)
        eq_term1.next_to(desc_2, DOWN, buff=0.3)
        self.play(Write(eq_term1))
        self.wait(1.5)

        desc_3_text = Text("同理，对于第二项", font="KaiTi", font_size=28)
        desc_3_math = MathTex(r"8 + 4b", font_size=30).set_color(YELLOW)
        desc_3_text2 = Text("：", font="KaiTi", font_size=28)
        desc_3 = VGroup(desc_3_text, desc_3_math, desc_3_text2).arrange(RIGHT, buff=0.1).next_to(eq_term1, DOWN, buff=0.5)
        self.play(Write(desc_3))

        eq_term2 = MathTex(r"8 + 4b = 4 + 4b + (a^2+b^2) = a^2 + (b+2)^2", font_size=36)
        eq_term2.next_to(desc_3, DOWN, buff=0.3)
        self.play(Write(eq_term2))
        self.wait(1.5)

        self.play(FadeOut(desc_1), FadeOut(known_eq), FadeOut(desc_2), FadeOut(desc_3))
        self.play(
            eq_term1.animate.to_edge(UP, buff=1.0),
            eq_term2.animate.next_to(eq_term1, DOWN, buff=0.5).to_edge(UP, buff=1.8)
        )

        desc_4_text = Text("此时，令原代数式为", font="KaiTi", font_size=28)
        desc_4_math = MathTex(r"E", font_size=30).set_color(BLUE)
        desc_4_text2 = Text("，其可等价变形为：", font="KaiTi", font_size=28)
        desc_4 = VGroup(desc_4_text, desc_4_math, desc_4_text2).arrange(RIGHT, buff=0.1).next_to(eq_term2, DOWN, buff=0.6)
        self.play(Write(desc_4))

        eq_E = MathTex(r"E = \sqrt{(4-a)^2 + (-b)^2} + \sqrt{a^2 + (b+2)^2}", font_size=40).set_color(BLUE)
        eq_E.next_to(desc_4, DOWN, buff=0.4)
        self.play(Write(eq_E))
        self.wait(2)

        self.play(FadeOut(eq_term1), FadeOut(eq_term2), FadeOut(desc_4))
        self.play(eq_E.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：引入柯西不等式并详细展开 ====================
        desc_5_text = Text("为了求", font="KaiTi", font_size=28)
        desc_5_math = MathTex(r"E", font_size=30).set_color(BLUE)
        desc_5_text2 = Text("的最小值，我们将等式两边平方：", font="KaiTi", font_size=28)
        desc_5 = VGroup(desc_5_text, desc_5_math, desc_5_text2).arrange(RIGHT, buff=0.1).next_to(eq_E, DOWN, buff=0.5)
        self.play(Write(desc_5))

        eq_E2 = MathTex(r"E^2 = (4-a)^2 + (-b)^2 + a^2 + (b+2)^2 + 2\sqrt{[(4-a)^2 + (-b)^2][a^2 + (b+2)^2]}", font_size=28)
        eq_E2.next_to(desc_5, DOWN, buff=0.4)
        self.play(Write(eq_E2))
        self.wait(1.5)

        desc_6 = Text("根据二维形式的柯西不等式，对包含根号的交叉项进行放缩：", font="KaiTi", font_size=28).next_to(eq_E2, DOWN, buff=0.6)
        self.play(Write(desc_6))

        eq_cauchy = MathTex(r"\sqrt{(x_1^2 + y_1^2)(x_2^2 + y_2^2)} \ge x_1x_2 + y_1y_2", font_size=36).set_color(GREEN)
        eq_cauchy.next_to(desc_6, DOWN, buff=0.4)
        self.play(Write(eq_cauchy))
        self.wait(2)

        # 彻底清场，为详细的代数重组留出全屏空间
        self.play(
            FadeOut(eq_E), FadeOut(desc_5), FadeOut(eq_E2), 
            FadeOut(desc_6), FadeOut(eq_cauchy)
        )

        desc_7 = Text("将柯西不等式的放缩结果代回原展开式：", font="KaiTi", font_size=30).to_edge(UP, buff=0.8)
        self.play(Write(desc_7))

        eq_subst = MathTex(
            r"E^2 \ge (4-a)^2 + (-b)^2 + a^2 + (b+2)^2 + 2[(4-a)a + (-b)(b+2)]", 
            font_size=32
        ).next_to(desc_7, DOWN, buff=0.5)
        self.play(Write(eq_subst))
        self.wait(2)

        desc_8 = Text("将常数2分配进括号，并依变量相关性重新分组：", font="KaiTi", font_size=30).next_to(eq_subst, DOWN, buff=0.6)
        self.play(Write(desc_8))

        # 将公式切片，通过独立上色清晰展示两组完全平方式的渊源
        eq_group = MathTex(
            r"E^2 \ge ", 
            r"[(4-a)^2 + 2(4-a)a + a^2]", 
            r" + ", 
            r"[(-b)^2 + 2(-b)(b+2) + (b+2)^2]", 
            font_size=32
        ).next_to(desc_8, DOWN, buff=0.5)
        eq_group[1].set_color(BLUE)
        eq_group[3].set_color(GREEN)
        self.play(Write(eq_group))
        self.wait(2.5)

        desc_9 = Text("观察可知，两个中括号内部恰好是完全平方式的展开：", font="KaiTi", font_size=30).next_to(eq_group, DOWN, buff=0.6)
        self.play(Write(desc_9))

        eq_perfect_sq = MathTex(
            r"E^2 \ge ", 
            r"[(4-a) + a]^2", 
            r" + ", 
            r"[(-b) + (b+2)]^2", 
            font_size=36
        ).next_to(desc_9, DOWN, buff=0.4)
        eq_perfect_sq[1].set_color(BLUE)
        eq_perfect_sq[3].set_color(GREEN)
        self.play(ReplacementTransform(eq_group.copy(), eq_perfect_sq))
        self.wait(2)

        # 整理屏幕，提炼出最终不等式
        self.play(
            FadeOut(desc_7), FadeOut(eq_subst), FadeOut(desc_8), FadeOut(eq_group), FadeOut(desc_9)
        )
        self.play(eq_perfect_sq.animate.to_edge(UP, buff=1.0))

        eq_calc = MathTex(r"E^2 \ge 4^2 + 2^2 = 20", font_size=36).set_color(YELLOW).next_to(eq_perfect_sq, DOWN, buff=0.5)
        self.play(Write(eq_calc))
        self.wait(1.5)

        desc_10 = Text("两边同时开平方，即可得到代数式的下界：", font="KaiTi", font_size=28).next_to(eq_calc, DOWN, buff=0.6)
        self.play(Write(desc_10))

        eq_min = MathTex(r"E \ge 2\sqrt{5}", font_size=45).set_color(RED).next_to(desc_10, DOWN, buff=0.4)
        self.play(Write(eq_min))
        self.wait(2)

        # ==================== 第三幕：验证等号成立条件 ====================
        self.play(
            FadeOut(eq_perfect_sq), FadeOut(eq_calc), FadeOut(desc_10)
        )
        self.play(eq_min.animate.to_edge(UP, buff=0.8))

        desc_11 = Text("为确保最小值能够取到，需要验证等号成立的条件：", font="KaiTi", font_size=30).next_to(eq_min, DOWN, buff=0.6)
        self.play(Write(desc_11))

        desc_12 = Text("即柯西不等式中对应的两组向量同向共线：", font="KaiTi", font_size=28).next_to(desc_11, DOWN, buff=0.3)
        self.play(Write(desc_12))

        eq_condition = MathTex(r"\frac{4-a}{a} = \frac{-b}{b+2} > 0", font_size=36).set_color(GREEN).next_to(desc_12, DOWN, buff=0.4)
        self.play(Write(eq_condition))
        self.wait(1.5)

        desc_13 = Text("化简该方程可得线性关系：", font="KaiTi", font_size=28).next_to(eq_condition, DOWN, buff=0.5)
        self.play(Write(desc_13))

        eq_linear = MathTex(r"a - 2b = 4", font_size=36).set_color(BLUE).next_to(desc_13, DOWN, buff=0.3)
        self.play(Write(eq_linear))
        self.wait(1)

        self.play(FadeOut(desc_11), FadeOut(desc_12), FadeOut(eq_condition), FadeOut(desc_13))
        self.play(eq_linear.animate.next_to(eq_min, DOWN, buff=0.8))

        desc_14_text1 = Text("将其与已知条件", font="KaiTi", font_size=28)
        desc_14_math = MathTex(r"a^2+b^2=4", font_size=30).set_color(GREEN)
        desc_14_text2 = Text("联立，解一元二次方程：", font="KaiTi", font_size=28)
        desc_14 = VGroup(desc_14_text1, desc_14_math, desc_14_text2).arrange(RIGHT, buff=0.1).next_to(eq_linear, DOWN, buff=0.5)
        self.play(Write(desc_14))

        eq_quadratic = MathTex(r"(2b+4)^2 + b^2 = 4 \implies 5b^2 + 16b + 12 = 0", font_size=32)
        eq_quadratic.next_to(desc_14, DOWN, buff=0.4)
        self.play(Write(eq_quadratic))
        self.wait(1.5)

        desc_15 = Text("解得符合同向共线条件的实数解为：", font="KaiTi", font_size=28).next_to(eq_quadratic, DOWN, buff=0.5)
        self.play(Write(desc_15))

        eq_roots = MathTex(r"a = 1.6,\quad b = -1.2", font_size=36).set_color(YELLOW).next_to(desc_15, DOWN, buff=0.3)
        self.play(Write(eq_roots))
        self.wait(2)

        # ==================== 第四幕：总结 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        final_desc = Text("综上所述，当满足上述条件时，原代数式取得最小值：", font="KaiTi", font_size=35).to_edge(UP, buff=2)
        self.play(Write(final_desc))
        self.wait(1)

        final_ans = MathTex(r"2\sqrt{5}", font_size=80).set_color_by_gradient(YELLOW, RED).next_to(final_desc, DOWN, buff=1.2)
        self.play(FadeIn(final_ans, shift=UP))

        outro_text = Text("求解完毕", font="KaiTi", font_size=40).set_color(BLUE).next_to(final_ans, DOWN, buff=1.2)
        self.play(Write(outro_text))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)