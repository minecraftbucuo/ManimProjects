from manim import *

class AlgebraMaxProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("求代数式最大值的两种方法", font="KaiTi", font_size=45)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"\max \frac{xy + 2yz}{x^2 + y^2 + z^2}",
            font_size=60
        ).set_color(BLUE)

        # 整体上移，给下方的倒计时留出绝对安全的空间
        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1).move_to(UP * 1.5)
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))
        
        # ==================== 3秒倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=150)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.move_to(DOWN * 1.5) # 放置在屏幕中下方
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 方法一：基本不等式与待定系数法 ====================
        title_method1 = Text("方法一：基本不等式与待定系数法", font="KaiTi", font_size=35).to_edge(UP, buff=0.8)
        self.play(Write(title_method1))

        # 步骤 1.1
        desc_1_t1 = Text("引入待定常数", font="KaiTi", font_size=28)
        desc_1_m = MathTex(r"a>0, b>0", font_size=30)
        desc_1_t2 = Text("，对分子各项进行放缩：", font="KaiTi", font_size=28)
        desc_1 = VGroup(desc_1_t1, desc_1_m, desc_1_t2).arrange(RIGHT, buff=0.1).next_to(title_method1, DOWN, buff=0.5)
        self.play(Write(desc_1))

        eq_1 = MathTex(r"xy \le \frac{a}{2}x^2 + \frac{1}{2a}y^2").set_color(BLUE).next_to(desc_1, DOWN, buff=0.4)
        eq_2 = MathTex(r"2yz \le \frac{b}{2}y^2 + \frac{2}{b}z^2").set_color(BLUE).next_to(eq_1, DOWN, buff=0.4)
        self.play(Write(eq_1))
        self.play(Write(eq_2))
        self.wait(2)

        # 清理步骤 1.1
        self.play(FadeOut(desc_1), FadeOut(eq_1), FadeOut(eq_2))

        # 步骤 1.2
        desc_2 = Text("将两式相加，并提取同类项：", font="KaiTi", font_size=28).next_to(title_method1, DOWN, buff=0.5)
        self.play(Write(desc_2))

        eq_3 = MathTex(r"xy + 2yz \le \frac{a}{2}x^2 + \left(\frac{1}{2a} + \frac{b}{2}\right)y^2 + \frac{2}{b}z^2").set_color(YELLOW).next_to(desc_2, DOWN, buff=0.4)
        self.play(Write(eq_3))
        self.wait(1.5)

        desc_3_t1 = Text("为配凑出分母，令各项系数均等于", font="KaiTi", font_size=28)
        desc_3_m = MathTex(r"k", font_size=30)
        desc_3_t2 = Text("：", font="KaiTi", font_size=28)
        desc_3 = VGroup(desc_3_t1, desc_3_m, desc_3_t2).arrange(RIGHT, buff=0.1).next_to(eq_3, DOWN, buff=0.6)
        self.play(Write(desc_3))

        eq_4 = MathTex(r"\frac{a}{2} = \frac{1}{2a} + \frac{b}{2} = \frac{2}{b} = k").set_color(GREEN).next_to(desc_3, DOWN, buff=0.4)
        self.play(Write(eq_4))
        self.wait(2)

        # 清理步骤 1.2
        self.play(FadeOut(desc_2), FadeOut(eq_3), FadeOut(desc_3), FadeOut(eq_4))

        # 步骤 1.3
        desc_4 = Text("解上述连等式，由左右两端可得：", font="KaiTi", font_size=28).next_to(title_method1, DOWN, buff=0.5)
        self.play(Write(desc_4))

        eq_5 = MathTex(r"a = 2k, \quad b = \frac{2}{k}").set_color(GREEN).next_to(desc_4, DOWN, buff=0.4)
        self.play(Write(eq_5))
        self.wait(1)

        desc_5 = Text("代入中间等式进行求解：", font="KaiTi", font_size=28).next_to(eq_5, DOWN, buff=0.6)
        self.play(Write(desc_5))

        eq_6 = MathTex(r"\frac{1}{2(2k)} + \frac{2/k}{2} = k \implies k^2 = \frac{5}{4}").set_color(BLUE).next_to(desc_5, DOWN, buff=0.4)
        self.play(Write(eq_6))
        self.wait(1.5)

        # 清理准备展示方法一结论
        self.play(FadeOut(desc_4), FadeOut(eq_5), FadeOut(desc_5), FadeOut(eq_6))

        desc_6_t1 = Text("取正值，即可得到最大值", font="KaiTi", font_size=28)
        desc_6_m = MathTex(r"k", font_size=30)
        desc_6_t2 = Text("：", font="KaiTi", font_size=28)
        desc_6 = VGroup(desc_6_t1, desc_6_m, desc_6_t2).arrange(RIGHT, buff=0.1).next_to(title_method1, DOWN, buff=1)
        self.play(Write(desc_6))

        ans_1 = MathTex(r"k = \frac{\sqrt{5}}{2}").scale(1.5).set_color(YELLOW).next_to(desc_6, DOWN, buff=0.6)
        self.play(FadeIn(ans_1, shift=UP))
        self.wait(2.5)

        # 彻底清场
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 方法二：柯西不等式与基本不等式 ====================
        title_method2 = Text("方法二：柯西不等式与换元法", font="KaiTi", font_size=35).to_edge(UP, buff=0.8)
        self.play(Write(title_method2))

        # 步骤 2.1
        desc_7_t1 = Text("提取分子中的公因式", font="KaiTi", font_size=28)
        desc_7_m = MathTex(r"y", font_size=30)
        desc_7_t2 = Text("：", font="KaiTi", font_size=28)
        desc_7 = VGroup(desc_7_t1, desc_7_m, desc_7_t2).arrange(RIGHT, buff=0.1).next_to(title_method2, DOWN, buff=0.5)
        self.play(Write(desc_7))

        eq_7 = MathTex(r"xy + 2yz = y(x + 2z)").set_color(BLUE).next_to(desc_7, DOWN, buff=0.4)
        self.play(Write(eq_7))
        self.wait(1.5)

        desc_8_t1 = Text("对含有", font="KaiTi", font_size=28)
        desc_8_m1 = MathTex(r"x", font_size=30)
        desc_8_t2 = Text("与", font="KaiTi", font_size=28)
        desc_8_m2 = MathTex(r"z", font_size=30)
        desc_8_t3 = Text("的部分单独使用二维柯西不等式：", font="KaiTi", font_size=28)
        desc_8 = VGroup(desc_8_t1, desc_8_m1, desc_8_t2, desc_8_m2, desc_8_t3).arrange(RIGHT, buff=0.1).next_to(eq_7, DOWN, buff=0.6)
        self.play(Write(desc_8))

        eq_8 = MathTex(r"(x + 2z)^2 \le (1^2 + 2^2)(x^2 + z^2) = 5(x^2 + z^2)").set_color(GREEN).next_to(desc_8, DOWN, buff=0.4)
        self.play(Write(eq_8))
        self.wait(2)

        # 清理步骤 2.1
        self.play(FadeOut(desc_7), FadeOut(eq_7), FadeOut(desc_8), FadeOut(eq_8))

        # 步骤 2.2
        desc_9 = Text("两边开平方，并代回原分式之中：", font="KaiTi", font_size=28).next_to(title_method2, DOWN, buff=0.5)
        self.play(Write(desc_9))

        eq_9 = MathTex(r"\frac{y(x + 2z)}{x^2 + y^2 + z^2} \le \frac{\sqrt{5}y\sqrt{x^2 + z^2}}{x^2 + y^2 + z^2}").set_color(YELLOW).next_to(desc_9, DOWN, buff=0.4)
        self.play(Write(eq_9))
        self.wait(1.5)

        desc_10_t1 = Text("为简化结构，令", font="KaiTi", font_size=28)
        desc_10_m = MathTex(r"t = \sqrt{x^2 + z^2}", font_size=30)
        desc_10_t2 = Text("，进行整体换元：", font="KaiTi", font_size=28)
        desc_10 = VGroup(desc_10_t1, desc_10_m, desc_10_t2).arrange(RIGHT, buff=0.1).next_to(eq_9, DOWN, buff=0.6)
        self.play(Write(desc_10))

        eq_10 = MathTex(r"\frac{\sqrt{5}yt}{y^2 + t^2}").set_color(BLUE).scale(1.2).next_to(desc_10, DOWN, buff=0.4)
        self.play(TransformMatchingTex(eq_9.copy(), eq_10))
        self.wait(2)

        # 清理步骤 2.2
        self.play(FadeOut(desc_9), FadeOut(eq_9), FadeOut(desc_10))
        self.play(eq_10.animate.next_to(title_method2, DOWN, buff=0.5))

        # 步骤 2.3
        desc_11_t1 = Text("最后，再次利用基本不等式", font="KaiTi", font_size=28)
        desc_11_m = MathTex(r"y^2 + t^2 \ge 2yt", font_size=30)
        desc_11_t2 = Text("放缩分母：", font="KaiTi", font_size=28)
        desc_11 = VGroup(desc_11_t1, desc_11_m, desc_11_t2).arrange(RIGHT, buff=0.1).next_to(eq_10, DOWN, buff=0.6)
        self.play(Write(desc_11))

        eq_11 = MathTex(r"\frac{\sqrt{5}yt}{y^2 + t^2} \le \frac{\sqrt{5}yt}{2yt} = \frac{\sqrt{5}}{2}").set_color(YELLOW).next_to(desc_11, DOWN, buff=0.4)
        self.play(Write(eq_11))
        self.wait(2.5)

        # 彻底清场
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 最终总结 ====================
        outro_1 = Text("综上所述，两种解法从不同角度切入", font="KaiTi", font_size=40).move_to(UP * 0.8)
        self.play(Write(outro_1))
        
        outro_2 = Text("最终求得该代数式的最大值均为：", font="KaiTi", font_size=30).next_to(outro_1, DOWN, buff=0.8)
        self.play(Write(outro_2))

        final_ans = MathTex(r"\frac{\sqrt{5}}{2}").scale(2).set_color(YELLOW).next_to(outro_2, DOWN, buff=0.6)
        self.play(FadeIn(final_ans, shift=UP))
        self.wait(3)

        # ==================== 散场 ====================
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(1)