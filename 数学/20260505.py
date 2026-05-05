from manim import *


class ProveIntegerFluidProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("如何证明这个代数式是整数？", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"\frac{n(n + 1)(2n + 1)}{3}",
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

        # ==================== 第一幕：化归思维 ====================
        desc_1_title = Text("视角一：化归思维", font="KaiTi", font_size=40).set_color(BLUE)
        desc_1_sub = Text(" ", font="KaiTi", font_size=32)
        desc_1 = VGroup(desc_1_title, desc_1_sub).arrange(DOWN, buff=0.2).to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        mod_text1 = Text("在模", font="KaiTi", font_size=30)
        mod_math1 = MathTex(r"3", font_size=30)
        mod_text2 = Text("的意义下，", font="KaiTi", font_size=30)
        mod_math2 = MathTex(r"2 \equiv -1", font_size=30).set_color(YELLOW)
        desc_mod = VGroup(mod_text1, mod_math1, mod_text2, mod_math2).arrange(RIGHT, buff=0.1).next_to(desc_1, DOWN,
                                                                                                       buff=0.5)
        self.play(Write(desc_mod))

        eq_orig = MathTex(r"2n + 1", r" \equiv ", r" -n + 1 ", r"= - (n - 1) \pmod 3").next_to(desc_mod, DOWN, buff=0.4)
        eq_orig[0].set_color(WHITE)
        eq_orig[2].set_color(YELLOW)
        self.play(Write(eq_orig))
        self.wait(1)

        sub_text1 = Text("代回原来的分子乘积中：", font="KaiTi", font_size=30).next_to(eq_orig, DOWN, buff=0.4)
        self.play(Write(sub_text1))

        eq_trans = MathTex(r"n(n+1)(2n+1)", r" \equiv ", r"-n(n-1)(n+1)", r" \pmod 3").next_to(sub_text1, DOWN,
                                                                                               buff=0.4)
        eq_trans[2].set_color(YELLOW)
        self.play(TransformMatchingTex(eq_orig.copy(), eq_trans))
        self.wait(1)

        rect_consec = SurroundingRectangle(eq_trans[2], color=RED, buff=0.15)
        self.play(Create(rect_consec))

        concl_text1 = Text("出现了", font="KaiTi", font_size=32).set_color(RED)
        concl_math1 = MathTex(r"n-1,\, n,\, n+1", font_size=32).set_color(YELLOW)
        concl_text2 = Text("是三个连续整数，必然有", font="KaiTi", font_size=32)
        concl_math2 = MathTex(r"3", font_size=32).set_color(RED)
        concl_text3 = Text("的倍数！", font="KaiTi", font_size=32)
        concl_1 = VGroup(concl_text1, concl_math1, concl_text2, concl_math2, concl_text3).arrange(RIGHT,
                                                                                                  buff=0.1).next_to(
            eq_trans, DOWN, buff=0.5)
        self.play(Write(concl_1))
        self.wait(2)

        # 本幕清场
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 第二幕：分情况讨论 ====================
        desc_2_title = Text("视角二：分情况讨论", font="KaiTi", font_size=40).set_color(GREEN)
        desc_2_sub = Text(" ", font="KaiTi", font_size=32)
        desc_2 = VGroup(desc_2_title, desc_2_sub).arrange(DOWN, buff=0.2).to_edge(UP, buff=0.8)
        self.play(Write(desc_2))

        c1_t1 = Text("情况1：设", font="KaiTi", font_size=28)
        c1_m1 = MathTex(r"n = 3k", font_size=28)
        c1_t2 = Text("，显然第一项含有因子", font="KaiTi", font_size=28)
        c1_m2 = MathTex(r"3", font_size=28).set_color(RED)
        case1 = VGroup(c1_t1, c1_m1, c1_t2, c1_m2).arrange(RIGHT, buff=0.05).next_to(desc_2, DOWN, buff=0.8)
        self.play(Write(case1))

        c2_t1 = Text("情况2：设", font="KaiTi", font_size=28)
        c2_m1 = MathTex(r"n = 3k+1", font_size=28)
        c2_t2 = Text("，代入得", font="KaiTi", font_size=28)
        c2_m2 = MathTex(r"2n+1 = 3(2k+1)", font_size=28).set_color(GREEN)
        case2 = VGroup(c2_t1, c2_m1, c2_t2, c2_m2).arrange(RIGHT, buff=0.05).next_to(case1, DOWN, buff=0.4)
        self.play(Write(case2))

        c3_t1 = Text("情况3：设", font="KaiTi", font_size=28)
        c3_m1 = MathTex(r"n = 3k+2", font_size=28)
        c3_t2 = Text("，代入得", font="KaiTi", font_size=28)
        c3_m2 = MathTex(r"n+1 = 3(k+1)", font_size=28).set_color(BLUE)
        case3 = VGroup(c3_t1, c3_m1, c3_t2, c3_m2).arrange(RIGHT, buff=0.05).next_to(case2, DOWN, buff=0.4)
        self.play(Write(case3))

        self.wait(1)

        relay_t1 = Text(" ", font="KaiTi", font_size=32).set_color(YELLOW)
        relay_m1 = MathTex(r"n,\; n+1,\; 2n+1", font_size=32).set_color(WHITE)
        relay_t2 = Text("刚好一“人”负责一种情况", font="KaiTi", font_size=32).set_color(YELLOW)
        relay = VGroup(relay_t1, relay_m1, relay_t2).arrange(RIGHT, buff=0.1).next_to(case3, DOWN, buff=0.8)
        self.play(Write(relay))
        self.wait(2)

        # 本幕清场
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 第三幕：溯源思维 ====================
        desc_3_title = Text("视角三：溯源思维", font="KaiTi", font_size=40).set_color(ORANGE)
        desc_3_sub = Text(" ", font="KaiTi", font_size=32)
        desc_3 = VGroup(desc_3_title, desc_3_sub).arrange(DOWN, buff=0.2).to_edge(UP, buff=1)
        self.play(Write(desc_3))

        origin_t1 = Text("注意到：", font="KaiTi", font_size=30).next_to(desc_3, DOWN, buff=0.6)
        self.play(Write(origin_t1))

        eq_sum = MathTex(r"1^2 + 2^2 + 3^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}").scale(0.9).move_to(ORIGIN)
        self.play(FadeIn(eq_sum, shift=UP))
        self.wait(1.5)

        self.play(FadeOut(origin_t1))

        mul_t1 = Text("等式两边同时乘以", font="KaiTi", font_size=28).next_to(eq_sum, UP, buff=0.5)
        mul_m1 = MathTex(r"2", font_size=28).set_color(YELLOW)
        mul = VGroup(mul_t1, mul_m1).arrange(RIGHT, buff=0.1).next_to(eq_sum, DOWN, buff=0.5)
        self.play(Write(mul))
        self.wait(0.5)

        # 避免拉扯变形，直接在原位淡入淡出替换
        eq_final = MathTex(r"2 \times ", r"(1^2 + 2^2 + \dots + n^2)", r" = \frac{n(n+1)(2n+1)}{3}").scale(1.1)
        eq_final[0].set_color(YELLOW)
        eq_final[2].set_color(YELLOW)
        eq_final.move_to(eq_sum)

        self.play(FadeOut(eq_sum), FadeIn(eq_final, shift=DOWN))
        self.wait(1.5)

        self.play(FadeOut(mul))

        logic_t1 = Text("等号左边是若干个整数的和，", font="KaiTi", font_size=35).next_to(eq_final, DOWN, buff=0.8)
        logic_t2 = Text("必然是整数", font="KaiTi", font_size=40).set_color(RED)
        logic_1 = VGroup(logic_t1, logic_t2).arrange(RIGHT, buff=0.2).next_to(eq_sum, DOWN, buff=0.5)
        self.play(Write(logic_1))
        self.wait(1)

        logic_t3 = Text("所以等号右边必然也是整数", font="KaiTi", font_size=40).set_color(YELLOW).next_to(logic_1,
                                                                                                           DOWN,
                                                                                                           buff=0.4)
        self.play(Write(logic_t3))
        self.wait(3)

        # 本幕清场
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 散场 ====================
        outro_1 = Text("证毕", font="KaiTi", font_size=50).set_color(BLUE)
        outro_2 = Text("感谢观看", font="KaiTi", font_size=50).set_color_by_gradient(GREEN, YELLOW)
        outro = VGroup(outro_1, outro_2).arrange(DOWN, buff=0.5)

        self.play(FadeIn(outro, shift=UP))
        self.wait(4)
        self.play(FadeOut(outro))