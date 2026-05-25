from manim import *

import manimpango


manimpango.register_font("simkai.ttf")


class ParameterLogIntegral(Scene):
    def t(self, content, size=30, color=WHITE):
        return Text(content, font="KaiTi", font_size=size, color=color)

    def m(self, content, size=36, color=WHITE):
        return MathTex(content, font_size=size, color=color)

    def mix(self, *parts, buff=0.12):
        group = VGroup()
        for kind, content, size, color in parts:
            if kind == "text":
                group.add(self.t(content, size, color))
            else:
                group.add(self.m(content, size, color))
        group.arrange(RIGHT, buff=buff)
        return group

    def show_title(self, content):
        title = self.t(content, size=36, color=YELLOW).to_edge(UP, buff=0.42)
        self.play(Write(title), run_time=0.8)
        self.wait(0.4)
        return title

    def add_line(self, obj, prev=None, buff=0.38, run_time=0.75):
        if prev is None:
            obj.next_to(UP * 2.6, DOWN)
        else:
            obj.next_to(prev, DOWN, buff=buff)
        self.play(FadeIn(obj, shift=UP * 0.12), run_time=run_time)
        self.wait(0.75)
        return obj

    def clear_all(self):
        self.play(*[FadeOut(obj) for obj in self.mobjects], run_time=0.7)
        self.wait(0.3)

    def construct(self):
        self.cover()
        self.define_function()
        self.differentiate()
        self.auxiliary_integral()
        self.simplify_derivative()
        self.integrate_back()
        self.verify_endpoint()
        self.summary()

    def cover(self):
        title = self.t("含参数对数积分", size=48)
        title.set_color_by_gradient(BLUE_B, TEAL, GREEN_B)
        title.move_to(UP * 1.05)
        problem = self.m(
            r"\int_0^{\frac{\pi}{2}}\ln(1+a\sin^2 x)\,dx",
            size=45,
            color=YELLOW,
        )
        condition = self.m(r"a>-1", size=38, color=GRAY_A)
        request = self.t("求积分的值", size=32)
        VGroup(problem, condition, request).arrange(DOWN, buff=0.38).next_to(title, DOWN, buff=0.65)
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(problem, shift=UP * 0.15), run_time=0.8)
        self.play(FadeIn(condition), FadeIn(request), run_time=0.7)
        self.wait(2.0)
        self.clear_all()

    def define_function(self):
        title = self.show_title("设含参数函数")
        line_1 = self.t("把积分看作参数的函数。", size=30)
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.m(
            r"F(a)=\int_0^{\frac{\pi}{2}}\ln(1+a\sin^2 x)\,dx",
            size=40,
            color=BLUE_B,
        )
        self.add_line(line_2, line_1, buff=0.42)
        line_3 = self.mix(
            ("text", "由", 30, WHITE),
            ("math", r"a>-1", 36, BLUE_B),
            ("text", "可知被积函数有意义。", 30, WHITE),
        )
        self.add_line(line_3, line_2, buff=0.46)
        line_4 = self.mix(
            ("text", "并且", 30, WHITE),
            ("math", r"F(0)=0", 38, GREEN_B),
            ("text", "。", 30, WHITE),
        )
        self.add_line(line_4, line_3, buff=0.44)
        self.wait(1.5)
        self.clear_all()

    def differentiate(self):
        title = self.show_title("对参数求导")
        line_1 = self.t("先求导，再把结果积分回去。", size=30)
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.m(
            r"F'(a)=\int_0^{\frac{\pi}{2}}\frac{\sin^2 x}{1+a\sin^2 x}\,dx",
            size=39,
            color=BLUE_B,
        )
        self.add_line(line_2, line_1, buff=0.46)
        line_3 = self.t("把分子改写为分母的线性组合。", size=30)
        self.add_line(line_3, line_2, buff=0.5)
        line_4 = self.m(
            r"\frac{\sin^2 x}{1+a\sin^2 x}"
            r"=\frac{1}{a}\left(1-\frac{1}{1+a\sin^2 x}\right)",
            size=36,
            color=GREEN_B,
        )
        self.add_line(line_4, line_3, buff=0.42)
        note = self.mix(
            ("text", "先按", 28, GRAY_A),
            ("math", r"a\ne0", 34, GRAY_A),
            ("text", "推导，最后由连续性包含", 28, GRAY_A),
            ("math", r"a=0", 34, GRAY_A),
            ("text", "。", 28, GRAY_A),
        )
        self.add_line(note, line_4, buff=0.42)
        self.wait(1.8)
        self.clear_all()

    def auxiliary_integral(self):
        title = self.show_title("计算辅助积分")
        line_1 = self.m(
            r"J(a)=\int_0^{\frac{\pi}{2}}\frac{dx}{1+a\sin^2 x}",
            size=40,
            color=BLUE_B,
        )
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.mix(
            ("text", "令", 30, WHITE),
            ("math", r"t=\tan x", 38, BLUE_B),
            ("text", "，则", 30, WHITE),
        )
        self.add_line(line_2, line_1, buff=0.46)
        facts = VGroup(
            self.m(r"\sin^2 x=\frac{t^2}{1+t^2}", size=34, color=BLUE_B),
            self.m(r"dx=\frac{dt}{1+t^2}", size=34, color=BLUE_B),
            self.m(r"x:0\to\frac{\pi}{2}\quad t:0\to+\infty", size=34, color=BLUE_B),
        ).arrange(DOWN, buff=0.24)
        self.add_line(facts, line_2, buff=0.36)
        self.wait(0.8)
        self.clear_all()

        title = self.show_title("化为标准积分")
        line_1 = self.m(
            r"J(a)=\int_0^{+\infty}\frac{dt}{1+(1+a)t^2}",
            size=41,
            color=BLUE_B,
        )
        self.add_line(line_1, title, buff=0.65)
        line_2 = self.mix(
            ("text", "因为", 30, WHITE),
            ("math", r"1+a>0", 38, BLUE_B),
            ("text", "，令", 30, WHITE),
            ("math", r"u=\sqrt{1+a}\,t", 38, BLUE_B),
            ("text", "。", 30, WHITE),
        )
        self.add_line(line_2, line_1, buff=0.48)
        line_3 = self.m(
            r"J(a)=\frac{1}{\sqrt{1+a}}\int_0^{+\infty}\frac{du}{1+u^2}",
            size=39,
            color=BLUE_B,
        )
        self.add_line(line_3, line_2, buff=0.45)
        line_4 = self.m(
            r"J(a)=\frac{\pi}{2\sqrt{1+a}}",
            size=43,
            color=GREEN_B,
        )
        self.add_line(line_4, line_3, buff=0.42)
        self.play(Create(SurroundingRectangle(line_4, color=YELLOW, buff=0.16)), run_time=0.8)
        self.wait(1.8)
        self.clear_all()

    def simplify_derivative(self):
        title = self.show_title("整理导函数")
        line_1 = self.m(
            r"F'(a)=\frac{1}{a}\left(\frac{\pi}{2}-J(a)\right)",
            size=40,
            color=BLUE_B,
        )
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.m(
            r"F'(a)=\frac{\pi}{2a}\left(1-\frac{1}{\sqrt{1+a}}\right)",
            size=39,
            color=BLUE_B,
        )
        self.add_line(line_2, line_1, buff=0.42)
        line_3 = self.t("把含参数的差式有理化。", size=30)
        self.add_line(line_3, line_2, buff=0.48)
        line_4 = self.m(
            r"1-\frac{1}{\sqrt{1+a}}=\frac{a}{\sqrt{1+a}\,(\sqrt{1+a}+1)}",
            size=35,
            color=BLUE_B,
        )
        self.add_line(line_4, line_3, buff=0.42)
        line_5 = self.m(
            r"F'(a)=\frac{\pi}{2\sqrt{1+a}\,(\sqrt{1+a}+1)}",
            size=39,
            color=GREEN_B,
        )
        self.add_line(line_5, line_4, buff=0.42)
        self.play(Indicate(line_5, color=YELLOW), run_time=1.0)
        self.wait(1.8)
        self.clear_all()

    def integrate_back(self):
        title = self.show_title("积分回原函数")
        line_1 = self.mix(
            ("text", "由", 30, WHITE),
            ("math", r"F(0)=0", 36, BLUE_B),
            ("text", "，有", 30, WHITE),
        )
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.m(
            r"F(a)=\int_0^a\frac{\pi}{2\sqrt{1+s}\,(\sqrt{1+s}+1)}\,ds",
            size=34,
            color=BLUE_B,
        )
        self.add_line(line_2, line_1, buff=0.44)
        line_3 = self.mix(
            ("text", "令", 30, WHITE),
            ("math", r"u=\sqrt{1+s}", 38, BLUE_B),
            ("text", "，则", 30, WHITE),
            ("math", r"ds=2u\,du", 38, BLUE_B),
            ("text", "。", 30, WHITE),
        )
        self.add_line(line_3, line_2, buff=0.46)
        line_4 = self.m(
            r"s:0\to a\quad u:1\to\sqrt{1+a}",
            size=35,
            color=BLUE_B,
        )
        self.add_line(line_4, line_3, buff=0.36)
        self.wait(0.8)
        self.clear_all()

        title = self.show_title("得到闭式")
        line_1 = self.m(
            r"F(a)=\int_1^{\sqrt{1+a}}\frac{\pi}{u+1}\,du",
            size=42,
            color=BLUE_B,
        )
        self.add_line(line_1, title, buff=0.68)
        line_2 = self.m(
            r"F(a)=\pi\ln(u+1)\Big|_1^{\sqrt{1+a}}",
            size=41,
            color=BLUE_B,
        )
        self.add_line(line_2, line_1, buff=0.45)
        line_3 = self.m(
            r"F(a)=\pi\ln\frac{1+\sqrt{1+a}}{2}",
            size=46,
            color=YELLOW,
        )
        self.add_line(line_3, line_2, buff=0.46)
        self.play(Create(SurroundingRectangle(line_3, color=YELLOW, buff=0.18)), run_time=0.9)
        self.wait(2.0)
        self.clear_all()

    def verify_endpoint(self):
        title = self.show_title("端点检验")
        line_1 = self.t("代入参数零点，结果应与原积分一致。", size=30)
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.m(
            r"F(0)=\pi\ln\frac{1+\sqrt{1}}{2}",
            size=41,
            color=BLUE_B,
        )
        self.add_line(line_2, line_1, buff=0.45)
        line_3 = self.m(
            r"F(0)=\pi\ln 1=0",
            size=42,
            color=GREEN_B,
        )
        self.add_line(line_3, line_2, buff=0.42)
        line_4 = self.t("这与原式中被积函数恒为零相同。", size=30, color=GREEN_B)
        self.add_line(line_4, line_3, buff=0.5)
        self.wait(1.8)
        self.clear_all()

    def summary(self):
        title = self.show_title("结论")
        line_1 = self.t("当参数满足", size=32)
        line_1.next_to(title, DOWN, buff=0.72)
        line_1.shift(LEFT * 1.0)
        cond = self.m(r"a>-1", size=40, color=BLUE_B)
        cond.next_to(line_1, RIGHT, buff=0.14)
        self.play(FadeIn(VGroup(line_1, cond), shift=UP * 0.12), run_time=0.7)
        self.wait(0.7)
        line_2 = self.m(
            r"\int_0^{\frac{\pi}{2}}\ln(1+a\sin^2 x)\,dx"
            r"=\pi\ln\frac{1+\sqrt{1+a}}{2}",
            size=39,
            color=YELLOW,
        )
        line_2.next_to(VGroup(line_1, cond), DOWN, buff=0.62)
        self.play(FadeIn(line_2, shift=UP * 0.12), run_time=0.8)
        self.play(Create(SurroundingRectangle(line_2, color=YELLOW, buff=0.18)), run_time=0.9)
        self.wait(3.0)
        self.clear_all()
