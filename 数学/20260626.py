from manim import *

# 强制设置竖屏分辨率和自适应帧大小
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 8.0
config.frame_height = 14.22

class PrimeReciprocalDivergenceVertical(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title_text_1 = Text("证明：所有质数的", font="KaiTi", font_size=35)
        title_highlight = Text("倒数和", font="KaiTi", font_size=40).set_color(YELLOW)
        title_text_2 = Text("发散", font="KaiTi", font_size=35)
        title_line1 = VGroup(title_text_1, title_highlight, title_text_2).arrange(RIGHT, buff=0.1)

        title_math_eq = MathTex(r"\sum_{p} \frac{1}{p} = \infty", font_size=55).set_color(BLUE)

        cover = VGroup(title_line1, title_math_eq).arrange(DOWN, buff=0.8)
        cover.move_to(UP * 3.5)
        
        self.play(Write(title_line1))
        self.play(FadeIn(title_math_eq, shift=UP))
        self.wait(0.5)
        
        # ==================== 倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=160)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.next_to(cover, DOWN, buff=2.0)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一部分：欧拉乘积 ====================
        step1_title = Text("欧拉乘积公式", font="KaiTi", font_size=32).to_edge(UP, buff=1.5)
        self.play(Write(step1_title))

        desc_1_t1 = Text("已知所有自然数的调和级数发散至", font="KaiTi", font_size=26)
        desc_1_m1 = MathTex(r"\infty", font_size=30).set_color(YELLOW)
        desc_1_t2 = Text("：", font="KaiTi", font_size=26)
        desc_1 = VGroup(desc_1_t1, desc_1_m1, desc_1_t2).arrange(RIGHT, buff=0.1).next_to(step1_title, DOWN, buff=0.8)
        self.play(Write(desc_1))

        eq_harmonic = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n} = \infty", font_size=40).set_color(BLUE).next_to(desc_1, DOWN, buff=0.4)
        self.play(Write(eq_harmonic))
        self.wait(1)

        desc_2_t1 = Text("根据算术基本定理，转化为质数", font="KaiTi", font_size=26)
        desc_2_m1 = MathTex(r"p", font_size=30).set_color(YELLOW)
        desc_2_t2 = Text("的乘积：", font="KaiTi", font_size=26)
        desc_2 = VGroup(desc_2_t1, desc_2_m1, desc_2_t2).arrange(RIGHT, buff=0.1).next_to(eq_harmonic, DOWN, buff=0.8)
        self.play(Write(desc_2))

        eq_euler = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n} = \prod_{p} \frac{1}{1 - \frac{1}{p}}", font_size=40).set_color(BLUE).next_to(desc_2, DOWN, buff=0.4)
        self.play(Write(eq_euler))
        self.wait(1)

        desc_3 = Text("由此可推导，右侧的无穷乘积也必然发散：", font="KaiTi", font_size=26).next_to(eq_euler, DOWN, buff=0.8)
        self.play(Write(desc_3))

        eq_prod_inf = MathTex(r"\prod_{p} \frac{1}{1 - \frac{1}{p}} = \infty", font_size=40).set_color(YELLOW).next_to(desc_3, DOWN, buff=0.4)
        self.play(ReplacementTransform(eq_euler.copy(), eq_prod_inf))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 第二部分：展开与分离 ====================
        step2_title = Text("级数展开与项数分离", font="KaiTi", font_size=32).to_edge(UP, buff=1.5)
        self.play(Write(step2_title))

        desc_4_t1 = Text("对发散等式两边同时取自然对数", font="KaiTi", font_size=26)
        desc_4_m1 = MathTex(r"\ln", font_size=30).set_color(YELLOW)
        desc_4_t2 = Text("：", font="KaiTi", font_size=26)
        desc_4 = VGroup(desc_4_t1, desc_4_m1, desc_4_t2).arrange(RIGHT, buff=0.1).next_to(step2_title, DOWN, buff=0.8)
        self.play(Write(desc_4))

        eq_log_1 = MathTex(r"\sum_{p} -\ln\left( 1 - \frac{1}{p} \right) = \infty", font_size=40).set_color(BLUE).next_to(desc_4, DOWN, buff=0.4)
        self.play(Write(eq_log_1))
        self.wait(1)

        desc_5_t1 = Text("引入", font="KaiTi", font_size=26)
        desc_5_m1 = MathTex(r"-\ln(1-x)", font_size=30).set_color(YELLOW)
        desc_5_t2 = Text("的麦克劳林展开式：", font="KaiTi", font_size=26)
        desc_5 = VGroup(desc_5_t1, desc_5_m1, desc_5_t2).arrange(RIGHT, buff=0.1).next_to(eq_log_1, DOWN, buff=0.8)
        self.play(Write(desc_5))

        eq_taylor = MathTex(r"-\ln(1-x) = x + \frac{x^2}{2} + \frac{x^3}{3} + \dots", font_size=36).set_color(GRAY).next_to(desc_5, DOWN, buff=0.4)
        self.play(Write(eq_taylor))
        self.wait(1)

        desc_6_t1 = Text("代入", font="KaiTi", font_size=26)
        desc_6_m1 = MathTex(r"x = \frac{1}{p}", font_size=30).set_color(YELLOW)
        desc_6_t2 = Text("，写出具体的多项式：", font="KaiTi", font_size=26)
        desc_6 = VGroup(desc_6_t1, desc_6_m1, desc_6_t2).arrange(RIGHT, buff=0.1).next_to(eq_taylor, DOWN, buff=0.8)
        self.play(Write(desc_6))

        eq_sub = MathTex(r"-\ln\left(1-\frac{1}{p}\right) = \frac{1}{p} + \frac{1}{2p^2} + \frac{1}{3p^3} + \dots", font_size=36).set_color(GREEN).next_to(desc_6, DOWN, buff=0.4)
        self.play(Write(eq_sub))
        self.wait(1)

        desc_7_t1 = Text("将第一项", font="KaiTi", font_size=26)
        desc_7_m1 = MathTex(r"\frac{1}{p}", font_size=30).set_color(YELLOW)
        desc_7_t2 = Text("分离，后面各项用求和符号表示：", font="KaiTi", font_size=26)
        desc_7 = VGroup(desc_7_t1, desc_7_m1, desc_7_t2).arrange(RIGHT, buff=0.1).next_to(eq_sub, DOWN, buff=0.6)
        self.play(Write(desc_7))

        eq_sub_sum = MathTex(r"-\ln\left(1-\frac{1}{p}\right) = \frac{1}{p} + \sum_{k=2}^{\infty} \frac{1}{k p^k}", font_size=40).set_color(GREEN).next_to(desc_7, DOWN, buff=0.4)
        self.play(Write(eq_sub_sum))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 第三部分：余项放缩 ====================
        step3_title = Text("明确余项并放大", font="KaiTi", font_size=32).to_edge(UP, buff=1.5)
        self.play(Write(step3_title))

        desc_8_t1 = Text("将上一步骤的结果代回带有", font="KaiTi", font_size=26)
        desc_8_m1 = MathTex(r"\sum_p", font_size=30).set_color(YELLOW)
        desc_8_t2 = Text("的发散等式：", font="KaiTi", font_size=26)
        desc_8 = VGroup(desc_8_t1, desc_8_m1, desc_8_t2).arrange(RIGHT, buff=0.1).next_to(step3_title, DOWN, buff=0.8)
        self.play(Write(desc_8))

        eq_split = MathTex(r"\sum_{p} \frac{1}{p} + \underbrace{\sum_{p} \sum_{k=2}^{\infty} \frac{1}{k p^k}}_{R} = \infty", font_size=40).set_color(BLUE).next_to(desc_8, DOWN, buff=0.5)
        self.play(Write(eq_split))
        self.wait(1.5)

        desc_9_t1 = Text("为证明左侧第一项无穷大，需证明余项", font="KaiTi", font_size=26)
        desc_9_m1 = MathTex(r"R", font_size=30).set_color(YELLOW)
        desc_9_t2 = Text("有限。", font="KaiTi", font_size=26)
        desc_9 = VGroup(desc_9_t1, desc_9_m1, desc_9_t2).arrange(RIGHT, buff=0.1).next_to(eq_split, DOWN, buff=0.8)
        self.play(Write(desc_9))

        desc_10_t1 = Text("首先去掉分母中的", font="KaiTi", font_size=26)
        desc_10_m1 = MathTex(r"k", font_size=30).set_color(YELLOW)
        desc_10_t2 = Text("（因为", font="KaiTi", font_size=26)
        desc_10_m2 = MathTex(r"k \ge 2", font_size=30).set_color(YELLOW)
        desc_10_t3 = Text("），将级数放大：", font="KaiTi", font_size=26)
        desc_10 = VGroup(desc_10_t1, desc_10_m1, desc_10_t2, desc_10_m2, desc_10_t3).arrange(RIGHT, buff=0.1).next_to(desc_9, DOWN, buff=0.6)
        self.play(Write(desc_10))

        eq_bound_1 = MathTex(r"R < \sum_{p} \left( \sum_{k=2}^{\infty} \frac{1}{p^k} \right)", font_size=40).set_color(GREEN).next_to(desc_10, DOWN, buff=0.4)
        self.play(Write(eq_bound_1))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 第四部分：等比数列与化简 ====================
        step4_title = Text("等比数列求和与代数化简", font="KaiTi", font_size=32).to_edge(UP, buff=1.5)
        self.play(Write(step4_title))

        desc_11 = Text("观察括号内部，这是一个无穷等比数列求和：", font="KaiTi", font_size=26).next_to(step4_title, DOWN, buff=0.8)
        self.play(Write(desc_11))

        desc_12_t1 = Text("首项为", font="KaiTi", font_size=26)
        desc_12_m1 = MathTex(r"\frac{1}{p^2}", font_size=30).set_color(YELLOW)
        desc_12_t2 = Text("，公比为", font="KaiTi", font_size=26)
        desc_12_m2 = MathTex(r"\frac{1}{p}", font_size=30).set_color(YELLOW)
        desc_12 = VGroup(desc_12_t1, desc_12_m1, desc_12_t2, desc_12_m2).arrange(RIGHT, buff=0.1).next_to(desc_11, DOWN, buff=0.4)
        self.play(Write(desc_12))

        eq_geom_1 = MathTex(r"\sum_{k=2}^{\infty} \frac{1}{p^k} = \frac{ \frac{1}{p^2} }{ 1 - \frac{1}{p} }", font_size=45).set_color(BLUE).next_to(desc_12, DOWN, buff=0.6)
        self.play(Write(eq_geom_1))
        self.wait(1)

        desc_13_t1 = Text("为了消除繁分式，分子分母同乘", font="KaiTi", font_size=26)
        desc_13_m1 = MathTex(r"p^2", font_size=30).set_color(YELLOW)
        desc_13_t2 = Text("：", font="KaiTi", font_size=26)
        desc_13 = VGroup(desc_13_t1, desc_13_m1, desc_13_t2).arrange(RIGHT, buff=0.1).next_to(eq_geom_1, DOWN, buff=0.8)
        self.play(Write(desc_13))

        eq_geom_2 = MathTex(r"= \frac{ \frac{1}{p^2} \cdot p^2 }{ \left(1 - \frac{1}{p}\right) \cdot p^2 }", font_size=45).set_color(GREEN).next_to(desc_13, DOWN, buff=0.4)
        self.play(Write(eq_geom_2))
        self.wait(1)

        eq_geom_3 = MathTex(r"= \frac{1}{p^2 - p} = \frac{1}{p(p-1)}", font_size=45).set_color(YELLOW).next_to(eq_geom_2, DOWN, buff=0.4)
        self.play(Write(eq_geom_3))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 第五部分：裂项相消 ====================
        step5_title = Text("裂项相消得出结论", font="KaiTi", font_size=32).to_edge(UP, buff=1.5)
        self.play(Write(step5_title))

        desc_14_t1 = Text("将化简结果代回，得到余项", font="KaiTi", font_size=26)
        desc_14_m1 = MathTex(r"R", font_size=30).set_color(YELLOW)
        desc_14_t2 = Text("的新边界：", font="KaiTi", font_size=26)
        desc_14 = VGroup(desc_14_t1, desc_14_m1, desc_14_t2).arrange(RIGHT, buff=0.1).next_to(step5_title, DOWN, buff=0.8)
        self.play(Write(desc_14))

        eq_bound_final = MathTex(r"R < \sum_{p} \frac{1}{p(p-1)}", font_size=40).set_color(BLUE).next_to(desc_14, DOWN, buff=0.4)
        self.play(Write(eq_bound_final))
        self.wait(1)

        desc_15_t1 = Text("质数集合是正整数", font="KaiTi", font_size=26)
        desc_15_m1 = MathTex(r"n \ge 2", font_size=30).set_color(YELLOW)
        desc_15_t2 = Text("的子集，继续放大：", font="KaiTi", font_size=26)
        desc_15 = VGroup(desc_15_t1, desc_15_m1, desc_15_t2).arrange(RIGHT, buff=0.1).next_to(eq_bound_final, DOWN, buff=0.8)
        self.play(Write(desc_15))

        eq_bound_n = MathTex(r"R < \sum_{n=2}^{\infty} \frac{1}{n(n-1)}", font_size=40).set_color(GREEN).next_to(desc_15, DOWN, buff=0.4)
        self.play(Write(eq_bound_n))
        self.wait(1)

        desc_16 = Text("对分数进行裂项分解，并写出前几项相消：", font="KaiTi", font_size=26).next_to(eq_bound_n, DOWN, buff=0.8)
        self.play(Write(desc_16))

        eq_tele_1 = MathTex(r"\sum_{n=2}^{\infty} \left( \frac{1}{n-1} - \frac{1}{n} \right)", font_size=40).set_color(YELLOW).next_to(desc_16, DOWN, buff=0.4)
        self.play(Write(eq_tele_1))

        eq_tele_2 = MathTex(r"= \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \left(\frac{1}{3} - \frac{1}{4}\right) + \dots", font_size=36).set_color(YELLOW).next_to(eq_tele_1, DOWN, buff=0.4)
        self.play(Write(eq_tele_2))
        self.wait(1)

        eq_tele_3 = MathTex(r"= 1", font_size=40).set_color(RED).next_to(eq_tele_2, DOWN, buff=0.4)
        self.play(Write(eq_tele_3))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 结局：剧终 ====================
        outro_1_t1 = Text("至此，我们严格证明了余项", font="KaiTi", font_size=28).move_to(UP * 2)
        outro_1_m1 = MathTex(r"R < 1", font_size=35).set_color(YELLOW)
        outro_1 = VGroup(outro_1_t1, outro_1_m1).arrange(RIGHT, buff=0.1)
        self.play(Write(outro_1))

        outro_2 = Text("既然余项收敛，原等式左侧的主项必为无穷大：", font="KaiTi", font_size=25).next_to(outro_1, DOWN, buff=1)
        self.play(Write(outro_2))

        final_ans = MathTex(r"\sum_{p \in \mathbb{P}} \frac{1}{p} = \infty", font_size=60).set_color(YELLOW).next_to(outro_2, DOWN, buff=0.8)
        self.play(FadeIn(final_ans, shift=UP))
        self.wait(3)

        self.play(*[FadeOut(m) for m in self.mobjects])
        
        outro_3 = Text("证明完毕", font="KaiTi", font_size=35).move_to(ORIGIN)
        self.play(Write(outro_3))
        self.wait(3)
        self.play(FadeOut(outro_3))