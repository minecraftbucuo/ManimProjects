from manim import *

import manimpango


manimpango.register_font("simkai.ttf")


class RecurrenceCover(Scene):
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

    def construct(self):
        background = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color="#050712",
            fill_opacity=1,
            stroke_width=0,
        )
        self.add(background)

        accent_top = Line(LEFT * 5.35, RIGHT * 5.35, stroke_width=7)
        accent_top.set_color_by_gradient(BLUE_B, TEAL, GREEN_B, YELLOW)
        accent_top.move_to(UP * 2.75)

        accent_bottom = Line(LEFT * 5.35, RIGHT * 5.35, stroke_width=7)
        accent_bottom.set_color_by_gradient(YELLOW, GREEN_B, TEAL, BLUE_B)
        accent_bottom.move_to(DOWN * 2.75)

        title = self.t("二重特征根递推求通项", size=58)
        title.set_color_by_gradient(YELLOW, GREEN_B, TEAL)
        title.move_to(UP * 1.85)

        panel = RoundedRectangle(
            width=11.25,
            height=3.55,
            corner_radius=0.14,
            stroke_width=2.4,
            stroke_color=TEAL,
            fill_color="#081728",
            fill_opacity=0.92,
        )
        panel.move_to(DOWN * 0.28)

        label = self.t("题目", size=36, color=YELLOW)
        label.move_to(UP * 0.85)

        line_1 = self.mix(
            ("text", "已知数列满足", 31, WHITE),
            ("math", r"a_0=1,\quad a_1=4", 38, BLUE_B),
        )
        line_1.move_to(UP * 0.18)

        line_2 = self.m(
            r"a_{n+2}-4a_{n+1}+4a_n=(n+1)2^n,\quad n\ge 0",
            size=39,
            color=WHITE,
        )
        line_2.set_color_by_tex("2^n", YELLOW)
        line_2.move_to(DOWN * 0.62)

        line_3 = self.mix(
            ("text", "求", 33, WHITE),
            ("math", r"a_n", 42, GREEN_B),
            ("text", "的通项公式", 33, WHITE),
        )
        line_3.move_to(DOWN * 1.36)

        side_left = Rectangle(
            width=0.12,
            height=3.55,
            stroke_width=0,
            fill_color=BLUE_B,
            fill_opacity=1,
        )
        side_left.next_to(panel, LEFT, buff=0.12)
        side_right = Rectangle(
            width=0.12,
            height=3.55,
            stroke_width=0,
            fill_color=YELLOW,
            fill_opacity=1,
        )
        side_right.next_to(panel, RIGHT, buff=0.12)

        cover = VGroup(
            accent_top,
            accent_bottom,
            panel,
            side_left,
            side_right,
            title,
            label,
            line_1,
            line_2,
            line_3,
        )
        self.add(cover)
