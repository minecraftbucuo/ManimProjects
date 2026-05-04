from manim import *


class WilsonRigorousProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("如何证明威尔逊定理？", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"(p-1)! \equiv -1 \pmod p",
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

        # ==================== 第一幕：特例检验 ====================
        desc_1 = Text("先从小素数的情况看起：", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        d2_text1 = Text("当", font="KaiTi", font_size=28)
        d2_math1 = MathTex(r"p=2", font_size=30).set_color(YELLOW)
        d2_text2 = Text("时，", font="KaiTi", font_size=28)
        d2_math2 = MathTex(r"1 \equiv -1 \pmod 2", font_size=30).set_color(GREEN)
        d2 = VGroup(d2_text1, d2_math1, d2_text2, d2_math2).arrange(RIGHT, buff=0.05).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(d2))

        d3_text1 = Text("当", font="KaiTi", font_size=28)
        d3_math1 = MathTex(r"p=3", font_size=30).set_color(YELLOW)
        d3_text2 = Text("时，", font="KaiTi", font_size=28)
        d3_math2 = MathTex(r"2 \equiv -1 \pmod 3", font_size=30).set_color(GREEN)
        d3 = VGroup(d3_text1, d3_math1, d3_text2, d3_math2).arrange(RIGHT, buff=0.05).next_to(d2, DOWN, buff=0.3)
        self.play(Write(d3))
        self.wait(1)

        desc_2_text1 = Text("结论均成立。接下来默认", font="KaiTi", font_size=28)
        desc_2_math1 = MathTex(r"p > 3", font_size=30).set_color(RED)
        desc_2 = VGroup(desc_2_text1, desc_2_math1).arrange(RIGHT, buff=0.05).next_to(d3, DOWN, buff=0.5)
        self.play(Write(desc_2))
        self.wait(2)

        # 整理屏幕
        self.play(FadeOut(desc_1), FadeOut(d2), FadeOut(d3), FadeOut(desc_2))

        # ==================== 第二幕：引出配对思想（关键过渡） ====================
        desc_3 = Text("面对庞大的阶乘，本能的策略是寻找化简规律：", font="KaiTi", font_size=30).to_edge(UP, buff=0.8)
        self.play(Write(desc_3))

        eq_expand_intro = MathTex(
            r"(p-1)! = 1 \times", r"2 \times 3 \times \dots \times (p-2)", r"\times (p-1)"
        )
        eq_expand_intro[1].set_color(YELLOW) # 给中间项上色
        eq_expand_intro.next_to(desc_3, DOWN, buff=0.5)
        self.play(Write(eq_expand_intro))
        self.wait(1)

        desc_4_text1 = Text("如果中间这些数，两两相乘的结果都是", font="KaiTi", font_size=28)
        desc_4_math1 = MathTex(r"1", font_size=30).set_color(GREEN)
        desc_4_text2 = Text("，问题就迎刃而解了！", font="KaiTi", font_size=28)
        desc_4 = VGroup(desc_4_text1, desc_4_math1, desc_4_text2).arrange(RIGHT, buff=0.05).next_to(eq_expand_intro, DOWN, buff=0.5)
        self.play(Write(desc_4))
        self.wait(1)

        desc_5_text1 = Text("这就引出了“逆元”的概念：当", font="KaiTi", font_size=28)
        desc_5_math1 = MathTex(r"a \times b \equiv 1 \pmod p", font_size=30).set_color(GREEN)
        desc_5_text2 = Text("时，", font="KaiTi", font_size=28)
        desc_5 = VGroup(desc_5_text1, desc_5_math1, desc_5_text2).arrange(RIGHT, buff=0.05).next_to(desc_4, DOWN, buff=0.4)
        self.play(Write(desc_5))

        desc_6_text1 = Text("称", font="KaiTi", font_size=28)
        desc_6_math1 = MathTex(r"b", font_size=30).set_color(YELLOW)
        desc_6_text2 = Text("是", font="KaiTi", font_size=28)
        desc_6_math2 = MathTex(r"a", font_size=30).set_color(YELLOW)
        desc_6_text3 = Text("的逆元，它们可以完美“配对”。", font="KaiTi", font_size=28)
        desc_6 = VGroup(desc_6_text1, desc_6_math1, desc_6_text2, desc_6_math2, desc_6_text3).arrange(RIGHT, buff=0.05).next_to(desc_5, DOWN, buff=0.3)
        self.play(Write(desc_6))
        self.wait(1.5)

        desc_7 = Text("要让配对策略成功，必须确认两个前提条件：", font="KaiTi", font_size=28).set_color(RED).next_to(desc_6, DOWN, buff=0.5)
        self.play(Write(desc_7))

        cond_1_text1 = Text("1. 每个元素都有唯一的逆元（逆元存在且唯一）", font="KaiTi", font_size=26).next_to(desc_7, DOWN, buff=0.3)
        self.play(Write(cond_1_text1))

        cond_2_text1 = Text("2. 没有元素会和自身互为逆元（排除自逆元）", font="KaiTi", font_size=26).next_to(cond_1_text1, DOWN, buff=0.2)
        self.play(Write(cond_2_text1))
        self.wait(2)

        # 大清场
        self.play(
            FadeOut(desc_3), FadeOut(eq_expand_intro), FadeOut(desc_4), FadeOut(desc_5),
            FadeOut(desc_6), FadeOut(desc_7), FadeOut(cond_1_text1), FadeOut(cond_2_text1)
        )

        # ==================== 第三幕：确认前提1（逆元存在与唯一） ====================
        desc_8 = Text("先确认：每个元素都有唯一的逆元吗？", font="KaiTi", font_size=30).to_edge(UP, buff=0.8)
        self.play(Write(desc_8))

        desc_9_text1 = Text("对于集合", font="KaiTi", font_size=28)
        desc_9_math1 = MathTex(r"S=\{1, 2, \dots, p-1\}", font_size=30).set_color(YELLOW)
        desc_9_text2 = Text("中的任意数", font="KaiTi", font_size=28)
        desc_9_math2 = MathTex(r"a", font_size=30).set_color(YELLOW)
        desc_9 = VGroup(desc_9_text1, desc_9_math1, desc_9_text2, desc_9_math2).arrange(RIGHT, buff=0.05).next_to(desc_8, DOWN, buff=0.5)
        self.play(Write(desc_9))

        desc_10_text1 = Text("因为", font="KaiTi", font_size=28)
        desc_10_math1 = MathTex(r"p", font_size=30).set_color(RED)
        desc_10_text2 = Text("是素数，所以", font="KaiTi", font_size=28)
        desc_10_math2 = MathTex(r"\gcd(a, p) = 1", font_size=30).set_color(RED)
        desc_10 = VGroup(desc_10_text1, desc_10_math1, desc_10_text2, desc_10_math2).arrange(RIGHT, buff=0.05).next_to(desc_9, DOWN, buff=0.4)
        self.play(Write(desc_10))

        desc_11 = Text("根据裴蜀定理，必然存在整数解：", font="KaiTi", font_size=28).next_to(desc_10, DOWN, buff=0.4)
        self.play(Write(desc_11))

        eq_bezout = MathTex(r"ax + py = 1").set_color(BLUE).next_to(desc_11, DOWN, buff=0.3)
        self.play(Write(eq_bezout))
        self.wait(1)

        desc_12_text1 = Text("两边同取模", font="KaiTi", font_size=28)
        desc_12_math1 = MathTex(r"p", font_size=30).set_color(RED)
        desc_12_text2 = Text("，这就证明了逆元存在：", font="KaiTi", font_size=28)
        desc_12 = VGroup(desc_12_text1, desc_12_math1, desc_12_text2).arrange(RIGHT, buff=0.05).next_to(eq_bezout, DOWN, buff=0.4)
        self.play(Write(desc_12))

        eq_mod = MathTex(r"ax \equiv 1 \pmod p").set_color(GREEN).scale(1.1).next_to(desc_12, DOWN, buff=0.3)
        self.play(TransformMatchingTex(eq_bezout.copy(), eq_mod))
        self.wait(1)

        desc_13 = Text("由消去律易知，逆元是唯一的。条件1成立！", font="KaiTi", font_size=28).next_to(eq_mod, DOWN, buff=0.4)
        self.play(Write(desc_13))
        self.wait(2)

        # 大清场
        self.play(
            FadeOut(desc_8), FadeOut(desc_9), FadeOut(desc_10), FadeOut(desc_11),
            FadeOut(eq_bezout), FadeOut(desc_12), FadeOut(eq_mod), FadeOut(desc_13)
        )

        # ==================== 第四幕：确认前提2（谁会落单？） ====================
        desc_14 = Text("再确认：有元素会和自身互为逆元吗？", font="KaiTi", font_size=30).to_edge(UP, buff=0.8)
        self.play(Write(desc_14))

        desc_15_text1 = Text("即寻找逆元是其本身的元素，解方程：", font="KaiTi", font_size=28).next_to(desc_14, DOWN, buff=0.5)
        self.play(Write(desc_15_text1))

        eq_self = MathTex(r"x^2 \equiv 1 \pmod p").set_color(YELLOW).next_to(desc_15_text1, DOWN, buff=0.4)
        self.play(Write(eq_self))
        self.wait(1)

        desc_16 = Text("移项并因式分解：", font="KaiTi", font_size=28).next_to(eq_self, DOWN, buff=0.4)
        self.play(Write(desc_16))

        eq_fact = MathTex(r"p \mid (x-1)(x+1)").set_color(BLUE).next_to(desc_16, DOWN, buff=0.3)
        self.play(Write(eq_fact))
        self.wait(1)

        desc_17_text1 = Text("由欧几里得引理，素数整除乘积必整除其中之一：", font="KaiTi", font_size=28).next_to(eq_fact, DOWN, buff=0.4)
        self.play(Write(desc_17_text1))

        eq_cases_1 = MathTex(r"p \mid (x-1)").set_color(RED)
        eq_cases_text = Text("或", font="KaiTi", font_size=28).set_color(RED)
        eq_cases_2 = MathTex(r"p \mid (x+1)").set_color(RED)
        eq_cases = VGroup(eq_cases_1, eq_cases_text, eq_cases_2).arrange(RIGHT, buff=0.3).next_to(desc_17_text1, DOWN, buff=0.3)
        self.play(Write(eq_cases))
        self.wait(1)

        desc_18_text1 = Text("这意味着，只有", font="KaiTi", font_size=28)
        desc_18_math1 = MathTex(r"1", font_size=30).set_color(YELLOW)
        desc_18_text2 = Text("和", font="KaiTi", font_size=28)
        desc_18_math2 = MathTex(r"p-1", font_size=30).set_color(YELLOW)
        desc_18_text3 = Text("会和自身互为逆元。条件2确认完毕！", font="KaiTi", font_size=28)
        desc_18 = VGroup(desc_18_text1, desc_18_math1, desc_18_text2, desc_18_math2, desc_18_text3).arrange(RIGHT, buff=0.05).next_to(eq_cases, DOWN, buff=0.5)
        self.play(Write(desc_18))
        self.wait(2)

        # 大清场
        self.play(
            FadeOut(desc_14), FadeOut(desc_15_text1), FadeOut(eq_self), FadeOut(desc_16),
            FadeOut(eq_fact), FadeOut(desc_17_text1), FadeOut(eq_cases), FadeOut(desc_18)
        )

        # ==================== 第五幕：完美配对 ====================
        desc_19 = Text("抛开这两个特例，剩下的元素可以完美配对！", font="KaiTi", font_size=30).to_edge(UP, buff=0.8)
        self.play(Write(desc_19))

        desc_20_text1 = Text("考虑集合", font="KaiTi", font_size=28)
        desc_20_math1 = MathTex(r"S'=\{2, 3, \dots, p-2\}", font_size=30).set_color(YELLOW)
        desc_20 = VGroup(desc_20_text1, desc_20_math1).arrange(RIGHT, buff=0.05).next_to(desc_19, DOWN, buff=0.5)
        self.play(Write(desc_20))

        desc_21_text1 = Text("因为", font="KaiTi", font_size=28)
        desc_21_math1 = MathTex(r"p>3", font_size=30).set_color(RED)
        desc_21_text2 = Text("是素数，所以", font="KaiTi", font_size=28)
        desc_21_math2 = MathTex(r"p", font_size=30).set_color(RED)
        desc_21_text3 = Text("必为奇数，元素个数", font="KaiTi", font_size=28)
        desc_21_math3 = MathTex(r"p-3", font_size=30).set_color(RED)
        desc_21_text4 = Text("必为偶数。", font="KaiTi", font_size=28)
        desc_21 = VGroup(desc_21_text1, desc_21_math1, desc_21_text2, desc_21_math2, desc_21_text3, desc_21_math3, desc_21_text4).arrange(RIGHT, buff=0.05).next_to(desc_20, DOWN, buff=0.4)
        self.play(Write(desc_21))
        self.wait(1)

        desc_22 = Text("它们两两互为不同的逆元，形成乘积为1的数对：", font="KaiTi", font_size=28).next_to(desc_21, DOWN, buff=0.4)
        self.play(Write(desc_22))

        eq_prod = MathTex(r"\prod_{i \in S'} i = 2 \times 3 \times \dots \times (p-2) \equiv 1 \pmod p").set_color(GREEN).next_to(desc_22, DOWN, buff=0.4)
        self.play(Write(eq_prod))
        self.wait(2)

        # 大清场
        self.play(
            FadeOut(desc_19), FadeOut(desc_20), FadeOut(desc_21), FadeOut(desc_22), FadeOut(eq_prod)
        )

        # ==================== 第六幕：汇总得出结论 ====================
        desc_23 = Text("将所有部分相乘，见证奇迹：", font="KaiTi", font_size=30).to_edge(UP, buff=0.8)
        self.play(Write(desc_23))

        eq_expand = MathTex(r"(p-1)! = 1", r"\times", r"[2 \times 3 \times \dots \times (p-2)]", r"\times", r"(p-1)")
        eq_expand[0].set_color(BLUE)
        eq_expand[2].set_color(GREEN)
        eq_expand[4].set_color(RED)
        eq_expand.next_to(desc_23, DOWN, buff=0.6)
        self.play(Write(eq_expand))
        self.wait(1)

        desc_24_text1 = Text("中间项全消为", font="KaiTi", font_size=28)
        desc_24_math1 = MathTex(r"1", font_size=30).set_color(GREEN)
        desc_24_text2 = Text("，代入同余式：", font="KaiTi", font_size=28)
        desc_24 = VGroup(desc_24_text1, desc_24_math1, desc_24_text2).arrange(RIGHT, buff=0.05).next_to(eq_expand, DOWN, buff=0.5)
        self.play(Write(desc_24))

        eq_merge = MathTex(r"(p-1)! \equiv 1 \times 1 \times (p-1) \pmod p").set_color(BLUE).next_to(desc_24, DOWN, buff=0.3)
        self.play(ReplacementTransform(eq_expand.copy(), eq_merge))
        self.wait(1)

        eq_final = MathTex(r"(p-1)! \equiv p-1 \equiv -1 \pmod p").set_color(YELLOW).scale(1.2).next_to(eq_merge, DOWN, buff=0.6)
        self.play(Write(eq_final))

        rect_final = SurroundingRectangle(eq_final, color=RED, buff=0.2)
        self.play(Create(rect_final))
        self.wait(2)

        # 全屏暴力清场
        self.play(
            FadeOut(desc_23), FadeOut(eq_expand), FadeOut(desc_24), FadeOut(eq_merge), FadeOut(eq_final), FadeOut(rect_final)
        )

        # ==================== 散场 ====================
        outro_1_text1 = Text("证毕", font="KaiTi", font_size=60).set_color_by_gradient(RED, YELLOW).move_to(UP * 0.5)
        self.play(Write(outro_1_text1))
        self.wait(1.5)


        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)