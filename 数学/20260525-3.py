from manim import *

import manimpango
import numpy as np


manimpango.register_font("simkai.ttf")


class RotatingCirclesDrawingTutorial(Scene):
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
        self.wait(0.35)
        return title

    def add_line(self, obj, prev=None, buff=0.36, run_time=0.7):
        if prev is None:
            obj.next_to(UP * 2.55, DOWN)
        else:
            obj.next_to(prev, DOWN, buff=buff)
        self.play(FadeIn(obj, shift=UP * 0.12), run_time=run_time)
        self.wait(0.65)
        return obj

    def clear_all(self):
        self.play(*[FadeOut(obj) for obj in self.mobjects], run_time=0.7)
        self.wait(0.25)

    def epicycle_points(self, time_value, origin, radii, speeds, phases):
        points = [origin]
        current = np.array(origin)
        for radius, speed, phase in zip(radii, speeds, phases):
            angle = speed * time_value + phase
            current = current + radius * np.array([np.cos(angle), np.sin(angle), 0])
            points.append(current.copy())
        return points

    def epicycle_group(self, tracker, origin, radii, speeds, phases, colors):
        def build():
            time_value = tracker.get_value()
            points = self.epicycle_points(time_value, origin, radii, speeds, phases)
            group = VGroup()
            for index, radius in enumerate(radii):
                circle = Circle(radius=radius, color=colors[index], stroke_width=2)
                circle.move_to(points[index])
                segment = Line(points[index], points[index + 1], color=colors[index], stroke_width=5)
                joint = Dot(points[index], radius=0.045, color=GRAY_B)
                group.add(circle, segment, joint)
            group.add(Dot(points[-1], radius=0.055, color=YELLOW))
            return group

        return always_redraw(build)

    def construct(self):
        self.cover()
        self.vector_model()
        self.single_circle()
        self.two_circles()
        self.full_drawing()
        self.parameter_table()
        self.summary()

    def cover(self):
        title = self.t("旋转圆绘图教程", size=50)
        title.set_color_by_gradient(BLUE_B, TEAL, GREEN_B, YELLOW)
        title.move_to(UP * 1.2)
        subtitle = self.t("用不同角速度的线段相连来生成轨迹", size=31)
        subtitle.next_to(title, DOWN, buff=0.5)
        formula = self.m(
            r"z(t)=\sum_{k=1}^{n} r_k e^{i(\omega_k t+\varphi_k)}",
            size=43,
            color=YELLOW,
        )
        formula.next_to(subtitle, DOWN, buff=0.55)
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.12), run_time=0.7)
        self.play(FadeIn(formula, shift=UP * 0.12), run_time=0.8)
        self.wait(2.2)
        self.clear_all()

    def vector_model(self):
        title = self.show_title("基本模型")
        line_1 = self.t("把每一条旋转线段看作一个向量。", size=30)
        self.add_line(line_1, title, buff=0.62)
        line_2 = self.m(
            r"\vec v_k(t)=r_k(\cos(\omega_k t+\varphi_k),\sin(\omega_k t+\varphi_k))",
            size=34,
            color=BLUE_B,
        )
        self.add_line(line_2, line_1, buff=0.43)
        line_3 = self.t("后一条线段的起点放在前一条线段的终点。", size=30)
        self.add_line(line_3, line_2, buff=0.46)
        line_4 = self.m(
            r"P(t)=\vec v_1(t)+\vec v_2(t)+\cdots+\vec v_n(t)",
            size=40,
            color=GREEN_B,
        )
        self.add_line(line_4, line_3, buff=0.43)
        line_5 = self.t("当时间连续变化时，最后一个端点扫出的曲线就是图像。", size=29)
        self.add_line(line_5, line_4, buff=0.48)
        self.wait(1.8)
        self.clear_all()

    def single_circle(self):
        title = self.show_title("一个旋转圆")
        tracker = ValueTracker(0)
        origin = LEFT * 2.7 + DOWN * 0.15
        radii = [1.15]
        speeds = [1]
        phases = [0]
        colors = [BLUE_B]
        circle_group = self.epicycle_group(tracker, origin, radii, speeds, phases, colors)
        moving_dot = always_redraw(
            lambda: Dot(
                self.epicycle_points(tracker.get_value(), origin, radii, speeds, phases)[-1],
                radius=0.06,
                color=YELLOW,
            )
        )
        trace = TracedPath(moving_dot.get_center, stroke_color=YELLOW, stroke_width=4)
        note_1 = self.t("只有一条线段时，端点画出一个圆。", size=29)
        note_1.to_corner(UR, buff=0.75).shift(DOWN * 1.0)
        formula = self.m(r"P(t)=r_1e^{i\omega_1t}", size=38, color=BLUE_B)
        formula.next_to(note_1, DOWN, buff=0.42)
        self.play(FadeIn(circle_group), FadeIn(moving_dot), FadeIn(note_1), FadeIn(formula), run_time=0.8)
        self.add(trace)
        self.play(tracker.animate.set_value(TAU), run_time=4.0, rate_func=linear)
        self.wait(1.0)
        self.clear_all()

    def two_circles(self):
        title = self.show_title("两个旋转圆")
        tracker = ValueTracker(0)
        origin = LEFT * 3.1 + DOWN * 0.15
        radii = [1.25, 0.58]
        speeds = [1, -3]
        phases = [0, PI / 3]
        colors = [BLUE_B, GREEN_B]
        circle_group = self.epicycle_group(tracker, origin, radii, speeds, phases, colors)
        moving_dot = always_redraw(
            lambda: Dot(
                self.epicycle_points(tracker.get_value(), origin, radii, speeds, phases)[-1],
                radius=0.06,
                color=YELLOW,
            )
        )
        trace = TracedPath(moving_dot.get_center, stroke_color=YELLOW, stroke_width=4)
        note_1 = self.t("第二条线段接在第一条的端点上。", size=29)
        note_1.to_corner(UR, buff=0.72).shift(DOWN * 0.9)
        note_2 = self.t("角速度不同，端点不再只画圆。", size=29)
        note_2.next_to(note_1, DOWN, buff=0.38)
        formula = self.m(
            r"P(t)=r_1e^{it}+r_2e^{-3it+i\varphi_2}",
            size=35,
            color=GREEN_B,
        )
        formula.next_to(note_2, DOWN, buff=0.45)
        self.play(FadeIn(circle_group), FadeIn(moving_dot), FadeIn(note_1), FadeIn(note_2), FadeIn(formula), run_time=0.9)
        self.add(trace)
        self.play(tracker.animate.set_value(TAU * 2), run_time=7.0, rate_func=linear)
        self.wait(1.0)
        self.clear_all()

    def full_drawing(self):
        title = self.show_title("多个圆叠加绘图")
        tracker = ValueTracker(0)
        origin = LEFT * 3.15 + DOWN * 0.25
        radii = [1.22, 0.62, 0.38, 0.24]
        speeds = [1, -2, 4, -7]
        phases = [0, PI / 4, -PI / 6, PI / 2]
        colors = [BLUE_B, GREEN_B, ORANGE, PURPLE_B]
        circle_group = self.epicycle_group(tracker, origin, radii, speeds, phases, colors)
        final_dot = always_redraw(
            lambda: Dot(
                self.epicycle_points(tracker.get_value(), origin, radii, speeds, phases)[-1],
                radius=0.055,
                color=YELLOW,
            )
        )
        trace = TracedPath(final_dot.get_center, stroke_color=YELLOW, stroke_width=4)
        side_title = self.t("本例参数", size=31, color=YELLOW)
        side_title.to_corner(UR, buff=0.9).shift(DOWN * 0.85)
        param_1 = self.m(r"r=(1.22,0.62,0.38,0.24)", size=26, color=BLUE_B)
        param_2 = self.m(r"\omega=(1,-2,4,-7)", size=28, color=GREEN_B)
        param_3 = self.m(r"\varphi=(0,\frac{\pi}{4},-\frac{\pi}{6},\frac{\pi}{2})", size=28, color=ORANGE)
        VGroup(param_1, param_2, param_3).arrange(DOWN, buff=0.24).next_to(side_title, DOWN, buff=0.38)
        instruction = self.t("观察黄色端点的轨迹。", size=25)
        instruction.next_to(param_3, DOWN, buff=0.5)
        self.play(
            FadeIn(circle_group),
            FadeIn(final_dot),
            FadeIn(side_title),
            FadeIn(param_1),
            FadeIn(param_2),
            FadeIn(param_3),
            FadeIn(instruction),
            run_time=0.9,
        )
        self.add(trace)
        self.play(tracker.animate.set_value(TAU * 5), run_time=13.0, rate_func=linear)
        self.wait(1.2)
        self.clear_all()

    def parameter_table(self):
        title = self.show_title("怎样设计图像")
        rows = VGroup(
            self.mix(("math", r"r_k", 34, BLUE_B), ("text", "控制第", 29, WHITE), ("math", r"k", 34, BLUE_B), ("text", "条线段的长度", 29, WHITE)),
            self.mix(("math", r"\omega_k", 34, GREEN_B), ("text", "控制旋转速度和方向", 29, WHITE)),
            self.mix(("math", r"\varphi_k", 34, ORANGE), ("text", "控制起始角度", 29, WHITE)),
            self.mix(("math", r"n", 34, PURPLE_B), ("text", "控制叠加的线段数量", 29, WHITE)),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        rows.next_to(title, DOWN, buff=0.62)
        self.play(LaggedStart(*[FadeIn(row, shift=UP * 0.12) for row in rows], lag_ratio=0.18), run_time=1.6)
        self.wait(0.8)
        line = Line(LEFT * 5.1, RIGHT * 5.1, color=GRAY_D, stroke_width=2)
        line.next_to(rows, DOWN, buff=0.5)
        self.play(Create(line), run_time=0.5)
        rule_1 = self.t("一般先取较大的主半径，再添加较小半径修正细节。", size=29)
        rule_2 = self.t("角速度取整数时，轨迹较容易形成闭合图案。", size=29)
        VGroup(rule_1, rule_2).arrange(DOWN, buff=0.34).next_to(line, DOWN, buff=0.46)
        self.play(FadeIn(rule_1, shift=UP * 0.12), run_time=0.7)
        self.play(FadeIn(rule_2, shift=UP * 0.12), run_time=0.7)
        self.wait(2.0)
        self.clear_all()

    def summary(self):
        title = self.show_title("总结")
        line_1 = self.t("旋转圆绘图的本质是向量相加。", size=32)
        self.add_line(line_1, title, buff=0.75)
        line_2 = self.m(
            r"P(t)=\sum_{k=1}^{n} r_k e^{i(\omega_k t+\varphi_k)}",
            size=44,
            color=YELLOW,
        )
        self.add_line(line_2, line_1, buff=0.55)
        line_3 = self.t("把每个时刻的最终端点连起来，就得到一条曲线。", size=31)
        self.add_line(line_3, line_2, buff=0.55)
        line_4 = self.t("改变半径、角速度和初相位，就能改变图像形状。", size=31, color=GREEN_B)
        self.add_line(line_4, line_3, buff=0.42)
        self.wait(2.5)
        self.clear_all()
