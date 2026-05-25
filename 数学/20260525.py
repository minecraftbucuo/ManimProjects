from manim import *

import manimpango


manimpango.register_font("simkai.ttf")


class RecurrenceSequenceSolution(Scene):
    def t(self, content, size=30, color=WHITE):
        return Text(content, font="KaiTi", font_size=size, color=color)

    def m(self, content, size=36, color=WHITE):
        return MathTex(content, font_size=size, color=color)

    def mix(self, *parts, buff=0.14):
        group = VGroup()
        for kind, content, size, color in parts:
            group.add(self.t(content, size, color) if kind == "text" else self.m(content, size, color))
        group.arrange(RIGHT, buff=buff)
        return group

    def title(self, content):
        obj = self.t(content, size=36, color=YELLOW).to_edge(UP, buff=0.45)
        self.play(Write(obj), run_time=0.8)
        self.wait(0.5)
        return obj

    def add_below(self, obj, prev=None, buff=0.38, shift=UP, run_time=0.8):
        if prev is None:
            obj.next_to(UP * 2.7, DOWN)
        else:
            obj.next_to(prev, DOWN, buff=buff)
        self.play(FadeIn(obj, shift=shift), run_time=run_time)
        self.wait(1.1)
        return obj

    def clear(self):
        self.play(*[FadeOut(obj) for obj in self.mobjects], run_time=0.7)
        self.wait(0.4)

    def construct(self):
        title = self.cover()
        self.problem(title)
        self.root_observation()
        self.change_variable()
        self.polynomial_reason()
        self.solve_coefficients()
        self.return_to_sequence()
        self.check_result()
        self.summary()

    def cover(self):
        title = self.t("二重特征根递推求通项", size=48)
        title.set_color_by_gradient(BLUE_B, TEAL, GREEN_B, YELLOW)
        title.move_to(UP * 1.1)
        self.play(Write(title), run_time=0.9)
        self.wait(0.4)
        return title

    def countdown(self):
        for value, color in [("3", RED), ("2", ORANGE), ("1", YELLOW)]:
            digit = self.t(value, size=140, color=color)
            digit.move_to(DOWN * 0.8)
            self.play(FadeIn(digit, scale=0.7), run_time=0.3)
            self.wait(0.8)
            self.play(FadeOut(digit, scale=1.2), run_time=0.3)

    def problem(self, title):
        line_1 = self.mix(
            ("text", "已知数列满足", 30, WHITE),
            ("math", r"a_0=1,\quad a_1=4", 35, BLUE_B),
        )
        line_1.next_to(title, DOWN, buff=0.55)
        self.play(FadeIn(line_1, shift=UP * 0.15), run_time=0.6)
        line_2 = self.m(
            r"a_{n+2}-4a_{n+1}+4a_n=(n+1)2^n,\quad n\ge 0",
            size=37,
            color=BLUE_B,
        )
        line_2.next_to(line_1, DOWN, buff=0.42)
        line_2.set_color_by_tex("2^n", YELLOW)
        self.play(FadeIn(line_2, shift=UP * 0.15), run_time=0.8)
        self.wait(0.6)
        self.countdown()
        self.wait(0.4)
        self.play(FadeOut(VGroup(title, line_1, line_2)), run_time=0.8)
        self.wait(0.3)

    def root_observation(self):
        title = self.title("观察结构")
        line_1 = self.t("先看对应的齐次递推。", size=30)
        self.add_below(line_1, title, buff=0.6)
        line_2 = self.m(r"a_{n+2}-4a_{n+1}+4a_n=0", size=38, color=BLUE_B)
        self.add_below(line_2, line_1)
        line_3 = self.mix(
            ("text", "设", 30, WHITE),
            ("math", r"a_n=r^n", 36, BLUE_B),
            ("text", "，得到", 30, WHITE),
        )
        self.add_below(line_3, line_2)
        line_4 = self.m(r"r^2-4r+4=0", size=38, color=BLUE_B)
        self.add_below(line_4, line_3)
        line_5 = self.m(r"(r-2)^2=0", size=40, color=GREEN_B)
        self.add_below(line_5, line_4)
        line_6 = self.mix(
            ("text", "因此", 30, WHITE),
            ("math", r"2", 38, GREEN_B),
            ("text", "是二重特征根。", 30, WHITE),
        )
        self.add_below(line_6, line_5)
        self.play(Indicate(line_5, color=YELLOW), run_time=1.1)
        self.wait(1.8)
        self.clear()

    def change_variable(self):
        title = self.title("换元")
        line_1 = self.t("右端含有同一个指数因子，先把它分离出来。", size=30)
        self.add_below(line_1, title, buff=0.6)
        line_2 = self.m(r"a_n=2^n b_n", size=42, color=BLUE_B)
        self.add_below(line_2, line_1, buff=0.48)
        line_3 = self.t("于是相邻三项分别为。", size=30)
        self.add_below(line_3, line_2, buff=0.48)
        line_4 = self.m(r"a_{n+1}=2^{n+1}b_{n+1}", size=36, color=BLUE_B)
        self.add_below(line_4, line_3, buff=0.32)
        line_5 = self.m(r"a_{n+2}=2^{n+2}b_{n+2}", size=36, color=BLUE_B)
        self.add_below(line_5, line_4, buff=0.28)
        self.wait(0.7)
        self.clear()

        title = self.title("代入递推")
        line_1 = self.m(
            r"2^{n+2}b_{n+2}-4\cdot 2^{n+1}b_{n+1}+4\cdot 2^n b_n=(n+1)2^n",
            size=31,
            color=BLUE_B,
        )
        self.add_below(line_1, title, buff=0.65)
        line_2 = self.t("左端提取公共因子。", size=29)
        self.add_below(line_2, line_1, buff=0.5)
        line_3 = self.m(
            r"2^{n+2}(b_{n+2}-2b_{n+1}+b_n)=(n+1)2^n",
            size=34,
            color=BLUE_B,
        )
        self.add_below(line_3, line_2, buff=0.45)
        line_4 = self.t("两边同除以公共指数因子。", size=29)
        self.add_below(line_4, line_3, buff=0.5)
        line_5 = self.m(
            r"b_{n+2}-2b_{n+1}+b_n=\frac{n+1}{4}",
            size=40,
            color=GREEN_B,
        )
        self.add_below(line_5, line_4, buff=0.45)
        self.play(Create(SurroundingRectangle(line_5, color=YELLOW, buff=0.16)), run_time=0.9)
        self.wait(2.0)
        self.clear()

    def polynomial_reason(self):
        title = self.title("差分方程")
        line_1 = self.m(
            r"b_{n+2}-2b_{n+1}+b_n=\frac{n+1}{4}",
            size=40,
            color=GREEN_B,
        )
        self.add_below(line_1, title, buff=0.6)
        line_2 = self.t("左端是数列的二阶差分。", size=30)
        self.add_below(line_2, line_1, buff=0.5)
        line_3 = self.t("二阶差分会使多项式次数降低二次。", size=30)
        self.add_below(line_3, line_2, buff=0.45)
        line_4 = self.mix(
            ("text", "右端关于", 30, WHITE),
            ("math", r"n", 36, BLUE_B),
            ("text", "是一次式，所以", 30, WHITE),
            ("math", r"b_n", 36, BLUE_B),
            ("text", "取三次式。", 30, WHITE),
        )
        self.add_below(line_4, line_3, buff=0.45)
        line_5 = self.m(r"b_n=\alpha n^3+\beta n^2+\gamma n+\delta", size=40, color=BLUE_B)
        self.add_below(line_5, line_4, buff=0.5)
        self.wait(2.0)
        self.clear()

    def solve_coefficients(self):
        title = self.title("比较系数")
        line_1 = self.m(r"b_n=\alpha n^3+\beta n^2+\gamma n+\delta", size=38, color=BLUE_B)
        self.add_below(line_1, title, buff=0.6)
        line_2 = self.t("代入二阶差分，分别计算三次项和二次项的贡献。", size=28)
        self.add_below(line_2, line_1, buff=0.5)
        line_3 = self.m(
            r"(n+2)^3-2(n+1)^3+n^3=6n+6",
            size=35,
            color=BLUE_B,
        )
        self.add_below(line_3, line_2, buff=0.42)
        line_4 = self.m(
            r"(n+2)^2-2(n+1)^2+n^2=2",
            size=35,
            color=BLUE_B,
        )
        self.add_below(line_4, line_3, buff=0.35)
        line_5 = self.m(
            r"b_{n+2}-2b_{n+1}+b_n=6\alpha n+6\alpha+2\beta",
            size=35,
            color=GREEN_B,
        )
        self.add_below(line_5, line_4, buff=0.42)
        self.wait(1.7)
        self.clear()

        title = self.title("比较系数")
        line_1 = self.m(r"6\alpha n+6\alpha+2\beta=\frac{1}{4}n+\frac{1}{4}", size=38, color=BLUE_B)
        self.add_below(line_1, title, buff=0.65)
        line_2 = self.t("比较一次项系数。", size=30)
        self.add_below(line_2, line_1, buff=0.55)
        line_3 = self.m(r"6\alpha=\frac{1}{4}", size=38, color=BLUE_B)
        self.add_below(line_3, line_2, buff=0.42)
        line_4 = self.m(r"\alpha=\frac{1}{24}", size=38, color=GREEN_B)
        self.add_below(line_4, line_3, buff=0.35)
        self.wait(1.6)
        self.clear()

        title = self.title("常数项")
        line_5 = self.t("再比较常数项。", size=30)
        self.add_below(line_5, title, buff=0.6)
        line_6 = self.m(r"6\alpha+2\beta=\frac{1}{4}", size=38, color=BLUE_B)
        self.add_below(line_6, line_5, buff=0.5)
        line_7 = self.mix(
            ("text", "代入", 28, WHITE),
            ("math", r"\alpha=\frac{1}{24}", 36, BLUE_B),
            ("text", "，解得", 28, WHITE),
            ("math", r"\beta=0", 40, GREEN_B),
        )
        self.add_below(line_7, line_6, buff=0.55)
        self.wait(1.8)
        self.clear()

        title = self.title("利用初值")
        line_1 = self.mix(
            ("text", "由", 30, WHITE),
            ("math", r"a_n=2^n b_n", 36, BLUE_B),
            ("text", "可得", 30, WHITE),
        )
        self.add_below(line_1, title, buff=0.5)
        line_2 = self.m(r"b_0=a_0=1", size=34, color=BLUE_B)
        self.add_below(line_2, line_1, buff=0.4)
        line_2b = self.m(r"b_1=\frac{a_1}{2}=2", size=34, color=BLUE_B)
        self.add_below(line_2b, line_2, buff=0.28)
        line_3 = self.m(r"b_n=\frac{1}{24}n^3+\gamma n+\delta", size=34, color=BLUE_B)
        self.add_below(line_3, line_2b, buff=0.38)
        line_4 = self.mix(
            ("text", "代入", 28, WHITE),
            ("math", r"n=0", 34, BLUE_B),
            ("text", "，得", 28, WHITE),
            ("math", r"\delta=1", 36, GREEN_B),
        )
        self.add_below(line_4, line_3, buff=0.3)
        self.wait(0.7)
        self.play(FadeOut(VGroup(line_1, line_2, line_2b, line_3, line_4)), run_time=0.6)

        line_5 = self.mix(
            ("text", "再代入", 28, WHITE),
            ("math", r"n=1", 34, BLUE_B),
            ("text", "，得", 28, WHITE),
            ("math", r"\frac{1}{24}+\gamma+1=2", 36, BLUE_B),
        )
        line_5.next_to(title, DOWN, buff=0.55)
        self.play(FadeIn(line_5, shift=UP * 0.15), run_time=0.6)
        line_6 = self.m(r"\gamma=\frac{23}{24}", size=38, color=GREEN_B)
        line_6.next_to(line_5, DOWN, buff=0.35)
        self.play(FadeIn(line_6, shift=UP * 0.15), run_time=0.6)
        self.wait(1.8)
        self.clear()

    def return_to_sequence(self):
        title = self.title("回到原数列")
        line_1 = self.m(r"b_n=\frac{1}{24}n^3+\frac{23}{24}n+1", size=42, color=BLUE_B)
        self.add_below(line_1, title, buff=0.65)
        line_2 = self.t("写成一个分式，便于代回原数列。", size=30)
        self.add_below(line_2, line_1, buff=0.55)
        line_3 = self.m(r"b_n=\frac{n^3+23n+24}{24}", size=44, color=GREEN_B)
        self.add_below(line_3, line_2)
        line_4 = self.mix(
            ("text", "因为", 30, WHITE),
            ("math", r"a_n=2^n b_n", 38, BLUE_B),
            ("text", "，所以", 30, WHITE),
        )
        self.add_below(line_4, line_3, buff=0.55)
        line_5 = self.m(r"a_n=\frac{2^n(n^3+23n+24)}{24}", size=46, color=YELLOW)
        self.add_below(line_5, line_4)
        self.play(Create(SurroundingRectangle(line_5, color=YELLOW, buff=0.18)), run_time=1.0)
        self.wait(2.2)
        self.clear()

    def check_result(self):
        title = self.title("检验")
        line_1 = self.t("先检验初值。", size=30)
        self.add_below(line_1, title, buff=0.65)
        line_2 = self.m(r"a_0=\frac{1(0+0+24)}{24}=1", size=38, color=BLUE_B)
        self.add_below(line_2, line_1)
        line_3 = self.m(r"a_1=\frac{2(1+23+24)}{24}=4", size=38, color=BLUE_B)
        self.add_below(line_3, line_2)
        line_4 = self.t("再看递推式。换元后已经化为等价的二阶差分式。", size=28)
        self.add_below(line_4, line_3, buff=0.55)
        line_5 = self.m(r"b_{n+2}-2b_{n+1}+b_n=\frac{n+1}{4}", size=40, color=GREEN_B)
        self.add_below(line_5, line_4)
        line_6 = self.t("因此原递推式也成立。", size=30, color=GREEN_B)
        self.add_below(line_6, line_5, buff=0.5)
        self.wait(2.0)
        self.clear()

    def summary(self):
        title = self.title("结论")
        line_1 = self.t("所求通项为", size=34)
        self.add_below(line_1, title, buff=0.85)
        line_2 = self.m(r"a_n=\frac{2^n(n^3+23n+24)}{24}", size=48, color=YELLOW)
        self.add_below(line_2, line_1, buff=0.55)
        line_3 = self.m(r"n\ge 0", size=38, color=GRAY_A)
        self.add_below(line_3, line_2, buff=0.45)
        self.wait(3.0)
        self.clear()
