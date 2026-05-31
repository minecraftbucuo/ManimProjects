from manim import *

class RemainderProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("大数除以180的余数求解", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"13579111315 \cdots 20192021 \pmod{180}",
            font_size=50
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

        # ==================== 第一幕：分解因数与局部同余 ====================
        desc_1_t1 = Text("设原多位数为", font="KaiTi", font_size=30)
        desc_1_m1 = MathTex(r"N", font_size=32).set_color(BLUE)
        desc_1_t2 = Text("，首先将除数分解为互素的因子：", font="KaiTi", font_size=30)
        desc_1 = VGroup(desc_1_t1, desc_1_m1, desc_1_t2).arrange(RIGHT, buff=0.1)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_factor = MathTex(r"180 = 4 \times 5 \times 9").set_color(YELLOW).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(eq_factor))
        self.wait(1)

        desc_2_t1 = Text("根据被除数末位特征，分别求", font="KaiTi", font_size=28)
        desc_2_m1 = MathTex(r"N", font_size=30).set_color(BLUE)
        desc_2_t2 = Text("模5和模4的余数：", font="KaiTi", font_size=28)
        desc_2 = VGroup(desc_2_t1, desc_2_m1, desc_2_t2).arrange(RIGHT, buff=0.1).next_to(eq_factor, DOWN, buff=0.8)
        self.play(Write(desc_2))

        eq_mod5_m = MathTex(r"N \equiv 1 \pmod 5")
        eq_mod5_t = Text("(末位为1)", font="KaiTi", font_size=24)
        eq_mod5 = VGroup(eq_mod5_m, eq_mod5_t).arrange(RIGHT, buff=0.5).next_to(desc_2, DOWN, buff=0.4)
        
        eq_mod4_m = MathTex(r"N \equiv 1 \pmod 4")
        eq_mod4_t = Text("(末两位为21)", font="KaiTi", font_size=24)
        eq_mod4 = VGroup(eq_mod4_m, eq_mod4_t).arrange(RIGHT, buff=0.5).next_to(eq_mod5, DOWN, buff=0.3)
        
        self.play(Write(eq_mod5))
        self.play(Write(eq_mod4))
        self.wait(1.5)

        desc_3_t1 = Text("由于4和5互素，联立可推导：", font="KaiTi", font_size=28)
        desc_3 = desc_3_t1.next_to(eq_mod4, DOWN, buff=0.6)
        self.play(Write(desc_3))

        eq_mod20 = MathTex(r"N \equiv 1 \pmod{20} \implies N = 20k + 1").set_color(GREEN).next_to(desc_3, DOWN, buff=0.3)
        self.play(Write(eq_mod20))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(desc_1), FadeOut(eq_factor), FadeOut(desc_2), 
            FadeOut(eq_mod5), FadeOut(eq_mod4), FadeOut(desc_3)
        )
        self.play(eq_mod20.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：模9同余与数列求和 ====================
        desc_4_t1 = Text("在模9意义下，多位数同余于其各位数字之和：", font="KaiTi", font_size=28)
        desc_4 = desc_4_t1.next_to(eq_mod20, DOWN, buff=0.8)
        self.play(Write(desc_4))

        eq_mod9_1 = MathTex(r"N \equiv 1 + 3 + 5 + \dots + 2021 \pmod 9").set_color(YELLOW).next_to(desc_4, DOWN, buff=0.4)
        self.play(Write(eq_mod9_1))
        self.wait(1)

        desc_5_t1 = Text("由等差数列性质，求项数", font="KaiTi", font_size=28)
        desc_5_m1 = MathTex(r"n", font_size=30).set_color(BLUE)
        desc_5_t2 = Text("：", font="KaiTi", font_size=28)
        desc_5 = VGroup(desc_5_t1, desc_5_m1, desc_5_t2).arrange(RIGHT, buff=0.1).next_to(eq_mod9_1, DOWN, buff=0.6)
        self.play(Write(desc_5))

        eq_n = MathTex(r"n = \frac{2021 - 1}{2} + 1 = 1011").next_to(desc_5, DOWN, buff=0.3)
        self.play(Write(eq_n))
        self.wait(1)

        desc_6_t1 = Text("奇数数列之和为项数的平方：", font="KaiTi", font_size=28)
        desc_6 = desc_6_t1.next_to(eq_n, DOWN, buff=0.6)
        self.play(Write(desc_6))

        eq_sum = MathTex(r"S = 1011^2").set_color(BLUE).next_to(desc_6, DOWN, buff=0.3)
        self.play(Write(eq_sum))
        self.wait(2)

        # 再次整理屏幕
        self.play(
            FadeOut(desc_4), FadeOut(eq_mod9_1), FadeOut(desc_5), 
            FadeOut(eq_n), FadeOut(desc_6)
        )
        self.play(eq_sum.animate.next_to(eq_mod20, DOWN, buff=0.5))

        # ==================== 第三幕：计算最终余数 ====================
        desc_7_t1 = Text("计算基础项", font="KaiTi", font_size=28)
        desc_7_m1 = MathTex(r"1011", font_size=30)
        desc_7_t2 = Text("模9的余数：", font="KaiTi", font_size=28)
        desc_7 = VGroup(desc_7_t1, desc_7_m1, desc_7_t2).arrange(RIGHT, buff=0.1).next_to(eq_sum, DOWN, buff=0.6)
        self.play(Write(desc_7))

        eq_1011 = MathTex(r"1011 \equiv 1+0+1+1 \equiv 3 \pmod 9").next_to(desc_7, DOWN, buff=0.3)
        self.play(Write(eq_1011))
        self.wait(1)

        desc_8_t1 = Text("因此，原数", font="KaiTi", font_size=28)
        desc_8_m1 = MathTex(r"N", font_size=30).set_color(BLUE)
        desc_8_t2 = Text("模9的余数为：", font="KaiTi", font_size=28)
        desc_8 = VGroup(desc_8_t1, desc_8_m1, desc_8_t2).arrange(RIGHT, buff=0.1).next_to(eq_1011, DOWN, buff=0.6)
        self.play(Write(desc_8))

        eq_mod9_final = MathTex(r"N \equiv 3^2 \equiv 9 \equiv 0 \pmod 9").set_color(GREEN).next_to(desc_8, DOWN, buff=0.3)
        self.play(Write(eq_mod9_final))
        
        rect_mod9 = SurroundingRectangle(eq_mod9_final, color=GREEN, buff=0.15)
        self.play(Create(rect_mod9))
        self.wait(2)

        # 暴力清场，准备结合条件
        self.play(
            FadeOut(eq_sum), FadeOut(desc_7), FadeOut(eq_1011), 
            FadeOut(desc_8)
        )
        mod9_group = VGroup(eq_mod9_final, rect_mod9)
        self.play(mod9_group.animate.next_to(eq_mod20, DOWN, buff=0.5))

        # ==================== 第四幕：综合推导结果 ====================
        desc_9_t1 = Text("结合上述两项条件，代入检验：", font="KaiTi", font_size=28)
        desc_9 = desc_9_t1.next_to(mod9_group, DOWN, buff=0.8)
        self.play(Write(desc_9))

        test_0 = MathTex(r"k=0 \implies 20 \times 0 + 1 = 1 \not\equiv 0 \pmod 9").next_to(desc_9, DOWN, buff=0.4)
        test_1 = MathTex(r"k=1 \implies 20 \times 1 + 1 = 21 \not\equiv 0 \pmod 9").next_to(test_0, DOWN, buff=0.2)
        test_dots = MathTex(r"\dots").next_to(test_1, DOWN, buff=0.2)
        test_4 = MathTex(r"k=4 \implies 20 \times 4 + 1 = 81 \equiv 0 \pmod 9").set_color(YELLOW).next_to(test_dots, DOWN, buff=0.2)
        
        self.play(Write(test_0))
        self.play(Write(test_1))
        self.play(Write(test_dots))
        self.play(Write(test_4))
        self.wait(2)

        # 全屏清场，展示最终答案
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        final_desc = Text("最终求得，该多位数除以180的余数为：", font="KaiTi", font_size=35).to_edge(UP, buff=2)
        self.play(Write(final_desc))

        final_ans = MathTex(r"81").scale(2.5).set_color(YELLOW).move_to(ORIGIN)
        self.play(FadeIn(final_ans, shift=UP))
        
        rect_ans = SurroundingRectangle(final_ans, color=YELLOW, buff=0.3)
        self.play(Create(rect_ans))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)