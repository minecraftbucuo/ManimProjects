from manim import *


class FactorialSumIntegerProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("求所有正整数使得：", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"\frac{n}{1!} + \frac{n}{2!} + \cdots + \frac{n}{n!} \in \mathbb{Z}^+",
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

        # ==================== 第一幕：设列与末项化简 ====================
        desc_1_t1 = Text("设原式总和为", font="KaiTi", font_size=30)
        desc_1_m1 = MathTex(r"S_n", font_size=32).set_color(YELLOW)
        desc_1_t2 = Text("，提取末项进行化简：", font="KaiTi", font_size=30)
        desc_1 = VGroup(desc_1_t1, desc_1_m1, desc_1_t2).arrange(RIGHT, buff=0.1)
        desc_1.to_edge(UP, buff=0.8)
        desc_1.shift(UP * 0.4)
        self.play(Write(desc_1))

        eq_orig = MathTex(r"S_n = \sum_{k=1}^{n-1} \frac{n}{k!} + \frac{n}{n!}").set_color(BLUE).next_to(desc_1, DOWN,
                                                                                                         buff=0.5)
        self.play(Write(eq_orig))
        self.wait(1.5)

        desc_2_t1 = Text("根据阶乘的定义，末项可变形为：", font="KaiTi", font_size=28)
        desc_2 = VGroup(desc_2_t1).arrange(RIGHT, buff=0.1).next_to(eq_orig, DOWN, buff=0.5)
        self.play(Write(desc_2))

        eq_sq_1 = MathTex(r"\frac{n}{n!} = \frac{n}{n \cdot (n-1)!} = ", r"\frac{1}{(n-1)!}")
        eq_sq_1[1].set_color(YELLOW)
        eq_sq_1.next_to(desc_2, DOWN, buff=0.3)
        self.play(Write(eq_sq_1))
        self.wait(1)

        desc_3_t1 = Text("将其代回原式，和式重写为：", font="KaiTi", font_size=28)
        desc_3 = VGroup(desc_3_t1).arrange(RIGHT, buff=0.1).next_to(eq_sq_1, DOWN, buff=0.5)
        self.play(Write(desc_3))

        eq_sq_final = MathTex(r"S_n = \sum_{k=1}^{n-1} \frac{n}{k!} + ", r"\frac{1}{(n-1)!}")
        eq_sq_final[0].set_color(BLUE)
        eq_sq_final[1].set_color(YELLOW)
        eq_sq_final.next_to(desc_3, DOWN, buff=0.3)
        self.play(ReplacementTransform(eq_orig.copy(), eq_sq_final))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(desc_1), FadeOut(eq_orig), FadeOut(desc_2), FadeOut(eq_sq_1), FadeOut(desc_3)
        )
        self.play(eq_sq_final.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：同乘与分离整数 ====================
        desc_4_t1 = Text("假设当", font="KaiTi", font_size=30)
        desc_4_m1 = MathTex(r"n \ge 4", font_size=32).set_color(YELLOW)
        desc_4_t2 = Text("时，", font="KaiTi", font_size=30)
        desc_4_m2 = MathTex(r"S_n", font_size=32).set_color(YELLOW)
        desc_4_t3 = Text("为整数。", font="KaiTi", font_size=30)
        desc_4 = VGroup(desc_4_t1, desc_4_m1, desc_4_t2, desc_4_m2, desc_4_t3).arrange(RIGHT, buff=0.1)
        desc_4.next_to(eq_sq_final, DOWN, buff=0.6)
        self.play(Write(desc_4))

        desc_5_t1 = Text("在等式两端同乘", font="KaiTi", font_size=28)
        desc_5_m1 = MathTex(r"(n-2)!", font_size=30).set_color(YELLOW)
        desc_5_t2 = Text("，以隔离可能的真分数项：", font="KaiTi", font_size=28)
        desc_5 = VGroup(desc_5_t1, desc_5_m1, desc_5_t2).arrange(RIGHT, buff=0.1).next_to(desc_4, DOWN, buff=0.3)
        self.play(Write(desc_5))

        eq_def_g = MathTex(
            r"(n-2)! \cdot S_n = (n-2)! \left( \sum_{k=1}^{n-2} \frac{n}{k!} + \frac{n}{(n-1)!} + \frac{1}{(n-1)!} \right)"
        ).scale(0.85).set_color(GREEN).next_to(desc_5, DOWN, buff=0.4)
        self.play(Write(eq_def_g))
        self.wait(1)

        desc_6_t1 = Text("将右侧展开并分析各项的整除性：", font="KaiTi", font_size=28)
        desc_6 = VGroup(desc_6_t1).arrange(RIGHT, buff=0.1).next_to(eq_def_g, DOWN, buff=0.5)
        self.play(Write(desc_6))

        eq_dict = MathTex(
            r"(n-2)! \cdot S_n = ", r"I", r" + \frac{n}{n-1} + \frac{1}{n-1}"
        ).set_color(GREEN).scale(1.1).next_to(desc_6, DOWN, buff=0.3)
        eq_dict[1].set_color(BLUE)
        self.play(TransformMatchingTex(eq_def_g.copy(), eq_dict))

        rect_dict = SurroundingRectangle(eq_dict, color=GREEN, buff=0.15)
        self.play(Create(rect_dict))
        self.wait(2)

        # 再次整理屏幕
        self.play(
            FadeOut(desc_4), FadeOut(desc_5), FadeOut(eq_def_g), FadeOut(desc_6), FadeOut(eq_sq_final)
        )
        dict_group = VGroup(eq_dict, rect_dict)
        self.play(dict_group.animate.to_edge(UP, buff=0.8))

        # ==================== 第三幕：矛盾推导 ====================
        desc_7_t1 = Text("其中", font="KaiTi", font_size=28)
        desc_7_m1 = MathTex(r"I", font_size=30).set_color(BLUE)
        desc_7_t2 = Text("为前项乘积之和，必定为整数。合并剩余分数项：", font="KaiTi", font_size=28)
        desc_7 = VGroup(desc_7_t1, desc_7_m1, desc_7_t2).arrange(RIGHT, buff=0.1).next_to(dict_group, DOWN, buff=0.6)
        self.play(Write(desc_7))

        eq_trans = MathTex(
            r"(n-2)! \cdot S_n = I + \frac{n+1}{n-1} = I + 1 + ", r"\frac{2}{n-1}"
        ).set_color(GREEN).next_to(desc_7, DOWN, buff=0.4)
        eq_trans[1].set_color(YELLOW)
        self.play(ReplacementTransform(eq_dict.copy(), eq_trans))
        self.wait(1.5)

        desc_8_t1 = Text("等式左侧与", font="KaiTi", font_size=28)
        desc_8_m1 = MathTex(r"I+1", font_size=30).set_color(BLUE)
        desc_8_t2 = Text("均为整数，故要求：", font="KaiTi", font_size=28)
        desc_8 = VGroup(desc_8_t1, desc_8_m1, desc_8_t2).arrange(RIGHT, buff=0.1).next_to(eq_trans, DOWN, buff=0.5)
        self.play(Write(desc_8))

        eq_core = MathTex(r"\frac{2}{n-1} \in \mathbb{Z}").scale(1.2).set_color(YELLOW).next_to(desc_8, DOWN, buff=0.4)
        self.play(Write(eq_core))
        self.wait(2)

        desc_9_t1 = Text("然而，根据前面的假设", font="KaiTi", font_size=28)
        desc_9_m1 = MathTex(r"n \ge 4", font_size=30).set_color(YELLOW)
        desc_9_t2 = Text("，可推出：", font="KaiTi", font_size=28)
        desc_9 = VGroup(desc_9_t1, desc_9_m1, desc_9_t2).arrange(RIGHT, buff=0.1).next_to(eq_core, DOWN, buff=0.5)
        desc_9.shift(LEFT * 3.3)
        desc_9.shift(UP * 0.3)
        self.play(Write(desc_9))

        eq_contradiction = MathTex(r"n - 1 \ge 3 \implies 0 < \frac{2}{n-1} < 1").set_color(RED).next_to(desc_9, RIGHT,
                                                                                                         buff=0.4)
        self.play(Write(eq_contradiction))
        self.wait(1.5)

        # 大清场
        self.play(
            FadeOut(dict_group), FadeOut(desc_7), FadeOut(eq_trans), FadeOut(desc_8),
            FadeOut(eq_core), FadeOut(desc_9), FadeOut(eq_contradiction)
        )

        # ==================== 第四幕：得出最终结论 ====================
        desc_11_t1 = Text("真分数不可能为整数，产生矛盾。", font="KaiTi", font_size=35)
        desc_11 = VGroup(desc_11_t1).arrange(RIGHT, buff=0.1).to_edge(UP, buff=1.5)
        self.play(Write(desc_11))

        desc_12_t1 = Text("因此，", font="KaiTi", font_size=30)
        desc_12_m1 = MathTex(r"n \ge 4", font_size=32).set_color(YELLOW)
        desc_12_t2 = Text("时原式无整数解。", font="KaiTi", font_size=30)
        desc_12 = VGroup(desc_12_t1, desc_12_m1, desc_12_t2).arrange(RIGHT, buff=0.1).next_to(desc_11, DOWN, buff=0.8)
        self.play(Write(desc_12))
        self.wait(1)

        outro_1_t1 = Text("只需验证", font="KaiTi", font_size=30)
        outro_1_m1 = MathTex(r"n = 1, 2, 3", font_size=32).set_color(YELLOW)
        outro_1_t2 = Text("的情况，代入算得总和分别为 1, 3, 5。均符合题意。", font="KaiTi", font_size=30)
        outro_1 = VGroup(outro_1_t1, outro_1_m1, outro_1_t2).arrange(RIGHT, buff=0.1).next_to(desc_12, DOWN, buff=0.8)
        self.play(Write(outro_1))
        self.wait(1.5)

        outro_2_t1 = Text("最终解集为：", font="KaiTi", font_size=35)
        outro_2 = VGroup(outro_2_t1).arrange(RIGHT, buff=0.1).next_to(outro_1, DOWN, buff=1)
        self.play(Write(outro_2))

        final_ans = MathTex(r"n \in \{1, 2, 3\}").scale(1.5).set_color(GREEN).next_to(outro_2, DOWN, buff=0.6)
        self.play(Write(final_ans))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)