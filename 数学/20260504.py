from manim import *


class SumOfDivisorsProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("如何求一个数所有因子的和？", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"\sigma(n) = \quad ?",
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

        # ==================== 第一幕：单一结构 ====================
        t1_1 = Text("从最简单的结构开始，假设", font="KaiTi", font_size=30)
        m1_1 = MathTex(r"n = p^a", font_size=36).set_color(BLUE)
        desc_1 = VGroup(t1_1, m1_1).arrange(RIGHT, buff=0.15)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        t1_2 = Text("它的因子非常规律：", font="KaiTi", font_size=28)
        m1_2 = MathTex(r"1, \ p, \ p^2, \ \dots, \ p^a", font_size=36).set_color(YELLOW)
        desc_2 = VGroup(t1_2, m1_2).arrange(RIGHT, buff=0.15).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(desc_2))
        self.wait(1.5)

        desc_3 = Text("求和？直接用等比数列求和公式：", font="KaiTi", font_size=28).next_to(desc_2, DOWN, buff=0.5)
        self.play(Write(desc_3))

        eq_gp = MathTex(r"S = 1 + p + p^2 + \dots + p^a = \frac{p^{a+1} - 1}{p - 1}").set_color(GREEN)
        eq_gp.next_to(desc_3, DOWN, buff=0.4)
        self.play(Write(eq_gp))
        self.wait(2)

        # 整理屏幕
        self.play(FadeOut(desc_1), FadeOut(desc_2), FadeOut(desc_3))
        self.play(eq_gp.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：乘法分配律的奇迹 ====================
        t2_1 = Text("难度升级，引入两个素数：", font="KaiTi", font_size=30)
        m2_1 = MathTex(r"n = p^a q^b", font_size=36).set_color(BLUE)
        desc_4 = VGroup(t2_1, m2_1).arrange(RIGHT, buff=0.15).next_to(eq_gp, DOWN, buff=0.6)
        self.play(Write(desc_4))

        t2_2 = Text("因子是两者的自由组合，排成矩阵：", font="KaiTi", font_size=28).next_to(desc_4, DOWN, buff=0.5)
        self.play(Write(t2_2))

        # 矩阵展示
        matrix_tex = MathTex(
            r"\begin{bmatrix} 1 & q & \cdots & q^b \\ p & pq & \cdots & pq^b \\ \vdots & \vdots & \ddots & \vdots \\ p^a & p^aq & \cdots & p^aq^b \end{bmatrix}"
        ).set_color(YELLOW).scale(0.9)
        matrix_tex.next_to(t2_2, DOWN, buff=0.4)
        self.play(Write(matrix_tex))
        self.wait(1.5)

        t2_3 = Text("这该如何求和？提取公因数！", font="KaiTi", font_size=30).set_color(RED).next_to(matrix_tex, DOWN,
                                                                                                     buff=0.5)
        self.play(Write(t2_3))
        self.wait(1)

        # 淡出矩阵和说明文字，腾出纵向空间
        self.play(FadeOut(matrix_tex), FadeOut(t2_2), FadeOut(eq_gp), FadeOut(t2_1), FadeOut(m2_1))
        self.play(t2_3.animate.move_to(ORIGIN + UP * 1.8))

        # 逐行分析
        t_row1_1 = Text("第一行：", font="KaiTi", font_size=26)
        m_row1_1 = MathTex(r"1 + q + q^2 + \dots + q^b", font_size=30).set_color(YELLOW)
        row1 = VGroup(t_row1_1, m_row1_1).arrange(RIGHT, buff=0.1).next_to(t2_3, DOWN, buff=0.5)

        t_row2_1 = Text("第二行：", font="KaiTi", font_size=26)
        m_row2_1 = MathTex(r"p", font_size=30).set_color(BLUE)
        m_row2_2 = MathTex(r"\times (1 + q + q^2 + \dots + q^b)", font_size=30).set_color(YELLOW)
        row2 = VGroup(t_row2_1, m_row2_1, m_row2_2).arrange(RIGHT, buff=0.1).next_to(row1, DOWN, buff=0.3)

        t_row3_1 = Text("依此类推...", font="KaiTi", font_size=26)
        row3 = VGroup(t_row3_1).next_to(row2, DOWN, buff=0.3)

        self.play(Write(row1), Write(row2), Write(row3))
        self.wait(1)

        desc_factor = Text("整理后可得：", font="KaiTi", font_size=32).set_color_by_gradient(GREEN,
                                                                                                        YELLOW).next_to(
            row3, DOWN, buff=0.5)
        self.play(Write(desc_factor))

        eq_factor = MathTex(r"S = (1 + p + \dots + p^a) \times (1 + q + \dots + q^b)").set_color(GREEN).scale(1.1)
        eq_factor.next_to(desc_factor, DOWN, buff=0.4)
        self.play(Write(eq_factor))
        self.wait(2)

        # 大清场，保留核心逻辑
        self.play(
            FadeOut(row1), FadeOut(row2), FadeOut(t2_3),
            FadeOut(row3), FadeOut(desc_factor)
        )
        self.play(eq_factor.animate.to_edge(UP, buff=0.8))

        # ==================== 第三幕：推广到一般情况 ====================
        t3_1 = Text("推广到任意正整数：", font="KaiTi", font_size=30)
        m3_1 = MathTex(r"n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}", font_size=36).set_color(BLUE)
        desc_5 = VGroup(t3_1, m3_1).arrange(RIGHT, buff=0.15).next_to(eq_factor, DOWN, buff=0.6)
        self.play(Write(desc_5))
        self.wait(1)

        t3_2 = Text("因子和等于各维度之和的乘积：", font="KaiTi", font_size=30).next_to(desc_5, DOWN, buff=0.5)
        self.play(Write(t3_2))

        eq_general = MathTex(r"\sigma(n) = \prod_{i=1}^{k} \frac{p_i^{a_i+1} - 1}{p_i - 1}").set_color(YELLOW).scale(
            1.2)
        eq_general.next_to(t3_2, DOWN, buff=0.5)

        rect_general = SurroundingRectangle(eq_general, color=YELLOW, buff=0.2)
        self.play(Write(eq_general), Create(rect_general))
        self.wait(2)

        # 全屏暴力清场
        self.play(
            FadeOut(eq_factor), FadeOut(desc_5), FadeOut(t3_2), FadeOut(eq_general), FadeOut(rect_general)
        )

        # ==================== 第四幕：实战与升华 ====================
        t4_1 = Text("以", font="KaiTi", font_size=35)
        m4_1 = MathTex(r"n = 12", font_size=40).set_color(BLUE)
        t4_2 = Text("为例感受力量：", font="KaiTi", font_size=35)
        desc_6 = VGroup(t4_1, m4_1, t4_2).arrange(RIGHT, buff=0.15).to_edge(UP, buff=1.5)
        self.play(Write(desc_6))

        # 暴力法
        t_vio = Text("暴力法：", font="KaiTi", font_size=28).set_color(RED)
        m_vio = MathTex(r"1+2+3+4+6+12 = 28", font_size=32)
        vio_group = VGroup(t_vio, m_vio).arrange(RIGHT, buff=0.2).shift(UP * 0.5 + LEFT * 2)
        self.play(Write(vio_group))

        # 结构法
        t_str = Text("结构法：", font="KaiTi", font_size=28).set_color(GREEN)
        m_str = MathTex(r"(1+2+4) \times (1+3) = 28", font_size=32)
        str_group = VGroup(t_str, m_str).arrange(RIGHT, buff=0.2).next_to(vio_group, DOWN, buff=0.6, aligned_edge=LEFT)
        self.play(Write(str_group))
        self.wait(2)

        # 全屏清空，进入结尾升华
        self.play(
            FadeOut(desc_6), FadeOut(vio_group), FadeOut(str_group)
        )

        t_final_1 = Text("更深一层的启发：", font="KaiTi", font_size=35).to_edge(UP, buff=2)
        self.play(Write(t_final_1))
        self.wait(1)

        m_final = MathTex(r"\sigma(ab) = \sigma(a)\sigma(b)").scale(1.2).set_color_by_gradient(BLUE, GREEN).next_to(
            t_final_1, DOWN, buff=0.8)
        self.play(Write(m_final))
        self.wait(1)

        t_final_2 = Text("这叫做", font="KaiTi", font_size=30).next_to(m_final, DOWN, buff=0.8)
        m_final_2 = Text("积性函数", font="KaiTi", font_size=50).set_color(YELLOW).next_to(t_final_2, RIGHT, buff=0.2)
        self.play(Write(t_final_2), Write(m_final_2))
        self.wait(2)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)