from manim import *
import numpy as np


class MathematicalHearts(Scene):
    def construct(self):
        self.show_title()
        self.show_parametric_heart()
        self.show_cartesian_heart()
        self.show_polar_cardioid()
        self.show_dynamic_heart()

    def show_title(self):
        title = Text("四种经典的心形数学曲线", font="KaiTi", font_size=50)
        title.set_color_by_gradient(RED_B, RED_E)

        subtitle = Text("参数方程、代数函数、极坐标与动态参数", font="KaiTi", font_size=30)
        subtitle.set_color(GRAY)

        cover = VGroup(title, subtitle).arrange(DOWN, buff=0.8)
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(2)
        self.play(FadeOut(cover))

    def show_parametric_heart(self):
        # 构建直角坐标系
        axes = Axes(
            x_range=[-20, 20, 5],
            y_range=[-20, 20, 5],
            x_length=7,
            y_length=7,
            axis_config={"include_tip": True}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        eq_group = VGroup(
            Text("经典参数方程心形线", font="KaiTi", font_size=25),
            MathTex(r"\begin{cases} x = 16\sin^3(t) \\ y = 13\cos(t) - 5\cos(2t) - 2\cos(3t) - \cos(4t) \end{cases}",
                    font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)

        def param_func(t):
            x = 16 * (np.sin(t) ** 3)
            y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
            return axes.c2p(x, y)

        curve = ParametricFunction(param_func, t_range=[0, TAU], color=RED)

        # 增加质点轨迹追踪
        dot = Dot(color=YELLOW).move_to(param_func(0))
        trace = TracedPath(dot.get_center, stroke_color=RED, stroke_width=4)

        self.play(Create(axes), FadeIn(axes_labels), Write(eq_group))
        self.add(trace, dot)
        self.play(MoveAlongPath(dot, curve), run_time=4, rate_func=linear)
        self.play(FadeOut(dot))
        self.wait(1)
        self.play(FadeOut(VGroup(axes, axes_labels, eq_group, trace, curve)))

    def show_cartesian_heart(self):
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 2.0, 0.5],
            x_length=6,
            y_length=7
        )

        eq_group = VGroup(
            Text("笛卡尔解析心形函数", font="KaiTi", font_size=25),
            MathTex(r"y = |x|^{\frac{2}{3}} \pm \sqrt{1 - x^2}, \quad x \in [-1, 1]", font_size=35)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)

        def upper_func(x):
            val = np.clip(1 - x ** 2, 0, None)
            return np.abs(x) ** (2. / 3.) + np.sqrt(val)

        def lower_func(x):
            val = np.clip(1 - x ** 2, 0, None)
            return np.abs(x) ** (2. / 3.) - np.sqrt(val)

        upper_curve = axes.plot(upper_func, color=PINK, x_range=[-1, 1])
        lower_curve = axes.plot(lower_func, color=PINK, x_range=[-1, 1])

        self.play(Create(axes), Write(eq_group))
        self.play(Create(upper_curve), Create(lower_curve), run_time=3)
        self.wait(1)
        self.play(FadeOut(VGroup(axes, eq_group, upper_curve, lower_curve)))

    def show_polar_cardioid(self):
        # 使用原生极坐标系
        plane = PolarPlane(radius_max=4, size=6).add_coordinates()

        eq_group = VGroup(
            Text("极坐标心脏线", font="KaiTi", font_size=25),
            MathTex(r"r = a(1 - \sin\theta), \quad a=2", font_size=35)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)

        def polar_func(t):
            r = 2 * (1 - np.sin(t))
            return plane.polar_to_point(r, t)

        curve = ParametricFunction(polar_func, t_range=[0, TAU], color=PURPLE)

        self.play(Create(plane), Write(eq_group))
        self.play(Create(curve), run_time=3)
        self.wait(1)
        self.play(FadeOut(VGroup(plane, eq_group, curve)))

    def show_dynamic_heart(self):
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 2.5, 0.5],
            x_length=7,
            y_length=7
        )

        a_tracker = ValueTracker(0)

        eq_group = VGroup(
            Text("含参动态心形函数", font="KaiTi", font_size=25),
            MathTex(r"y = |x|^{\frac{2}{3}} + \sqrt{1 - x^2}\sin(a\pi x)", font_size=35)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)

        # 增加参数a的数值监视器
        a_value_text = MathTex(r"a = ").next_to(eq_group, DOWN, aligned_edge=LEFT)
        a_value = always_redraw(
            lambda: DecimalNumber(a_tracker.get_value(), num_decimal_places=1).next_to(a_value_text, RIGHT)
        )

        def lower_func(x):
            val = np.clip(1 - x ** 2, 0, None)
            return np.abs(x) ** (2. / 3.) - np.sqrt(val)

        lower_curve = axes.plot(lower_func, color=RED, x_range=[-1, 1])

        # 上半部动态函数（提高采样率防止高频锯齿）
        upper_curve = always_redraw(
            lambda: axes.plot(
                lambda x: np.abs(x) ** (2. / 3.) + np.sqrt(np.clip(1 - x ** 2, 0, None)) * np.sin(
                    a_tracker.get_value() * PI * x),
                color=RED,
                x_range=[-1, 1, 0.005]
            )
        )

        self.play(Create(axes), Write(eq_group), FadeIn(a_value_text), FadeIn(a_value))
        self.play(Create(lower_curve), Create(upper_curve))

        self.play(a_tracker.animate.set_value(30), run_time=8, rate_func=linear)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])