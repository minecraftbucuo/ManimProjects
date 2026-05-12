from manim import *


class InfiniteProductProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        eq_cover_1 = MathTex(
            r"f(x) = (1+x)(1+x^2)(1+x^4)\cdots",
            font_size=55
        ).set_color(BLUE)

        eq_cover_2 = MathTex(
            r"f\left(\frac{1}{3}\right) = ?",
            font_size=55
        ).set_color(YELLOW)

        cover = VGroup(eq_cover_1, eq_cover_2).arrange(DOWN, buff=1.2)
        self.play(FadeIn(eq_cover_1, shift=UP))
        self.play(FadeIn(eq_cover_2, shift=UP))
        self.wait(1)

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

        # ==================== 第一幕：引入因式 ====================
        desc_1 = Text("观察连乘式，各项的指数呈两倍递增：", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_orig = MathTex(r"f(x) = (1+x)(1+x^2)(1+x^4)\cdots").set_color(BLUE).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(eq_orig))
        self.wait(1.5)

        desc_2_t1 = Text("为构造平方差公式，在等式两端同乘", font="KaiTi", font_size=28)
        desc_2_m1 = MathTex(r"(1-x)", font_size=30).set_color(YELLOW)
        desc_2_t2 = Text("：", font="KaiTi", font_size=28)
        desc_2 = VGroup(desc_2_t1, desc_2_m1, desc_2_t2).arrange(RIGHT, buff=0.1).next_to(eq_orig, DOWN, buff=0.5)
        self.play(Write(desc_2))

        eq_mult = MathTex(r"(1-x)", r"f(x) = ", r"(1-x)", r"(1+x)(1+x^2)(1+x^4)\cdots")
        eq_mult[0].set_color(YELLOW)
        eq_mult[2].set_color(YELLOW)
        eq_mult.next_to(desc_2, DOWN, buff=0.3)
        self.play(Write(eq_mult))
        self.wait(1.5)

        # 整理屏幕
        self.play(
            FadeOut(desc_1), FadeOut(eq_orig), FadeOut(desc_2)
        )
        self.play(eq_mult.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：连锁化简 ====================
        desc_3 = Text("应用平方差公式，右侧项开始连续合并：", font="KaiTi", font_size=30).next_to(eq_mult, DOWN, buff=0.6)
        self.play(Write(desc_3))

        eq_step1 = MathTex(r"(1-x)f(x) = ", r"(1-x^2)", r"(1+x^2)(1+x^4)\cdots").set_color(GREEN).next_to(desc_3, DOWN,
                                                                                                          buff=0.4)
        eq_step1[1].set_color(RED)
        self.play(ReplacementTransform(eq_mult.copy(), eq_step1))
        self.wait(1)

        eq_step2 = MathTex(r"(1-x)f(x) = ", r"(1-x^4)", r"(1+x^4)\cdots").set_color(GREEN).next_to(desc_3, DOWN,
                                                                                                   buff=0.4)
        eq_step2[1].set_color(RED)
        self.play(ReplacementTransform(eq_step1, eq_step2))
        self.wait(1.5)

        desc_4_t1 = Text("递推至前", font="KaiTi", font_size=28)
        desc_4_m1 = MathTex(r"n", font_size=30).set_color(YELLOW)
        desc_4_t2 = Text("项，一般形式可表示为：", font="KaiTi", font_size=28)
        desc_4 = VGroup(desc_4_t1, desc_4_m1, desc_4_t2).arrange(RIGHT, buff=0.1).next_to(eq_step2, DOWN, buff=0.5)
        self.play(Write(desc_4))

        eq_general = MathTex(r"(1-x) \prod_{k=0}^{n-1} (1+x^{2^k}) = 1 - x^{2^n}").scale(1.1).set_color(YELLOW).next_to(
            desc_4, DOWN, buff=0.4)
        self.play(Write(eq_general))

        rect_general = SurroundingRectangle(eq_general, color=YELLOW, buff=0.15)
        self.play(Create(rect_general))
        self.wait(2)

        # 大清场
        self.play(
            FadeOut(eq_mult), FadeOut(desc_3), FadeOut(eq_step2), FadeOut(desc_4)
        )
        gen_group = VGroup(eq_general, rect_general)
        self.play(gen_group.animate.to_edge(UP, buff=0.8).shift(UP * 0.33))

        # ==================== 第三幕：极限与收敛 ====================
        desc_5_t1 = Text("由于", font="KaiTi", font_size=28)
        desc_5_m1 = MathTex(r"x = \frac{1}{3}", font_size=30).set_color(BLUE)
        desc_5_t2 = Text("，满足", font="KaiTi", font_size=28)
        desc_5_m2 = MathTex(r"|x| < 1", font_size=30).set_color(BLUE)
        desc_5_t3 = Text("的收敛条件：", font="KaiTi", font_size=28)
        desc_5 = VGroup(desc_5_t1, desc_5_m1, desc_5_t2, desc_5_m2, desc_5_t3).arrange(RIGHT, buff=0.1).next_to(
            gen_group, DOWN, buff=0.8)
        desc_5.shift(UP * 0.2)
        self.play(Write(desc_5))

        desc_6_t1 = Text("当", font="KaiTi", font_size=28)
        desc_6_m1 = MathTex(r"n \to \infty", font_size=30).set_color(YELLOW)
        desc_6_t2 = Text("时，右侧末项极限为：", font="KaiTi", font_size=28)
        desc_6 = VGroup(desc_6_t1, desc_6_m1, desc_6_t2).arrange(RIGHT, buff=0.1).next_to(desc_5, DOWN, buff=0.5)
        desc_6.shift(UP * 0.2)
        self.play(Write(desc_6))

        eq_limit = MathTex(r"\lim_{n \to \infty} x^{2^n} = 0").set_color(GREEN).next_to(desc_6, DOWN, buff=0.4)
        self.play(Write(eq_limit))
        self.wait(1.5)

        desc_7_t1 = Text("代回原式，化简得到等效解析式：", font="KaiTi", font_size=28)
        desc_7 = VGroup(desc_7_t1).next_to(eq_limit, DOWN, buff=0.5)
        self.play(Write(desc_7))

        eq_final_func = MathTex(r"(1-x)f(x) = 1 \implies f(x) = \frac{1}{1-x}").set_color(YELLOW).next_to(
            desc_7, DOWN, buff=0.4)
        self.play(Write(eq_final_func))
        self.wait(2)

        # 全屏暴力清场
        self.play(
            FadeOut(gen_group), FadeOut(desc_5), FadeOut(desc_6), FadeOut(eq_limit), FadeOut(desc_7),
            FadeOut(eq_final_func)
        )

        # ==================== 第四幕：求解特值 ====================
        desc_8 = Text("将待求数值代入极简解析式：", font="KaiTi", font_size=35).to_edge(UP, buff=1.5)
        self.play(Write(desc_8))

        # 绝对居中定位
        final_ans_1 = MathTex(r"f\left(\frac{1}{3}\right) = \frac{1}{1 - \frac{1}{3}}").scale(1.3).set_color(
            BLUE).move_to(UP * 0.5)
        final_ans_2 = MathTex(r"= \frac{3}{2}").scale(1.5).set_color(YELLOW).move_to(DOWN * 1.2)

        self.play(FadeIn(final_ans_1, shift=UP))
        self.wait(1)
        self.play(FadeIn(final_ans_2, shift=UP))
        self.wait(3)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)