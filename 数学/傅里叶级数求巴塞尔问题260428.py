from manimlib import *


class BaselFourierProof(Scene):
    def construct(self):
        # ==================== 封面与倒计时 ====================
        title = Text("如何用傅里叶级数证明巴塞尔问题？", font="KaiTi", font_size=50)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW)

        series = Tex(
            r"\sum_{n=1}^{\infty} \frac{1}{n^2} = 1 + \frac{1}{4} + \frac{1}{9} + \cdots = \frac{\pi^2}{6}",
            font_size=50
        )
        series.set_color_by_gradient(GREEN, BLUE, YELLOW)

        cover = VGroup(title, series).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(Write(series))
        self.wait(2)

        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=180)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.move_to(ORIGIN)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)

        self.play(FadeOut(cover))

        # ==================== 场景一：傅里叶展开与常数项 (已完美恢复) ====================
        hint_1 = VGroup(
            Text("考虑将函数 ", font="KaiTi", font_size=32),
            Tex(r"f(x) = x^2", font_size=35).set_color(YELLOW),
            Text(" 在区间 ", font="KaiTi", font_size=32),
            Tex(r"(-\pi, \pi)", font_size=35).set_color(GREEN),
            Text(" 展开：", font="KaiTi", font_size=32)
        ).arrange(RIGHT, buff=0.1).to_edge(UP, buff=0.6)
        self.play(Write(hint_1))

        eq_fourier = Tex(
            r"x^2 = \frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx)"
        ).set_color(BLUE).next_to(hint_1, DOWN, buff=0.4)
        self.play(Write(eq_fourier))
        self.wait(1.5)

        hint_2 = Text("首先计算常数项：", font="KaiTi", font_size=30).next_to(eq_fourier, DOWN, buff=0.6)
        self.play(Write(hint_2))

        eq_a0_step1 = Tex(
            r"a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} x^2 dx = \frac{1}{\pi} \left[ \frac{x^3}{3} \right]_{-\pi}^{\pi}"
        ).scale(0.85).next_to(hint_2, DOWN, buff=0.4)

        eq_a0_step2 = Tex(
            r"a_0 = \frac{2\pi^2}{3} \quad \Rightarrow \quad \frac{a_0}{2} = \frac{\pi^2}{3}"
        ).set_color(YELLOW).scale(0.9).move_to(eq_a0_step1)

        self.play(Write(eq_a0_step1))
        self.wait(1.5)
        self.play(TransformMatchingTex(eq_a0_step1, eq_a0_step2))
        self.wait(1.5)

        # 【排版控制】：淡出前两句文本，保留常数项结果在顶部
        self.play(FadeOut(hint_1), FadeOut(hint_2), FadeOut(eq_fourier))
        self.play(eq_a0_step2.animate.to_edge(UP, buff=0.5))

        # ==================== 场景二：奇偶性秒杀正弦项 bn ====================
        hint_3 = VGroup(
            Text("接下来计算正弦项系数 ", font="KaiTi", font_size=30),
            Tex("b_n", font_size=35).set_color(RED),
            Text(" ：", font="KaiTi", font_size=30)
        ).arrange(RIGHT, buff=0.1).next_to(eq_a0_step2, DOWN, buff=0.6)
        self.play(Write(hint_3))

        eq_bn = Tex(
            r"b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} x^2 \sin nx dx = 0"
        ).set_color(RED).scale(0.9).next_to(hint_3, DOWN, buff=0.3)

        note_bn = Text("（奇函数在对称区间积分为 0）", font="KaiTi", font_size=24, color=GREY).next_to(eq_bn, DOWN,
                                                                                                     buff=0.3)

        self.play(Write(eq_bn), Write(note_bn))
        self.wait(1.5)

        # 清理屏幕，为最难的 an 腾出完整空间
        self.play(FadeOut(eq_a0_step2), FadeOut(hint_3), FadeOut(eq_bn), FadeOut(note_bn))

        # ==================== 场景三：死磕余弦项 a_n (超详细两次分部积分) ====================
        hint_4 = VGroup(
            Text("核心难点：计算余弦项系数 ", font="KaiTi", font_size=32),
            Tex("a_n", font_size=35).set_color(GREEN),
            Text(" （需两次分部积分）", font="KaiTi", font_size=32)
        ).arrange(RIGHT, buff=0.1).to_edge(UP, buff=0.6)
        self.play(Write(hint_4))

        eq_an_start = Tex(
            r"a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} x^2 \cos nx dx"
        ).set_color(GREEN).next_to(hint_4, DOWN, buff=0.5)
        self.play(Write(eq_an_start))
        self.wait(1)

        # 严格混合排版 1
        hint_part1 = VGroup(
            Text("第一次分部积分：令 ", font="KaiTi", font_size=24, color=GREY),
            Tex(r"u=x^2, \ dv=\cos(nx)dx", font_size=24, color=GREY)
        ).arrange(RIGHT, buff=0.1).next_to(eq_an_start, DOWN, buff=0.4)
        self.play(Write(hint_part1))

        eq_an_step1 = Tex(
            r"= \frac{1}{\pi} \left( \left[ x^2 \frac{\sin nx}{n} \right]_{-\pi}^{\pi} - \int_{-\pi}^{\pi} 2x \frac{\sin nx}{n} dx \right)"
        ).scale(0.85).next_to(hint_part1, DOWN, buff=0.4)
        self.play(Write(eq_an_step1))
        self.wait(1.5)

        # 严格混合排版 2
        note_zero1 = VGroup(
            Text("代入 ", font="KaiTi", font_size=24, color=YELLOW),
            Tex(r"\pm\pi", font_size=24, color=YELLOW),
            Text(" 时，", font="KaiTi", font_size=24, color=YELLOW),
            Tex(r"\sin(\pm n\pi)", font_size=24, color=YELLOW),
            Text(" 均为 0", font="KaiTi", font_size=24, color=YELLOW)
        ).arrange(RIGHT, buff=0.1).next_to(eq_an_step1, RIGHT, buff=0.5)
        self.play(Write(note_zero1))

        # 画红叉
        cross_line = Line(eq_an_step1[0][4:14].get_corner(DL), eq_an_step1[0][4:14].get_corner(UR), color=RED)
        self.play(ShowCreation(cross_line))
        self.wait(1)

        eq_an_step2 = Tex(
            r"= - \frac{2}{n\pi} \int_{-\pi}^{\pi} x \sin nx dx"
        ).scale(0.9).set_color(BLUE).next_to(eq_an_step1, DOWN, buff=0.4)
        self.play(ReplacementTransform(eq_an_step1.copy(), eq_an_step2))
        self.wait(2)

        # 把第一次降次的结果推到最上面
        self.play(FadeOut(hint_4), FadeOut(eq_an_start), FadeOut(hint_part1), FadeOut(eq_an_step1), FadeOut(note_zero1),
                  FadeOut(cross_line))
        self.play(eq_an_step2.animate.to_edge(UP, buff=0.8))

        # 严格混合排版 3
        hint_part2 = VGroup(
            Text("成功降次！对剩余部分进行第二次分部积分：令 ", font="KaiTi", font_size=24, color=GREY),
            Tex(r"u=x, \ dv=\sin(nx)dx", font_size=24, color=GREY)
        ).arrange(RIGHT, buff=0.1).next_to(eq_an_step2, DOWN, buff=0.4)
        self.play(Write(hint_part2))

        eq_an_step3 = Tex(
            r"= - \frac{2}{n\pi} \left( \left[ -x \frac{\cos nx}{n} \right]_{-\pi}^{\pi} - \int_{-\pi}^{\pi} \left(-\frac{\cos nx}{n}\right) dx \right)"
        ).scale(0.85).next_to(hint_part2, DOWN, buff=0.4)
        self.play(Write(eq_an_step3))
        self.wait(1.5)

        note_zero2 = Text("余弦在一个整周期内积分为 0", font="KaiTi", font_size=24, color=YELLOW).next_to(eq_an_step3,
                                                                                                          DOWN,
                                                                                                          buff=0.3)
        self.play(Write(note_zero2))

        # 画红叉 2
        cross_line2 = Line(eq_an_step3[0][17:30].get_corner(DL), eq_an_step3[0][17:30].get_corner(UR), color=RED)
        self.play(ShowCreation(cross_line2))
        self.wait(1)

        eq_an_step4 = Tex(
            r"= \frac{2}{n^2\pi} \left[ x \cos nx \right]_{-\pi}^{\pi}"
        ).scale(0.9).next_to(note_zero2, DOWN, buff=0.4)
        self.play(ReplacementTransform(eq_an_step3.copy(), eq_an_step4))
        self.wait(1)

        # 留空给最后的上下限计算
        self.play(FadeOut(eq_an_step2), FadeOut(hint_part2), FadeOut(eq_an_step3), FadeOut(note_zero2),
                  FadeOut(cross_line2))
        self.play(eq_an_step4.animate.to_edge(UP, buff=1.0))

        eq_an_step5 = Tex(
            r"= \frac{2}{n^2\pi} \Big( \pi \cos(n\pi) - (-\pi) \cos(-n\pi) \Big)"
        ).scale(0.9).next_to(eq_an_step4, DOWN, buff=0.5)
        self.play(Write(eq_an_step5))
        self.wait(1)

        # 严格混合排版 4
        note_cos = VGroup(
            Text("因为 ", font="KaiTi", font_size=26, color=YELLOW),
            Tex(r"\cos(n\pi) = \cos(-n\pi) = (-1)^n", font_size=26, color=YELLOW)
        ).arrange(RIGHT, buff=0.1).next_to(eq_an_step5, DOWN, buff=0.4)
        self.play(Write(note_cos))

        eq_an_final = Tex(
            r"a_n = \frac{2}{n^2\pi} \Big( 2\pi (-1)^n \Big) = \frac{4(-1)^n}{n^2}"
        ).set_color(GREEN).scale(1.1).next_to(note_cos, DOWN, buff=0.5)
        self.play(TransformMatchingTex(eq_an_step5.copy(), eq_an_final))

        box_an = SurroundingRectangle(eq_an_final, color=GREEN)
        self.play(ShowCreation(box_an))
        self.wait(3)

        self.play(FadeOut(VGroup(eq_an_step4, eq_an_step5, note_cos, eq_an_final, box_an)))

        # ==================== 场景四：组装展开式与特殊值代入 ====================
        hint_5 = Text("大功告成！组装出完整的傅里叶展开式：", font="KaiTi", font_size=32).to_edge(UP, buff=0.6)
        self.play(Write(hint_5))

        eq_full_series = Tex(
            r"x^2 = \frac{\pi^2}{3} + \sum_{n=1}^{\infty} \frac{4(-1)^n}{n^2} \cos nx"
        ).set_color(BLUE).scale(1.0).next_to(hint_5, DOWN, buff=0.6)
        self.play(Write(eq_full_series))
        self.wait(1.5)

        self.play(FadeOut(hint_5))
        self.play(eq_full_series.animate.to_edge(UP, buff=0.6))

        # 严格混合排版 5
        hint_6 = VGroup(
            Text("代入特殊值 ", font="KaiTi", font_size=32),
            Tex(r"x = \pi", font_size=35).set_color(YELLOW),
            Text(" ：", font="KaiTi", font_size=32)
        ).arrange(RIGHT, buff=0.1).next_to(eq_full_series, DOWN, buff=0.6)
        self.play(Write(hint_6))

        eq_sub_pi = Tex(
            r"\pi^2 = \frac{\pi^2}{3} + \sum_{n=1}^{\infty} \frac{4(-1)^n}{n^2} \cos(n\pi)"
        ).set_color(BLUE).scale(1.0).next_to(hint_6, DOWN, buff=0.4)
        self.play(Write(eq_sub_pi))
        self.wait(1.5)

        # 严格混合排版 6
        hint_7 = VGroup(
            Text("利用 ", font="KaiTi", font_size=30),
            Tex(r"(-1)^n \times (-1)^n = 1", font_size=32).set_color(GREEN),
            Text("，符号完美抵消：", font="KaiTi", font_size=30)
        ).arrange(RIGHT, buff=0.1).next_to(eq_sub_pi, DOWN, buff=0.5)
        self.play(Write(hint_7))

        eq_simplified = Tex(
            r"\pi^2 = \frac{\pi^2}{3} + \sum_{n=1}^{\infty} \frac{4}{n^2}"
        ).set_color(YELLOW).scale(1.0).next_to(hint_7, DOWN, buff=0.4)

        self.play(ReplacementTransform(eq_sub_pi.copy(), eq_simplified))
        self.wait(2)

        self.play(FadeOut(VGroup(eq_full_series, hint_6, eq_sub_pi, hint_7)))
        self.play(eq_simplified.animate.move_to(ORIGIN))

        # ==================== 场景五：得出最终巴塞尔结果 ====================
        eq_final_step1 = Tex(
            r"\frac{2\pi^2}{3} = 4 \sum_{n=1}^{\infty} \frac{1}{n^2}"
        ).set_color(YELLOW).scale(1.2).move_to(eq_simplified)

        self.play(TransformMatchingTex(eq_simplified, eq_final_step1))
        self.wait(1.5)

        final_eq = Tex(
            r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}"
        ).scale(1.5).set_color(YELLOW).move_to(eq_final_step1)

        self.play(TransformMatchingTex(eq_final_step1, final_eq))

        rect = SurroundingRectangle(final_eq, buff=0.4, color=YELLOW)
        self.play(ShowCreation(rect))
        self.play(
            final_eq.animate.set_color_by_gradient(BLUE, YELLOW, RED),
            rect.animate.set_color_by_gradient(BLUE, YELLOW, RED)
        )
        self.wait(4)

        # ==================== 尾声 ====================
        self.play(FadeOut(final_eq), FadeOut(rect))
        xiexie = Text("感谢观看", font="KaiTi", font_size=80).set_color_by_gradient(BLUE, YELLOW, RED)
        self.play(Write(xiexie))
        self.wait(3)