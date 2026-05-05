from manim import *


class Euler641Proof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("如何证明这个整除命题？", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"641 \mid 2^{32} + 1",
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

        # ==================== 第一幕：问题分析 ====================
        desc_1 = Text("直接计算指数过于繁琐：", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        calc_val = MathTex(r"2^{32} + 1 = 4294967297").next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(calc_val))

        desc_2 = Text("我们需要寻找代数上的降维方法，观察除数的结构：", font="KaiTi", font_size=28).next_to(calc_val, DOWN, buff=0.5)
        self.play(Write(desc_2))
        self.wait(1.5)

        # 整理屏幕
        self.play(
            FadeOut(desc_1), FadeOut(calc_val), FadeOut(desc_2)
        )

        # ==================== 第二幕：拆解除数 641 ====================
        desc_3 = Text("将除数进行两种不同方向的拆分：", font="KaiTi", font_size=30)
        desc_3.to_edge(UP, buff=0.8)
        self.play(Write(desc_3))

        split1 = MathTex(r"641 = 640 + 1 = 5 \times 2^7 + 1").next_to(desc_3, DOWN, buff=0.5)
        self.play(Write(split1))

        desc_4_t = Text("改写为同余式：", font="KaiTi", font_size=28)
        desc_4 = VGroup(desc_4_t).next_to(split1, DOWN, buff=0.3)
        self.play(Write(desc_4))

        cong1 = MathTex(r"5 \times 2^7 \equiv -1 \pmod{641}").set_color(BLUE).next_to(desc_4, DOWN, buff=0.3)
        self.play(Write(cong1))

        desc_5 = Text("另一方面，尝试另一种拆分：", font="KaiTi", font_size=28).next_to(cong1, DOWN, buff=0.5)
        self.play(Write(desc_5))

        split2 = MathTex(r"641 = 625 + 16 = 5^4 + 2^4").next_to(desc_5, DOWN, buff=0.3)
        self.play(Write(split2))

        desc_6_t = Text("同样改写为同余式：", font="KaiTi", font_size=28)
        desc_6 = VGroup(desc_6_t).next_to(split2, DOWN, buff=0.3)
        self.play(Write(desc_6))

        cong2 = MathTex(r"5^4 \equiv -2^4 \pmod{641}").set_color(GREEN).next_to(desc_6, DOWN, buff=0.3)
        self.play(Write(cong2))
        self.wait(2)

        # 整理屏幕，只保留两个同余式
        self.play(
            FadeOut(desc_3), FadeOut(split1), FadeOut(desc_4), FadeOut(desc_5),
            FadeOut(split2), FadeOut(desc_6)
        )
        self.play(cong1.animate.to_edge(UP, buff=0.8))
        self.play(cong2.animate.next_to(cong1, DOWN, buff=0.8))

        # ==================== 第三幕：代数推演 ====================
        desc_7_t1 = Text("为了凑出目标指数", font="KaiTi", font_size=28)
        target_exp = MathTex(r"2^{32}", font_size=30).set_color(YELLOW)
        desc_7_t2 = Text("，将第一个同余式两边同时取四次方：", font="KaiTi", font_size=28)
        desc_7 = VGroup(desc_7_t1, target_exp, desc_7_t2).arrange(RIGHT, buff=0.1).next_to(cong2, DOWN, buff=0.6)
        self.play(Write(desc_7))

        step1 = MathTex(r"(5 \times 2^7)^4 \equiv (-1)^4 \pmod{641}").set_color(BLUE).next_to(desc_7, DOWN, buff=0.3)
        self.play(Write(step1))

        desc_8 = Text("展开并化简指数项：", font="KaiTi", font_size=28).next_to(step1, DOWN, buff=0.3)
        self.play(Write(desc_8))

        step2 = MathTex(r"5^4 \times 2^{28} \equiv 1 \pmod{641}").set_color(BLUE).next_to(desc_8, DOWN, buff=0.3)
        self.play(TransformMatchingTex(step1.copy(), step2))
        self.wait(1.5)

        # 整理屏幕，保留同余式2和化简后的式子
        self.play(
            FadeOut(desc_7), FadeOut(step1), FadeOut(desc_8), FadeOut(cong1)
        )
        self.play(cong2.animate.to_edge(UP, buff=0.8))
        self.play(step2.animate.next_to(cong2, DOWN, buff=0.8))

        desc_9_t1 = Text("此时，将第二个同余式代入，替换掉左边的", font="KaiTi", font_size=28)
        target_5 = MathTex(r"5^4", font_size=30).set_color(GREEN)
        desc_9 = VGroup(desc_9_t1, target_5).arrange(RIGHT, buff=0.1).next_to(step2, DOWN, buff=0.6)
        self.play(Write(desc_9))

        step3 = MathTex(r"(-2^4) \times 2^{28} \equiv 1 \pmod{641}").set_color(PURPLE).next_to(desc_9, DOWN, buff=0.3)
        self.play(TransformMatchingTex(step2.copy(), step3))

        desc_10 = Text("合并同底数幂：", font="KaiTi", font_size=28).next_to(step3, DOWN, buff=0.3)
        self.play(Write(desc_10))

        step4 = MathTex(r"-2^{32} \equiv 1 \pmod{641}").set_color(YELLOW).next_to(desc_10, DOWN, buff=0.3)
        self.play(TransformMatchingTex(step3.copy(), step4))

        desc_11 = Text("移项即可得到结论：", font="KaiTi", font_size=28).next_to(step4, DOWN, buff=0.3)
        self.play(Write(desc_11))

        step_final = MathTex(r"2^{32} + 1 \equiv 0 \pmod{641}").set_color(RED).scale(1.1).next_to(desc_11, DOWN, buff=0.3)
        self.play(TransformMatchingTex(step4.copy(), step_final))

        rect_final = SurroundingRectangle(step_final, color=RED, buff=0.15)
        self.play(Create(rect_final))
        self.wait(3)

        # 全屏暴力清场
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        # ==================== 第四幕：结论与意义 ====================
        desc_12_t1 = Text("得证。该方法由欧拉于", font="KaiTi", font_size=32)
        year = MathTex(r"1732", font_size=34)
        desc_12_t2 = Text("年提出。", font="KaiTi", font_size=32)
        desc_12 = VGroup(desc_12_t1, year, desc_12_t2).arrange(RIGHT, buff=0.1).to_edge(UP, buff=2)
        self.play(Write(desc_12))

        desc_13_t1 = Text("由此否定了费马关于", font="KaiTi", font_size=32)
        formula_fn = MathTex(r"F_n = 2^{2^n}+1", font_size=34).set_color(YELLOW)
        desc_13_t2 = Text("均为素数的猜想。", font="KaiTi", font_size=32)
        desc_13 = VGroup(desc_13_t1, formula_fn, desc_13_t2).arrange(RIGHT, buff=0.1).next_to(desc_12, DOWN, buff=0.8)
        self.play(Write(desc_13))
        self.wait(1.5)

        desc_14 = Text("这种通过同余式降维并利用辅助变量消元的技巧，", font="KaiTi", font_size=30).next_to(desc_13, DOWN, buff=1.2)
        self.play(Write(desc_14))

        desc_15 = Text("在处理大数整除问题时具有普遍意义。", font="KaiTi", font_size=34).set_color(BLUE).next_to(desc_14, DOWN, buff=0.6)
        self.play(Write(desc_15))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)