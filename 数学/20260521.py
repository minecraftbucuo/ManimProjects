from manim import *


class InequalityProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("经典代数不等式证明", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, TEAL, GREEN)

        # 严格遵守：中文和公式分离
        cond_text1 = Text("已知实数", font="KaiTi", font_size=32)
        cond_math1 = MathTex(r"a, b, c > 0", font_size=32).set_color(TEAL)
        cond_text2 = Text("且", font="KaiTi", font_size=32)
        cond_math2 = MathTex(r"a b c = 1", font_size=32).set_color(ORANGE)
        cond_text3 = Text("，求证：", font="KaiTi", font_size=32)
        cond_group = VGroup(cond_text1, cond_math1, cond_text2, cond_math2, cond_text3).arrange(RIGHT, buff=0.1)

        eq_cover = MathTex(
            r"a^2 + b^2 + c^2", r" \ge ", r"a + b + c",
            font_size=60
        )
        eq_cover[0].set_color(BLUE)
        eq_cover[2].set_color(GREEN)

        cover = VGroup(title, cond_group, eq_cover).arrange(DOWN, buff=0.8)
        self.play(Write(title))
        self.play(FadeIn(cond_group, shift=UP))
        self.play(FadeIn(eq_cover, shift=UP))

        # ==================== 3秒倒计时 ====================
        self.wait(1)
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=180)
            countdown_text.set_color_by_gradient(GRAY, LIGHT_GREY, WHITE)
            countdown_text.move_to(ORIGIN)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：基本不等式配凑 ====================
        desc_1 = Text("根据基本不等式（均值不等式），对各项引入常数配凑：", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        # 分段染色：左边高次蓝，右边低次绿
        eq_a = MathTex(r"a^2", r" + 1 \ge ", r"2a")
        eq_a[0].set_color(BLUE)
        eq_a[2].set_color(GREEN)

        eq_b = MathTex(r"b^2", r" + 1 \ge ", r"2b")
        eq_b[0].set_color(BLUE)
        eq_b[2].set_color(GREEN)

        eq_c = MathTex(r"c^2", r" + 1 \ge ", r"2c")
        eq_c[0].set_color(BLUE)
        eq_c[2].set_color(GREEN)

        eq_group = VGroup(eq_a, eq_b, eq_c).arrange(DOWN, buff=0.4).next_to(desc_1, DOWN, buff=0.8)

        self.play(Write(eq_a))
        self.play(Write(eq_b))
        self.play(Write(eq_c))
        self.wait(1.5)

        # ==================== 第二幕：不等式相加与拆分 ====================
        desc_2 = Text("将上述三个不等式同向相加，得到：", font="KaiTi", font_size=28).next_to(eq_group, DOWN, buff=0.8)
        self.play(Write(desc_2))

        eq_sum = MathTex(r"a^2 + b^2 + c^2", r" + 3 \ge ", r"2(a + b + c)")
        eq_sum[0].set_color(BLUE)
        eq_sum[2].set_color(GREEN)
        eq_sum.next_to(desc_2, DOWN, buff=0.4)
        self.play(Write(eq_sum))
        self.wait(2)

        # 清场并将其移动到上方
        self.play(
            FadeOut(desc_1), FadeOut(eq_group), FadeOut(desc_2)
        )
        self.play(eq_sum.animate.to_edge(UP, buff=0.8))

        desc_3 = Text("将不等式右侧展开并进行结构拆解：", font="KaiTi", font_size=30).next_to(eq_sum, DOWN, buff=0.6)
        self.play(Write(desc_3))

        eq_split = MathTex(r"a^2 + b^2 + c^2", r" + 3 \ge ", r"(a + b + c)", r" + ", r"(a + b + c)")
        eq_split[0].set_color(BLUE)
        eq_split[2].set_color(GREEN)
        eq_split[4].set_color(GREEN)
        eq_split.next_to(desc_3, DOWN, buff=0.4)

        self.play(ReplacementTransform(eq_sum.copy(), eq_split))
        self.wait(2)

        # ==================== 第三幕：利用已知条件放缩 ====================
        # 局部清场
        self.play(FadeOut(eq_sum), FadeOut(desc_3))
        self.play(eq_split.animate.to_edge(UP, buff=0.8))

        desc_4_text1 = Text("由已知条件", font="KaiTi", font_size=30)
        desc_4_math = MathTex(r"abc=1", font_size=32).set_color(ORANGE)
        desc_4_text2 = Text("，再次应用三元基本不等式：", font="KaiTi", font_size=30)
        desc_4 = VGroup(desc_4_text1, desc_4_math, desc_4_text2).arrange(RIGHT, buff=0.1).next_to(eq_split, DOWN,
                                                                                                  buff=0.8)
        self.play(Write(desc_4))

        eq_am_gm = MathTex(r"a + b + c \ge 3\sqrt[3]{ abc } = 3\sqrt[3]{1} = 3")
        eq_am_gm.set_color(GREEN)
        eq_am_gm.next_to(desc_4, DOWN, buff=0.4)

        self.play(Write(eq_am_gm))

        rect_am_gm = SurroundingRectangle(eq_am_gm, color=YELLOW, buff=0.15)
        self.play(Create(rect_am_gm))
        self.wait(2)

        # ==================== 第四幕：代入并得出最终结论 ====================
        # 整体清场，准备推导最终结果
        self.play(
            FadeOut(eq_split), FadeOut(desc_4), FadeOut(eq_am_gm), FadeOut(rect_am_gm)
        )

        desc_5_text1 = Text("由于", font="KaiTi", font_size=30)
        desc_5_math = MathTex(r"a + b + c \ge 3", font_size=32)
        desc_5_math[0].set_color_by_gradient(GREEN, YELLOW)
        desc_5_text2 = Text("，将其代回拆分后的不等式右侧：", font="KaiTi", font_size=30)
        desc_5 = VGroup(desc_5_text1, desc_5_math, desc_5_text2).arrange(RIGHT, buff=0.1).to_edge(UP, buff=1.5)
        self.play(Write(desc_5))

        eq_sub = MathTex(r"a^2 + b^2 + c^2", r" + 3 \ge ", r"(a + b + c)", r" + ", r"3")
        eq_sub[0].set_color(BLUE)
        eq_sub[2].set_color(GREEN)
        eq_sub[4].set_color(YELLOW)
        eq_sub.next_to(desc_5, DOWN, buff=0.8)
        self.play(Write(eq_sub))
        self.wait(1.5)

        desc_6 = Text("不等式两边同时减去常数 3，结论即得证：", font="KaiTi", font_size=30).next_to(eq_sub, DOWN,
                                                                                                  buff=0.8)
        self.play(Write(desc_6))

        eq_final = MathTex(r"a^2 + b^2 + c^2", r" \ge ", r"a + b + c").scale(1.5)
        eq_final[0].set_color(BLUE)
        eq_final[2].set_color(GREEN)
        eq_final.next_to(desc_6, DOWN, buff=0.6)

        # 最终外框用红色和黄色渐变强调
        rect_final = SurroundingRectangle(eq_final, color=RED, buff=0.2)
        rect_final.set_color_by_gradient(RED, YELLOW)

        self.play(ReplacementTransform(eq_sub.copy(), eq_final))
        self.play(Create(rect_final))
        self.wait(3)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)