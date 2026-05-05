from manim import *


class FermatNumberFluidProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("如何证明这个命题？", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        cover_t1 = Text("若", font="KaiTi", font_size=42)
        cover_m1 = MathTex(r"2^n + 1", font_size=42)
        cover_t2 = Text("是素数", font="KaiTi", font_size=42)
        cover_m2 = MathTex(r"(n > 1)", font_size=42)
        cover_t3 = Text("，则", font="KaiTi", font_size=42)
        cover_m3 = MathTex(r"n", font_size=42)
        cover_t4 = Text("是", font="KaiTi", font_size=42)
        cover_m4 = MathTex(r"2", font_size=42)
        cover_t5 = Text("的方幂", font="KaiTi", font_size=42)

        eq_cover = VGroup(cover_t1, cover_m1, cover_t2, cover_m2, cover_t3, cover_m3, cover_t4, cover_m4,
                          cover_t5).arrange(RIGHT, buff=0.15)
        eq_cover.set_color(BLUE)

        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))

        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=180)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.move_to(ORIGIN)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 顺其自然的开篇 ====================
        desc_1 = Text("面对这种“若A则B”的结构，直接证明往往比较困难。", font="KaiTi", font_size=32).to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        desc_2 = Text("此时采用逆否命题进行证明会更加清晰：", font="KaiTi", font_size=30).next_to(desc_1, DOWN, buff=0.6)
        self.play(Write(desc_2))

        logic_text1 = Text("假设", font="KaiTi", font_size=32)
        logic_math1 = MathTex(r"n", font_size=32).set_color(YELLOW)
        logic_text2 = Text("不是", font="KaiTi", font_size=32)
        logic_math2 = MathTex(r"2", font_size=32).set_color(YELLOW)
        logic_text3 = Text("的方幂，那么", font="KaiTi", font_size=32)
        logic_math3 = MathTex(r"2^n + 1", font_size=32).set_color(RED)
        logic_text4 = Text("必然可以分解。", font="KaiTi", font_size=32).set_color(RED)
        logic_1 = VGroup(logic_text1, logic_math1, logic_text2, logic_math2, logic_text3, logic_math3,
                         logic_text4).arrange(RIGHT, buff=0.1)
        logic_1.next_to(desc_2, DOWN, buff=0.6)
        self.play(Write(logic_1))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 剖析“不是2的方幂” ====================
        desc_3 = Text("若 n 不是 2 的方幂，意味着它提取完所有的因子 2 后，", font="KaiTi", font_size=30).to_edge(UP,
                                                                                                               buff=0.8)
        self.play(Write(desc_3))

        desc_4 = Text("必然包含一个大于 1 的奇因子。因此可以设：", font="KaiTi", font_size=30).next_to(desc_3, DOWN,
                                                                                                     buff=0.5)
        self.play(Write(desc_4))

        eq_n = MathTex(r"n = a \times b").scale(1.4).next_to(desc_4, DOWN, buff=0.6)
        self.play(FadeIn(eq_n, shift=UP))
        self.wait(1)

        desc_5_text = Text("其中", font="KaiTi", font_size=30)
        desc_5_math = MathTex(r"b \ge 3", font_size=30)
        desc_5_text2 = Text("为奇数。", font="KaiTi", font_size=30).set_color(YELLOW)
        desc_5 = VGroup(desc_5_text, desc_5_math, desc_5_text2).arrange(RIGHT, buff=0.1)
        desc_5.next_to(eq_n, DOWN, buff=0.5)
        self.play(Write(desc_5))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 奇数次幂的专杀公式 ====================
        desc_6 = Text("将 n 的分解式代入原式，我们面对的结构变为：", font="KaiTi", font_size=30).to_edge(UP, buff=0.8)
        self.play(Write(desc_6))

        desc_7_text = Text("这是一个底数的", font="KaiTi", font_size=28)
        desc_7_math = MathTex(r"b", font_size=28).set_color(YELLOW)
        desc_7_text2 = Text("次奇数幂加", font="KaiTi", font_size=28)
        desc_7_math2 = MathTex(r"1", font_size=28)
        desc_7_text3 = Text("的形式。", font="KaiTi", font_size=28)
        desc_7 = VGroup(desc_7_text, desc_7_math, desc_7_text2, desc_7_math2, desc_7_text3).arrange(RIGHT, buff=0.1)
        desc_7.next_to(desc_6, DOWN, buff=0.5)
        self.play(Write(desc_7))

        eq_target = MathTex(r"(2^a)^b + 1").scale(1.2).next_to(desc_7, DOWN, buff=0.4)
        self.play(FadeIn(eq_target, shift=UP))
        self.wait(1.5)
        self.play(FadeOut(desc_7))

        desc_8 = Text("对于奇数次幂加 1，我们可以利用代数恒等式进行因式分解：", font="KaiTi", font_size=28).next_to(
            eq_target, UP, buff=0.4)
        self.play(Write(desc_8))

        eq_expand = MathTex(
            r"x^b + 1 = ", r"(x + 1)", r"(x^{b-1} - x^{b-2} + \dots - x + 1)"
        ).scale(0.9).next_to(eq_target, DOWN, buff=0.5)
        eq_expand[1].set_color(RED)
        self.play(Write(eq_expand))
        self.wait(1)

        rect_key = SurroundingRectangle(eq_expand[1], color=RED, buff=0.15)
        self.play(Create(rect_key))

        desc_9 = Text("注意，这里要求 b 必须是奇数，这样才能保证符号交替并最终凑出因式。", font="KaiTi",
                      font_size=26).set_color(RED)
        desc_9.next_to(eq_expand, DOWN, buff=0.4)
        self.play(Write(desc_9))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 顺水推舟 ====================
        desc_10 = Text("利用上述恒等式，只需进行简单的代换即可完成证明。", font="KaiTi", font_size=32).to_edge(UP,
                                                                                                             buff=0.8)
        self.play(Write(desc_10))

        desc_11_text = Text("令", font="KaiTi", font_size=30)
        desc_11_math = MathTex(r"x = 2^a", font_size=30).set_color(YELLOW)
        desc_11 = VGroup(desc_11_text, desc_11_math).arrange(RIGHT, buff=0.1)
        desc_11.next_to(desc_10, DOWN, buff=0.5)
        self.play(Write(desc_11))

        eq_final = MathTex(
            r"2^n + 1 = ", r"(2^a + 1)", r" \times [\cdots]"
        ).scale(1.2).next_to(desc_11, DOWN, buff=0.5)
        eq_final[1].set_color(YELLOW)
        self.play(Write(eq_final))
        self.wait(1)

        desc_12_text = Text("由于", font="KaiTi", font_size=30)
        desc_12_math = MathTex(r"a < n", font_size=30)
        desc_12_text2 = Text("，可知", font="KaiTi", font_size=30)
        desc_12_math2 = MathTex(r"1 < 2^a + 1 < 2^n + 1", font_size=30).set_color(YELLOW)
        desc_12_text3 = Text("。因此它是真因数，命题得证。", font="KaiTi", font_size=30).set_color(RED)
        desc_12 = VGroup(desc_12_text, desc_12_math, desc_12_text2, desc_12_math2, desc_12_text3).arrange(RIGHT,
                                                                                                          buff=0.1)
        desc_12.next_to(eq_final, DOWN, buff=0.6)
        self.play(Write(desc_12))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 好奇心的延伸 ====================
        desc_13 = Text("至此，逆否命题得证，原命题成立。", font="KaiTi", font_size=32).to_edge(UP, buff=0.8)
        self.play(Write(desc_13))
        self.wait(1.5)
        self.play(FadeOut(desc_13))

        desc_14 = Text("在此基础上，我们可以进一步探讨一个相关的问题。", font="KaiTi", font_size=32).to_edge(UP, buff=0.8)
        self.play(Write(desc_14))
        self.wait(1.5)
        self.play(FadeOut(desc_14))

        desc_15 = Text("既然", font="KaiTi", font_size=30)
        desc_15_math = MathTex(r"n", font_size=30)
        desc_15_text2 = Text("必须具有", font="KaiTi", font_size=30)
        desc_15_math2 = MathTex(r"2^k", font_size=30).set_color(YELLOW)
        desc_15_text3 = Text("的形式，那么形如这样的数是否全为素数？", font="KaiTi", font_size=30)
        desc_15_group = VGroup(desc_15, desc_15_math, desc_15_text2, desc_15_math2, desc_15_text3).arrange(RIGHT,
                                                                                                           buff=0.1).to_edge(
            UP, buff=0.8)
        self.play(Write(desc_15_group))
        self.wait(2)
        self.play(FadeOut(desc_15_group))

        # 列出前5项，使用绝对坐标精准控制，防止出界
        start_pos = UP * 2 + LEFT * 2.5

        eq_f0 = MathTex(r"F_0 = 2^{2^0} + 1 =", " 3").move_to(start_pos)
        eq_f1 = MathTex(r"F_1 = 2^{2^1} + 1 =", " 5").next_to(eq_f0, DOWN, buff=0.3).align_to(eq_f0, LEFT)
        eq_f2 = MathTex(r"F_2 = 2^{2^2} + 1 =", " 17").next_to(eq_f1, DOWN, buff=0.3).align_to(eq_f0, LEFT)
        eq_f3 = MathTex(r"F_3 = 2^{2^3} + 1 =", " 257").next_to(eq_f2, DOWN, buff=0.3).align_to(eq_f0, LEFT)
        eq_f4 = MathTex(r"F_4 = 2^{2^4} + 1 =", " 65537").next_to(eq_f3, DOWN, buff=0.3).align_to(eq_f0, LEFT)

        fermat_list = VGroup(eq_f0, eq_f1, eq_f2, eq_f3, eq_f4)
        for eq in fermat_list:
            eq[1].set_color(YELLOW)

        self.play(Write(eq_f0), run_time=0.5)
        self.play(Write(eq_f1), run_time=0.5)
        self.play(Write(eq_f2), run_time=0.5)
        self.play(Write(eq_f3), run_time=0.5)
        self.play(Write(eq_f4), run_time=0.5)
        self.wait(1)

        # 将右侧文字锚定在列表的右侧，防止重叠
        tag_prime = Text("均为素数。", font="KaiTi", font_size=32).set_color(GREEN)
        tag_prime.next_to(fermat_list, RIGHT, buff=0.8).align_to(fermat_list, UP)
        self.play(FadeIn(tag_prime, shift=LEFT))
        self.wait(1.5)

        desc_16_1 = Text("费马在计算了前几项后，", font="KaiTi", font_size=28)
        desc_16_2 = Text("曾猜想所有此类数均为素数。", font="KaiTi", font_size=28)
        desc_16 = VGroup(desc_16_1, desc_16_2).arrange(DOWN)
        desc_16.next_to(tag_prime, DOWN, buff=0.5).align_to(tag_prime, LEFT)
        self.play(Write(desc_16))
        self.wait(3)

        # 彻底清场，保证后续绝对不重叠
        self.play(*[FadeOut(m) for m in self.mobjects])

        # 欧拉的反击
        desc_17_1 = Text("然而，半个世纪后，", font="KaiTi", font_size=32).to_edge(UP, buff=1.5)
        desc_17_2 = Text("善于计算的大数学家欧拉给出了反例。他计算出第 6 项：", font="KaiTi", font_size=32).to_edge(UP, buff=1.5)
        desc_17 = VGroup(desc_17_1, desc_17_2).arrange(DOWN)

        self.play(Write(desc_17))
        self.wait(1)

        eq_f5 = MathTex(r"F_5 = 2^{32} + 1 = 4294967297").scale(1.1).next_to(desc_17, DOWN, buff=0.8)
        self.play(Write(eq_f5))
        self.wait(1.5)

        eq_euler = MathTex(r"= 641 \times 6700417").scale(1.2).set_color(RED).next_to(eq_f5, DOWN, buff=0.5)
        self.play(Write(eq_euler))
        self.wait(3)

        # 彻底清场
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 散场 ====================
        desc_18 = Text("这个反例说明，我们证明的条件仅仅是必要条件，而非充分条件。", font="KaiTi", font_size=30).to_edge(
            UP, buff=1.5)
        self.play(Write(desc_18))
        self.wait(2)
        self.play(FadeOut(desc_18))

        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(1)