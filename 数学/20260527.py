from manim import *


class QuadraticFormOnCircle(Scene):
    def construct(self):
        self.camera.background_color = "#172126"

        title_color = "#f2efe6"
        text_color = "#e8e2d4"
        formula_color = "#b9d7ff"
        accent = "#d9a441"
        green = "#86d49b"
        pace = 1.35
        read_pace = 1.55

        def cn(text, size=30, color=text_color):
            return Text(text, font_size=size, color=color, font="Microsoft YaHei")

        def mt(tex, size=36, color=formula_color):
            return MathTex(tex, font_size=size, color=color)

        def mixed(*parts, buff=0.12):
            group = VGroup()
            for kind, value, size in parts:
                if kind == "text":
                    group.add(cn(value, size))
                else:
                    group.add(mt(value, size))
            group.arrange(RIGHT, buff=buff, aligned_edge=DOWN)
            return group

        def countdown():
            nums = VGroup(mt("3", 84, accent), mt("2", 84, accent), mt("1", 84, accent))
            for number in nums:
                number.move_to(2.25 * DOWN)
                self.play(FadeIn(number, scale=0.8), run_time=0.15)
                self.wait(0.7)
                self.play(FadeOut(number, scale=1.1), run_time=0.15)

        def show_block(header, lines, hold=1.2):
            head = cn(header, 30, title_color).to_edge(UP, buff=0.42)
            underline = Line(LEFT, RIGHT, color=accent).set_width(3.6).next_to(head, DOWN, buff=0.1)
            body = VGroup(*lines).arrange(DOWN, buff=0.36, aligned_edge=LEFT)
            body.next_to(underline, DOWN, buff=0.42)
            body.set_x(0)
            if body.width > 12:
                body.scale_to_fit_width(12)
            self.play(FadeIn(head), Create(underline), run_time=0.6 * pace)
            for line in body:
                self.play(FadeIn(line, shift=0.16 * DOWN), run_time=0.5 * pace)
                self.wait(0.35)
            self.wait(hold * read_pace)
            self.play(FadeOut(VGroup(head, underline, body)), run_time=0.7 * pace)

        title = cn("单位圆上二次型的最值", 40, title_color).to_edge(UP, buff=0.45)
        problem = VGroup(
            cn("求函数", 30),
            mt("f(x,y)=5x^2+4xy+2y^2", 38),
            cn("在约束", 30),
            mt("x^2+y^2=1", 38),
            cn("下的最大值与最小值。", 30),
        ).arrange(RIGHT, buff=0.16, aligned_edge=DOWN)
        problem.scale_to_fit_width(11.6).next_to(title, DOWN, buff=0.8)
        note = cn("约束集合是闭且有界的圆，连续函数必能取到最大值和最小值。", 26)
        note.next_to(problem, DOWN, buff=0.72)
        self.play(FadeIn(title), run_time=0.6 * pace)
        self.play(FadeIn(problem, shift=0.18 * DOWN), run_time=0.8 * pace)
        countdown()
        self.play(FadeIn(note), run_time=0.5 * pace)
        self.wait(2.4)
        self.play(FadeOut(VGroup(title, problem, note)), run_time=0.7 * pace)

        show_block(
            "建立拉格朗日方程",
            [
                mixed(("text", "设", 30), ("math", "g(x,y)=x^2+y^2-1", 36), ("text", "。", 30)),
                mixed(("text", "极值点满足", 30), ("math", "\\nabla f=\\lambda \\nabla g", 36), ("text", "。", 30)),
                mt(
                    "\\begin{cases}"
                    "10x+4y=2\\lambda x,\\\\"
                    "4x+4y=2\\lambda y,\\\\"
                    "x^2+y^2=1."
                    "\\end{cases}",
                    40,
                ),
            ],
            hold=1.4,
        )

        show_block(
            "化为线性方程组",
            [
                mixed(("text", "前两式同时除以", 30), ("math", "2", 34), ("text", "，得到", 30)),
                mt(
                    "\\begin{cases}"
                    "(5-\\lambda)x+2y=0,\\\\"
                    "2x+(2-\\lambda)y=0."
                    "\\end{cases}",
                    40,
                ),
                mixed(
                    ("text", "因为", 30),
                    ("math", "x^2+y^2=1", 36),
                    ("text", "，所以", 30),
                    ("math", "(x,y)\\ne(0,0)", 36),
                    ("text", "。", 30),
                ),
            ],
            hold=1.2,
        )

        show_block(
            "确定乘数",
            [
                mixed(("text", "齐次线性方程组有非零解，系数行列式必须为", 30), ("math", "0", 36), ("text", "。", 30)),
                mt(
                    "\\begin{vmatrix}"
                    "5-\\lambda&2\\\\"
                    "2&2-\\lambda"
                    "\\end{vmatrix}=0",
                    42,
                ),
                mt("(5-\\lambda)(2-\\lambda)-4=0", 40),
                mt("\\lambda^2-7\\lambda+6=0", 40),
                mixed(
                    ("math", "\\lambda=1", 40),
                    ("text", "或", 30),
                    ("math", "\\lambda=6", 40),
                ),
            ],
            hold=1.1,
        )

        head = cn("求对应点", 30, title_color).to_edge(UP, buff=0.42)
        underline = Line(LEFT, RIGHT, color=accent).set_width(2.7).next_to(head, DOWN, buff=0.1)
        left_title = mixed(("text", "当", 28), ("math", "\\lambda=1", 32), ("text", "时", 28))
        left_lines = VGroup(
            mt("4x+2y=0", 34),
            mt("y=-2x", 34),
            mt("x^2+4x^2=1", 34),
            mt("x=\\pm\\frac{1}{\\sqrt5}", 34),
            mt("y=\\mp\\frac{2}{\\sqrt5}", 34),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        left = VGroup(left_title, left_lines).arrange(DOWN, buff=0.28, aligned_edge=LEFT)

        right_title = mixed(("text", "当", 28), ("math", "\\lambda=6", 32), ("text", "时", 28))
        right_lines = VGroup(
            mt("-x+2y=0", 34),
            mt("x=2y", 34),
            mt("4y^2+y^2=1", 34),
            mt("y=\\pm\\frac{1}{\\sqrt5}", 34),
            mt("x=\\pm\\frac{2}{\\sqrt5}", 34),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        right = VGroup(right_title, right_lines).arrange(DOWN, buff=0.28, aligned_edge=LEFT)

        cols = VGroup(left, right).arrange(RIGHT, buff=1.35, aligned_edge=UP)
        cols.next_to(underline, DOWN, buff=0.48)
        if cols.width > 11.3:
            cols.scale_to_fit_width(11.3)
        self.play(FadeIn(head), Create(underline), run_time=0.6 * pace)
        self.play(FadeIn(cols, shift=0.18 * DOWN), run_time=0.8 * pace)
        self.wait(4.4)
        self.play(FadeOut(VGroup(head, underline, cols)), run_time=0.7 * pace)

        show_block(
            "计算函数值",
            [
                mixed(
                    ("text", "由", 30),
                    ("math", "\\nabla f=\\lambda\\nabla g", 36),
                    ("text", "可知", 30),
                ),
                mt("f(x,y)=5x^2+4xy+2y^2=\\lambda(x^2+y^2)", 38),
                mixed(
                    ("text", "在圆上", 30),
                    ("math", "x^2+y^2=1", 36),
                    ("text", "，所以", 30),
                    ("math", "f(x,y)=\\lambda", 36),
                    ("text", "。", 30),
                ),
                mt("\\lambda=1\\Rightarrow f=1", 38, green),
                mt("\\lambda=6\\Rightarrow f=6", 38, green),
            ],
            hold=1.3,
        )

        title2 = cn("结论", 34, title_color).to_edge(UP, buff=0.5)
        max_line = mixed(
            ("text", "最大值为", 30),
            ("math", "6", 42),
            ("text", "，在", 30),
            ("math", "\\left(\\frac{2}{\\sqrt5},\\frac{1}{\\sqrt5}\\right)", 38),
            ("text", "和", 30),
            ("math", "\\left(-\\frac{2}{\\sqrt5},-\\frac{1}{\\sqrt5}\\right)", 38),
            ("text", "处取得。", 30),
        )
        min_line = mixed(
            ("text", "最小值为", 30),
            ("math", "1", 42),
            ("text", "，在", 30),
            ("math", "\\left(\\frac{1}{\\sqrt5},-\\frac{2}{\\sqrt5}\\right)", 38),
            ("text", "和", 30),
            ("math", "\\left(-\\frac{1}{\\sqrt5},\\frac{2}{\\sqrt5}\\right)", 38),
            ("text", "处取得。", 30),
        )
        matrix_note = VGroup(
            cn("这个结果也说明：", 27),
            mt(
                "\\begin{pmatrix}x&y\\end{pmatrix}"
                "\\begin{pmatrix}5&2\\\\2&2\\end{pmatrix}"
                "\\begin{pmatrix}x\\\\y\\end{pmatrix}",
                36,
            ),
            cn("在单位圆上的取值范围由矩阵特征值确定。", 27),
        ).arrange(DOWN, buff=0.28)
        lines = VGroup(max_line, min_line, matrix_note).arrange(DOWN, buff=0.5)
        lines.next_to(title2, DOWN, buff=0.75)
        if lines.width > 12.0:
            lines.scale_to_fit_width(12.0)
        self.play(FadeIn(title2), run_time=0.5 * pace)
        self.play(FadeIn(max_line, shift=0.16 * DOWN), run_time=0.6 * pace)
        self.play(FadeIn(min_line, shift=0.16 * DOWN), run_time=0.6 * pace)
        self.play(FadeIn(matrix_note, shift=0.16 * DOWN), run_time=0.6 * pace)
        self.wait(3.6)
        self.play(FadeOut(VGroup(title2, lines)), run_time=0.8 * pace)


class QuadraticFormOnCircleCover(Scene):
    def construct(self):
        self.camera.background_color = "#10191f"

        title_color = "#f7efe0"
        text_color = "#efe7d8"
        formula_color = "#b9d7ff"
        accent = "#f0b84a"
        red = "#e26d5a"
        green = "#6fd08c"

        def cn(text, size=30, color=text_color):
            return Text(text, font_size=size, color=color, font="Microsoft YaHei")

        def mt(tex, size=40, color=formula_color):
            return MathTex(tex, font_size=size, color=color)

        def mixed(*parts, buff=0.14):
            group = VGroup()
            for kind, value, size, *maybe_color in parts:
                color = maybe_color[0] if maybe_color else (text_color if kind == "text" else formula_color)
                if kind == "text":
                    group.add(cn(value, size, color))
                else:
                    group.add(mt(value, size, color))
            group.arrange(RIGHT, buff=buff, aligned_edge=DOWN)
            return group

        top_band = Rectangle(width=14.3, height=1.7, color=accent, fill_color="#1f2f3a", fill_opacity=0.9)
        top_band.to_edge(UP, buff=0)
        accent_line = Line(LEFT, RIGHT, color=accent).set_width(12.0).move_to(2.55 * UP)

        title = cn("单位圆上二次型的最值", 48, title_color)
        title.move_to(2.95 * UP)

        problem = mixed(
            ("text", "求", 33),
            ("math", "f(x,y)=5x^2+4xy+2y^2", 46),
            ("text", "在", 33),
            ("math", "x^2+y^2=1", 46),
            ("text", "上的最值", 33),
        )
        problem.next_to(accent_line, DOWN, buff=0.45)
        if problem.width > 12.2:
            problem.scale_to_fit_width(12.2)

        plane = NumberPlane(
            x_range=[-2.2, 2.2, 1],
            y_range=[-1.7, 1.7, 1],
            x_length=5.8,
            y_length=4.4,
            background_line_style={
                "stroke_color": "#42525c",
                "stroke_width": 1,
                "stroke_opacity": 0.35,
            },
            axis_config={"stroke_color": "#8aa0ad", "stroke_width": 2},
        )
        plane.move_to(LEFT * 3.6 + DOWN * 0.85)
        circle = Circle(radius=1.0, color=accent, stroke_width=6)
        circle.set_width(2.35)
        circle.move_to(plane.c2p(0, 0))

        curve1 = ParametricFunction(
            lambda t: plane.c2p(1.15 * np.cos(t), 0.45 * np.sin(t)),
            t_range=[0, TAU],
            color=red,
            stroke_width=4,
        ).rotate(0.43, about_point=plane.c2p(0, 0))
        curve2 = ParametricFunction(
            lambda t: plane.c2p(0.72 * np.cos(t), 1.18 * np.sin(t)),
            t_range=[0, TAU],
            color=green,
            stroke_width=4,
        ).rotate(0.43, about_point=plane.c2p(0, 0))

        left_label = cn("约束圆", 25, accent).next_to(circle, DOWN, buff=0.18)

        question = VGroup(
            cn("两个方向", 34, text_color),
            cn("哪个使二次型达到边界？", 34, title_color),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        method = VGroup(
            mixed(("text", "条件", 28), ("math", "x^2+y^2=1", 36)),
            mixed(("text", "目标", 28), ("math", "\\max f,\\ \\min f", 38)),
            mixed(("text", "方法", 28), ("math", "\\nabla f=\\lambda\\nabla g", 38)),
        ).arrange(DOWN, buff=0.34, aligned_edge=LEFT)

        right_panel = VGroup(question, method).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        right_panel.move_to(RIGHT * 3.15 + DOWN * 0.75)

        tag = cn("拉格朗日乘数法", 27, "#10191f")
        tag_box = RoundedRectangle(
            corner_radius=0.08,
            width=tag.width + 0.55,
            height=0.5,
            color=accent,
            fill_color=accent,
            fill_opacity=1,
        )
        tag_group = VGroup(tag_box, tag).move_to(RIGHT * 4.2 + DOWN * 3.0)

        self.add(top_band, accent_line, title)
        self.add(problem)
        self.add(plane, curve1, curve2, circle, left_label)
        self.add(right_panel, tag_group)
