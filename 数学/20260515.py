from manim import *


class SymmetricPolynomialProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        eq_cover_1 = MathTex(r"x + y + z = 1", font_size=55)
        eq_cover_2 = MathTex(r"x^2 + y^2 + z^2 = 2", font_size=55)
        eq_cover_3 = MathTex(r"x^3 + y^3 + z^3 = 3", font_size=55)
        eq_cover_4 = MathTex(r"x^5 + y^5 + z^5 = ?", font_size=60).set_color(YELLOW)

        cover = VGroup(eq_cover_1, eq_cover_2, eq_cover_3, eq_cover_4).arrange(DOWN, buff=0.6)

        self.play(FadeIn(cover, shift=UP))
        self.wait(1.5)

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

        # ==================== 第一幕：基本对称多项式 ====================
        desc_1_t1 = Text("设", font="KaiTi", font_size=28)
        desc_1_m1 = MathTex(r"S_n = x^n + y^n + z^n", font_size=30).set_color(BLUE)
        desc_1_t2 = Text("，引入三个基本对称多项式：", font="KaiTi", font_size=28)
        desc_1 = VGroup(desc_1_t1, desc_1_m1, desc_1_t2).arrange(RIGHT, buff=0.1).to_edge(UP, buff=0.3)
        self.play(Write(desc_1))

        eq_e = MathTex(
            r"e_1 = x+y+z = 1, \quad e_2 = xy+yz+zx, \quad e_3 = xyz"
        ).set_color(YELLOW).next_to(desc_1, DOWN, buff=0.4)
        self.play(Write(eq_e))
        self.wait(1)

        desc_2 = Text("利用完全平方公式求二阶对称式：", font="KaiTi", font_size=28).next_to(eq_e, DOWN, buff=0.5)
        self.play(Write(desc_2))

        eq_e2 = MathTex(
            r"e_1^2 = S_2 + 2e_2 \implies 1 = 2 + 2e_2 \implies e_2 = -\frac{1}{2}"
        ).next_to(desc_2, DOWN, buff=0.3)
        self.play(Write(eq_e2))
        self.wait(1.5)

        # 核心防溢出操作 1：清空说明文字，公式整体上移腾出空间
        self.play(FadeOut(desc_1), FadeOut(desc_2))
        self.play(VGroup(eq_e, eq_e2).animate.to_edge(UP, buff=0.3))

        desc_3 = Text("利用三次恒等式求三阶对称式：", font="KaiTi", font_size=28).next_to(eq_e2, DOWN, buff=0.5)
        self.play(Write(desc_3))

        eq_e3 = MathTex(
            r"S_3 - 3e_3 = e_1(S_2 - e_2) \implies 3 - 3e_3 = \frac{5}{2} \implies e_3 = \frac{1}{6}"
        ).next_to(desc_3, DOWN, buff=0.3)
        self.play(Write(eq_e3))
        self.wait(2)

        # 屏幕清理，保留最终特征结论
        self.play(
            FadeOut(eq_e), FadeOut(eq_e2), FadeOut(desc_3), FadeOut(eq_e3)
        )

        eq_e_final = MathTex(
            r"e_1 = 1, \quad e_2 = -\frac{1}{2}, \quad e_3 = \frac{1}{6}"
        ).set_color(YELLOW).to_edge(UP, buff=0.4)
        self.play(FadeIn(eq_e_final, shift=UP))
        self.wait(1)

        # ==================== 第二幕：韦达定理与特征方程 ====================
        desc_4_t1 = Text("根据", font="KaiTi", font_size=28)
        desc_4_t2 = Text("韦达定理", font="KaiTi", font_size=28, weight=BOLD).set_color(RED)
        desc_4_t3 = Text("，构造以这三个变量为根的方程：", font="KaiTi", font_size=28)
        desc_4 = VGroup(desc_4_t1, desc_4_t2, desc_4_t3).arrange(RIGHT, buff=0.1).next_to(eq_e_final, DOWN, buff=0.6)
        self.play(Write(desc_4))

        eq_vieta = MathTex(r"t^3 - e_1t^2 + e_2t - e_3 = 0").set_color(GREEN).next_to(desc_4, DOWN, buff=0.3)
        self.play(Write(eq_vieta))
        self.wait(1.5)

        # 核心防溢出操作 2：删掉文字，保留公式紧凑排列
        self.play(FadeOut(desc_4))
        self.play(eq_vieta.animate.next_to(eq_e_final, DOWN, buff=0.4))

        desc_5 = Text("代入具体数值，并移项保留最高次幂：", font="KaiTi", font_size=28).next_to(eq_vieta, DOWN, buff=0.5)
        self.play(Write(desc_5))

        eq_char = MathTex(r"t^3 = t^2 + \frac{1}{2}t + \frac{1}{6}").scale(1.1).set_color(GREEN).next_to(desc_5, DOWN,
                                                                                                         buff=0.3)
        self.play(Write(eq_char))

        rect_char = SurroundingRectangle(eq_char, color=GREEN, buff=0.15)
        self.play(Create(rect_char))
        self.wait(2)

        # 清屏准备推导递推式
        self.play(
            FadeOut(eq_e_final), FadeOut(eq_vieta), FadeOut(desc_5)
        )
        char_group = VGroup(eq_char, rect_char)
        self.play(char_group.animate.to_edge(UP, buff=0.3))

        # ==================== 第三幕：详细展开纵向求和 ====================
        desc_7_t1 = Text("代入根", font="KaiTi", font_size=28)
        desc_7_m1 = MathTex(r"x", font_size=30).set_color(BLUE)
        desc_7_t2 = Text("，并在等式两端同乘", font="KaiTi", font_size=28)
        desc_7_m2 = MathTex(r"x^{n-3}", font_size=30).set_color(YELLOW)
        desc_7_t3 = Text("：", font="KaiTi", font_size=28)
        desc_7 = VGroup(desc_7_t1, desc_7_m1, desc_7_t2, desc_7_m2, desc_7_t3).arrange(RIGHT, buff=0.1).next_to(
            char_group, DOWN, buff=0.5)
        self.play(Write(desc_7))

        eq_x = MathTex(r"x^n = x^{n-1} + \frac{1}{2}x^{n-2} + \frac{1}{6}x^{n-3}").set_color(BLUE).next_to(desc_7, DOWN,
                                                                                                           buff=0.3)
        self.play(Write(eq_x))
        self.wait(1.5)

        # 核心防溢出操作 3：彻底淡出上方冗余信息，让推导居中
        self.play(FadeOut(char_group), FadeOut(desc_7))
        self.play(eq_x.animate.move_to(UP * 1.5))

        desc_8 = Text("同理，变量 y, z 亦满足完全相同结构的等式：", font="KaiTi", font_size=28).next_to(eq_x, DOWN,
                                                                                                      buff=0.5)
        self.play(Write(desc_8))

        eq_y = MathTex(r"y^n = y^{n-1} + \frac{1}{2}y^{n-2} + \frac{1}{6}y^{n-3}").set_color(BLUE)
        eq_z = MathTex(r"z^n = z^{n-1} + \frac{1}{2}z^{n-2} + \frac{1}{6}z^{n-3}").set_color(BLUE)

        # 初始暂放在文字下方
        VGroup(eq_y, eq_z).arrange(DOWN, buff=0.3).next_to(desc_8, DOWN, buff=0.4)
        self.play(Write(eq_y), Write(eq_z))
        self.wait(1.5)

        # 再次淡出过渡文字，并将三个等式极度紧凑地排在一起
        eq_system = VGroup(eq_x, eq_y, eq_z)
        self.play(
            FadeOut(desc_8),
            eq_system.animate.arrange(DOWN, buff=0.25).move_to(UP * 1.0)
        )
        self.wait(0.5)

        plus_sign = MathTex(r"+").next_to(eq_system, LEFT, buff=0.3)
        sum_line = Line(start=eq_system.get_left() + LEFT * 0.8 + DOWN * 0.2,
                        end=eq_system.get_right() + RIGHT * 0.2 + DOWN * 0.2)
        sum_line.next_to(eq_system, DOWN, buff=0.1)

        self.play(Write(plus_sign), Create(sum_line))

        desc_9 = Text("纵向相加，即导出线性递推关系：", font="KaiTi", font_size=28).next_to(sum_line, DOWN, buff=0.4)
        self.play(Write(desc_9))

        eq_recurrence = MathTex(
            r"S_n = S_{n-1} + \frac{1}{2}S_{n-2} + \frac{1}{6}S_{n-3}"
        ).scale(1.2).set_color(YELLOW).next_to(desc_9, DOWN, buff=0.3)
        self.play(Write(eq_recurrence))
        self.wait(2)

        # ==================== 第四幕：求解最终数值 ====================
        self.play(
            FadeOut(eq_system), FadeOut(plus_sign),
            FadeOut(sum_line), FadeOut(desc_9)
        )
        self.play(eq_recurrence.animate.to_edge(UP, buff=0.6))

        desc_10 = Text("依次代入初值计算低阶项：", font="KaiTi", font_size=28).next_to(eq_recurrence, DOWN, buff=0.6)
        self.play(Write(desc_10))

        # 核心防溢出操作 4：改为单行长等式，极大节省垂直空间
        eq_s4 = MathTex(
            r"S_4 = S_3 + \frac{1}{2}S_2 + \frac{1}{6}S_1 = 3 + 1 + \frac{1}{6} = \frac{25}{6}"
        ).next_to(desc_10, DOWN, buff=0.6)
        self.play(Write(eq_s4))
        self.wait(1.5)

        eq_s5 = MathTex(
            r"S_5 = S_4 + \frac{1}{2}S_3 + \frac{1}{6}S_2 = \frac{25}{6} + \frac{3}{2} + \frac{2}{6} = 6"
        ).next_to(eq_s4, DOWN, buff=0.6)
        self.play(Write(eq_s5))
        self.wait(2)

        # ==================== 结局 ====================
        self.play(
            FadeOut(eq_recurrence), FadeOut(desc_10), FadeOut(eq_s4), FadeOut(eq_s5)
        )

        desc_11 = Text("原方程组的五次幂求和结果为：", font="KaiTi", font_size=35).to_edge(UP, buff=2.5)
        self.play(Write(desc_11))

        final_ans = MathTex(r"x^5 + y^5 + z^5 = 6").scale(1.5).set_color(YELLOW).next_to(desc_11, DOWN, buff=1)
        self.play(FadeIn(final_ans, shift=UP))
        self.wait(4)

        # 散场
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(1)