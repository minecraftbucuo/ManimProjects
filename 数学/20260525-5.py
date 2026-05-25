from manim import *

import manimpango
import numpy as np


manimpango.register_font("simkai.ttf")


class EpicycleFourierHeartTutorial(Scene):
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
        self.play(Write(title), run_time=0.75)
        self.wait(0.25)
        return title

    def add_line(self, obj, prev, buff=0.38, run_time=0.65):
        obj.next_to(prev, DOWN, buff=buff)
        self.play(FadeIn(obj, shift=UP * 0.1), run_time=run_time)
        self.wait(0.45)
        return obj

    def clear_all(self):
        self.play(*[FadeOut(obj) for obj in self.mobjects], run_time=0.65)
        self.wait(0.2)

    def points_from_terms(self, time_value, origin, scale, terms):
        points = [np.array(origin)]
        current = np.array(origin)
        for speed, radius, phase in terms:
            angle = speed * time_value + phase
            current = current + scale * radius * np.array([np.cos(angle), np.sin(angle), 0])
            points.append(current.copy())
        return points

    def epicycle_group(self, tracker, origin, scale, terms, colors, stroke_width=4):
        def build():
            points = self.points_from_terms(tracker.get_value(), origin, scale, terms)
            group = VGroup()
            for index, (_, radius, _) in enumerate(terms):
                color = colors[index % len(colors)]
                circle = Circle(radius=scale * radius, color=color, stroke_width=1.8)
                circle.move_to(points[index])
                segment = Line(points[index], points[index + 1], color=color, stroke_width=stroke_width)
                joint = Dot(points[index], radius=0.035, color=GRAY_B)
                group.add(circle, segment, joint)
            group.add(Dot(points[-1], radius=0.055, color=YELLOW))
            return group

        return always_redraw(build)

    def construct(self):
        self.cover()
        self.geometric_model()
        self.first_demo()
        self.transition_to_fourier()
        self.heart_equation()
        self.coefficients()
        self.parameter_table()
        self.draw_heart()
        self.high_view_summary()

    def cover(self):
        title = self.t("旋转圆与傅里叶绘图", size=50)
        title.set_color_by_gradient(BLUE_B, TEAL, YELLOW, RED_B)
        title.move_to(UP * 1.18)
        subtitle = self.t("从旋转线段到爱心曲线", size=31)
        subtitle.next_to(title, DOWN, buff=0.45)
        formula = self.m(r"z(t)=\sum_{k=-N}^{N}c_k e^{ikt}", size=48, color=YELLOW)
        formula.next_to(subtitle, DOWN, buff=0.55)
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(formula, shift=UP * 0.1), run_time=0.8)
        self.wait(2.0)
        self.clear_all()

    def geometric_model(self):
        title = self.show_title("几何模型")
        line_1 = self.t("每一条旋转线段都可以看作一个复数向量。", size=30)
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.m(r"c_k e^{ikt}=r_k e^{i(\omega_k t+\varphi_k)}", size=41, color=BLUE_B)
        self.add_line(line_2, line_1, buff=0.42)
        line_3 = self.t("后一条线段接在前一条线段的终点。", size=30)
        self.add_line(line_3, line_2, buff=0.45)
        line_4 = self.m(r"P(t)=c_1e^{i\omega_1t}+c_2e^{i\omega_2t}+\cdots+c_ne^{i\omega_nt}", size=32, color=GREEN_B)
        self.add_line(line_4, line_3, buff=0.42)
        line_5 = self.t("最后一个端点随时间运动，轨迹就是所画图像。", size=30)
        self.add_line(line_5, line_4, buff=0.48)
        self.wait(1.5)
        self.clear_all()

    def first_demo(self):
        title = self.show_title("先看一个自由叠加")
        tracker = ValueTracker(0)
        origin = LEFT * 3.1 + DOWN * 0.22
        terms = [
            (1, 1.15, 0),
            (-2, 0.58, PI / 4),
            (4, 0.34, -PI / 6),
            (-7, 0.22, PI / 2),
        ]
        colors = [BLUE_B, GREEN_B, ORANGE, PURPLE_B]
        circles = self.epicycle_group(tracker, origin, 1.0, terms, colors)
        final_dot = always_redraw(lambda: Dot(self.points_from_terms(tracker.get_value(), origin, 1.0, terms)[-1], radius=0.055, color=YELLOW))
        trace = TracedPath(final_dot.get_center, stroke_color=YELLOW, stroke_width=4)

        side_title = self.t("观察", size=31, color=YELLOW)
        side_title.to_corner(UR, buff=0.9).shift(DOWN * 0.92)
        side_1 = self.t("角速度不同。", size=26)
        side_2 = self.t("端点形成复杂轨迹。", size=26)
        side_3 = self.m(r"\omega=(1,-2,4,-7)", size=28, color=GREEN_B)
        VGroup(side_1, side_2, side_3).arrange(DOWN, buff=0.3).next_to(side_title, DOWN, buff=0.38)

        self.play(FadeIn(circles), FadeIn(final_dot), FadeIn(side_title), FadeIn(side_1), FadeIn(side_2), FadeIn(side_3), run_time=0.85)
        self.add(trace)
        self.play(tracker.animate.set_value(TAU * 4), run_time=8.0, rate_func=linear)
        self.wait(0.8)
        self.clear_all()

    def transition_to_fourier(self):
        title = self.show_title("从经验到方法")
        line_1 = self.t("随意选参数可以产生图案，但不能保证画出指定曲线。", size=29)
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.t("要画指定曲线，先把曲线看成一个随时间变化的复数。", size=29)
        self.add_line(line_2, line_1, buff=0.42)
        line_3 = self.m(r"z(t)=x(t)+iy(t)", size=42, color=BLUE_B)
        self.add_line(line_3, line_2, buff=0.42)
        line_4 = self.t("傅里叶级数告诉我们，周期函数可以分解成旋转指数的和。", size=28)
        self.add_line(line_4, line_3, buff=0.48)
        line_5 = self.m(r"z(t)\sim\sum_{k=-\infty}^{+\infty}c_k e^{ikt}", size=43, color=YELLOW)
        self.add_line(line_5, line_4, buff=0.42)
        line_6 = self.t("每个傅里叶系数就是一个旋转圆的参数来源。", size=30, color=GREEN_B)
        self.add_line(line_6, line_5, buff=0.48)
        self.wait(1.8)
        self.clear_all()

    def heart_equation(self):
        title = self.show_title("指定图像：爱心")
        line_1 = self.t("选用常见的爱心参数方程。", size=30)
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.m(r"x(t)=16\sin^3t", size=42, color=RED_B)
        self.add_line(line_2, line_1, buff=0.4)
        line_3 = self.m(r"y(t)=13\cos t-5\cos2t-2\cos3t-\cos4t", size=35, color=BLUE_B)
        self.add_line(line_3, line_2, buff=0.34)
        line_4 = self.m(r"0\le t\le2\pi", size=38, color=GRAY_A)
        self.add_line(line_4, line_3, buff=0.36)
        line_5 = self.t("现在的任务，是求出它的旋转圆参数。", size=30)
        self.add_line(line_5, line_4, buff=0.48)
        self.wait(1.4)
        self.clear_all()

    def coefficients(self):
        title = self.show_title("化成复指数")
        line_1 = self.mix(
            ("text", "令", 30, WHITE),
            ("math", r"z(t)=x(t)+iy(t)", 38, BLUE_B),
            ("text", "。", 30, WHITE),
        )
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.m(r"\sin^3t=\frac{3\sin t-\sin3t}{4}", size=39, color=GREEN_B)
        self.add_line(line_2, line_1, buff=0.42)
        line_3 = self.m(r"x(t)=12\sin t-4\sin3t", size=42, color=GREEN_B)
        self.add_line(line_3, line_2, buff=0.38)
        line_4 = self.t("再用欧拉公式合并同频率项。", size=30)
        self.add_line(line_4, line_3, buff=0.45)
        line_5 = self.m(r"z(t)=\sum c_k e^{ikt}", size=42, color=YELLOW)
        self.add_line(line_5, line_4, buff=0.38)
        self.wait(1.5)
        self.clear_all()

        title = self.show_title("得到傅里叶系数")
        coeffs = VGroup(
            self.m(r"c_{-1}=\frac{25}{2}i,\quad c_1=\frac{1}{2}i", size=35, color=BLUE_B),
            self.m(r"c_{-2}=-\frac{5}{2}i,\quad c_2=-\frac{5}{2}i", size=35, color=GREEN_B),
            self.m(r"c_{-3}=-3i,\quad c_3=i", size=35, color=ORANGE),
            self.m(r"c_{-4}=-\frac{1}{2}i,\quad c_4=-\frac{1}{2}i", size=35, color=PURPLE_B),
        ).arrange(DOWN, buff=0.34)
        coeffs.next_to(title, DOWN, buff=0.66)
        self.play(LaggedStart(*[FadeIn(row, shift=UP * 0.1) for row in coeffs], lag_ratio=0.16), run_time=1.5)
        note = self.t("这里是有限项，因此可以精确画出这条爱心曲线。", size=29, color=YELLOW)
        note.next_to(coeffs, DOWN, buff=0.52)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.7)
        self.wait(1.9)
        self.clear_all()

    def parameter_table(self):
        title = self.show_title("系数变成圆")
        line_1 = self.m(r"c_k=r_k e^{i\varphi_k}", size=42, color=YELLOW)
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.m(r"r_k=|c_k|,\quad \omega_k=k,\quad \varphi_k=\arg(c_k)", size=39, color=GREEN_B)
        self.add_line(line_2, line_1, buff=0.42)
        self.wait(1.0)
        self.clear_all()

        title = self.show_title("爱心的圆参数")
        headers = VGroup(
            self.m(r"k", size=30, color=YELLOW),
            self.m(r"r_k", size=30, color=YELLOW),
            self.m(r"\omega_k", size=30, color=YELLOW),
            self.m(r"\varphi_k", size=30, color=YELLOW),
        ).arrange(RIGHT, buff=0.82)
        headers.next_to(title, DOWN, buff=0.52)
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
        rows.arrange(DOWN, buff=0.12).next_to(headers, DOWN, buff=0.22)
        note = self.t("按半径从大到小连接，便于观察；和式不受顺序影响。", size=27, color=GREEN_B)
        note.next_to(rows, DOWN, buff=0.32)
        self.play(FadeIn(headers, shift=UP * 0.08), run_time=0.55)
        self.play(LaggedStart(*[FadeIn(row, shift=UP * 0.06) for row in rows], lag_ratio=0.07), run_time=1.45)
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.65)
        self.wait(1.8)
        self.clear_all()

    def draw_heart(self):
        title = self.show_title("绘制爱心")
        tracker = ValueTracker(0)
        origin = LEFT * 3.35 + DOWN * 0.22
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
        final_dot = always_redraw(lambda: Dot(self.points_from_terms(tracker.get_value(), origin, scale, terms)[-1], radius=0.052, color=YELLOW))
        trace = TracedPath(final_dot.get_center, stroke_color=RED_B, stroke_width=5)

        side_title = self.t("傅里叶描述", size=31, color=YELLOW)
        side_title.to_corner(UR, buff=0.78).shift(DOWN * 0.9)
        side_1 = self.t("一项对应一个圆。", size=25)
        side_2 = self.t("大圆决定轮廓。", size=25)
        side_3 = self.t("小圆修正细节。", size=25)
        side_4 = self.m(r"0\le t\le2\pi", size=30, color=GREEN_B)
        VGroup(side_1, side_2, side_3, side_4).arrange(DOWN, buff=0.28).next_to(side_title, DOWN, buff=0.38)

        self.play(FadeIn(circles), FadeIn(final_dot), FadeIn(side_title), FadeIn(side_1), FadeIn(side_2), FadeIn(side_3), FadeIn(side_4), run_time=0.85)
        self.add(trace)
        self.play(tracker.animate.set_value(TAU), run_time=12.0, rate_func=linear)
        self.wait(1.1)
        self.clear_all()

    def high_view_summary(self):
        title = self.show_title("高观点")
        line_1 = self.t("平面曲线可以看作复值周期信号。", size=31)
        self.add_line(line_1, title, buff=0.68)
        line_2 = self.m(r"z(t)=x(t)+iy(t)", size=42, color=BLUE_B)
        self.add_line(line_2, line_1, buff=0.42)
        line_3 = self.t("傅里叶级数把这个信号分解为不同频率的旋转圆。", size=29)
        self.add_line(line_3, line_2, buff=0.46)
        line_4 = self.m(r"c_k=\frac{1}{2\pi}\int_0^{2\pi}z(t)e^{-ikt}\,dt", size=39, color=YELLOW)
        self.add_line(line_4, line_3, buff=0.42)
        line_5 = self.t("这些系数也叫傅里叶描述子。", size=30, color=GREEN_B)
        self.add_line(line_5, line_4, buff=0.46)
        line_6 = self.t("保留更多频率，曲线细节就越完整。", size=30, color=RED_B)
        self.add_line(line_6, line_5, buff=0.36)
        self.wait(2.5)
        self.clear_all()


