# 2025.4.20
from manimlib import *

class MovingPointOnLine(Scene):
    def construct(self):
        title = Text("点到直线距离公式的推导", font="KaiTi", font_size=80)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.move_to(2 * UP))

        # 创建坐标系
        axes = Axes(
            x_range=(-5, 5),
            y_range=(-5, 5),
            axis_config={
                "include_tip": True,
                "color": BLUE
            }
        ).scale(0.45).move_to(1.6 * DOWN)
        self.play(Write(axes))

        # 创建直线 y = 0.5x + 1
        line_start = axes.c2p(-5, 0.5 * (-5) + 1)
        line_end = axes.c2p(5, 0.5 * 5 + 1)
        line = Line(line_start, line_end, color=GREEN)
        self.play(Write(line))

        # 直线外固定点 (-1, 3)
        fixed_dot = Dot(axes.c2p(-1, 3), color=RED)
        self.play(Write(fixed_dot))

        # 创建值追踪器和移动点
        tracker = ValueTracker(0)
        moving_dot = Dot(color=YELLOW).add_updater(
            lambda m: m.move_to(
                line.point_from_proportion(tracker.get_value())
            )
        )
        self.play(Write(moving_dot))

        # 动态连接线
        connection = always_redraw(
            lambda: Line(
                fixed_dot.get_center(),
                moving_dot.get_center(),
                color=YELLOW,
                stroke_width=2
            )
        )
        self.add(connection)

        # 计算垂直点位置（通过数学推导得出参数值）
        perpendicular_proportion = 0.5  # 对应直线参数化后的0.5位置

        # 运行动画并在垂直点停止
        self.play(
            tracker.animate.set_value(perpendicular_proportion),
            rate_func=linear,
            run_time=2
        )

        # 保持最终状态
        self.play(
            tracker.animate.set_value(perpendicular_proportion),  # 保持位置
            run_time=0  # 立即完成
        )
        self.wait(0.5)
        self.play(
            FadeOut(connection, shift=DOWN),
            FadeOut(moving_dot, shift=DOWN),
            FadeOut(fixed_dot, shift=DOWN),
            FadeOut(line, shift=DOWN),
            FadeOut(axes, shift=DOWN),
            FadeOut(title, shift=DOWN),
            run_time=1
        )
        self.wait(0.3)

        gongshi = Tex(r"Ax+By+C=0 \quad \quad D(x_0,y_0)").move_to(UP * 3).set_color(BLUE)
        self.play(Write(gongshi))
        group1 = VGroup(
            Tex(r"\sqrt {(x-x_0)^2+(y-y_0)^2}"),
            Tex(r"(x-x_0)^2+(y-y_0)^2"),
            Tex(r"\left[ (x-x_0)^2+(y-y_0)^2 \right] (A^2+B^2)"),
            Tex(r"\left[ (x-x_0)^2+(y-y_0)^2 \right] (A^2+B^2) \ge \left[ A(x-x_0)+B(y-y_0) \right]^2"),
            Tex(r"\left[ (x-x_0)^2+(y-y_0)^2 \right] (A^2+B^2) \ge \left[Ax+By-(Ax_0+By_0) \right]^2"),
            Tex(r"\left[ (x-x_0)^2+(y-y_0)^2 \right] (A^2+B^2) \ge \left[-C-(Ax_0+By_0) \right]^2"),
            Tex(r"\left[ (x-x_0)^2+(y-y_0)^2 \right] (A^2+B^2) \ge \left[Ax_0+By_0+C \right]^2"),
            Tex(r"\left[ (x-x_0)^2+(y-y_0)^2 \right] \ge \frac{\left[Ax_0+By_0+C \right]^2} {A^2+B^2}"),
            Tex(r"\sqrt {(x-x_0)^2+(y-y_0)^2} \ge \frac{\left | Ax_0+By_0+C \right | } {\sqrt {A^2+B^2}}"),
        ).set_color(BLUE)

        self.play(Write(group1[0]))
        self.wait(1)
        for i in range(1, len(group1)):
            self.play(TransformMatchingTex(group1[i - 1], group1[i]))
            self.wait(1)

        rect = SurroundingRectangle(group1[-1], buff=0.05, color=YELLOW)
        self.play(Write(rect))

        self.wait(2)

        xiexie = Text("谢谢观看", font="KaiTi", font_size=140).set_color_by_gradient(BLUE, YELLOW, RED)
        self.play(
            ReplacementTransform(group1[-1], xiexie),
            FadeOut(rect),
            FadeOut(gongshi)
        )

