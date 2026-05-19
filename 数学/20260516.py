from manim import *


class DiophantineEquationProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("求所有正整数满足：", font="KaiTi", font_size=50)

        eq_cover = MathTex(
            r"4^a + 4a^2 + 4 = b^2",
            font_size=60
        ).set_color(BLUE)

        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))

        # ==================== 3秒倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=180)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.move_to(ORIGIN)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：提取公因式 ====================
        desc_1 = Text("首先提取等式左边的公因数：", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_orig = MathTex(r"4(4^{a-1} + a^2 + 1) = b^2").set_color(BLUE).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(eq_orig))
        self.wait(1.5)

        # 拼接文字与公式
        desc_2_t1 = Text("由此可知", font="KaiTi", font_size=28)
        desc_2_m1 = MathTex(r"b^2", font_size=30).set_color(YELLOW)
        desc_2_t2 = Text("是4的倍数，设", font="KaiTi", font_size=28)
        desc_2_m2 = MathTex(r"b = 2k", font_size=30).set_color(YELLOW)
        desc_2 = VGroup(desc_2_t1, desc_2_m1, desc_2_t2, desc_2_m2).arrange(RIGHT, buff=0.1)
        desc_2.next_to(eq_orig, DOWN, buff=0.5)
        self.play(Write(desc_2))

        eq_sub = MathTex(r"4(4^{a-1} + a^2 + 1) = 4k^2").next_to(desc_2, DOWN, buff=0.3)
        self.play(Write(eq_sub))
        self.wait(1)

        desc_3 = Text("化简并将其写成完全平方的形式：", font="KaiTi", font_size=28).next_to(eq_sub, DOWN, buff=0.5)
        self.play(Write(desc_3))

        eq_sq_final = MathTex(r"(2^{a-1})^2 + a^2 + 1 = k^2").set_color(GREEN)
        eq_sq_final.next_to(desc_3, DOWN, buff=0.3)
        self.play(TransformMatchingTex(eq_sub.copy(), eq_sq_final))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(desc_1), FadeOut(eq_orig), FadeOut(desc_2), FadeOut(eq_sub), FadeOut(desc_3)
        )
        self.play(eq_sq_final.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：平方数放缩 ====================
        desc_4_t1 = Text("因为", font="KaiTi", font_size=28)
        desc_4_m1 = MathTex(r"a \ge 1", font_size=30).set_color(YELLOW)
        desc_4_t2 = Text("，所以", font="KaiTi", font_size=28)
        desc_4_m2 = MathTex(r"a^2 + 1 > 0", font_size=30).set_color(YELLOW)
        desc_4 = VGroup(desc_4_t1, desc_4_m1, desc_4_t2, desc_4_m2).arrange(RIGHT, buff=0.1)
        desc_4.next_to(eq_sq_final, DOWN, buff=0.6)
        self.play(Write(desc_4))

        desc_5 = Text("显然有以下不等关系：", font="KaiTi", font_size=28).next_to(desc_4, DOWN, buff=0.4)
        self.play(Write(desc_5))

        eq_ineq_1 = MathTex(r"k^2 > (2^{a-1})^2 \implies k > 2^{a-1}").set_color(BLUE).next_to(desc_5, DOWN, buff=0.4)
        self.play(Write(eq_ineq_1))
        self.wait(1)

        desc_6_t1 = Text("由于", font="KaiTi", font_size=28)
        desc_6_m1 = MathTex(r"k", font_size=30).set_color(YELLOW)
        desc_6_t2 = Text("为整数，必然满足：", font="KaiTi", font_size=28)
        desc_6 = VGroup(desc_6_t1, desc_6_m1, desc_6_t2).arrange(RIGHT, buff=0.1)
        desc_6.next_to(eq_ineq_1, DOWN, buff=0.5)
        self.play(Write(desc_6))

        eq_ineq_2 = MathTex(r"k \ge 2^{a-1} + 1").set_color(GREEN).next_to(desc_6, DOWN, buff=0.3)
        self.play(Write(eq_ineq_2))

        desc_7 = Text("将其平方，得到不等式：", font="KaiTi", font_size=28).next_to(eq_ineq_2, DOWN, buff=0.5)
        self.play(Write(desc_7))

        eq_ineq_3 = MathTex(r"k^2 \ge (2^{a-1} + 1)^2").set_color(GREEN).next_to(desc_7, DOWN, buff=0.3)
        self.play(TransformMatchingTex(eq_ineq_2.copy(), eq_ineq_3))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(desc_4), FadeOut(desc_5), FadeOut(eq_ineq_1),
            FadeOut(desc_6), FadeOut(eq_ineq_2), FadeOut(desc_7)
        )
        self.play(eq_ineq_3.animate.next_to(eq_sq_final, DOWN, buff=0.6))

        # ==================== 第三幕：核心不等式 ====================
        desc_8 = Text("将原等式左侧代入上述不等式：", font="KaiTi", font_size=28).next_to(eq_ineq_3, DOWN, buff=0.6)
        self.play(Write(desc_8))

        eq_expand = MathTex(r"(2^{a-1})^2 + a^2 + 1 \ge (2^{a-1})^2 + 2 \cdot 2^{a-1} + 1").next_to(desc_8, DOWN,
                                                                                                    buff=0.4)
        self.play(Write(eq_expand))
        self.wait(1.5)

        desc_9 = Text("两边消去相同项，化简得：", font="KaiTi", font_size=28).next_to(eq_expand, DOWN, buff=0.5)
        self.play(Write(desc_9))

        eq_core = MathTex(r"a^2 \ge 2^a").scale(1.2).set_color(YELLOW).next_to(desc_9, DOWN, buff=0.4)
        self.play(TransformMatchingTex(eq_expand.copy(), eq_core))

        rect_core = SurroundingRectangle(eq_core, color=YELLOW, buff=0.15)
        self.play(Create(rect_core))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(eq_sq_final), FadeOut(eq_ineq_3), FadeOut(desc_8), FadeOut(eq_expand), FadeOut(desc_9)
        )
        core_group = VGroup(eq_core, rect_core)
        self.play(core_group.animate.to_edge(UP, buff=0.8))

        # ==================== 第四幕：求解范围 ====================
        desc_10_t1 = Text("当", font="KaiTi", font_size=28)
        desc_10_m1 = MathTex(r"a \ge 5", font_size=30).set_color(YELLOW)
        desc_10_t2 = Text("时，指数增长大于幂函数，该不等式不成立。", font="KaiTi", font_size=28)
        desc_10 = VGroup(desc_10_t1, desc_10_m1, desc_10_t2).arrange(RIGHT, buff=0.1)
        desc_10.next_to(core_group, DOWN, buff=0.6)
        self.play(Write(desc_10))

        desc_11_t1 = Text("因此正整数", font="KaiTi", font_size=28)
        desc_11_m1 = MathTex(r"a", font_size=30).set_color(YELLOW)
        desc_11_t2 = Text("的可能取值只能是：", font="KaiTi", font_size=28)
        desc_11 = VGroup(desc_11_t1, desc_11_m1, desc_11_t2).arrange(RIGHT, buff=0.1)
        desc_11.next_to(desc_10, DOWN, buff=0.4)
        self.play(Write(desc_11))

        eq_domain = MathTex(r"a \in \{1, 2, 3, 4\}").set_color(GREEN).next_to(desc_11, DOWN, buff=0.4)
        self.play(Write(eq_domain))
        self.wait(2)

        self.play(
            FadeOut(core_group), FadeOut(desc_10), FadeOut(desc_11), FadeOut(eq_domain)
        )

        # ==================== 第五幕：代入检验与结论 ====================
        desc_12 = Text("将可能的值逐一代入原方程检验：", font="KaiTi", font_size=30).to_edge(UP, buff=1.0)
        self.play(Write(desc_12))

        # 检验过程
        chk1_m = MathTex(r"a=1 \implies 12 = b^2")
        chk1_t = Text("（无整数解）", font="KaiTi", font_size=24).set_color(GRAY)
        chk1 = VGroup(chk1_m, chk1_t).arrange(RIGHT, buff=0.2)

        chk2_m = MathTex(r"a=2 \implies 36 = b^2 \implies b=6").set_color(GREEN)

        chk3_m = MathTex(r"a=3 \implies 104 = b^2")
        chk3_t = Text("（无整数解）", font="KaiTi", font_size=24).set_color(GRAY)
        chk3 = VGroup(chk3_m, chk3_t).arrange(RIGHT, buff=0.2)

        chk4_m = MathTex(r"a=4 \implies 324 = b^2 \implies b=18").set_color(GREEN)

        checks = VGroup(chk1, chk2_m, chk3, chk4_m).arrange(DOWN, buff=0.5).next_to(desc_12, DOWN, buff=0.8)

        for check in checks:
            self.play(FadeIn(check, shift=LEFT * 0.5))
            self.wait(0.5)
        self.wait(1.5)

        self.play(
            FadeOut(desc_12), FadeOut(checks)
        )

        # 最终结论
        final_text = Text("方程的正整数解为：", font="KaiTi", font_size=35).to_edge(UP, buff=2)
        self.play(Write(final_text))

        final_ans_1 = MathTex(r"(a, b) = (2, 6)").scale(1.2).set_color(YELLOW).move_to(UP * 0.2)
        final_ans_2 = MathTex(r"(a, b) = (4, 18)").scale(1.2).set_color(YELLOW).move_to(DOWN * 1.0)

        self.play(FadeIn(final_ans_1, shift=UP))
        self.play(FadeIn(final_ans_2, shift=UP))
        self.wait(3)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)