class EpicycleFourierHeartCover(EpicycleFourierHeartTutorial):
    def construct(self):
        self.camera.background_color = "#07080d"

        title = self.t("傅里叶旋转圆", size=58, color=YELLOW)
        title.set_color_by_gradient(YELLOW, GOLD, RED_B)
        title.to_edge(UP, buff=0.28)

        subtitle = self.t("画出爱心曲线", size=38, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.14).align_to(title, LEFT)

        formula = self.m(r"z(t)=\sum_{k=-N}^{N}c_k e^{ikt}", size=36, color=BLUE_B)
        formula.move_to(RIGHT * 3.65 + UP * 1.35)

        coeff = self.m(
            r"c_k=\frac{1}{2\pi}\int_0^{2\pi}z(t)e^{-ikt}\,dt",
            size=27,
            color=GREEN_B,
        )
        coeff.move_to(RIGHT * 3.65 + DOWN * 0.18)

        formula_frame_1 = RoundedRectangle(
            width=4.15,
            height=1.05,
            corner_radius=0.12,
            color=BLUE_E,
            fill_color="#111827",
            fill_opacity=0.46,
            stroke_width=2,
        )
        formula_frame_1.move_to(formula)
        formula_frame_2 = RoundedRectangle(
            width=4.15,
            height=0.86,
            corner_radius=0.12,
            color=GREEN_E,
            fill_color="#111827",
            fill_opacity=0.40,
            stroke_width=2,
        )
        formula_frame_2.move_to(coeff)

        origin = LEFT * 3.05 + DOWN * 0.36
        scale = 0.135
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

        heart_points = [
            self.points_from_terms(t, origin, scale, terms)[-1]
            for t in np.linspace(0, TAU, 360)
        ]
        heart = VMobject(color=RED_B, stroke_width=7)
        heart.set_points_smoothly(heart_points)
        heart.set_color_by_gradient(RED_B, RED_C, YELLOW)

        time_value = 4.75
        points = self.points_from_terms(time_value, origin, scale, terms)
        epicycles = VGroup()
        for index, (_, radius, _) in enumerate(terms):
            color = colors[index % len(colors)]
            circle = Circle(radius=scale * radius, color=color, stroke_width=2.4)
            circle.move_to(points[index])
            segment = Line(points[index], points[index + 1], color=color, stroke_width=5.2)
            joint = Dot(points[index], radius=0.035, color=GRAY_B)
            epicycles.add(circle, segment, joint)
        tip = Dot(points[-1], radius=0.07, color=YELLOW)

        glow_1 = heart.copy().set_stroke(RED_B, width=16, opacity=0.18)
        glow_2 = heart.copy().set_stroke(YELLOW, width=28, opacity=0.08)

        right_panel = VGroup()
        label_1 = self.t("复值曲线", size=26, color=GRAY_A)
        label_2 = self.t("傅里叶系数", size=26, color=GRAY_A)
        label_3 = self.t("旋转圆参数", size=26, color=GRAY_A)
        arrow_1 = self.m(r"\longrightarrow", size=34, color=YELLOW)
        arrow_2 = self.m(r"\longrightarrow", size=34, color=YELLOW)
        right_panel.add(label_1, arrow_1, label_2, arrow_2, label_3)
        right_panel.arrange(RIGHT, buff=0.16)
        right_panel.to_edge(DOWN, buff=0.55).shift(RIGHT * 1.3)

        badge = RoundedRectangle(
            width=2.65,
            height=0.52,
            corner_radius=0.12,
            color=RED_B,
            fill_color=RED_E,
            fill_opacity=0.62,
            stroke_width=2,
        )
        badge_text = self.t("参数方程到图像", size=21, color=WHITE)
        badge_group = VGroup(badge, badge_text).move_to(RIGHT * 3.65 + DOWN * 1.08)

        sparkles = VGroup(
            Star(n=5, outer_radius=0.1, inner_radius=0.04, color=YELLOW, fill_opacity=0.9).move_to(LEFT * 5.7 + UP * 1.75),
            Star(n=5, outer_radius=0.075, inner_radius=0.03, color=BLUE_B, fill_opacity=0.9).move_to(LEFT * 1.05 + UP * 1.95),
            Star(n=5, outer_radius=0.085, inner_radius=0.034, color=GREEN_B, fill_opacity=0.9).move_to(RIGHT * 5.55 + DOWN * 1.45),
        )

        divider = Line(UP * 1.78, DOWN * 1.75, color=GRAY_E, stroke_width=2)
        divider.move_to(RIGHT * 0.78 + DOWN * 0.12)
        divider.set_opacity(0.55)

        right_panel.move_to(RIGHT * 1.25 + DOWN * 3.05)

        self.add(glow_2, glow_1, heart, epicycles, tip)
        self.add(formula_frame_1, formula_frame_2, divider)
        self.add(title, subtitle, formula, coeff, right_panel, badge_group, sparkles)
