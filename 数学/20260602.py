from manim import *


class FractionMaximumProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("分式最值的求法", font="KaiTi", font_size=48)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        cond_text = Text("已知", font="KaiTi", font_size=32)
        cond_math = MathTex(r"a>0,\ b>0", font_size=38).set_color(BLUE)
        cond_line = VGroup(cond_text, cond_math).arrange(RIGHT, buff=0.12)

        target_line = MathTex(
            r"\frac{ab+2b}{a^2+b^2+1}",
            font_size=56
        ).set_color(YELLOW)

        ask_text = Text("的最大值。", font="KaiTi", font_size=32)

        cover = VGroup(title, cond_line, target_line, ask_text).arrange(DOWN, buff=0.45)
        self.play(Write(title))
        self.play(FadeIn(cond_line, shift=UP))
        self.play(FadeIn(target_line, shift=UP))
        self.play(FadeIn(ask_text, shift=UP))

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

        # ==================== 第一幕：先固定一个变量 ====================
        desc_1 = Text("先固定一个变量，把二元最值化为一元最值。", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_orig = MathTex(
            r"M=\frac{ab+2b}{a^2+b^2+1}=\frac{b(a+2)}{a^2+b^2+1}",
            font_size=46
        ).set_color(BLUE).next_to(desc_1, DOWN, buff=0.45)
        self.play(Write(eq_orig))
        self.wait(1.2)

        desc_2_t1 = Text("对固定的", font="KaiTi", font_size=28)
        desc_2_m1 = MathTex(r"a", font_size=32).set_color(YELLOW)
        desc_2_t2 = Text("而言，它是关于", font="KaiTi", font_size=28)
        desc_2_m2 = MathTex(r"b", font_size=32).set_color(YELLOW)
        desc_2_t3 = Text("的函数。", font="KaiTi", font_size=28)
        desc_2 = VGroup(desc_2_t1, desc_2_m1, desc_2_t2, desc_2_m2, desc_2_t3).arrange(RIGHT, buff=0.08)
        desc_2.next_to(eq_orig, DOWN, buff=0.55)
        self.play(Write(desc_2))

        eq_fixed = MathTex(
            r"M=\frac{(a+2)b}{b^2+(a^2+1)}",
            font_size=44
        ).next_to(desc_2, DOWN, buff=0.35)
        self.play(Write(eq_fixed))
        self.wait(1.2)

        desc_3 = Text("此时分子对 b 是一次式，分母对 b 是二次式。", font="KaiTi", font_size=28)
        desc_3.next_to(eq_fixed, DOWN, buff=0.55)
        self.play(Write(desc_3))
        self.wait(1.5)

        self.play(
            FadeOut(desc_1), FadeOut(desc_2), FadeOut(eq_fixed), FadeOut(desc_3)
        )
        self.play(eq_orig.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：先对 b 估计 ====================
        desc_4 = Text("先用基本不等式处理分母。", font="KaiTi", font_size=30)
        desc_4.next_to(eq_orig, DOWN, buff=0.55)
        self.play(Write(desc_4))

        eq_ineq_1 = MathTex(
            r"b^2+(a^2+1)\geq 2b\sqrt{a^2+1}",
            font_size=44
        ).set_color(YELLOW).next_to(desc_4, DOWN, buff=0.35)
        self.play(Write(eq_ineq_1))
        self.wait(1.2)

        desc_5 = Text("代回原式，就能把 b 消掉。", font="KaiTi", font_size=28)
        desc_5.next_to(eq_ineq_1, DOWN, buff=0.55)
        self.play(Write(desc_5))

        eq_ineq_2 = MathTex(
            r"M=\frac{(a+2)b}{a^2+b^2+1}",
            r"\leq",
            r"\frac{(a+2)b}{2b\sqrt{a^2+1}}",
            r"=",
            r"\frac{a+2}{2\sqrt{a^2+1}}",
            font_size=40
        )
        eq_ineq_2[0].set_color(BLUE)
        eq_ineq_2[2].set_color(GREEN)
        eq_ineq_2[4].set_color(GREEN)
        eq_ineq_2.next_to(desc_5, DOWN, buff=0.35)
        self.play(Write(eq_ineq_2))
        self.wait(1.5)

        self.play(
            FadeOut(desc_4), FadeOut(eq_ineq_1), FadeOut(desc_5)
        )
        self.play(eq_ineq_2.animate.next_to(eq_orig, DOWN, buff=0.45))

        desc_6 = Text("于是问题转化为只含一个变量的最值问题。", font="KaiTi", font_size=28)
        desc_6.next_to(eq_ineq_2, DOWN, buff=0.45)
        self.play(Write(desc_6))

        eq_reduce = MathTex(
            r"M\leq \frac{a+2}{2\sqrt{a^2+1}}",
            font_size=44
        ).set_color(GREEN).next_to(desc_6, DOWN, buff=0.28)
        self.play(Write(eq_reduce))
        self.wait(2)

        self.play(
            FadeOut(eq_orig), FadeOut(eq_ineq_2), FadeOut(desc_6)
        )
        self.play(eq_reduce.animate.to_edge(UP, buff=0.8))

        # ==================== 第三幕：再对 a 估计 ====================
        desc_7 = Text("下面只需求这个一元式的上界。", font="KaiTi", font_size=28)
        desc_7.next_to(eq_reduce, DOWN, buff=0.55)
        self.play(Write(desc_7))

        desc_8 = Text("只要证明分子不超过一个合适的常数倍即可。", font="KaiTi", font_size=26)
        desc_8.next_to(desc_7, DOWN, buff=0.3)
        self.play(Write(desc_8))

        eq_square_1 = MathTex(
            r"(a+2)^2\leq 5(a^2+1)",
            font_size=40
        ).set_color(YELLOW).next_to(desc_8, DOWN, buff=0.28)
        self.play(Write(eq_square_1))
        self.wait(1)

        self.play(FadeOut(desc_7), FadeOut(desc_8))
        self.play(eq_square_1.animate.next_to(eq_reduce, DOWN, buff=0.5))

        desc_9 = Text("因为这等价于一个恒成立的平方不等式。", font="KaiTi", font_size=26)
        desc_9.next_to(eq_square_1, DOWN, buff=0.45)
        self.play(Write(desc_9))

        eq_square_2 = MathTex(
            r"5(a^2+1)-(a+2)^2=4a^2-4a+1=(2a-1)^2\geq 0",
            font_size=34
        ).next_to(desc_9, DOWN, buff=0.28)
        self.play(Write(eq_square_2))
        self.wait(1.5)

        desc_10 = Text("因此可以得到：", font="KaiTi", font_size=26)
        desc_10.next_to(eq_square_2, DOWN, buff=0.4)
        self.play(Write(desc_10))

        eq_square_3 = MathTex(
            r"a+2\leq \sqrt{5}\sqrt{a^2+1}",
            font_size=38
        ).set_color(GREEN).next_to(desc_10, DOWN, buff=0.28)
        self.play(Write(eq_square_3))
        self.wait(1.8)

        self.play(
            FadeOut(eq_square_1),
            FadeOut(desc_9), FadeOut(eq_square_2), FadeOut(desc_10)
        )
        self.play(eq_square_3.animate.next_to(eq_reduce, DOWN, buff=0.45))

        # ==================== 第四幕：合并两次估计 ====================
        desc_11 = Text("把上面的结论代回一元式。", font="KaiTi", font_size=28)
        desc_11.next_to(eq_square_3, DOWN, buff=0.5)
        self.play(Write(desc_11))

        eq_final_1 = MathTex(
            r"M\leq \frac{a+2}{2\sqrt{a^2+1}}",
            r"\leq",
            r"\frac{\sqrt{5}}{2}",
            font_size=38
        )
        eq_final_1[0].set_color(BLUE)
        eq_final_1[2].set_color(YELLOW)
        eq_final_1.next_to(desc_11, DOWN, buff=0.28)
        self.play(Write(eq_final_1))
        self.wait(1.5)

        desc_12 = Text("所以原式的最大值已经得到。", font="KaiTi", font_size=26)
        desc_12.next_to(eq_final_1, DOWN, buff=0.4)
        self.play(Write(desc_12))

        eq_final_2 = MathTex(
            r"\max \frac{ab+2b}{a^2+b^2+1}=\frac{\sqrt{5}}{2}",
            font_size=40
        ).set_color(YELLOW).next_to(desc_12, DOWN, buff=0.28)
        rect_final = SurroundingRectangle(eq_final_2, color=YELLOW, buff=0.18)
        self.play(Write(eq_final_2))
        self.play(Create(rect_final))
        self.wait(2)

        self.play(
            FadeOut(eq_reduce), FadeOut(eq_square_3),
            FadeOut(desc_11), FadeOut(eq_final_1), FadeOut(desc_12)
        )
        final_group = VGroup(eq_final_2, rect_final)
        self.play(final_group.animate.to_edge(UP, buff=0.6))

        # ==================== 第五幕：说明取等条件 ====================
        desc_13 = Text("最后检查两次不等式同时取等的条件。", font="KaiTi", font_size=28)
        desc_13.next_to(final_group, DOWN, buff=0.48)
        self.play(Write(desc_13))

        eq_equal_1 = MathTex(
            r"b^2+(a^2+1)=2b\sqrt{a^2+1}",
            r"\Longrightarrow",
            r"b=\sqrt{a^2+1}",
            font_size=36
        ).next_to(desc_13, DOWN, buff=0.28)
        eq_equal_1[2].set_color(GREEN)
        self.play(Write(eq_equal_1))
        self.wait(1.2)

        eq_equal_2 = MathTex(
            r"(2a-1)^2=0",
            r"\Longrightarrow",
            r"a=\frac{1}{2}",
            font_size=36
        ).next_to(eq_equal_1, DOWN, buff=0.28)
        eq_equal_2[2].set_color(GREEN)
        self.play(Write(eq_equal_2))
        self.wait(1.2)

        self.play(
            FadeOut(desc_13), FadeOut(eq_equal_1), FadeOut(eq_equal_2)
        )

        desc_14 = Text("代入前式，就得到对应的 b 。", font="KaiTi", font_size=26)
        desc_14.next_to(final_group, DOWN, buff=0.55)
        self.play(Write(desc_14))

        eq_equal_3 = MathTex(
            r"b=\sqrt{a^2+1}=\sqrt{\frac{1}{4}+1}=\frac{\sqrt{5}}{2}",
            font_size=36
        ).next_to(desc_14, DOWN, buff=0.28)
        self.play(Write(eq_equal_3))
        self.wait(1.8)

        self.play(FadeOut(desc_14))
        self.play(eq_equal_3.animate.next_to(final_group, DOWN, buff=0.55))

        # ==================== 第六幕：最终结论 ====================
        self.play(FadeOut(eq_equal_3))

        desc_15 = Text("因此，当下列条件成立时取到最大值。", font="KaiTi", font_size=28)
        desc_15.next_to(final_group, DOWN, buff=0.48)
        self.play(Write(desc_15))

        cond_final = MathTex(
            r"a=\frac{1}{2},\qquad b=\frac{\sqrt{5}}{2}",
            font_size=38
        ).set_color(GREEN).next_to(desc_15, DOWN, buff=0.28)
        self.play(Write(cond_final))
        self.wait(1.2)

        result_final = MathTex(
            r"\boxed{\max \frac{ab+2b}{a^2+b^2+1}=\frac{\sqrt{5}}{2}}",
            font_size=40
        ).set_color(YELLOW).next_to(cond_final, DOWN, buff=0.35)
        self.play(FadeIn(result_final, shift=UP))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)
