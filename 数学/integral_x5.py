from manim import *

class MathTexColor(MathTex):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_color_by_gradient(GREEN, BLUE, YELLOW)


class IntegrateOneOverX5PlusOneStart(MovingCameraScene):
    def construct(self):
        # ==========================================
        # 1. 开场
        # ==========================================
        title = Text("求 解 不 定 积 分", font="KaiTi", font_size=90)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        integral = MathTexColor(r"\int \frac{1}{1+x^5} \, dx = \, ?", font_size=60)

        title.shift(UP * 1.5)
        integral.next_to(title, DOWN, buff=1.5)
        self.play(Write(title))
        self.wait(0.1)
        self.play(Write(integral))

        self.wait(0.5)

        self.play(FadeOut(title), FadeOut(integral))


class IntegrateOneOverX5PlusOne(MovingCameraScene):
    def construct(self):
        # ==========================================
        # 1. 开场
        # ==========================================
        title = Text("求解不定积分", font="KaiTi", font_size=48)
        integral = MathTexColor(r"\int \frac{1}{1+x^5} \, dx", font_size=50)

        title.to_edge(UP, buff=0.8)
        integral.next_to(title, DOWN, buff=0.6)

        # ==========================================
        # 2. 步骤 1：因式分解
        # ==========================================
        self.play(self.camera.frame.animate.scale(1.2), run_time=0.5)

        step1_title = Text("步骤 1：分母因式分解", font="KaiTi", font_size=32, color=BLUE)
        # 【修改点】buff=0.5 改为 0.2，整体左移
        step1_title.next_to(integral, DOWN, buff=0.6).to_edge(LEFT, buff=0.2)

        self.play(
            self.camera.frame.animate.move_to(step1_title.get_center() + DOWN * 1 + RIGHT),
            run_time=1
        )

        self.play(Write(step1_title))

        eq1_line1 = MathTexColor(r"x^5 + 1 = (x + 1)(x^4 - x^3 + x^2 - x + 1)", font_size=40)
        eq1_line1.next_to(step1_title, DOWN, buff=0.4).align_to(step1_title, LEFT)
        self.play(Write(eq1_line1))

        eq1_line2 = MathTexColor(
            r"=", r"(x + 1)",
            r"\left( x^2 - \frac{\sqrt{5}+1}{2} x + 1 \right)",
            r"\left( x^2 + \frac{\sqrt{5}-1}{2} x + 1 \right)",
            font_size=36
        )
        eq1_line2.next_to(eq1_line1, DOWN, buff=0.3).align_to(eq1_line1, LEFT)
        self.play(Write(eq1_line2))
        self.wait(0.5)

        # ==========================================
        # 3. 步骤 2：部分分式与 a,b 常量卡片
        # ==========================================
        step2_title = Text("步骤 2：部分分式分解", font="KaiTi", font_size=32, color=YELLOW)
        # 【修改点】align_to 改为 step1_title，保持左对齐
        step2_title.next_to(eq1_line2, DOWN, buff=0.8).align_to(step1_title, LEFT)

        self.play(
            self.camera.frame.animate.move_to(step2_title.get_center() + DOWN * 1.5 + RIGHT),
            run_time=1.5
        )

        self.play(Write(step2_title))

        eq2_setup = MathTexColor(
            r"\frac{1}{1+x^5} = \frac{A}{x+1} + \frac{Bx + C}{x^2 - a x + 1} + \frac{Dx + E}{x^2 + b x + 1}",
            font_size=34
        )
        eq2_setup.next_to(step2_title, DOWN, buff=0.4).align_to(step2_title, LEFT)
        self.play(Write(eq2_setup))

        # --- 创建 a, b 常量卡片 ---
        a_val = MathTexColor(r"a = \frac{\sqrt{5}+1}{2}", font_size=28, color=PURPLE)
        b_val = MathTexColor(r"b = \frac{\sqrt{5}-1}{2}", font_size=28, color=PURPLE)

        ab_group = VGroup(a_val, b_val).arrange(DOWN, buff=0.2)
        ab_box = SurroundingRectangle(ab_group, color=PURPLE, buff=0.2, corner_radius=0.1)
        ab_card = VGroup(ab_group, ab_box)

        # 放置在镜头右上角
        camera_top_right = self.camera.frame.get_corner(UR)
        ab_card.move_to(camera_top_right + DL * 1.5)

        self.play(FadeIn(ab_card, shift=LEFT))
        # ------------------------------

        # 求解系数
        sol_A = MathTexColor(r"A = \frac{1}{5}", font_size=32, color=GREEN)
        sol_others = MathTexColor(r"B = -\frac{a}{5}, C = \frac{2}{5}, D = \frac{b}{5}, E = \frac{2}{5}", font_size=32,
                             color=GREEN)

        sol_A.next_to(eq2_setup, DOWN, buff=0.4).align_to(eq2_setup, LEFT)
        sol_others.next_to(sol_A, DOWN, buff=0.2).align_to(sol_A, LEFT)
        self.play(Write(sol_A), Write(sol_others))

        eq2_final = MathTexColor(
            r"\frac{1}{1+x^5} = \frac{1}{5}\left[ \frac{1}{x+1} + \frac{ -a x + 2 }{x^2 - a x + 1} + \frac{ b x + 2 }{x^2 + b x + 1} \right]",
            font_size=34
        )
        eq2_final.next_to(sol_others, DOWN, buff=0.5).align_to(sol_others, LEFT)
        box2 = SurroundingRectangle(eq2_final, color=WHITE, buff=0.1)
        self.play(Write(eq2_final), Create(box2))
        self.wait(0.5)

        # ==========================================
        # 4. 步骤 3：逐项积分 (带常量卡片跟随)
        # ==========================================
        step3_title = Text("步骤 3：逐项积分", font="KaiTi", font_size=32, color=TEAL)
        # 【修改点】保持左对齐
        step3_title.next_to(eq2_final, DOWN, buff=0.8).align_to(eq2_final, LEFT)

        # 运镜
        shift_vector = step3_title.get_center() + DOWN * 2 - self.camera.frame.get_center() + RIGHT

        self.play(
            self.camera.frame.animate.shift(shift_vector),
            ab_card.animate.shift(shift_vector),
            run_time=1
        )

        self.play(Write(step3_title))

        # I1
        I1 = MathTexColor(r"I_1 = \ln |x + 1|", font_size=36)
        I1.next_to(step3_title, DOWN, buff=0.5).align_to(step3_title, LEFT)
        self.play(Write(I1))

        # I2
        I2_main = MathTexColor(r"I_2 = \int \frac{ -a x + 2 }{x^2 - a x + 1} \, dx", font_size=36)
        I2_main.next_to(I1, DOWN, buff=0.6).align_to(I1, LEFT)

        shift_vec2 = DOWN * 0.8
        self.play(
            self.camera.frame.animate.shift(shift_vec2),
            ab_card.animate.shift(shift_vec2),
            Write(I2_main)
        )

        I2_res = MathTexColor(
            r"= -\frac{a}{2} \ln \left| x^2 - ax + 1 \right| + \frac{\sqrt{10 - 2\sqrt{5}}}{2} \arctan \left( \frac{4x - \sqrt{5} - 1}{\sqrt{10 - 2\sqrt{5}}} \right)",
            font_size=28, color=ORANGE
        )
        I2_res.next_to(I2_main, DOWN, buff=0.2).align_to(I2_main, LEFT)
        self.play(Write(I2_res))

        # I3
        I3_main = MathTexColor(r"I_3 = \int \frac{ b x + 2 }{x^2 + b x + 1} \, dx", font_size=36)
        I3_main.next_to(I2_res, DOWN, buff=0.6).align_to(I2_res, LEFT)

        shift_vec3 = DOWN * 1.2
        self.play(
            self.camera.frame.animate.shift(shift_vec3),
            ab_card.animate.shift(shift_vec3),
            Write(I3_main)
        )

        I3_res = MathTexColor(
            r"= \frac{b}{2} \ln \left| x^2 + bx + 1 \right| + \frac{\sqrt{10 + 2\sqrt{5}}}{2} \arctan \left( \frac{4x + \sqrt{5} - 1}{\sqrt{10 + 2\sqrt{5}}} \right)",
            font_size=28, color=ORANGE
        )
        I3_res.next_to(I3_main, DOWN, buff=0.2).align_to(I3_main, LEFT)
        self.play(Write(I3_res))
        self.wait(0.5)

        # ==========================================
        # 5. 最终结果
        # ==========================================
        all_objects = self.mobjects
        self.play(
            *[FadeOut(mob) for mob in all_objects],
            self.camera.frame.animate.move_to(ORIGIN).set_height(config["frame_height"]),
            run_time=1
        )

        final_title = Text("步骤 4：最终结果", font="KaiTi", font_size=40, color=RED)
        final_title.move_to(UP * 3)

        result_tex = MathTexColor(
            r"\int \frac{1}{1+x^5} \, dx = &\ \frac{1}{5} \ln |x + 1| \\",
            r"& - \frac{\sqrt{5} + 1}{20} \ln \left| x^2 - \frac{\sqrt{5} + 1}{2} x + 1 \right| \\",
            r"& + \frac{\sqrt{5} - 1}{20} \ln \left| x^2 + \frac{\sqrt{5} - 1}{2} x + 1 \right| \\",
            r"& + \frac{\sqrt{10 - 2\sqrt{5}}}{10} \arctan \left( \frac{4x - \sqrt{5} - 1}{\sqrt{10 - 2\sqrt{5}}} \right) \\",
            r"& + \frac{\sqrt{10 + 2\sqrt{5}}}{10} \arctan \left( \frac{4x + \sqrt{5} - 1}{\sqrt{10 + 2\sqrt{5}}} \right) + C",
            font_size=32
        )
        result_tex.next_to(final_title, DOWN, buff=0.6)

        self.play(Write(final_title))
        self.play(Write(result_tex), run_time=8)

        box_final = SurroundingRectangle(result_tex, color=YELLOW, buff=0.3)
        self.play(Create(box_final))

        self.wait(2)

        self.play(FadeOut(box_final), FadeOut(result_tex), FadeOut(final_title))