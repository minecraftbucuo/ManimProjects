from manim import *

import manimpango
import numpy as np


manimpango.register_font("simkai.ttf")


class HeartEpicycleTutorial(Scene):
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
        title = self.t(content, size=36, color=YELLOW).to_edge(UP, buff=0.38)
        self.play(Write(title), run_time=0.8)
        self.wait(0.3)
        return title

    def add_line(self, obj, prev=None, buff=0.36, run_time=0.7):
        if prev is None:
            obj.next_to(UP * 2.55, DOWN)
        else:
            obj.next_to(prev, DOWN, buff=buff)
        self.play(FadeIn(obj, shift=UP * 0.12), run_time=run_time)
        self.wait(0.6)
        return obj

    def clear_all(self):
        self.play(*[FadeOut(obj) for obj in self.mobjects], run_time=0.7)
        self.wait(0.25)

    def points_from_terms(self, time_value, origin, scale, terms):
        points = [np.array(origin)]
        current = np.array(origin)
        for speed, radius, phase in terms:
            angle = speed * time_value + phase
            current = current + scale * radius * np.array([np.cos(angle), np.sin(angle), 0])
            points.append(current.copy())
        return points

    def epicycle_group(self, tracker, origin, scale, terms, colors):
        def build():
            points = self.points_from_terms(tracker.get_value(), origin, scale, terms)
            group = VGroup()
            for index, (_, radius, _) in enumerate(terms):
                color = colors[index % len(colors)]
                circle = Circle(radius=scale * radius, color=color, stroke_width=1.8)
                circle.move_to(points[index])
                segment = Line(points[index], points[index + 1], color=color, stroke_width=4)
                joint = Dot(points[index], radius=0.035, color=GRAY_B)
                group.add(circle, segment, joint)
            group.add(Dot(points[-1], radius=0.055, color=YELLOW))
            return group

        return always_redraw(build)

    def construct(self):
        self.cover()
        self.heart_equation()
        self.convert_x()
        self.complex_coefficients()
        self.extract_parameters()
        self.draw_heart()
        self.summary()

    def cover(self):
        title = self.t("用旋转圆绘制爱心", size=50)
        title.set_color_by_gradient(RED_B, YELLOW, GREEN_B)
        title.move_to(UP * 1.18)
        subtitle = self.t("从参数方程求出圆的半径、角速度和初相位", size=30)
        subtitle.next_to(title, DOWN, buff=0.48)
        formula = self.m(
            r"P(t)=\sum c_k e^{ikt}",
            size=48,
            color=YELLOW,
        )
        formula.next_to(subtitle, DOWN, buff=0.52)
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.12), run_time=0.7)
        self.play(FadeIn(formula, shift=UP * 0.12), run_time=0.8)
        self.wait(2.0)
        self.clear_all()

    def heart_equation(self):
        title = self.show_title("爱心参数方程")
        line_1 = self.t("先选用一条常见的爱心曲线。", size=30)
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.m(r"x(t)=16\sin^3 t", size=42, color=RED_B)
        self.add_line(line_2, line_1, buff=0.42)
        line_3 = self.m(
            r"y(t)=13\cos t-5\cos 2t-2\cos 3t-\cos 4t",
            size=36,
            color=BLUE_B,
        )
        self.add_line(line_3, line_2, buff=0.36)
        line_4 = self.m(r"0\le t\le 2\pi", size=38, color=GRAY_A)
        self.add_line(line_4, line_3, buff=0.4)
        line_5 = self.t("目标是把它写成若干个旋转向量的和。", size=30)
        self.add_line(line_5, line_4, buff=0.48)
        self.wait(1.5)
        self.clear_all()

    def convert_x(self):
        title = self.show_title("整理横坐标")
        line_1 = self.t("横坐标中含有三次正弦，先降次。", size=30)
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.m(
            r"\sin^3 t=\frac{3\sin t-\sin 3t}{4}",
            size=40,
            color=BLUE_B,
        )
        self.add_line(line_2, line_1, buff=0.42)
        line_3 = self.m(
            r"x(t)=12\sin t-4\sin 3t",
            size=43,
            color=GREEN_B,
        )
        self.add_line(line_3, line_2, buff=0.45)
        line_4 = self.t("纵坐标已经是余弦项的和。", size=30)
        self.add_line(line_4, line_3, buff=0.46)
        line_5 = self.m(
            r"y(t)=13\cos t-5\cos 2t-2\cos 3t-\cos 4t",
            size=35,
            color=BLUE_B,
        )
        self.add_line(line_5, line_4, buff=0.36)
        self.wait(1.6)
        self.clear_all()

    def complex_coefficients(self):
        title = self.show_title("转为复数形式")
        line_1 = self.mix(
            ("text", "令", 30, WHITE),
            ("math", r"P(t)=x(t)+iy(t)", 38, BLUE_B),
            ("text", "。", 30, WHITE),
        )
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.t("用欧拉公式把正弦、余弦改写为指数项。", size=30)
        self.add_line(line_2, line_1, buff=0.43)
        formulas = VGroup(
            self.m(r"\sin nt=\frac{e^{int}-e^{-int}}{2i}", size=35, color=BLUE_B),
            self.m(r"\cos nt=\frac{e^{int}+e^{-int}}{2}", size=35, color=BLUE_B),
        ).arrange(DOWN, buff=0.28)
        self.add_line(formulas, line_2, buff=0.4)
        self.wait(0.7)
        self.clear_all()

        title = self.show_title("合并同频率项")
        line_1 = self.m(
            r"P(t)=\sum c_k e^{ikt}",
            size=42,
            color=YELLOW,
        )
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.t("合并后只出现下列频率。", size=30)
        self.add_line(line_2, line_1, buff=0.44)
        coeffs = VGroup(
            self.m(r"c_{-1}=\frac{25}{2}i,\quad c_1=\frac{1}{2}i", size=35, color=BLUE_B),
            self.m(r"c_{-2}=-\frac{5}{2}i,\quad c_2=-\frac{5}{2}i", size=35, color=GREEN_B),
            self.m(r"c_{-3}=-3i,\quad c_3=i", size=35, color=ORANGE),
            self.m(r"c_{-4}=-\frac{1}{2}i,\quad c_4=-\frac{1}{2}i", size=35, color=PURPLE_B),
        ).arrange(DOWN, buff=0.28)
        self.add_line(coeffs, line_2, buff=0.42)
        self.wait(2.0)
        self.clear_all()

    def extract_parameters(self):
        title = self.show_title("求出旋转圆参数")
        line_1 = self.t("每个复系数都写成极坐标形式。", size=30)
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.m(
            r"c_k=r_k e^{i\varphi_k}",
            size=42,
            color=YELLOW,
        )
        self.add_line(line_2, line_1, buff=0.44)
        line_3 = self.t("于是第一个参数来自系数模长，第二个来自频率。", size=29)
        self.add_line(line_3, line_2, buff=0.48)
        line_4 = self.m(
            r"r_k=|c_k|,\quad \omega_k=k,\quad \varphi_k=\arg(c_k)",
            size=39,
            color=GREEN_B,
        )
        self.add_line(line_4, line_3, buff=0.42)
        self.wait(1.5)
        self.clear_all()

        title = self.show_title("参数表")
        headers = VGroup(
            self.m(r"k", size=30, color=YELLOW),
            self.m(r"r_k", size=30, color=YELLOW),
            self.m(r"\omega_k", size=30, color=YELLOW),
            self.m(r"\varphi_k", size=30, color=YELLOW),
        ).arrange(RIGHT, buff=0.82)
        headers.next_to(title, DOWN, buff=0.56)

        data = [
            (r"-1", r"\frac{25}{2}", r"-1", r"\frac{\pi}{2}"),
            (r"-3", r"3", r"-3", r"-\frac{\pi}{2}"),
            (r"-2", r"\frac{5}{2}", r"-2", r"-\frac{\pi}{2}"),
            (r"2", r"\frac{5}{2}", r"2", r"-\frac{\pi}{2}"),
            (r"3", r"1", r"3", r"\frac{\pi}{2}"),
            (r"1", r"\frac{1}{2}", r"1", r"\frac{\pi}{2}"),
            (r"-4", r"\frac{1}{2}", r"-4", r"-\frac{\pi}{2}"),
            (r"4", r"\frac{1}{2}", r"4", r"-\frac{\pi}{2}"),
        ]
        rows = VGroup()
        for row in data:
            rows.add(VGroup(*[self.m(value, size=27, color=WHITE) for value in row]).arrange(RIGHT, buff=0.88))
        rows.arrange(DOWN, buff=0.13).next_to(headers, DOWN, buff=0.24)
        self.play(FadeIn(headers, shift=UP * 0.1), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(row, shift=UP * 0.08) for row in rows], lag_ratio=0.08), run_time=1.6)
        note = self.t("绘图时可按半径从大到小连接，和式结果不变。", size=28, color=GREEN_B)
        note.next_to(rows, DOWN, buff=0.38)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.7)
        self.wait(2.0)
        self.clear_all()

    def draw_heart(self):
        title = self.show_title("用参数绘制爱心")
        tracker = ValueTracker(0)
        origin = LEFT * 3.35 + DOWN * 0.25
        scale = 0.125
        terms = [
            (-1, 12.5, PI / 2),
            (-3, 3.0, -PI / 2),
            (-2, 2.5, -PI / 2),
            (2, 2.5, -PI / 2),
            (3, 1.0, PI / 2),
            (1, 0.5, PI / 2),
            (-4, 0.5, -PI / 2),
            (4, 0.5, -PI / 2),
        ]
        colors = [RED_B, BLUE_B, GREEN_B, ORANGE, PURPLE_B, TEAL, MAROON_B, GOLD]
        circles = self.epicycle_group(tracker, origin, scale, terms, colors)
        final_dot = always_redraw(
            lambda: Dot(
                self.points_from_terms(tracker.get_value(), origin, scale, terms)[-1],
                radius=0.052,
                color=YELLOW,
            )
        )
        trace = TracedPath(final_dot.get_center, stroke_color=RED_B, stroke_width=5)

        side_title = self.t("绘图参数", size=31, color=YELLOW)
        side_title.to_corner(UR, buff=0.8).shift(DOWN * 0.92)
        f_1 = self.t("按参数表依次连接。", size=24, color=WHITE)
        f_2 = self.m(r"0\le t\le 2\pi", size=30, color=GREEN_B)
        f_3 = self.m(r"s=0.125", size=29, color=GRAY_A)
        VGroup(f_1, f_2, f_3).arrange(DOWN, buff=0.25).next_to(side_title, DOWN, buff=0.36)
        note = self.t("黄色端点扫出爱心。", size=26)
        note.next_to(f_3, DOWN, buff=0.48)

        self.play(
            FadeIn(circles),
            FadeIn(final_dot),
            FadeIn(side_title),
            FadeIn(f_1),
            FadeIn(f_2),
            FadeIn(f_3),
            FadeIn(note),
            run_time=0.9,
        )
        self.add(trace)
        self.play(tracker.animate.set_value(TAU), run_time=12.0, rate_func=linear)
        self.wait(1.2)
        self.clear_all()

    def summary(self):
        title = self.show_title("结论")
        line_1 = self.t("爱心曲线可以由有限个旋转向量精确合成。", size=31)
        self.add_line(line_1, title, buff=0.72)
        line_2 = self.m(
            r"P(t)=\sum_{k\in\{-4,-3,-2,-1,1,2,3,4\}} c_k e^{ikt}",
            size=34,
            color=YELLOW,
        )
        self.add_line(line_2, line_1, buff=0.5)
        line_3 = self.t("每一项对应一个圆、一条线段和一个角速度。", size=31)
        self.add_line(line_3, line_2, buff=0.5)
        line_4 = self.t("最后一个端点的轨迹就是原来的爱心图像。", size=31, color=RED_B)
        self.add_line(line_4, line_3, buff=0.42)
        self.wait(2.5)
        self.clear_all()
