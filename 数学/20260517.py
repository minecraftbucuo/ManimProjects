from manim import *


class IntegerExpressionProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("求使表达式为整数的正整数解:", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"\left(b - \frac{1}{a}\right)\left(c - \frac{1}{b}\right)\left(a - \frac{1}{c}\right)",
            font_size=60
        ).set_color(BLUE)

        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))

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

        # ==================== 第一幕：展开与分离 ====================
        desc_1 = Text("首先将原表达式展开：", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_orig = MathTex(
            r"E = abc - a - b - c + \frac{1}{a} + \frac{1}{b} + \frac{1}{c} - \frac{1}{abc}"
        ).set_color(BLUE).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(eq_orig))
        self.wait(1.5)

        desc_2 = Text("分离出明显的整数部分与分数部分：", font="KaiTi", font_size=28).next_to(eq_orig, DOWN, buff=0.5)
        self.play(Write(desc_2))

        eq_sep = MathTex(
            r"E = (abc - a - b - c) + \left(\frac{1}{a} + \frac{1}{b} + \frac{1}{c} - \frac{1}{abc}\right)"
        )
        eq_sep.set_color_by_tex("abc", YELLOW)
        eq_sep.next_to(desc_2, DOWN, buff=0.3)
        self.play(Write(eq_sep))
        self.wait(1)

        # 拼接文字与公式
        desc_3_t1 = Text("令分数部分为", font="KaiTi", font_size=28)
        desc_3_m1 = MathTex(r"k", font_size=30).set_color(GREEN)
        desc_3_t2 = Text("，则", font="KaiTi", font_size=28)
        desc_3_m2 = MathTex(r"k", font_size=30).set_color(GREEN)
        desc_3_t3 = Text("必须为整数：", font="KaiTi", font_size=28)
        desc_3 = VGroup(desc_3_t1, desc_3_m1, desc_3_t2, desc_3_m2, desc_3_t3).arrange(RIGHT, buff=0.1)
        desc_3.next_to(eq_sep, DOWN, buff=0.5)
        self.play(Write(desc_3))

        eq_k = MathTex(r"k = \frac{1}{a} + \frac{1}{b} + \frac{1}{c} - \frac{1}{abc}").set_color(GREEN).next_to(desc_3,
                                                                                                                DOWN,
                                                                                                                buff=0.3)
        self.play(Write(eq_k))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(desc_1), FadeOut(eq_orig), FadeOut(desc_2), FadeOut(eq_sep), FadeOut(desc_3)
        )
        self.play(eq_k.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：利用对称性讨论 (a=1) ====================
        desc_4_t1 = Text("由表达式的对称性，不妨假设", font="KaiTi", font_size=28)
        desc_4_m1 = MathTex(r"1 \le a \le b \le c", font_size=30).set_color(YELLOW)
        desc_4_t2 = Text("。", font="KaiTi", font_size=28)
        desc_4 = VGroup(desc_4_t1, desc_4_m1, desc_4_t2).arrange(RIGHT, buff=0.1).next_to(eq_k, DOWN, buff=0.6)
        self.play(Write(desc_4))

        desc_5_t1 = Text("当", font="KaiTi", font_size=28)
        desc_5_m1 = MathTex(r"a = 1", font_size=30).set_color(YELLOW)
        desc_5_t2 = Text("时，代入可得：", font="KaiTi", font_size=28)
        desc_5 = VGroup(desc_5_t1, desc_5_m1, desc_5_t2).arrange(RIGHT, buff=0.1).next_to(desc_4, DOWN, buff=0.4)
        self.play(Write(desc_5))

        eq_k1 = MathTex(r"k = 1 + \frac{1}{b} + \frac{1}{c} - \frac{1}{bc} = 1 + \frac{b+c-1}{bc}").set_color(
            BLUE).next_to(desc_5, DOWN, buff=0.4)
        self.play(Write(eq_k1))
        self.wait(1)

        desc_6_t1 = Text("由于", font="KaiTi", font_size=28)
        desc_6_m1 = MathTex(r"b, c \ge 1", font_size=30).set_color(YELLOW)
        desc_6_t2 = Text("，分式部分大于零，且：", font="KaiTi", font_size=28)
        desc_6 = VGroup(desc_6_t1, desc_6_m1, desc_6_t2).arrange(RIGHT, buff=0.1).next_to(eq_k1, DOWN, buff=0.5)
        self.play(Write(desc_6))

        eq_bound = MathTex(r"(b-1)(c-1) \ge 0 \implies bc \ge b+c-1").set_color(GREEN).next_to(desc_6, DOWN, buff=0.3)
        self.play(Write(eq_bound))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(eq_k), FadeOut(desc_4), FadeOut(desc_5), FadeOut(eq_k1), FadeOut(desc_6)
        )
        self.play(eq_bound.animate.to_edge(UP, buff=0.8))

        desc_7_t1 = Text("因此该分式的值只能为", font="KaiTi", font_size=28)
        desc_7_m1 = MathTex(r"1", font_size=30).set_color(YELLOW)
        desc_7_t2 = Text("，即分子等于分母：", font="KaiTi", font_size=28)
        desc_7 = VGroup(desc_7_t1, desc_7_m1, desc_7_t2).arrange(RIGHT, buff=0.1).next_to(eq_bound, DOWN, buff=0.6)
        self.play(Write(desc_7))

        eq_solve_1 = MathTex(r"b+c-1 = bc \implies (b-1)(c-1) = 0").set_color(BLUE).next_to(desc_7, DOWN, buff=0.4)
        self.play(Write(eq_solve_1))
        self.wait(1)

        desc_8_t1 = Text("结合假设，解得", font="KaiTi", font_size=28)
        desc_8_m1 = MathTex(r"b = 1", font_size=30).set_color(YELLOW)
        desc_8_t2 = Text("，此时", font="KaiTi", font_size=28)
        desc_8_m2 = MathTex(r"c", font_size=30).set_color(YELLOW)
        desc_8_t3 = Text("为任意正整数。", font="KaiTi", font_size=28)
        desc_8 = VGroup(desc_8_t1, desc_8_m1, desc_8_t2, desc_8_m2, desc_8_t3).arrange(RIGHT, buff=0.1).next_to(
            eq_solve_1, DOWN, buff=0.5)
        self.play(Write(desc_8))
        self.wait(2)

        self.play(
            FadeOut(eq_bound), FadeOut(desc_7), FadeOut(eq_solve_1), FadeOut(desc_8)
        )

        # ==================== 第三幕：讨论 (a>=2) ====================
        desc_9_t1 = Text("当", font="KaiTi", font_size=28)
        desc_9_m1 = MathTex(r"a \ge 2", font_size=30).set_color(YELLOW)
        desc_9_t2 = Text("时，即", font="KaiTi", font_size=28)
        desc_9_m2 = MathTex(r"2 \le a \le b \le c", font_size=30).set_color(YELLOW)
        desc_9_t3 = Text("，进行放缩：", font="KaiTi", font_size=28)
        desc_9 = VGroup(desc_9_t1, desc_9_m1, desc_9_t2, desc_9_m2, desc_9_t3).arrange(RIGHT, buff=0.1).to_edge(UP,
                                                                                                                buff=0.8)
        self.play(Write(desc_9))

        eq_k2_bound = MathTex(
            r"0 < k \le \frac{1}{2} + \frac{1}{2} + \frac{1}{2} - \frac{1}{8} = \frac{11}{8} < 2").set_color(
            BLUE).next_to(desc_9, DOWN, buff=0.5)
        self.play(Write(eq_k2_bound))
        self.wait(1)

        desc_10_t1 = Text("故整数", font="KaiTi", font_size=28)
        desc_10_m1 = MathTex(r"k", font_size=30).set_color(GREEN)
        desc_10_t2 = Text("只能等于 1，代入化简可得：", font="KaiTi", font_size=28)
        desc_10 = VGroup(desc_10_t1, desc_10_m1, desc_10_t2).arrange(RIGHT, buff=0.1).next_to(eq_k2_bound, DOWN,
                                                                                              buff=0.6)
        self.play(Write(desc_10))

        eq_k2 = MathTex(r"abc - ab - bc - ca = -1").set_color(GREEN).next_to(desc_10, DOWN, buff=0.4)
        self.play(Write(eq_k2))
        self.wait(1.5)

        # ==================== 第四幕：凑因式求解 ====================
        desc_11_t1 = Text("若", font="KaiTi", font_size=28)
        desc_11_m1 = MathTex(r"a = 2", font_size=30).set_color(YELLOW)
        desc_11_t2 = Text("，代入上式并两边同加 4 凑因式：", font="KaiTi", font_size=28)
        desc_11 = VGroup(desc_11_t1, desc_11_m1, desc_11_t2).arrange(RIGHT, buff=0.1).next_to(eq_k2, DOWN, buff=0.6)
        self.play(Write(desc_11))

        eq_a2 = MathTex(r"bc - 2b - 2c + 4 = 3 \implies (b-2)(c-2) = 3").set_color(YELLOW).next_to(desc_11, DOWN,
                                                                                                   buff=0.4)
        self.play(Write(eq_a2))

        desc_12_t1 = Text("由于", font="KaiTi", font_size=28)
        desc_12_m1 = MathTex(r"b \le c", font_size=30).set_color(YELLOW)
        desc_12_t2 = Text("，解得", font="KaiTi", font_size=28)
        desc_12_m2 = MathTex(r"b = 3, c = 5", font_size=30).set_color(YELLOW)
        desc_12_t3 = Text("。", font="KaiTi", font_size=28)
        desc_12 = VGroup(desc_12_t1, desc_12_m1, desc_12_t2, desc_12_m2, desc_12_t3).arrange(RIGHT, buff=0.1).next_to(
            eq_a2, DOWN, buff=0.4)
        self.play(Write(desc_12))
        self.wait(2)

        # 暴力清场
        self.play(
            FadeOut(desc_9), FadeOut(eq_k2_bound), FadeOut(desc_10), FadeOut(eq_k2),
            FadeOut(desc_11), FadeOut(eq_a2), FadeOut(desc_12)
        )

        # ==================== 第五幕：最终结论 ====================
        desc_13_t1 = Text("同理可证", font="KaiTi", font_size=35)
        desc_13_m1 = MathTex(r"a \ge 3", font_size=38).set_color(YELLOW)
        desc_13_t2 = Text("时无解。", font="KaiTi", font_size=35)
        desc_13 = VGroup(desc_13_t1, desc_13_m1, desc_13_t2).arrange(RIGHT, buff=0.1).to_edge(UP, buff=1.5)
        self.play(Write(desc_13))

        desc_14 = Text("消除对称性假设，对所得解进行全排列：", font="KaiTi", font_size=35).next_to(desc_13, DOWN,
                                                                                                 buff=1.0)
        self.play(Write(desc_14))

        final_ans_1 = MathTex(r"(a,b,c) = (1, 1, m), (1, m, 1), (m, 1, 1)\quad (m \in \mathbb{Z}^+)").scale(
            1.1).set_color(BLUE).next_to(desc_14, DOWN, buff=0.8)
        final_ans_2 = MathTex(r"(a,b,c) = (2, 3, 5), (2, 5, 3), (3, 2, 5)").scale(1.1).set_color(GREEN).next_to(
            final_ans_1, DOWN, buff=0.5)
        final_ans_3 = MathTex(r"(3, 5, 2), (5, 2, 3), (5, 3, 2)").scale(1.1).set_color(GREEN).next_to(final_ans_2, DOWN,
                                                                                                      buff=0.3)

        self.play(FadeIn(final_ans_1, shift=UP))
        self.play(FadeIn(final_ans_2, shift=UP))
        self.play(FadeIn(final_ans_3, shift=UP))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)