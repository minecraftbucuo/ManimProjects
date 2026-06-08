from manim import *


class SequenceLimitProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("经典数列极限问题的分析与求解", font="KaiTi", font_size=45)
        title.set_color_by_gradient(BLUE, GREEN)

        eq_cover = MathTex(
            r"\lim_{n \to \infty} \left[ \sqrt[n+1]{(n+1)!} - \sqrt[n]{n!} \right]",
            font_size=55
        ).set_color(BLUE)

        cover = VGroup(title, eq_cover).arrange(DOWN, buff=0.6).to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))

        # ==================== 倒计时（位于题目下方） ====================
        countdown_pos = eq_cover.get_bottom() + DOWN * 1.2
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=120)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.move_to(countdown_pos)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：核心战略与转化 ====================
        desc_1_1 = Text("首先引入记号，令", font="KaiTi", font_size=28)
        math_1_1 = MathTex(r"a_n = \sqrt[n]{n!}", font_size=30).set_color(YELLOW)
        desc_1_2 = Text("，则原极限可以写为：", font="KaiTi", font_size=28)
        line1 = VGroup(desc_1_1, math_1_1, desc_1_2).arrange(RIGHT, buff=0.1).to_edge(UP, buff=0.8)
        self.play(Write(line1))

        eq_orig = MathTex(r"\lim_{n \to \infty} (a_{n+1} - a_n)").set_color(BLUE).next_to(line1, DOWN, buff=0.4)
        self.play(Write(eq_orig))
        self.wait(1.5)

        desc_2 = Text("提取公因式，将式子转化为比值结构：", font="KaiTi", font_size=28).next_to(eq_orig, DOWN, buff=0.4)
        self.play(Write(desc_2))

        eq_trans1 = MathTex(r"a_{n+1} - a_n = a_n \left( \frac{a_{n+1}}{a_n} - 1 \right)").set_color(GREEN).next_to(desc_2, DOWN, buff=0.3)
        self.play(Write(eq_trans1))
        self.wait(1.5)

        desc_3_1 = Text("考虑到比值极限趋于 ", font="KaiTi", font_size=28)
        math_3_1 = MathTex(r"1", font_size=30).set_color(YELLOW)
        desc_3_2 = Text("，可引入等价无穷小代换：", font="KaiTi", font_size=28)
        line3 = VGroup(desc_3_1, math_3_1, desc_3_2).arrange(RIGHT, buff=0.1).next_to(eq_trans1, DOWN, buff=0.4)
        self.play(Write(line3))

        eq_equiv = MathTex(r"\frac{a_{n+1}}{a_n} - 1 \sim \ln \left( \frac{a_{n+1}}{a_n} \right)").set_color(YELLOW).next_to(line3, DOWN, buff=0.3)
        self.play(Write(eq_equiv))
        self.wait(2)

        # 及时清理屏幕，防止后续公式溢出或重叠
        self.play(FadeOut(line1), FadeOut(eq_orig), FadeOut(desc_2), FadeOut(eq_trans1), FadeOut(line3), FadeOut(eq_equiv))

        desc_4 = Text("通过对数性质与配凑，将原式拆分为两个独立部分：", font="KaiTi", font_size=28).to_edge(UP, buff=0.8)
        self.play(Write(desc_4))

        eq_split = MathTex(
            r"a_n \left( \frac{a_{n+1}}{a_n} - 1 \right) \sim ",
            r"\left( \frac{a_n}{n} \right)",
            r"\cdot",
            r"\left[ n \ln \left( \frac{a_{n+1}}{a_n} \right) \right]"
        ).next_to(desc_4, DOWN, buff=0.5)
        eq_split[1].set_color(BLUE)
        eq_split[3].set_color(GREEN)
        self.play(Write(eq_split))
        self.wait(2.5)

        self.play(FadeOut(desc_4), FadeOut(eq_split))

        # ==================== 第二幕：求解第一部分极限 ====================
        desc_part1 = Text("第一部分：求解数列的主部极限", font="KaiTi", font_size=32).to_edge(UP, buff=0.8)
        desc_part1.set_color(BLUE)
        self.play(Write(desc_part1))

        eq_p1_target = MathTex(r"\lim_{n \to \infty} \frac{a_n}{n} = \lim_{n \to \infty} \sqrt[n]{\frac{n!}{n^n}}").next_to(desc_part1, DOWN, buff=0.4)
        self.play(Write(eq_p1_target))

        desc_cauchy = Text("根据柯西第二极限定理，可将其转换为相邻项的比值极限：", font="KaiTi", font_size=28).next_to(eq_p1_target, DOWN, buff=0.4)
        self.play(Write(desc_cauchy))

        eq_cauchy = MathTex(
            r"\lim_{n \to \infty} \frac{(n+1)!}{(n+1)^{n+1}} \cdot \frac{n^n}{n!}",
            r"= \lim_{n \to \infty} \left( \frac{n}{n+1} \right)^n"
        ).next_to(desc_cauchy, DOWN, buff=0.3)
        self.play(Write(eq_cauchy))
        self.wait(1.5)

        eq_p1_ans = MathTex(r"= \lim_{n \to \infty} \frac{1}{\left(1 + \frac{1}{n}\right)^n} = \frac{1}{e}").set_color(BLUE).next_to(eq_cauchy, DOWN, buff=0.3)
        self.play(Write(eq_p1_ans))
        self.wait(2.5)

        # 彻底清场
        self.play(FadeOut(desc_part1), FadeOut(eq_p1_target), FadeOut(desc_cauchy), FadeOut(eq_cauchy), FadeOut(eq_p1_ans))

        # ==================== 第三幕：求解第二部分极限 ====================
        desc_part2 = Text("第二部分：利用定积分求解对数项极限", font="KaiTi", font_size=32).to_edge(UP, buff=0.8)
        desc_part2.set_color(GREEN)
        self.play(Write(desc_part2))

        eq_p2_target = MathTex(r"n \ln \left( \frac{a_{n+1}}{a_n} \right) = \frac{n}{n+1} \ln(n+1)! - \ln n!").next_to(desc_part2, DOWN, buff=0.4)
        self.play(Write(eq_p2_target))

        desc_p2_expand = Text("展开阶乘并重新组合，提炼出对应结构：", font="KaiTi", font_size=28).next_to(eq_p2_target, DOWN, buff=0.4)
        self.play(Write(desc_p2_expand))

        eq_p2_step1 = MathTex(r"= \frac{n}{n+1} \left[ \ln\left(1+\frac{1}{n}\right) + \frac{1}{n} \sum_{k=1}^n \left(-\ln \frac{k}{n}\right) \right]").next_to(desc_p2_expand, DOWN, buff=0.3)
        self.play(Write(eq_p2_step1))
        self.wait(2)

        # 清理局部，向上收拢，为积分推导留出空间
        self.play(FadeOut(eq_p2_target), FadeOut(desc_p2_expand), eq_p2_step1.animate.next_to(desc_part2, DOWN, buff=0.4))

        desc_riemann = Text("当极限趋于无穷时，求和部分构成黎曼和：", font="KaiTi", font_size=28).next_to(eq_p2_step1, DOWN, buff=0.4)
        self.play(Write(desc_riemann))

        eq_integral = MathTex(
            r"\lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n \left(-\ln \frac{k}{n}\right) =",
            r"\int_0^1 -\ln x \, dx"
        ).next_to(desc_riemann, DOWN, buff=0.3)
        eq_integral[1].set_color(YELLOW)
        self.play(Write(eq_integral))

        eq_p2_ans = MathTex(r"\int_0^1 -\ln x \, dx = \left[ -x \ln x + x \right]_0^1 = 1").set_color(GREEN).next_to(eq_integral, DOWN, buff=0.3)
        self.play(Write(eq_p2_ans))
        self.wait(2.5)

        # 彻底清场
        self.play(FadeOut(desc_part2), FadeOut(eq_p2_step1), FadeOut(desc_riemann), FadeOut(eq_integral), FadeOut(eq_p2_ans))

        # ==================== 第四幕：总结与结论 ====================
        desc_final = Text("第三部分：结合两部分得出最终结论", font="KaiTi", font_size=32).to_edge(UP, buff=1.0)
        self.play(Write(desc_final))

        ans_p1_text = Text("第一部分的主部极限为：", font="KaiTi", font_size=26)
        ans_p1_math = MathTex(r"\frac{1}{e}", font_size=30).set_color(BLUE)
        ans_p1 = VGroup(ans_p1_text, ans_p1_math).arrange(RIGHT, buff=0.1).next_to(desc_final, DOWN, buff=0.6)

        ans_p2_text = Text("第二部分的对数极限为：", font="KaiTi", font_size=26)
        ans_p2_math = MathTex(r"1", font_size=30).set_color(GREEN)
        ans_p2 = VGroup(ans_p2_text, ans_p2_math).arrange(RIGHT, buff=0.1).next_to(ans_p1, DOWN, buff=0.4)

        self.play(Write(ans_p1), Write(ans_p2))
        self.wait(1.5)

        desc_res = Text("综合两部分，原式极限结果为：", font="KaiTi", font_size=28).next_to(ans_p2, DOWN, buff=0.6)
        self.play(Write(desc_res))

        final_ans = MathTex(
            r"\lim_{n \to \infty} \left[ \sqrt[n+1]{(n+1)!} - \sqrt[n]{n!} \right] = \frac{1}{e}",
            font_size=38
        ).set_color(YELLOW).next_to(desc_res, DOWN, buff=0.4)

        rect_final = SurroundingRectangle(final_ans, color=YELLOW, buff=0.2)
        self.play(Write(final_ans))
        self.play(Create(rect_final))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(1)