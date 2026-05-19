from manim import *


class TanPiOver48Proof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("如何求解该正切值？", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"\tan\left(\frac{\pi}{48}\right) = ?",
            font_size=60
        ).set_color(BLUE)

        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))

        # ==================== 3秒高燃倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=180)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.move_to(ORIGIN)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：基本三角恒等式 ====================
        desc_1 = Text("首先，由三角函数定义推导半角恒等式：", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_tan = MathTex(r"\tan\left(\frac{\theta}{2}\right) = \csc\theta - \cot\theta").set_color(BLUE).next_to(desc_1,
                                                                                                                 DOWN,
                                                                                                                 buff=0.6)
        self.play(Write(eq_tan))
        self.wait(1)

        eq_cot = MathTex(r"\cot\left(\frac{\theta}{2}\right) = \csc\theta + \cot\theta").set_color(GREEN).next_to(
            eq_tan, DOWN, buff=0.4)
        self.play(Write(eq_cot))
        self.wait(1)

        eq_csc = MathTex(r"\csc^2\left(\frac{\theta}{2}\right) = 1 + \cot^2\left(\frac{\theta}{2}\right)").set_color(
            YELLOW).next_to(eq_cot, DOWN, buff=0.4)
        self.play(Write(eq_csc))
        self.wait(1.5)

        desc_2 = Text("由此可得一组关于余割和余切的递推关系。", font="KaiTi", font_size=28).next_to(eq_csc, DOWN,
                                                                                                   buff=0.6)
        self.play(Write(desc_2))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(desc_1), FadeOut(eq_tan), FadeOut(eq_cot), FadeOut(eq_csc), FadeOut(desc_2)
        )

        # ==================== 第二幕：初始状态与第一次递推 ====================
        desc_3_text1 = Text("代入初始状态，令", font="KaiTi", font_size=30)
        desc_3_math = MathTex(r"\theta = \frac{\pi}{6}", font_size=32).set_color(YELLOW)
        desc_3_text2 = Text("：", font="KaiTi", font_size=30)
        desc_3 = VGroup(desc_3_text1, desc_3_math, desc_3_text2).arrange(RIGHT, buff=0.1).to_edge(UP, buff=0.8)
        self.play(Write(desc_3))

        eq_init_c = MathTex(r"C_0 = \cot\left(\frac{\pi}{6}\right) = \sqrt{3}").set_color(BLUE).next_to(desc_3, DOWN,
                                                                                                        buff=0.4)
        eq_init_s = MathTex(r"S_0 = \csc\left(\frac{\pi}{6}\right) = 2").set_color(GREEN).next_to(eq_init_c, DOWN,
                                                                                                  buff=0.3)
        self.play(Write(eq_init_c), Write(eq_init_s))
        self.wait(1)

        desc_4_text1 = Text("进行第一次计算，令", font="KaiTi", font_size=28)
        desc_4_math = MathTex(r"\theta = \frac{\pi}{12}", font_size=30).set_color(YELLOW)
        desc_4_text2 = Text("：", font="KaiTi", font_size=28)
        desc_4 = VGroup(desc_4_text1, desc_4_math, desc_4_text2).arrange(RIGHT, buff=0.1).next_to(eq_init_s, DOWN,
                                                                                                  buff=0.6)
        self.play(Write(desc_4))

        eq_step1_c = MathTex(r"C_1 = S_0 + C_0 = 2 + \sqrt{3}").next_to(desc_4, DOWN, buff=0.4)
        self.play(Write(eq_step1_c))

        desc_5 = Text("利用完全平方公式化简余割值：", font="KaiTi", font_size=28).next_to(eq_step1_c, DOWN, buff=0.4)
        self.play(Write(desc_5))

        eq_step1_s = MathTex(r"S_1 = \sqrt{1 + C_1^2} = \sqrt{2(\sqrt{3}+1)^2} = \sqrt{6} + \sqrt{2}").next_to(desc_5,
                                                                                                               DOWN,
                                                                                                               buff=0.3)
        self.play(Write(eq_step1_s))
        self.wait(2)

        # 再次整理屏幕
        self.play(
            FadeOut(desc_3), FadeOut(eq_init_c), FadeOut(eq_init_s),
            FadeOut(desc_4), FadeOut(eq_step1_c), FadeOut(desc_5), FadeOut(eq_step1_s)
        )

        # ==================== 第三幕：第二次递推计算 ====================
        desc_6_text1 = Text("进行第二次计算，令", font="KaiTi", font_size=30)
        desc_6_math = MathTex(r"\theta = \frac{\pi}{24}", font_size=32).set_color(YELLOW)
        desc_6_text2 = Text("：", font="KaiTi", font_size=30)
        desc_6 = VGroup(desc_6_text1, desc_6_math, desc_6_text2).arrange(RIGHT, buff=0.1).to_edge(UP, buff=0.8)
        self.play(Write(desc_6))

        eq_step2_c = MathTex(r"C_2 = S_1 + C_1 = \sqrt{2} + \sqrt{3} + 2 + \sqrt{6}").set_color(GREEN).next_to(desc_6,
                                                                                                               DOWN,
                                                                                                               buff=0.4)
        self.play(Write(eq_step2_c))
        self.wait(1)

        desc_7_text1 = Text("将其因式分解，方便后续求", font="KaiTi", font_size=28)
        desc_7_math = MathTex(r"S_2", font_size=30).set_color(BLUE)
        desc_7_text2 = Text("的平方：", font="KaiTi", font_size=28)
        desc_7 = VGroup(desc_7_text1, desc_7_math, desc_7_text2).arrange(RIGHT, buff=0.1).next_to(eq_step2_c, DOWN,
                                                                                                  buff=0.5)
        self.play(Write(desc_7))

        eq_step2_c_fac = MathTex(r"C_2 = (1+\sqrt{2})(\sqrt{2}+\sqrt{3})").set_color(GREEN).next_to(desc_7, DOWN,
                                                                                                    buff=0.3)
        self.play(Write(eq_step2_c_fac))
        self.wait(1)

        desc_8_text1 = Text("计算", font="KaiTi", font_size=28)
        desc_8_math1 = MathTex(r"C_2^2", font_size=30).set_color(GREEN)
        desc_8_text2 = Text("展开式，并求得", font="KaiTi", font_size=28)
        desc_8_math2 = MathTex(r"S_2", font_size=30).set_color(BLUE)
        desc_8_text3 = Text("：", font="KaiTi", font_size=28)
        desc_8 = VGroup(desc_8_text1, desc_8_math1, desc_8_text2, desc_8_math2, desc_8_text3).arrange(RIGHT,
                                                                                                      buff=0.1).next_to(
            eq_step2_c_fac, DOWN, buff=0.5)
        self.play(Write(desc_8))

        eq_step2_c_sq = MathTex(r"C_2^2 = 15 + 8\sqrt{3} + 10\sqrt{2} + 6\sqrt{6}").scale(0.9).next_to(desc_8, DOWN,
                                                                                                       buff=0.3)
        self.play(Write(eq_step2_c_sq))

        eq_step2_s = MathTex(r"S_2 = \sqrt{1 + C_2^2} = \sqrt{16 + 8\sqrt{3} + 10\sqrt{2} + 6\sqrt{6}}").scale(
            0.9).set_color(BLUE).next_to(eq_step2_c_sq, DOWN, buff=0.3)
        self.play(Write(eq_step2_s))
        self.wait(2)

        # 大清场，准备输出结论
        self.play(
            FadeOut(desc_6), FadeOut(eq_step2_c), FadeOut(desc_7),
            FadeOut(eq_step2_c_fac), FadeOut(desc_8), FadeOut(eq_step2_c_sq)
        )
        self.play(
            eq_step2_s.animate.to_edge(UP, buff=1.0)
        )

        # ==================== 第四幕：得出最终结论 ====================
        desc_9_text1 = Text("代入正切公式", font="KaiTi", font_size=30)
        desc_9_math = MathTex(r"\tan\left(\frac{\theta}{2}\right) = \csc\theta - \cot\theta", font_size=32).set_color(
            YELLOW)
        desc_9_text2 = Text("，得出结论：", font="KaiTi", font_size=30)
        desc_9 = VGroup(desc_9_text1, desc_9_math, desc_9_text2).arrange(RIGHT, buff=0.2).next_to(eq_step2_s, DOWN,
                                                                                                  buff=0.8)
        self.play(Write(desc_9))

        eq_final_logic = MathTex(r"\tan\left(\frac{\pi}{48}\right) = S_2 - C_2").set_color(GREEN).next_to(desc_9, DOWN,
                                                                                                          buff=0.5)
        self.play(Write(eq_final_logic))
        self.wait(1)

        final_ans = MathTex(
            r"\tan\left(\frac{\pi}{48}\right) = \sqrt{16 + 8\sqrt{3} + 10\sqrt{2} + 6\sqrt{6}} - (2 + \sqrt{2} + \sqrt{3} + \sqrt{6})"
        ).scale(0.85).set_color(YELLOW).next_to(eq_final_logic, DOWN, buff=0.5)

        self.play(ReplacementTransform(eq_final_logic.copy(), final_ans))

        rect_ans = SurroundingRectangle(final_ans, color=GREEN, buff=0.2)
        self.play(Create(rect_ans))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        outro_1 = Text("求解完毕", font="KaiTi", font_size=40).set_color(WHITE)
        self.play(Write(outro_1))
        self.wait(2)
        self.play(FadeOut(outro_1))
        self.wait(1)