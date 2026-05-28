from manim import *


TEXT_FONT = "KaiTi"
BG_COLOR = "#111827"
TEXT_COLOR = "#F8FAFC"
MATH_COLOR = "#93C5FD"
ACCENT_COLOR = "#FBBF24"
RESULT_COLOR = "#86EFAC"
MUTED_COLOR = "#CBD5E1"


def text(content, size=34, color=TEXT_COLOR):
    return Text(content, font=TEXT_FONT, font_size=size, color=color)


def math(content, size=42, color=MATH_COLOR):
    return MathTex(content, font_size=size, color=color)


def mixed(*parts, buff=0.12):
    mobs = []
    for kind, content, size, color in parts:
        if kind == "text":
            mobs.append(text(content, size=size, color=color))
        else:
            mobs.append(math(content, size=size, color=color))
    return VGroup(*mobs).arrange(RIGHT, buff=buff)


class CauchyMinimumSolution(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.pace = 1.45
        self.read_pace = 2.15

        title = text("柯西不等式求最小值", size=44, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.34)
        problem = VGroup(
            mixed(
                ("text", "已知", 31, TEXT_COLOR),
                ("math", "x,y,z>0", 37, MATH_COLOR),
                ("text", "且", 31, TEXT_COLOR),
                ("math", "x+y+z=1", 37, MATH_COLOR),
            ),
            mixed(
                ("text", "求", 31, TEXT_COLOR),
                ("math", r"\frac{1}{x}+\frac{1}{y}+\frac{1}{z}", 40, MATH_COLOR),
                ("text", "的最小值。", 31, TEXT_COLOR),
            ),
        ).arrange(DOWN, buff=0.32)
        problem.next_to(title, DOWN, buff=0.45)
        problem_box = SurroundingRectangle(problem, buff=0.25, color=ACCENT_COLOR)

        self.play(FadeIn(title, shift=DOWN), run_time=0.9)
        self.play(FadeIn(problem), Create(problem_box), run_time=1.3)
        self.wait(1.6)

        for number in ["3", "2", "1"]:
            countdown = Text(number, font=TEXT_FONT, font_size=148, color=ACCENT_COLOR)
            self.play(FadeIn(countdown, scale=0.6), run_time=0.25)
            self.wait(0.5)
            self.play(FadeOut(countdown, scale=1.35), run_time=0.25)
        self.wait(0.4)

        self.play(
            FadeOut(title),
            FadeOut(problem_box),
            FadeOut(problem),
            run_time=1.1,
        )

        self.show_inequality_form()
        self.show_apply_cauchy()
        self.show_equality_case()
        self.show_conclusion()

    def show_centered_block(self, header, lines, hold=1.4, max_width=11.5):
        head = text(header, size=34, color=ACCENT_COLOR).to_edge(UP, buff=0.42)
        underline = Line(LEFT, RIGHT, color=ACCENT_COLOR).set_width(3.8)
        underline.next_to(head, DOWN, buff=0.12)
        body = VGroup(*lines).arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        if body.width > max_width:
            body.scale_to_fit_width(max_width)
        body.next_to(underline, DOWN, buff=0.46)
        body.set_x(0)

        self.play(FadeIn(head), Create(underline), run_time=0.75 * self.pace)
        for line in body:
            self.play(FadeIn(line, shift=0.16 * DOWN), run_time=0.85 * self.pace)
            self.wait(0.75 * self.read_pace)
        self.wait(hold * self.read_pace)
        self.play(FadeOut(VGroup(head, underline, body)), run_time=0.9 * self.pace)

    def show_inequality_form(self):
        eq1 = math(
            r"(a_1^2+a_2^2+a_3^2)(b_1^2+b_2^2+b_3^2)"
            r"\geq(a_1b_1+a_2b_2+a_3b_3)^2",
            size=31,
        )
        self.show_centered_block(
            "使用柯西不等式",
            [
                text("先写出本题需要的形式。", size=29),
                eq1,
                text("等号成立当且仅当两组数成比例。", size=29, color=MUTED_COLOR),
            ],
            hold=2.2,
        )

    def show_apply_cauchy(self):
        line = mixed(
            ("text", "取", 30, TEXT_COLOR),
            ("math", r"a_1=\frac{1}{\sqrt{x}},\ a_2=\frac{1}{\sqrt{y}},\ a_3=\frac{1}{\sqrt{z}}", 35, MATH_COLOR),
        )
        line2 = mixed(
            ("text", "并取", 30, TEXT_COLOR),
            ("math", r"b_1=\sqrt{x},\ b_2=\sqrt{y},\ b_3=\sqrt{z}", 35, MATH_COLOR),
        )
        eq1 = math(
            r"\left(\frac{1}{x}+\frac{1}{y}+\frac{1}{z}\right)(x+y+z)"
            r"\geq(1+1+1)^2",
            size=33,
        )
        eq2 = math(
            r"\left(\frac{1}{x}+\frac{1}{y}+\frac{1}{z}\right)(x+y+z)\geq9",
            size=37,
        )
        eq3 = math(r"x+y+z=1", size=39, color=ACCENT_COLOR)
        eq4 = math(r"\frac{1}{x}+\frac{1}{y}+\frac{1}{z}\geq9", size=42, color=RESULT_COLOR)
        self.show_centered_block(
            "选择两组三项",
            [line, line2, eq1, eq2, eq3, eq4],
            hold=2.4,
        )

    def show_equality_case(self):
        eq1 = math(
            r"\frac{1}{\sqrt{x}}:\frac{1}{\sqrt{y}}:\frac{1}{\sqrt{z}}"
            r"=\sqrt{x}:\sqrt{y}:\sqrt{z}",
            size=36,
        )
        eq2 = math(r"x=y=z", size=43, color=ACCENT_COLOR)
        eq3 = math(r"x+y+z=1", size=39)
        eq4 = math(r"x=y=z=\frac{1}{3}", size=43, color=RESULT_COLOR)
        self.show_centered_block(
            "检查等号成立条件",
            [
                text("只有下界能够取到时，它才是最小值。", size=29),
                eq1,
                eq2,
                eq3,
                eq4,
            ],
            hold=2.3,
        )

    def show_conclusion(self):
        section = text("得到最小值", size=36, color=ACCENT_COLOR)
        section.to_edge(UP, buff=0.6)

        eq1 = math(r"\frac{1}{x}+\frac{1}{y}+\frac{1}{z}\geq9", size=46)
        eq2_math = math(r"x=y=z=\frac{1}{3}", size=42, color=MATH_COLOR)
        eq2_text = text("时等号成立", size=32, color=TEXT_COLOR)
        eq2_group = VGroup(eq2_math, eq2_text).arrange(RIGHT, buff=0.18)
        eq3 = math(r"\boxed{\min\left(\frac{1}{x}+\frac{1}{y}+\frac{1}{z}\right)=9}", size=48, color=RESULT_COLOR)
        group = VGroup(eq1, eq2_group, eq3).arrange(DOWN, buff=0.58)
        group.move_to(ORIGIN).shift(DOWN * 0.12)
        box = SurroundingRectangle(eq3, buff=0.22, color=RESULT_COLOR)

        self.play(FadeIn(section, shift=DOWN), run_time=0.75 * self.pace)
        self.play(Write(eq1), run_time=1.25 * self.pace)
        self.wait(1.2 * self.read_pace)
        self.play(FadeIn(eq2_group), run_time=0.95 * self.pace)
        self.wait(1.25 * self.read_pace)
        self.play(Write(eq3), Create(box), run_time=1.35 * self.pace)
        self.wait(2.2 * self.read_pace)


class CauchyMinimumCover(Scene):
    def construct(self):
        self.camera.background_color = "#0B1020"

        panel = RoundedRectangle(
            width=11.35,
            height=5.55,
            corner_radius=0.22,
            stroke_color=ACCENT_COLOR,
            stroke_width=5,
            fill_color="#111827",
            fill_opacity=0.92,
        )
        panel.move_to(DOWN * 0.05)

        title = text("柯西不等式", size=76, color=ACCENT_COLOR)
        subtitle = text("求约束条件下的最小值", size=38, color=TEXT_COLOR)
        condition = mixed(
            ("math", "x,y,z>0", 46, MATH_COLOR),
            ("text", "且", 34, TEXT_COLOR),
            ("math", "x+y+z=1", 46, MATH_COLOR),
        )
        target = math(r"\frac{1}{x}+\frac{1}{y}+\frac{1}{z}\geq ?", size=58, color=MATH_COLOR)
        request = mixed(
            ("text", "求最小值与等号条件", 32, TEXT_COLOR),
        )

        title.move_to(UP * 2.08)
        subtitle.next_to(title, DOWN, buff=0.18)
        condition.next_to(subtitle, DOWN, buff=0.42)
        target.next_to(condition, DOWN, buff=0.34)
        request.next_to(target, DOWN, buff=0.34)

        left_line = Line(LEFT * 5.45 + DOWN * 2.28, LEFT * 5.45 + UP * 2.28, color=RESULT_COLOR, stroke_width=8)
        right_line = Line(RIGHT * 5.45 + DOWN * 2.28, RIGHT * 5.45 + UP * 2.28, color=RESULT_COLOR, stroke_width=8)

        self.add(panel, left_line, right_line, title, subtitle, condition, target, request)
