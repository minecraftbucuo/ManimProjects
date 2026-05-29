from manim import *

import manimpango


manimpango.register_font("simkai.ttf")


TEXT_FONT = "KaiTi"
BG_COLOR = "#0B1220"
TEXT_COLOR = "#F8FAFC"
MUTED_COLOR = "#CBD5E1"
A_COLOR = "#38BDF8"
B_COLOR = "#F97316"
C_COLOR = "#A78BFA"
TRIANGLE_COLOR = "#22C55E"
TRIANGLE_FILL = "#064E3B"
RESULT_COLOR = "#FDE047"


def t(content, size=32, color=TEXT_COLOR):
    return Text(content, font=TEXT_FONT, font_size=size, color=color)


def m(content, size=40, color=TEXT_COLOR):
    return MathTex(content, font_size=size, color=color)


def mix(*parts, buff=0.12):
    group = VGroup()
    for kind, content, size, color in parts:
        group.add(t(content, size, color) if kind == "text" else m(content, size, color))
    group.arrange(RIGHT, buff=buff)
    return group


class PythagoreanTheoremProof(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.show_cover()
        self.show_triangle()
        left_square, right_square = self.show_two_arrangements()
        self.finish_proof(left_square, right_square)
        self.show_similarity_proof()
        self.show_garfield_proof()
        self.show_summary()

    def show_cover(self):
        title = t("勾股定理的面积证明", size=54, color=RESULT_COLOR)
        formula = m(r"a^2+b^2=c^2", size=58, color=TEXT_COLOR)
        formula.set_color_by_tex("a", A_COLOR)
        formula.set_color_by_tex("b", B_COLOR)
        formula.set_color_by_tex("c", C_COLOR)
        subtitle = t("三个角度：重排、相似、梯形面积", size=30, color=MUTED_COLOR)
        group = VGroup(title, formula, subtitle).arrange(DOWN, buff=0.36)

        self.play(FadeIn(title, shift=DOWN), run_time=0.8)
        self.play(Write(formula), run_time=1.0)
        self.play(FadeIn(subtitle, shift=UP * 0.15), run_time=0.7)
        self.wait(1.3)
        self.play(FadeOut(group), run_time=0.8)

    def show_triangle(self):
        title = t("先看一个直角三角形", size=36, color=RESULT_COLOR).to_edge(UP, buff=0.42)

        a, b = 3.25, 2.05
        p0 = LEFT * 1.8 + DOWN * 1.1
        p1 = p0 + RIGHT * a
        p2 = p0 + UP * b
        triangle = Polygon(
            p0,
            p1,
            p2,
            color=TRIANGLE_COLOR,
            stroke_width=5,
            fill_color=TRIANGLE_FILL,
            fill_opacity=0.72,
        )
        right_angle = RightAngle(Line(p0, p1), Line(p0, p2), length=0.28, color=TEXT_COLOR)

        a_label = m("a", size=42, color=A_COLOR).next_to(Line(p0, p1), DOWN, buff=0.18)
        b_label = m("b", size=42, color=B_COLOR).next_to(Line(p0, p2), LEFT, buff=0.18)
        c_label = self.edge_label("c", p1, p2, C_COLOR, size=42, offset=0.33, side=-1)

        note = mix(
            ("text", "两条直角边为", 28, TEXT_COLOR),
            ("math", "a,b", 34, TEXT_COLOR),
            ("text", "，斜边为", 28, TEXT_COLOR),
            ("math", "c", 34, C_COLOR),
        )
        note.next_to(triangle, DOWN, buff=0.55)

        self.play(FadeIn(title), run_time=0.6)
        self.play(Create(triangle), Create(right_angle), run_time=1.0)
        self.play(FadeIn(VGroup(a_label, b_label, c_label)), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.12), run_time=0.7)
        self.wait(1.4)
        self.play(FadeOut(VGroup(title, triangle, right_angle, a_label, b_label, c_label, note)), run_time=0.8)

    def edge_label(self, content, p_start, p_end, color, size=34, offset=0.24, side=1):
        direction = p_end - p_start
        normal = np.array([-direction[1], direction[0], 0.0])
        length = np.linalg.norm(normal)
        if length > 0:
            normal = normal / length
        label = m(content, size=size, color=color)
        label.move_to((p_start + p_end) / 2 + normal * offset * side)
        return label

    def local_to_scene(self, x, y, center, side):
        return center + np.array([x - side / 2, y - side / 2, 0])

    def triangle_at(self, points, fill_opacity=0.76):
        return Polygon(
            *points,
            color=TRIANGLE_COLOR,
            stroke_width=3,
            fill_color=TRIANGLE_FILL,
            fill_opacity=fill_opacity,
        )

    def left_arrangement(self, center, a, b):
        side = a + b
        p = lambda x, y: self.local_to_scene(x, y, center, side)

        outer = Square(side_length=side, color=TEXT_COLOR, stroke_width=4).move_to(center)
        triangles = VGroup(
            self.triangle_at([p(0, 0), p(b, 0), p(0, a)]),
            self.triangle_at([p(side, 0), p(b, 0), p(side, b)]),
            self.triangle_at([p(side, side), p(side, b), p(a, side)]),
            self.triangle_at([p(0, side), p(a, side), p(0, a)]),
        )
        c_square = Polygon(
            p(b, 0),
            p(side, b),
            p(a, side),
            p(0, a),
            color=C_COLOR,
            stroke_width=5,
            fill_color="#312E81",
            fill_opacity=0.72,
        )
        c_label = m("c^2", size=38, color=C_COLOR).move_to(c_square.get_center())
        side_label = mix(
            ("math", "a+b", 30, RESULT_COLOR),
        )
        side_label.next_to(outer, DOWN, buff=0.18)
        caption = t("摆法一：中间剩下斜边正方形", size=25, color=MUTED_COLOR).next_to(outer, UP, buff=0.2)
        return VGroup(outer, triangles, c_square, c_label, side_label, caption)

    def right_arrangement(self, center, a, b):
        side = a + b
        p = lambda x, y: self.local_to_scene(x, y, center, side)

        outer = Square(side_length=side, color=TEXT_COLOR, stroke_width=4).move_to(center)
        a_square = Square(side_length=a, color=A_COLOR, stroke_width=5, fill_color="#075985", fill_opacity=0.72)
        a_square.move_to((p(0, 0) + p(a, a)) / 2)
        b_square = Square(side_length=b, color=B_COLOR, stroke_width=5, fill_color="#7C2D12", fill_opacity=0.72)
        b_square.move_to((p(a, a) + p(side, side)) / 2)

        triangles = VGroup(
            self.triangle_at([p(a, 0), p(side, 0), p(side, a)]),
            self.triangle_at([p(a, 0), p(a, a), p(side, a)]),
            self.triangle_at([p(0, a), p(0, side), p(a, side)]),
            self.triangle_at([p(0, a), p(a, a), p(a, side)]),
        )
        a_label = m("a^2", size=36, color=A_COLOR).move_to(a_square)
        b_label = m("b^2", size=36, color=B_COLOR).move_to(b_square)
        side_label = mix(
            ("math", "a+b", 30, RESULT_COLOR),
        )
        side_label.next_to(outer, DOWN, buff=0.18)
        caption = t("摆法二：中间剩下两个直角边正方形", size=25, color=MUTED_COLOR).next_to(outer, UP, buff=0.2)
        return VGroup(outer, a_square, b_square, triangles, a_label, b_label, side_label, caption)

    def show_two_arrangements(self):
        title = t("证明一：重排面积", size=36, color=RESULT_COLOR).to_edge(UP, buff=0.35)
        a, b = 1.92, 1.26
        left = self.left_arrangement(LEFT * 3.25 + DOWN * 0.15, a, b)
        right = self.right_arrangement(RIGHT * 3.25 + DOWN * 0.15, a, b)
        divider = DashedLine(UP * 2.55, DOWN * 2.85, color="#475569", stroke_width=2)

        left_outer, left_triangles, left_c_square, left_c_label = left[0], left[1], left[2], left[3]
        right_outer, right_a_square, right_b_square, right_triangles, right_a_label, right_b_label = (
            right[0],
            right[1],
            right[2],
            right[3],
            right[4],
            right[5],
        )

        self.play(FadeIn(title), Create(divider), run_time=0.7)
        self.play(Create(left_outer), Create(right_outer), run_time=0.9)
        self.play(
            LaggedStart(
                *[FadeIn(tri, scale=0.88) for tri in left_triangles],
                *[FadeIn(tri, scale=0.88) for tri in right_triangles],
                lag_ratio=0.08,
            ),
            run_time=1.6,
        )
        self.play(
            FadeIn(left[5], shift=DOWN * 0.1),
            FadeIn(right[7], shift=DOWN * 0.1),
            FadeIn(left[4]),
            FadeIn(right[6]),
            run_time=0.8,
        )
        self.wait(0.6)
        self.play(FadeIn(left_c_square), FadeIn(left_c_label), run_time=0.8)
        self.play(FadeIn(right_a_square), FadeIn(right_b_square), FadeIn(right_a_label), FadeIn(right_b_label), run_time=0.8)
        self.wait(1.2)

        same_triangles = t("四个绿色三角形全等，且数量相同", size=28, color=TRIANGLE_COLOR)
        same_triangles.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(same_triangles, shift=UP * 0.15), run_time=0.7)
        self.play(
            AnimationGroup(
                *[Indicate(tri, color=RESULT_COLOR, scale_factor=1.03) for tri in left_triangles],
                lag_ratio=0.05,
            ),
            AnimationGroup(
                *[Indicate(tri, color=RESULT_COLOR, scale_factor=1.03) for tri in right_triangles],
                lag_ratio=0.05,
            ),
            run_time=1.4,
        )
        self.wait(0.9)
        self.play(FadeOut(same_triangles), FadeOut(title), FadeOut(divider), run_time=0.7)
        return left, right

    def finish_proof(self, left_square, right_square):
        statement = t("减去相同的四个三角形，剩余面积必然相等", size=32, color=RESULT_COLOR)
        statement.to_edge(UP, buff=0.38)

        c_area = left_square[2]
        a_area = right_square[1]
        b_area = right_square[2]
        c_label = left_square[3]
        a_label = right_square[4]
        b_label = right_square[5]

        self.play(FadeIn(statement), run_time=0.7)
        self.play(
            Indicate(c_area, color=C_COLOR, scale_factor=1.04),
            Indicate(a_area, color=A_COLOR, scale_factor=1.04),
            Indicate(b_area, color=B_COLOR, scale_factor=1.04),
            run_time=1.2,
        )
        equation = m(r"c^2=a^2+b^2", size=52, color=TEXT_COLOR)
        equation.set_color_by_tex("c", C_COLOR)
        equation.set_color_by_tex("a", A_COLOR)
        equation.set_color_by_tex("b", B_COLOR)
        equation.to_edge(DOWN, buff=0.28)
        self.play(Write(equation), run_time=0.9)
        self.wait(0.7)

        final = m(r"\boxed{a^2+b^2=c^2}", size=60, color=RESULT_COLOR)
        final.move_to(ORIGIN).shift(DOWN * 0.15)
        final.set_color_by_tex("a", A_COLOR)
        final.set_color_by_tex("b", B_COLOR)
        final.set_color_by_tex("c", C_COLOR)
        box = SurroundingRectangle(final, buff=0.2, color=RESULT_COLOR, stroke_width=3)

        self.play(
            FadeOut(statement),
            FadeOut(left_square),
            FadeOut(right_square),
            FadeOut(equation),
            run_time=0.9,
        )
        closing = t("所以，任意直角三角形都有", size=33, color=TEXT_COLOR)
        closing.next_to(final, UP, buff=0.42)
        self.play(FadeIn(closing), Write(final), Create(box), run_time=1.2)
        self.wait(2.4)
        self.play(FadeOut(VGroup(closing, final, box)), run_time=0.8)

    def show_similarity_proof(self):
        title = t("证明二：相似三角形", size=36, color=RESULT_COLOR).to_edge(UP, buff=0.35)

        p_a = LEFT * 3.35 + DOWN * 1.7
        p_b = p_a + RIGHT * 5.2
        p_c = p_a + UP * 3.0
        hyp = p_c - p_b
        foot = p_b + np.dot(p_a - p_b, hyp) / np.dot(hyp, hyp) * hyp

        triangle = Polygon(
            p_a,
            p_b,
            p_c,
            color=TRIANGLE_COLOR,
            stroke_width=5,
            fill_color=TRIANGLE_FILL,
            fill_opacity=0.58,
        )
        altitude = DashedLine(p_a, foot, color=RESULT_COLOR, stroke_width=4)
        right_angle = RightAngle(Line(p_a, p_b), Line(p_a, p_c), length=0.24, color=TEXT_COLOR)
        foot_angle = RightAngle(Line(foot, p_a), Line(foot, p_b), length=0.18, color=RESULT_COLOR)

        a_label = self.edge_label("a", p_a, p_b, A_COLOR, size=38, offset=0.25, side=-1)
        b_label = self.edge_label("b", p_a, p_c, B_COLOR, size=38, offset=0.25, side=1)
        c_label = self.edge_label("c", p_b, p_c, C_COLOR, size=38, offset=0.26, side=-1)
        x_label = self.edge_label("x", p_b, foot, RESULT_COLOR, size=31, offset=0.24, side=1)
        y_label = self.edge_label("y", foot, p_c, RESULT_COLOR, size=31, offset=0.24, side=1)
        d_label = t("垂足", size=22, color=MUTED_COLOR).next_to(foot, LEFT, buff=0.12)

        formulas = VGroup(
            t("斜边被高分成两段：", size=27, color=MUTED_COLOR),
            m(r"x+y=c", size=38, color=RESULT_COLOR),
            m(r"a^2=cx,\qquad b^2=cy", size=38, color=TEXT_COLOR),
            m(r"a^2+b^2=cx+cy", size=38, color=TEXT_COLOR),
            m(r"a^2+b^2=c(x+y)=c^2", size=40, color=RESULT_COLOR),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        formulas.to_edge(RIGHT, buff=0.55).shift(DOWN * 0.12)
        formulas[2].set_color_by_tex("a", A_COLOR)
        formulas[2].set_color_by_tex("b", B_COLOR)
        formulas[2].set_color_by_tex("c", C_COLOR)
        formulas[3].set_color_by_tex("a", A_COLOR)
        formulas[3].set_color_by_tex("b", B_COLOR)
        formulas[3].set_color_by_tex("c", C_COLOR)
        formulas[4].set_color_by_tex("a", A_COLOR)
        formulas[4].set_color_by_tex("b", B_COLOR)
        formulas[4].set_color_by_tex("c", C_COLOR)

        self.play(FadeIn(title), run_time=0.7)
        self.play(Create(triangle), Create(right_angle), run_time=1.0)
        self.play(FadeIn(VGroup(a_label, b_label, c_label)), run_time=0.7)
        self.play(Create(altitude), Create(foot_angle), FadeIn(VGroup(x_label, y_label, d_label)), run_time=0.9)
        self.wait(0.5)
        self.play(FadeIn(formulas[0], shift=UP * 0.1), run_time=0.5)
        for line in formulas[1:]:
            self.play(Write(line), run_time=0.75)
            self.wait(0.35)
        self.wait(1.6)
        self.play(
            FadeOut(VGroup(title, triangle, altitude, right_angle, foot_angle, a_label, b_label, c_label, x_label, y_label, d_label, formulas)),
            run_time=0.9,
        )

    def show_garfield_proof(self):
        title = t("证明三：加菲尔德梯形证明", size=36, color=RESULT_COLOR).to_edge(UP, buff=0.35)

        a_len, b_len = 2.35, 1.5
        origin = LEFT * 3.7 + DOWN * 1.9
        p0 = origin
        p1 = origin + RIGHT * b_len
        p2 = origin + UP * a_len
        p3 = origin + UP * (a_len + b_len)
        p4 = p3 + RIGHT * a_len

        trapezoid = Polygon(p0, p1, p4, p3, color=TEXT_COLOR, stroke_width=5)
        tri_left = Polygon(p0, p1, p2, color=TRIANGLE_COLOR, stroke_width=3, fill_color=TRIANGLE_FILL, fill_opacity=0.7)
        tri_right = Polygon(p2, p3, p4, color=TRIANGLE_COLOR, stroke_width=3, fill_color=TRIANGLE_FILL, fill_opacity=0.7)
        middle = Polygon(p1, p2, p4, color=C_COLOR, stroke_width=5, fill_color="#312E81", fill_opacity=0.7)
        right_left = RightAngle(Line(p0, p1), Line(p0, p2), length=0.18, color=TEXT_COLOR)
        right_right = RightAngle(Line(p3, p2), Line(p3, p4), length=0.18, color=TEXT_COLOR)
        middle_angle = RightAngle(Line(p2, p1), Line(p2, p4), length=0.2, color=RESULT_COLOR)

        a_top = self.edge_label("a", p3, p4, A_COLOR, size=33, offset=0.22, side=1)
        a_left = self.edge_label("a", p0, p2, A_COLOR, size=33, offset=0.22, side=1)
        b_bottom = self.edge_label("b", p0, p1, B_COLOR, size=33, offset=0.22, side=-1)
        b_side = self.edge_label("b", p2, p3, B_COLOR, size=33, offset=0.22, side=1)
        c_one = self.edge_label("c", p1, p2, C_COLOR, size=34, offset=0.24, side=-1)
        c_two = self.edge_label("c", p2, p4, C_COLOR, size=34, offset=0.24, side=-1)

        note = t("梯形面积 = 三个三角形面积之和", size=28, color=MUTED_COLOR)
        note.next_to(trapezoid, DOWN, buff=0.35)

        formulas = VGroup(
            m(r"S_1=\frac{1}{2}(a+b)^2", size=35, color=TEXT_COLOR),
            m(r"S_2=\frac{ab}{2}+\frac{ab}{2}+\frac{c^2}{2}", size=35, color=TEXT_COLOR),
            m(r"\frac{(a+b)^2}{2}=ab+\frac{c^2}{2}", size=38, color=TEXT_COLOR),
            m(r"a^2+b^2=c^2", size=46, color=RESULT_COLOR),
        ).arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        formulas.to_edge(RIGHT, buff=0.55).shift(DOWN * 0.1)
        for formula in formulas:
            formula.set_color_by_tex("a", A_COLOR)
            formula.set_color_by_tex("b", B_COLOR)
            formula.set_color_by_tex("c", C_COLOR)

        self.play(FadeIn(title), run_time=0.7)
        self.play(Create(trapezoid), run_time=0.8)
        self.play(
            FadeIn(tri_left, scale=0.94),
            FadeIn(tri_right, scale=0.94),
            FadeIn(middle, scale=0.94),
            run_time=1.0,
        )
        self.play(
            FadeIn(VGroup(a_top, a_left, b_bottom, b_side, c_one, c_two, note)),
            Create(right_left),
            Create(right_right),
            Create(middle_angle),
            run_time=0.9,
        )
        for line in formulas:
            self.play(Write(line), run_time=0.8)
            self.wait(0.35)
        self.wait(1.7)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    trapezoid,
                    tri_left,
                    tri_right,
                    middle,
                    right_left,
                    right_right,
                    middle_angle,
                    a_top,
                    a_left,
                    b_bottom,
                    b_side,
                    c_one,
                    c_two,
                    note,
                    formulas,
                )
            ),
            run_time=0.9,
        )

    def show_summary(self):
        title = t("三种证明，指向同一个结论", size=42, color=RESULT_COLOR).to_edge(UP, buff=0.55)
        lines = VGroup(
            t("1. 重排面积：相同大正方形，减去相同三角形", size=30, color=TEXT_COLOR),
            t("2. 相似三角形：斜边投影给出平方关系", size=30, color=TEXT_COLOR),
            t("3. 梯形面积：同一图形两种算法", size=30, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        result = m(r"\boxed{a^2+b^2=c^2}", size=60, color=RESULT_COLOR)
        result.set_color_by_tex("a", A_COLOR)
        result.set_color_by_tex("b", B_COLOR)
        result.set_color_by_tex("c", C_COLOR)
        group = VGroup(lines, result).arrange(DOWN, buff=0.58)
        group.move_to(ORIGIN).shift(DOWN * 0.1)
        box = SurroundingRectangle(result, buff=0.2, color=RESULT_COLOR, stroke_width=3)

        self.play(FadeIn(title, shift=DOWN), run_time=0.8)
        for line in lines:
            self.play(FadeIn(line, shift=UP * 0.12), run_time=0.55)
        self.play(Write(result), Create(box), run_time=1.0)
        self.wait(2.6)
