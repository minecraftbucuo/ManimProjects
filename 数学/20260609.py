from manim import *


class SequenceStructureProofGaokao(Scene):
    def construct(self):
        # ==================== 封面：完整题目展示 ====================
        main_title = Text("2026新高考全国一卷数学填空压轴", font="KaiTi", font_size=45, weight=BOLD).set_color(RED)

        title_l1_t1 = Text("设实数", font="KaiTi", font_size=28)
        title_l1_m1 = MathTex(r"q", font_size=32).set_color(YELLOW)
        title_l1_t2 = Text("满足：存在数列", font="KaiTi", font_size=28)
        title_l1_m2 = MathTex(r"\{a_n\}", font_size=32).set_color(BLUE)
        title_l1_t3 = Text("，使得对于任意", font="KaiTi", font_size=28)
        title_l1_m3 = MathTex(r"n \in \mathbf{N}^*", font_size=32).set_color(YELLOW)
        title_l1_t4 = Text("，均有", font="KaiTi", font_size=28)
        title_l1 = VGroup(
            title_l1_t1, title_l1_m1, title_l1_t2, title_l1_m2,
            title_l1_t3, title_l1_m3, title_l1_t4
        ).arrange(RIGHT, buff=0.1)

        title_l2 = MathTex(r"a_1 + a_2 + \cdots + a_{3n} = n^2 + n", font_size=40).set_color(BLUE)

        title_l3_t1 = Text("且", font="KaiTi", font_size=28)
        title_l3_m1 = MathTex(r"\{a_n\}", font_size=32).set_color(BLUE)
        title_l3_t2 = Text("中有某连续", font="KaiTi", font_size=28)
        title_l3_m2 = MathTex(r"9", font_size=32).set_color(YELLOW)
        title_l3_t3 = Text("项是公比为", font="KaiTi", font_size=28)
        title_l3_m3 = MathTex(r"q", font_size=32).set_color(YELLOW)
        title_l3_t4 = Text("的等比数列", font="KaiTi", font_size=28)
        title_l3 = VGroup(
            title_l3_t1, title_l3_m1, title_l3_t2, title_l3_m2,
            title_l3_t3, title_l3_m3, title_l3_t4
        ).arrange(RIGHT, buff=0.1)

        title_l4_t1 = Text("则", font="KaiTi", font_size=28)
        title_l4_m1 = MathTex(r"q", font_size=32).set_color(YELLOW)
        title_l4_t2 = Text("的最大值为 ________.", font="KaiTi", font_size=28)
        title_l4 = VGroup(title_l4_t1, title_l4_m1, title_l4_t2).arrange(RIGHT, buff=0.1)

        cover_text = VGroup(title_l1, title_l2, title_l3, title_l4).arrange(DOWN, buff=0.4)
        cover = VGroup(main_title, cover_text).arrange(DOWN, buff=0.8).shift(UP * 0.2)

        self.play(Write(main_title))
        self.play(FadeIn(cover_text, shift=UP))
        self.wait(2)

        # ==================== 倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = MathTex(i, font_size=100)
            countdown_text.set_color(GRAY)
            countdown_text.next_to(cover, DOWN, buff=0.5)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.play(FadeOut(cover))

        # ==================== 第一幕：详细求出分块通项 ====================
        step1_t1 = Text("首先，我们对原数列进行分块，令", font="KaiTi", font_size=30)
        step1_m1 = MathTex(r"A_n = a_{3n-2} + a_{3n-1} + a_{3n}", font_size=35).set_color(BLUE)
        step1 = VGroup(step1_t1, step1_m1).arrange(RIGHT, buff=0.2).to_edge(UP, buff=0.8)
        self.play(Write(step1))

        step1_sub1_t1 = Text("根据已知条件，前", font="KaiTi", font_size=28)
        step1_sub1_m1 = MathTex(r"n", font_size=32).set_color(YELLOW)
        step1_sub1_t2 = Text("个块的和为：", font="KaiTi", font_size=28)
        step1_sub1 = VGroup(step1_sub1_t1, step1_sub1_m1, step1_sub1_t2).arrange(RIGHT, buff=0.1).next_to(step1, DOWN,
                                                                                                          buff=0.5)
        self.play(Write(step1_sub1))

        eq_sum = MathTex(r"S_{n}' = A_1 + A_2 + \cdots + A_n = n^2 + n").set_color(WHITE).next_to(step1_sub1, DOWN,
                                                                                                  buff=0.3)
        self.play(Write(eq_sum))
        self.wait(1)

        step1_sub2_t1 = Text("当", font="KaiTi", font_size=28)
        step1_sub2_m1 = MathTex(r"n \ge 2", font_size=32).set_color(YELLOW)
        step1_sub2_t2 = Text("时，利用", font="KaiTi", font_size=28)
        step1_sub2_m2 = MathTex(r"A_n = S_{n}' - S_{n-1}'", font_size=32)
        step1_sub2 = VGroup(step1_sub2_t1, step1_sub2_m1, step1_sub2_t2, step1_sub2_m2).arrange(RIGHT,
                                                                                                buff=0.1).next_to(
            eq_sum, DOWN, buff=0.5)
        self.play(Write(step1_sub2))

        eq_calc = MathTex(r"A_n = (n^2 + n) - [(n-1)^2 + (n-1)] = 2n").set_color(GREEN).next_to(step1_sub2, DOWN,
                                                                                                buff=0.3)
        self.play(Write(eq_calc))
        self.wait(1)

        step1_sub3_t1 = Text("且", font="KaiTi", font_size=28)
        step1_sub3_m1 = MathTex(r"A_1 = 2", font_size=32).set_color(YELLOW)
        step1_sub3_t2 = Text("也满足上式，由此得到新数列的通项：", font="KaiTi", font_size=28)
        step1_sub3 = VGroup(step1_sub3_t1, step1_sub3_m1, step1_sub3_t2).arrange(RIGHT, buff=0.1).next_to(eq_calc, DOWN,
                                                                                                          buff=0.5)
        eq_an = MathTex(r"A_n = 2n \quad (n \in \mathbf{N}^*)").scale(1.2).set_color(YELLOW).next_to(step1_sub3, DOWN,
                                                                                                     buff=0.3)

        self.play(Write(step1_sub3))
        self.play(Write(eq_an))
        self.wait(2)

        # 彻底清屏
        self.play(
            FadeOut(step1), FadeOut(step1_sub1), FadeOut(eq_sum),
            FadeOut(step1_sub2), FadeOut(eq_calc), FadeOut(step1_sub3)
        )
        self.play(eq_an.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：严格排查对齐情况 ====================
        step2_t1_1 = Text("接下来，切入核心：寻找连续", font="KaiTi", font_size=30)
        step2_t1_2 = MathTex(r"9", font_size=34).set_color(YELLOW)
        step2_t1_3 = Text("项等比数列的位置", font="KaiTi", font_size=30)
        step2_t1 = VGroup(step2_t1_1, step2_t1_2, step2_t1_3).arrange(RIGHT, buff=0.1).next_to(eq_an, DOWN, buff=0.8)
        self.play(Write(step2_t1))

        step2_sub1_t1 = Text("假设这", font="KaiTi", font_size=28)
        step2_sub1_m1 = MathTex(r"9", font_size=32).set_color(YELLOW)
        step2_sub1_t2 = Text("项刚好完美覆盖了三个数据块", font="KaiTi", font_size=28)
        step2_sub1 = VGroup(step2_sub1_t1, step2_sub1_m1, step2_sub1_t2).arrange(RIGHT, buff=0.1).next_to(step2_t1,
                                                                                                          DOWN,
                                                                                                          buff=0.4)
        step2_sub2_m = MathTex(r"A_m, A_{m+1}, A_{m+2}", font_size=32).set_color(BLUE).next_to(step2_sub1, DOWN,
                                                                                               buff=0.3)

        self.play(Write(step2_sub1))
        self.play(Write(step2_sub2_m))
        self.wait(1)

        step2_sub3_t1 = Text("那么这三个块必然也成等比数列，且公比为", font="KaiTi", font_size=26)
        step2_sub3_m1 = MathTex(r"q^3", font_size=30).set_color(YELLOW)
        step2_sub3 = VGroup(step2_sub3_t1, step2_sub3_m1).arrange(RIGHT, buff=0.1).next_to(step2_sub2_m, DOWN, buff=0.4)
        self.play(Write(step2_sub3))

        step2_sub4 = Text("但将通项公式代入后，它们的值为：", font="KaiTi", font_size=26).next_to(step2_sub3, DOWN,
                                                                                                    buff=0.4)
        self.play(Write(step2_sub4))

        eq_arith = MathTex(r"2m, 2m+2, 2m+4").set_color(WHITE).next_to(step2_sub4, DOWN, buff=0.3)
        self.play(Write(eq_arith))

        eq_contra = MathTex(r"(2m+2)^2 \neq (2m)(2m+4)").set_color(RED).next_to(eq_arith, DOWN, buff=0.3)
        self.play(Write(eq_contra))

        step2_sub5 = Text("显然等差数列无法构成等比数列，产生矛盾！说明位置必定错开。", font="KaiTi",
                          font_size=26).next_to(eq_contra, DOWN, buff=0.3)
        self.play(Write(step2_sub5))
        self.wait(2.5)

        # 彻底清屏
        self.play(
            FadeOut(step2_t1), FadeOut(step2_sub1), FadeOut(step2_sub2_m),
            FadeOut(step2_sub3), FadeOut(step2_sub4), FadeOut(eq_arith),
            FadeOut(eq_contra), FadeOut(step2_sub5)
        )

        # ==================== 第三幕：错位与极值推导 ====================
        step3_t1 = Text("既然不能完美对齐，窗口必然发生错位", font="KaiTi", font_size=30).next_to(eq_an, DOWN, buff=0.8)
        self.play(Write(step3_t1))

        step3_sub1_t1 = Text("此时连续", font="KaiTi", font_size=28)
        step3_sub1_m1 = MathTex(r"9", font_size=32).set_color(YELLOW)
        step3_sub1_t2 = Text("项一定会完整包含两个相邻的块：", font="KaiTi", font_size=28)
        step3_sub1_txt_group = VGroup(step3_sub1_t1, step3_sub1_m1, step3_sub1_t2).arrange(RIGHT, buff=0.1)
        step3_sub1_m2 = MathTex(r"A_{k+1}, A_{k+2}", font_size=32).set_color(BLUE)
        step3_sub1 = VGroup(step3_sub1_txt_group, step3_sub1_m2).arrange(RIGHT, buff=0.2).next_to(step3_t1, DOWN,
                                                                                                  buff=0.4)
        self.play(Write(step3_sub1))

        step3_sub2 = Text("利用等比数列的性质，我们可以剥离出一个纯粹的代数关系：", font="KaiTi", font_size=28).next_to(
            step3_sub1, DOWN, buff=0.5)
        self.play(Write(step3_sub2))

        eq_ratio_1 = MathTex(r"q^3 = \frac{A_{k+2}}{A_{k+1}} = \frac{2(k+2)}{2(k+1)}")
        eq_ratio_1.next_to(step3_sub2, DOWN, buff=0.4)
        self.play(Write(eq_ratio_1))
        self.wait(1)

        eq_ratio_final = MathTex(r"q^3 = 1 + \frac{1}{k+1} \quad (k \ge 1)")
        eq_ratio_final.set_color(GREEN).next_to(eq_ratio_1, DOWN, buff=0.4)
        self.play(Write(eq_ratio_final))
        self.wait(2)

        # 全局大清理！第三幕完全消失！
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        # ==================== 第四幕：绝不越界的终极居中排版 ====================
        step4_title = Text("锁定目标：求解最大公比", font="KaiTi", font_size=32).to_edge(UP, buff=1)

        step4_t1_1 = Text("由错位分析我们得到了最终的极限表达式：", font="KaiTi", font_size=30)
        step4_t1_2 = MathTex(r"q^3 = 1 + \frac{1}{k+1}", font_size=32).set_color(GREEN)
        step4_t1 = VGroup(step4_t1_1, step4_t1_2).arrange(RIGHT, buff=0.2).next_to(step4_title, DOWN, buff=0.6)
        self.play(Write(step4_t1))

        step4_t2_1 = Text("要使公比", font="KaiTi", font_size=30)
        step4_t2_2 = MathTex(r"q", font_size=32).set_color(YELLOW)
        step4_t2_3 = Text("最大，分母中的正整数", font="KaiTi", font_size=30)
        step4_t2_4 = MathTex(r"k", font_size=32).set_color(YELLOW)
        step4_t2_5 = Text("需取极小值", font="KaiTi", font_size=30)
        step4_t2_6 = MathTex(r"1", font_size=32).set_color(YELLOW)
        step4_t2 = VGroup(step4_t2_1, step4_t2_2, step4_t2_3, step4_t2_4, step4_t2_5, step4_t2_6).arrange(RIGHT,
                                                                                                          buff=0.1).next_to(
            step4_t1, DOWN, buff=0.6)
        self.play(Write(step4_t2))

        eq_q3_max = MathTex(r"q^3 = \frac{3}{2}").scale(1.2).set_color(WHITE).next_to(step4_t2, DOWN, buff=0.5)
        self.play(Write(eq_q3_max))
        self.wait(2)

        # ★ 动态释放空间 ★
        # 将铺垫内容隐去，把中心舞台让给最终结论
        self.play(
            FadeOut(step4_t1), FadeOut(step4_t2), FadeOut(eq_q3_max)
        )

        step4_t3 = Text("左右两边同时开立方根，得出本题的最终答案：", font="KaiTi", font_size=30).next_to(step4_title,
                                                                                                        DOWN, buff=1.2)
        self.play(Write(step4_t3))

        eq_final_ans = MathTex(r"q_{\max} = \sqrt[3]{\frac{3}{2}}").scale(1.8).set_color(YELLOW).next_to(step4_t3, DOWN,
                                                                                                         buff=0.8)
        self.play(FadeIn(eq_final_ans, shift=UP))

        rect_final = SurroundingRectangle(eq_final_ans, color=YELLOW, buff=0.3)
        self.play(Create(rect_final))
        self.wait(3)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)