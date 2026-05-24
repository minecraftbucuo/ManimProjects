from manim import *

import manimpango


manimpango.register_font("simkai.ttf")

ZH_FONT = "KaiTi"
BLUE_MAIN = "#4CC9F0"
GREEN_MAIN = "#80ED99"
YELLOW_MAIN = "#FFD166"
RED_MAIN = "#FF6B6B"
PURPLE_MAIN = "#C77DFF"


def zh(text, font_size=32, color=WHITE):
    return Text(text, font=ZH_FONT, font_size=font_size, color=color)


def formula(tex, font_size=42, color=WHITE):
    return MathTex(tex, font_size=font_size, color=color)


def mixed_line(*parts, buff=0.12):
    return VGroup(*parts).arrange(RIGHT, buff=buff)


class QuarticReductionEquation(Scene):
    def construct(self):
        self.camera.background_color = "#0F172A"

        # Cover
        title = zh("四次方程的求解", 48)
        title.set_color_by_gradient(BLUE_MAIN, GREEN_MAIN, YELLOW_MAIN)

        problem = formula(
            r"(x+1)(x+2)(x+3)(x+4)=120",
            font_size=54,
            color=YELLOW_MAIN,
        )

        hint = mixed_line(
            zh("目标：求所有实数", 30),
            formula(r"x", 34, BLUE_MAIN),
        )

        cover = VGroup(title, problem, hint).arrange(DOWN, buff=0.65)
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(problem, shift=UP), FadeIn(hint, shift=UP), run_time=1.0)
        self.wait(0.8)

        for number in [r"3", r"2", r"1"]:
            countdown = formula(number, font_size=130, color=RED_MAIN)
            countdown.move_to(ORIGIN)
            self.play(FadeIn(countdown, scale=0.6), run_time=0.25)
            self.wait(0.25)
            self.play(FadeOut(countdown, scale=1.4), run_time=0.25)

        self.play(FadeOut(cover), run_time=0.8)

        # Step 1: symmetric pairing
        header_1 = zh("配对因式", 34, BLUE_MAIN).to_edge(UP, buff=0.55)
        original = formula(
            r"(x+1)(x+2)(x+3)(x+4)=120",
            font_size=48,
            color=WHITE,
        ).next_to(header_1, DOWN, buff=0.55)

        paired = formula(
            r"(x+1)(x+4)(x+2)(x+3)=120",
            font_size=48,
            color=WHITE,
        ).next_to(original, DOWN, buff=0.45)
        paired[0][0:6].set_color(BLUE_MAIN)
        paired[0][6:12].set_color(GREEN_MAIN)

        note_1 = mixed_line(
            zh("左右两组都会出现同一个核心：", 28),
            formula(r"x^2+5x", 32, YELLOW_MAIN),
        ).next_to(paired, DOWN, buff=0.55)

        self.play(Write(header_1), run_time=0.8)
        self.play(Write(original), run_time=0.8)
        self.play(TransformMatchingTex(original.copy(), paired), run_time=1.0)
        self.play(FadeIn(note_1, shift=UP), run_time=0.8)
        self.wait(1.0)

        # Step 2: expand the pairs
        expanded_left = formula(
            r"(x^2+5x+4)(x^2+5x+6)=120",
            font_size=47,
            color=WHITE,
        ).move_to(ORIGIN + UP * 0.5)
        expanded_left[0][1:7].set_color(YELLOW_MAIN)
        expanded_left[0][13:19].set_color(YELLOW_MAIN)

        pair_calc_1 = formula(r"(x+1)(x+4)=x^2+5x+4", font_size=39, color=BLUE_MAIN)
        pair_calc_2 = formula(r"(x+2)(x+3)=x^2+5x+6", font_size=39, color=GREEN_MAIN)
        pair_calcs = VGroup(pair_calc_1, pair_calc_2).arrange(DOWN, buff=0.32)
        pair_calcs.next_to(header_1, DOWN, buff=0.45)

        self.play(FadeOut(original), FadeOut(note_1), run_time=0.5)
        self.play(paired.animate.next_to(pair_calcs, DOWN, buff=0.5), Write(pair_calcs))
        self.wait(0.8)
        self.play(
            FadeOut(pair_calcs),
            TransformMatchingTex(paired, expanded_left),
            run_time=1.2,
        )
        self.wait(1.0)

        # Step 3: substitution
        self.play(FadeOut(header_1), run_time=0.3)
        self.wait(0.5)
        header_2 = zh("设元降次", 34, GREEN_MAIN).to_edge(UP, buff=0.55)
        substitute = mixed_line(
            zh("令", 32),
            formula(r"u=x^2+5x", 40, YELLOW_MAIN),
        ).next_to(header_2, DOWN, buff=0.5)

        reduced = formula(
            r"(u+4)(u+6)=120",
            font_size=52,
            color=WHITE,
        ).next_to(substitute, DOWN, buff=0.5)
        reduced[0][1].set_color(YELLOW_MAIN)
        reduced[0][6].set_color(YELLOW_MAIN)

        quadratic = formula(
            r"u^2+10u+24=120",
            font_size=50,
            color=WHITE,
        ).next_to(reduced, DOWN, buff=0.42)
        standard = formula(
            r"u^2+10u-96=0",
            font_size=54,
            color=BLUE_MAIN,
        ).move_to(quadratic)

        self.play(Write(header_2), run_time=0.8)
        self.play(expanded_left.animate.next_to(substitute, DOWN, buff=0.5), Write(substitute))
        self.play(TransformMatchingTex(expanded_left, reduced), run_time=1.0)
        self.play(Write(quadratic), run_time=0.8)
        self.play(FadeOut(quadratic, shift=DOWN * 0.12), run_time=0.35)
        self.play(FadeIn(standard, shift=UP * 0.12), run_time=0.55)
        self.wait(1.0)

        # Step 4: solve the auxiliary equation
        self.play(
            FadeOut(substitute),
            FadeOut(reduced),
            standard.animate.to_edge(UP, buff=1.25),
            run_time=0.8,
        )

        factor_title = mixed_line(
            zh("因式分解得到", 32),
            formula(r"u", 36, YELLOW_MAIN),
            zh("的两个候选值", 32),
        ).next_to(standard, DOWN, buff=0.55)

        factored = formula(
            r"(u-6)(u+16)=0",
            font_size=56,
            color=GREEN_MAIN,
        ).next_to(factor_title, DOWN, buff=0.45)

        u_value_left = formula(r"u=6", font_size=50, color=YELLOW_MAIN)
        u_value_or = zh("或", 32, WHITE)
        u_value_right = formula(r"u=-16", font_size=50, color=YELLOW_MAIN)
        u_values = mixed_line(u_value_left, u_value_or, u_value_right, buff=0.28)
        u_values.next_to(factored, DOWN, buff=0.5)

        self.play(Write(factor_title), run_time=0.7)
        self.play(TransformMatchingTex(standard.copy(), factored), run_time=1.0)
        self.play(Write(u_values), run_time=0.8)
        self.wait(1.0)

        # Step 5: substitute back
        self.play(
            FadeOut(header_2),
            FadeOut(standard),
            FadeOut(factor_title),
            FadeOut(factored),
            u_values.animate.to_edge(UP, buff=0.65),
            run_time=0.8,
        )
        self.wait(0.5)

        header_3 = zh("回代求解", 34, PURPLE_MAIN).next_to(u_values, DOWN, buff=0.45)
        self.play(Write(header_3), run_time=0.8)

        case_a_label = mixed_line(
            zh("情况一：", 28),
            formula(r"u=6", 34, YELLOW_MAIN),
        )
        case_a_eq = formula(r"x^2+5x=6", font_size=36, color=WHITE)
        case_a_std = formula(r"x^2+5x-6=0", font_size=36, color=BLUE_MAIN)
        case_a_factored = formula(r"(x-1)(x+6)=0", font_size=36, color=GREEN_MAIN)
        case_a_ans = mixed_line(
            formula(r"x=1", font_size=38, color=YELLOW_MAIN),
            zh("或", 28, WHITE),
            formula(r"x=-6", font_size=38, color=YELLOW_MAIN),
            buff=0.2,
        )

        case_a = VGroup(case_a_label, case_a_eq, case_a_std, case_a_factored, case_a_ans).arrange(
            DOWN, buff=0.24
        )
        case_a.move_to(LEFT * 3.25 + DOWN * 0.45)

        case_b_label = mixed_line(
            zh("情况二：", 28),
            formula(r"u=-16", 34, YELLOW_MAIN),
        )
        case_b_eq = formula(r"x^2+5x=-16", font_size=36, color=WHITE)
        case_b_std = formula(r"x^2+5x+16=0", font_size=36, color=BLUE_MAIN)
        case_b_delta = formula(r"\Delta=25-64=-39<0", font_size=36, color=RED_MAIN)
        case_b_ans = zh("没有实数解", 30, RED_MAIN)

        case_b = VGroup(case_b_label, case_b_eq, case_b_std, case_b_delta, case_b_ans).arrange(
            DOWN, buff=0.24
        )
        case_b.move_to(RIGHT * 3.25 + DOWN * 0.45)

        divider = Line(UP * 2.05, DOWN * 2.05, color=GRAY).move_to(DOWN * 0.45)

        self.play(FadeIn(case_a_label, shift=RIGHT), FadeIn(case_b_label, shift=LEFT), Create(divider))
        self.play(Write(case_a_eq), Write(case_b_eq), run_time=0.9)
        self.play(TransformMatchingTex(case_a_eq.copy(), case_a_std), TransformMatchingTex(case_b_eq.copy(), case_b_std), run_time=0.9)
        self.play(TransformMatchingTex(case_a_std.copy(), case_a_factored), Write(case_b_delta), run_time=0.9)
        self.play(Write(case_a_ans), FadeIn(case_b_ans, shift=UP), run_time=0.9)
        self.wait(1.2)

        # Final check and answer
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.8)

        final_title = zh("最后答案", 46, GREEN_MAIN).to_edge(UP, buff=0.8)
        final_values = mixed_line(
            formula(r"x=1", font_size=66, color=YELLOW_MAIN),
            zh("或", 40, WHITE),
            formula(r"x=-6", font_size=66, color=YELLOW_MAIN),
            buff=0.32,
        ).move_to(ORIGIN + UP * 0.2)

        check_line_1 = formula(
            r"(1+1)(1+2)(1+3)(1+4)=120",
            font_size=36,
            color=BLUE_MAIN,
        )
        check_line_2 = formula(
            r"(-6+1)(-6+2)(-6+3)(-6+4)=120",
            font_size=36,
            color=PURPLE_MAIN,
        )
        check_group = VGroup(check_line_1, check_line_2).arrange(DOWN, buff=0.25)
        check_group.next_to(final_values, DOWN, buff=0.65)

        closing = zh("利用对称配对，可以把四次方程化为二次方程", 31, WHITE).to_edge(DOWN, buff=0.75)

        self.play(Write(final_title), run_time=0.8)
        self.play(FadeIn(final_values, scale=1.08), run_time=0.9)
        self.play(Write(check_group), run_time=1.1)
        self.play(FadeIn(closing, shift=UP), run_time=0.8)
        self.wait(2.2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.8)
        self.wait(0.5)
