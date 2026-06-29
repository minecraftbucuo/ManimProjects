from manim import *

# 强制设置竖屏分辨率和自适应帧大小
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 8.0
config.frame_height = 14.22


class IntegralProofBothMethods(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("求解不定积分", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN)

        eq_cover = MathTex(
            r"I = \int \frac{1 - \ln x}{(x - \ln x)^2} \mathrm{d}x",
            font_size=55
        ).set_color(BLUE)

        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1.2).move_to(UP * 2)
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))

        # ==================== 倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=150)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.next_to(cover, DOWN, buff=2.0)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 方法一：代数变形与分部积分法 ====================
        method_1_title = Text("方法一：代数变形与分部积分法", font="KaiTi", font_size=40).set_color(BLUE)
        self.play(Write(method_1_title))
        self.wait(1)
        self.play(method_1_title.animate.to_edge(UP, buff=1.0).scale(0.8))

        desc_1_text = Text("首先对积分的被积函数分子进行代数变形：", font="KaiTi", font_size=30)
        desc_1_text.next_to(method_1_title, DOWN, buff=0.8)
        self.play(Write(desc_1_text))

        eq_num = MathTex(r"1 - \ln x = (x - \ln x) - (x - 1)").scale(0.9)
        eq_num.next_to(desc_1_text, DOWN, buff=0.6)
        self.play(Write(eq_num))
        self.wait(1)

        desc_2_text = Text("将其代入原积分，并拆分为两项：", font="KaiTi", font_size=30)
        desc_2_text.next_to(eq_num, DOWN, buff=0.8)
        self.play(Write(desc_2_text))

        eq_split = MathTex(
            r"I &= \int \frac{(x - \ln x) - (x - 1)}{(x - \ln x)^2} \mathrm{d}x \\",
            r"&= \int \frac{1}{x - \ln x} \mathrm{d}x - \int \frac{x - 1}{(x - \ln x)^2} \mathrm{d}x"
        ).scale(0.85)
        eq_split.next_to(desc_2_text, DOWN, buff=0.6)
        self.play(Write(eq_split))
        self.wait(1.5)

        # 清理屏幕，保留两项积分式
        self.play(FadeOut(desc_1_text), FadeOut(eq_num), FadeOut(desc_2_text))
        self.play(eq_split.animate.next_to(method_1_title, DOWN, buff=0.5))

        desc_3_text = Text("考察右侧第二项，凑入微分：", font="KaiTi", font_size=30)
        desc_3_text.next_to(eq_split, DOWN, buff=0.8)
        self.play(Write(desc_3_text))

        eq_diff = MathTex(r"(x - 1)\mathrm{d}x = x\mathrm{d}(x - \ln x)").scale(0.9).set_color(YELLOW)
        eq_diff.next_to(desc_3_text, DOWN, buff=0.5)
        self.play(Write(eq_diff))
        self.wait(1)

        desc_4_text = Text("代入后应用分部积分公式：", font="KaiTi", font_size=30)
        desc_4_text.next_to(eq_diff, DOWN, buff=0.8)
        self.play(Write(desc_4_text))

        eq_ibp = MathTex(
            r"\int \frac{x \mathrm{d}(x - \ln x)}{(x - \ln x)^2} ",
            r"&= \int x \mathrm{d}\left(-\frac{1}{x - \ln x}\right) \\",
            r"&= -\frac{x}{x - \ln x} + \int \frac{1}{x - \ln x} \mathrm{d}x"
        ).scale(0.8)
        eq_ibp.next_to(desc_4_text, DOWN, buff=0.5)
        self.play(Write(eq_ibp[0]))
        self.play(Write(eq_ibp[1]))
        self.wait(0.5)
        self.play(Write(eq_ibp[2]))
        self.wait(1.5)

        # 结论得出
        self.play(*[FadeOut(m) for m in self.mobjects if m != method_1_title])
        
        desc_5_text = Text("代回原式，两项积分恰好抵消：", font="KaiTi", font_size=32)
        desc_5_text.next_to(method_1_title, DOWN, buff=1.5)
        self.play(Write(desc_5_text))

        eq_final_1 = MathTex(r"I = \frac{x}{x - \ln x} + C").scale(1.2).set_color(YELLOW)
        eq_final_1.next_to(desc_5_text, DOWN, buff=1.0)
        self.play(Write(eq_final_1))
        self.wait(2)

        # ==================== 方法二：商的求导法则逆向构造 ====================
        # 全屏清场
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(0.5)

        method_2_title = Text("方法二：商的求导法则逆向构造", font="KaiTi", font_size=40).set_color(GREEN)
        self.play(Write(method_2_title))
        self.wait(1)
        self.play(method_2_title.animate.to_edge(UP, buff=1.0).scale(0.8))

        desc_6_text1 = Text("对于分母为", font="KaiTi", font_size=30)
        desc_6_math1 = MathTex(r"v^2", font_size=32).set_color(YELLOW)
        desc_6_text2 = Text("的结构，逆用商的求导法则：", font="KaiTi", font_size=30)
        desc_6 = VGroup(desc_6_text1, desc_6_math1, desc_6_text2).arrange(RIGHT, buff=0.1)
        desc_6.next_to(method_2_title, DOWN, buff=0.8)
        self.play(Write(desc_6))

        eq_quotient = MathTex(r"\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}").scale(1.1)
        eq_quotient.next_to(desc_6, DOWN, buff=0.6)
        self.play(Write(eq_quotient))
        self.wait(1.5)

        desc_7_text1 = Text("令", font="KaiTi", font_size=30)
        desc_7_math1 = MathTex(r"v = x - \ln x", font_size=32).set_color(YELLOW)
        desc_7_text2 = Text("，尝试构造未知分子", font="KaiTi", font_size=30)
        desc_7_math2 = MathTex(r"u(x)", font_size=32).set_color(YELLOW)
        desc_7_text3 = Text("：", font="KaiTi", font_size=30)
        desc_7 = VGroup(desc_7_text1, desc_7_math1, desc_7_text2, desc_7_math2, desc_7_text3).arrange(RIGHT, buff=0.1)
        desc_7.next_to(eq_quotient, DOWN, buff=1.0)
        self.play(Write(desc_7))

        eq_construct_1 = MathTex(r"u'v - uv' = u'(x - \ln x) - u\left(1 - \frac{1}{x}\right)").scale(0.85)
        eq_construct_1.next_to(desc_7, DOWN, buff=0.5)
        self.play(Write(eq_construct_1))
        self.wait(1)

        desc_8_text = Text("令该展开式严格等于原积分分子：", font="KaiTi", font_size=30)
        desc_8_text.next_to(eq_construct_1, DOWN, buff=0.8)
        self.play(Write(desc_8_text))

        eq_construct_2 = MathTex(r"u'(x - \ln x) - u\left(1 - \frac{1}{x}\right) = 1 - \ln x").scale(0.9).set_color(BLUE)
        eq_construct_2.next_to(desc_8_text, DOWN, buff=0.5)
        self.play(Write(eq_construct_2))
        self.wait(2)

        # 整理屏幕准备检验
        self.play(
            FadeOut(desc_6), FadeOut(eq_quotient), FadeOut(desc_7), 
            FadeOut(eq_construct_1), FadeOut(desc_8_text)
        )
        self.play(eq_construct_2.animate.next_to(method_2_title, DOWN, buff=0.8))

        desc_9_text1 = Text("观察多项式对应关系，若取", font="KaiTi", font_size=30)
        desc_9_math1 = MathTex(r"u = x", font_size=32).set_color(YELLOW)
        desc_9_text2 = Text("，代入检验：", font="KaiTi", font_size=30)
        desc_9 = VGroup(desc_9_text1, desc_9_math1, desc_9_text2).arrange(RIGHT, buff=0.1)
        desc_9.next_to(eq_construct_2, DOWN, buff=1.0)
        self.play(Write(desc_9))

        eq_check = MathTex(r"1 \cdot (x - \ln x) - x \cdot \left(1 - \frac{1}{x}\right) = 1 - \ln x").scale(0.9)
        eq_check.next_to(desc_9, DOWN, buff=0.6)
        self.play(Write(eq_check))
        self.wait(1.5)

        desc_10_text = Text("等式成立。由此可知被积函数正是全导数：", font="KaiTi", font_size=30)
        desc_10_text.next_to(eq_check, DOWN, buff=1.0)
        self.play(Write(desc_10_text))

        eq_exact_deriv = MathTex(r"\left( \frac{x}{x - \ln x} \right)' = \frac{1 - \ln x}{(x - \ln x)^2}").scale(1.0).set_color(GREEN)
        eq_exact_deriv.next_to(desc_10_text, DOWN, buff=0.6)
        self.play(Write(eq_exact_deriv))
        self.wait(2)

        # 大结局清场
        self.play(
            *[FadeOut(m) for m in self.mobjects if m != method_2_title]
        )

        desc_11_text = Text("对等式两边同时积分，殊途同归：", font="KaiTi", font_size=32)
        desc_11_text.next_to(method_2_title, DOWN, buff=1.5)
        self.play(Write(desc_11_text))

        eq_final_2 = MathTex(r"\int \frac{1 - \ln x}{(x - \ln x)^2} \mathrm{d}x = \frac{x}{x - \ln x} + C").scale(1.0).set_color(YELLOW)
        eq_final_2.next_to(desc_11_text, DOWN, buff=1.0)
        self.play(Write(eq_final_2))
        self.wait(3)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)