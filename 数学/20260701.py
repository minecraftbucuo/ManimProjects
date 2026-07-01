from manim import *

# 强制设置竖屏分辨率和自适应帧大小
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 8.0
config.frame_height = 14.22

class StirlingFormulaRigorousProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title_line1 = Text("斯特林公式的推导", font="KaiTi", font_size=45)
        title_line2 = Text("", font="KaiTi", font_size=40)
        title = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.3)
        
        eq_cover = MathTex(
            r"n! \sim \sqrt{2\pi n} \left(\frac{n}{e}\right)^n",
            font_size=60
        ).set_color(BLUE)

        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1.2).to_edge(UP, buff=2.5)
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))
        
        # ==================== 3秒倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=150)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.next_to(cover, DOWN, buff=1.5)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：指数化积分 ====================
        desc_1_L1 = Text("由伽马函数定义，", font="KaiTi", font_size=28)
        desc_1_L2 = VGroup(
            Text("阶乘", font="KaiTi", font_size=28),
            MathTex(r"n!", font_size=30).set_color(YELLOW),
            Text("的积分表示为：", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1)
        desc_1 = VGroup(desc_1_L1, desc_1_L2).arrange(DOWN, buff=0.2).to_edge(UP, buff=1.0)
        self.play(Write(desc_1))

        eq_1 = MathTex(r"n! = \int_0^\infty x^n e^{-x} dx").set_color(BLUE).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(eq_1))
        self.wait(1)

        desc_2_L1 = VGroup(
            Text("为研究当", font="KaiTi", font_size=28),
            MathTex(r"n \to \infty", font_size=30).set_color(YELLOW),
            Text("时的行为，", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1)
        desc_2_L2 = Text("将积分核改写为指数形式：", font="KaiTi", font_size=28)
        desc_2 = VGroup(desc_2_L1, desc_2_L2).arrange(DOWN, buff=0.2).next_to(eq_1, DOWN, buff=0.6)
        self.play(Write(desc_2))

        eq_2 = MathTex(r"x^n e^{-x} = e^{n \ln x - x}").set_color(GREEN).next_to(desc_2, DOWN, buff=0.4)
        self.play(Write(eq_2))
        self.wait(1)

        desc_3 = VGroup(
            Text("令指数部分的函数为", font="KaiTi", font_size=28),
            MathTex(r"f(x)", font_size=30).set_color(YELLOW),
            Text("：", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1).next_to(eq_2, DOWN, buff=0.6)
        self.play(Write(desc_3))

        eq_3 = MathTex(r"n! = \int_0^\infty e^{f(x)} dx").set_color(BLUE).next_to(desc_3, DOWN, buff=0.4)
        self.play(Write(eq_3))
        self.wait(2)

        self.play(
            FadeOut(desc_1), FadeOut(eq_1), FadeOut(desc_2), FadeOut(eq_2), FadeOut(desc_3)
        )
        
        f_def = MathTex(r"f(x) = n \ln x - x").set_color(YELLOW).to_edge(UP, buff=1.0)
        self.play(ReplacementTransform(eq_3, f_def))

        # ==================== 第二幕：求导与极值分析 ====================
        desc_4_L1 = Text("积分值集中在极值点附近。", font="KaiTi", font_size=28)
        desc_4_L2 = Text("对其求一阶导数：", font="KaiTi", font_size=28)
        desc_4 = VGroup(desc_4_L1, desc_4_L2).arrange(DOWN, buff=0.2).next_to(f_def, DOWN, buff=0.6)
        self.play(Write(desc_4))

        eq_4 = MathTex(r"f'(x) = \frac{n}{x} - 1").set_color(BLUE).next_to(desc_4, DOWN, buff=0.4)
        self.play(Write(eq_4))
        self.wait(1)

        desc_5 = VGroup(
            Text("令", font="KaiTi", font_size=28),
            MathTex(r"f'(x) = 0", font_size=30).set_color(YELLOW),
            Text("，解得驻点：", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1).next_to(eq_4, DOWN, buff=0.6)
        self.play(Write(desc_5))

        eq_5 = MathTex(r"x_0 = n").set_color(GREEN).next_to(desc_5, DOWN, buff=0.4)
        self.play(Write(eq_5))
        self.wait(1)

        desc_6_L1 = Text("求二阶导数并代入驻点验证，", font="KaiTi", font_size=28)
        desc_6_L2 = Text("确认其为极大值：", font="KaiTi", font_size=28)
        desc_6 = VGroup(desc_6_L1, desc_6_L2).arrange(DOWN, buff=0.2).next_to(eq_5, DOWN, buff=0.6)
        self.play(Write(desc_6))

        eq_6 = MathTex(r"f''(n) = -\frac{1}{n} < 0").set_color(BLUE).next_to(desc_6, DOWN, buff=0.4)
        self.play(Write(eq_6))
        self.wait(2)

        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        # ==================== 第三幕：泰勒级数展开 ====================
        desc_7_L1 = VGroup(
            Text("将", font="KaiTi", font_size=28),
            MathTex(r"f(x)", font_size=30).set_color(YELLOW),
            Text("在极大值点", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1)
        desc_7_L2 = VGroup(
            MathTex(r"x = n", font_size=30).set_color(YELLOW),
            Text("处作二阶泰勒展开：", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1)
        desc_7 = VGroup(desc_7_L1, desc_7_L2).arrange(DOWN, buff=0.2).to_edge(UP, buff=1.0)
        self.play(Write(desc_7))

        eq_7 = MathTex(r"f(x) \approx f(n) + \frac{1}{2}f''(n)(x-n)^2").set_color(BLUE).next_to(desc_7, DOWN, buff=0.5)
        self.play(Write(eq_7))
        self.wait(1)

        desc_8 = Text("代入已求得的各项数值：", font="KaiTi", font_size=28).next_to(eq_7, DOWN, buff=0.6)
        self.play(Write(desc_8))

        eq_8_1 = MathTex(r"f(n) = n \ln n - n").set_color(GREEN)
        eq_8_2 = MathTex(r"f'(n) = 0").set_color(GREEN)
        eq_8_3 = MathTex(r"f''(n) = -\frac{1}{n}").set_color(GREEN)
        eq_8_group = VGroup(eq_8_1, eq_8_2, eq_8_3).arrange(DOWN, buff=0.3).next_to(desc_8, DOWN, buff=0.4)
        self.play(Write(eq_8_group))
        self.wait(1.5)

        desc_9 = Text("得到局部近似多项式：", font="KaiTi", font_size=28).next_to(eq_8_group, DOWN, buff=0.6)
        self.play(Write(desc_9))

        eq_9 = MathTex(r"f(x) \approx (n \ln n - n) - \frac{(x-n)^2}{2n}").set_color(YELLOW).next_to(desc_9, DOWN, buff=0.4)
        self.play(Write(eq_9))
        self.wait(2)

        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        # ==================== 第四幕：代回积分与换元 ====================
        desc_10 = Text("将展开式代回原积分：", font="KaiTi", font_size=28).to_edge(UP, buff=1.0)
        self.play(Write(desc_10))

        eq_10 = MathTex(r"n! \approx \int_0^\infty e^{(n \ln n - n) - \frac{(x-n)^2}{2n}} dx").set_color(BLUE).next_to(desc_10, DOWN, buff=0.5)
        self.play(Write(eq_10))
        self.wait(1)

        desc_11 = Text("提取无关常数到积分外：", font="KaiTi", font_size=28).next_to(eq_10, DOWN, buff=0.6)
        self.play(Write(desc_11))

        eq_11 = MathTex(r"n! \approx n^n e^{-n} \int_0^\infty e^{-\frac{(x-n)^2}{2n}} dx").set_color(GREEN).next_to(desc_11, DOWN, buff=0.4)
        self.play(Write(eq_11))
        self.wait(1.5)

        desc_12_L1 = VGroup(
            Text("作变量代换令", font="KaiTi", font_size=28),
            MathTex(r"t = x - n", font_size=30).set_color(YELLOW),
            Text("，", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1)
        desc_12_L2 = VGroup(
            Text("延拓下限至", font="KaiTi", font_size=28),
            MathTex(r"-\infty", font_size=30).set_color(YELLOW),
            Text("：", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1)
        desc_12 = VGroup(desc_12_L1, desc_12_L2).arrange(DOWN, buff=0.2).next_to(eq_11, DOWN, buff=0.6)
        self.play(Write(desc_12))

        eq_12 = MathTex(r"n! \approx n^n e^{-n} \int_{-\infty}^\infty e^{-\frac{t^2}{2n}} dt").set_color(BLUE).next_to(desc_12, DOWN, buff=0.4)
        self.play(Write(eq_12))
        self.wait(2)

        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        # ==================== 第五幕：高斯积分求解 ====================
        desc_13 = Text("转化为标准高斯积分：", font="KaiTi", font_size=28).to_edge(UP, buff=1.0)
        self.play(Write(desc_13))

        eq_13 = MathTex(r"\int_{-\infty}^\infty e^{-a t^2} dt = \sqrt{\frac{\pi}{a}}").set_color(GREEN).next_to(desc_13, DOWN, buff=0.5)
        self.play(Write(eq_13))
        self.wait(1)

        desc_14_L1 = VGroup(
            Text("此处参数", font="KaiTi", font_size=28),
            MathTex(r"a = \frac{1}{2n}", font_size=30).set_color(YELLOW),
            Text("，", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1)
        desc_14_L2 = Text("代入计算得：", font="KaiTi", font_size=28)
        desc_14 = VGroup(desc_14_L1, desc_14_L2).arrange(DOWN, buff=0.2).next_to(eq_13, DOWN, buff=0.6)
        self.play(Write(desc_14))

        eq_14 = MathTex(r"\int_{-\infty}^\infty e^{-\frac{t^2}{2n}} dt = \sqrt{2\pi n}").set_color(BLUE).next_to(desc_14, DOWN, buff=0.4)
        self.play(Write(eq_14))
        self.wait(2)

        # ==================== 第六幕：最终结论 ====================
        self.play(
            FadeOut(desc_13), FadeOut(eq_13), FadeOut(desc_14)
        )
        self.play(eq_14.animate.to_edge(UP, buff=2.0))

        desc_15_L1 = Text("将积分结果与外侧系数相乘，", font="KaiTi", font_size=30)
        desc_15_L2 = Text("即得斯特林公式：", font="KaiTi", font_size=30)
        desc_15 = VGroup(desc_15_L1, desc_15_L2).arrange(DOWN, buff=0.3).next_to(eq_14, DOWN, buff=1.0)
        self.play(Write(desc_15))

        final_ans = MathTex(r"n! \sim \sqrt{2\pi n} \left(\frac{n}{e}\right)^n").scale(1.5).set_color(YELLOW).next_to(desc_15, DOWN, buff=1.0)
        self.play(FadeIn(final_ans, shift=UP))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)