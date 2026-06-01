from manim import *


class FractionIdentityProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        # 严格按照原题文字和公式进行图文混排，分为三行防止超宽
        t_1 = Text("已知", font="KaiTi", font_size=32)
        m_1 = MathTex(r"\frac{1}{a} + \frac{1}{b} + \frac{1}{c} = \frac{1}{a+b+c}", font_size=38).set_color(BLUE)
        t_2 = Text("，求证：", font="KaiTi", font_size=32)
        line_1 = VGroup(t_1, m_1, t_2).arrange(RIGHT, buff=0.2)

        t_3 = Text("对于任意的正奇数", font="KaiTi", font_size=32)
        m_2 = MathTex(r"n", font_size=36)
        t_4 = Text("，有", font="KaiTi", font_size=32)
        line_2 = VGroup(t_3, m_2, t_4).arrange(RIGHT, buff=0.1)

        line_3 = MathTex(r"\frac{1}{a^n} + \frac{1}{b^n} + \frac{1}{c^n} = \frac{1}{a^n+b^n+c^n}", font_size=42).set_color(YELLOW)

        # 将三行组合居中显示
        title = VGroup(line_1, line_2, line_3).arrange(DOWN, buff=0.4)
        
        self.play(Write(title))
        self.wait(2)
        
        # ==================== 3秒倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=160)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.move_to(ORIGIN)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(title))

        # ==================== 第一幕：代数变形 ====================
        desc_1 = Text("由已知条件出发：", font="KaiTi", font_size=28)
        desc_1.to_edge(UP, buff=0.5)
        self.play(Write(desc_1))

        eq_orig = MathTex(r"\frac{1}{a} + \frac{1}{b} + \frac{1}{c} = \frac{1}{a+b+c}").set_color(BLUE).next_to(desc_1, DOWN, buff=0.3)
        self.play(Write(eq_orig))
        self.wait(1)

        desc_2 = Text("对等式左侧进行通分：", font="KaiTi", font_size=26).next_to(eq_orig, DOWN, buff=0.4)
        self.play(Write(desc_2))

        eq_step1 = MathTex(r"\frac{bc + ac + ab}{abc} = \frac{1}{a+b+c}")
        eq_step1.next_to(desc_2, DOWN, buff=0.3)
        self.play(Write(eq_step1))
        self.wait(1)

        desc_3 = Text("交叉相乘，化分式为整式：", font="KaiTi", font_size=26).next_to(eq_step1, DOWN, buff=0.4)
        self.play(Write(desc_3))

        eq_step2 = MathTex(r"(a+b+c)(ab + bc + ca) = abc")
        eq_step2.set_color(YELLOW)
        eq_step2.next_to(desc_3, DOWN, buff=0.3)
        self.play(ReplacementTransform(eq_step1.copy(), eq_step2))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(desc_1), FadeOut(eq_orig), FadeOut(desc_2), FadeOut(eq_step1), FadeOut(desc_3)
        )
        self.play(eq_step2.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：因式分解 ====================
        desc_4 = Text("移项并对左侧多项式进行因式分解：", font="KaiTi", font_size=26).next_to(eq_step2, DOWN, buff=0.5)
        self.play(Write(desc_4))

        eq_step3 = MathTex(r"(a+b+c)(ab + bc + ca) - abc = 0").next_to(desc_4, DOWN, buff=0.3)
        self.play(Write(eq_step3))
        self.wait(1)

        desc_5 = Text("经过分组提取公因式，可化简为：", font="KaiTi", font_size=26).next_to(eq_step3, DOWN, buff=0.5)
        self.play(Write(desc_5))

        eq_core = MathTex(r"(a+b)(b+c)(c+a) = 0").set_color(GREEN).scale(1.1).next_to(desc_5, DOWN, buff=0.3)
        self.play(TransformMatchingTex(eq_step3.copy(), eq_core))
        
        rect_core = SurroundingRectangle(eq_core, color=GREEN, buff=0.15)
        self.play(Create(rect_core))
        self.wait(1.5)
        
        t_a = Text("由此推断，", font="KaiTi", font_size=26)
        m_a = MathTex(r"a, b, c", font_size=28)
        t_b = Text("中必有两数互为相反数。", font="KaiTi", font_size=26)
        desc_6 = VGroup(t_a, m_a, t_b).arrange(RIGHT, buff=0.1).next_to(eq_core, DOWN, buff=0.5)
        self.play(Write(desc_6))
        self.wait(2)

        # 大清场
        self.play(
            FadeOut(eq_step2), FadeOut(desc_4), FadeOut(eq_step3), FadeOut(desc_5),
            FadeOut(eq_core), FadeOut(rect_core), FadeOut(desc_6)
        )

        # ==================== 第三幕：代入左式验证 ====================
        t_c = Text("根据对称性，不妨设", font="KaiTi", font_size=28)
        m_c = MathTex(r"a = -b", font_size=30).set_color(YELLOW)
        desc_7 = VGroup(t_c, m_c).arrange(RIGHT, buff=0.1).to_edge(UP, buff=1.0)
        self.play(Write(desc_7))

        desc_8 = Text("代入目标等式的左侧：", font="KaiTi", font_size=26).next_to(desc_7, DOWN, buff=0.5)
        self.play(Write(desc_8))

        # 严格分离中文和公式
        t_lhs = Text("左式", font="KaiTi", font_size=26)
        m_lhs = MathTex(r"= \frac{1}{(-b)^n} + \frac{1}{b^n} + \frac{1}{c^n}")
        eq_lhs_1 = VGroup(t_lhs, m_lhs).arrange(RIGHT, buff=0.2).next_to(desc_8, DOWN, buff=0.3)
        self.play(Write(eq_lhs_1))
        self.wait(1)

        t_d = Text("已知", font="KaiTi", font_size=26)
        m_d = MathTex(r"n", font_size=28)
        t_e = Text("为正奇数，负号得以保留：", font="KaiTi", font_size=26)
        desc_9 = VGroup(t_d, m_d, t_e).arrange(RIGHT, buff=0.1).next_to(eq_lhs_1, DOWN, buff=0.5)
        self.play(Write(desc_9))

        eq_lhs_2 = MathTex(r"= -\frac{1}{b^n} + \frac{1}{b^n} + \frac{1}{c^n} = \frac{1}{c^n}").set_color(GREEN).next_to(desc_9, DOWN, buff=0.3)
        self.play(Write(eq_lhs_2))
        self.wait(2)

        # 清场
        self.play(
            FadeOut(desc_7), FadeOut(desc_8), FadeOut(eq_lhs_1), FadeOut(desc_9), FadeOut(eq_lhs_2)
        )

        # ==================== 第四幕：代入右式及最终结论 ====================
        desc_10 = Text("同理，代入目标等式的右侧：", font="KaiTi", font_size=28).to_edge(UP, buff=1.0)
        self.play(Write(desc_10))

        # 严格分离中文和公式
        t_rhs = Text("右式", font="KaiTi", font_size=26)
        m_rhs = MathTex(r"= \frac{1}{(-b)^n + b^n + c^n}")
        eq_rhs_1 = VGroup(t_rhs, m_rhs).arrange(RIGHT, buff=0.2).next_to(desc_10, DOWN, buff=0.5)
        self.play(Write(eq_rhs_1))
        self.wait(1)

        desc_11 = Text("化简得到完全相同的结果：", font="KaiTi", font_size=26).next_to(eq_rhs_1, DOWN, buff=0.5)
        self.play(Write(desc_11))

        eq_rhs_2 = MathTex(r"= \frac{1}{-b^n + b^n + c^n} = \frac{1}{c^n}").set_color(GREEN).next_to(desc_11, DOWN, buff=0.3)
        self.play(Write(eq_rhs_2))
        self.wait(2)

        # 为了防止最底部的结论被切断，先清空推导过程
        self.play(
            FadeOut(desc_10), FadeOut(eq_rhs_1), FadeOut(desc_11), FadeOut(eq_rhs_2)
        )

        desc_12 = Text("左式与右式结果一致，原命题得证：", font="KaiTi", font_size=32).to_edge(UP, buff=2.0)
        self.play(Write(desc_12))

        final_ans = MathTex(r"\frac{1}{a^n} + \frac{1}{b^n} + \frac{1}{c^n} = \frac{1}{a^n+b^n+c^n}").scale(1.3).set_color(YELLOW).next_to(desc_12, DOWN, buff=0.8)
        self.play(FadeIn(final_ans, shift=UP))
        self.wait(3)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)