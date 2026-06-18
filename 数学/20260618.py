from manim import *

class EulerPrimeProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("欧拉对质数无限的证明", font="KaiTi", font_size=45)
        title.set_color(WHITE)

        eq_cover = MathTex(
            r"\prod_{p} \frac{1}{1 - p^{-1}} = \sum_{n=1}^{\infty} \frac{1}{n}",
            font_size=55
        ).set_color(BLUE)

        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1.0)
        # 整体上移，为倒计时留出空间
        cover.move_to(UP * 0.5) 
        
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))

        # ==================== 3秒倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=120)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            # 定位在标题和公式的下方，避免遮挡
            countdown_text.next_to(cover, DOWN, buff=1.0) 
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：基础事实的引入 ====================
        desc_1 = Text("首先，回顾微积分中调和级数发散的性质：", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_harmonic = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \dots = \infty")
        eq_harmonic.set_color(BLUE).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(eq_harmonic))
        self.wait(1.5)

        # 严格遵守混合排版规则
        desc_2_1 = Text("其次，对于任意大于 1 的质数", font="KaiTi", font_size=28)
        p_math = MathTex("p", font_size=30).set_color(YELLOW)
        desc_2_2 = Text("，其几何级数收敛于：", font="KaiTi", font_size=28)
        desc_2 = VGroup(desc_2_1, p_math, desc_2_2).arrange(RIGHT, buff=0.1)
        desc_2.next_to(eq_harmonic, DOWN, buff=0.8)
        self.play(Write(desc_2))

        eq_geometric = MathTex(r"1 + \frac{1}{p} + \frac{1}{p^2} + \dots = \frac{1}{1 - \frac{1}{p}}")
        eq_geometric.set_color(YELLOW).next_to(desc_2, DOWN, buff=0.3)
        self.play(Write(eq_geometric))
        self.wait(2)

        # 整理屏幕，避免公式超出屏幕外
        self.play(
            FadeOut(desc_1), FadeOut(eq_harmonic), FadeOut(desc_2), FadeOut(eq_geometric)
        )

        # ==================== 第二幕：欧拉乘积公式 ====================
        desc_3_1 = Text("将所有质数", font="KaiTi", font_size=30)
        p_math_2 = MathTex("p", font_size=32).set_color(YELLOW)
        desc_3_2 = Text("对应的几何级数相乘：", font="KaiTi", font_size=30)
        desc_3 = VGroup(desc_3_1, p_math_2, desc_3_2).arrange(RIGHT, buff=0.1)
        desc_3.to_edge(UP, buff=0.8)
        self.play(Write(desc_3))

        eq_prod = MathTex(r"\prod_{p} \left( 1 + \frac{1}{p} + \frac{1}{p^2} + \dots \right)")
        eq_prod.set_color(BLUE).next_to(desc_3, DOWN, buff=0.4)
        self.play(Write(eq_prod))
        self.wait(1.5)

        desc_4_1 = Text("根据算术基本定理，任意正整数", font="KaiTi", font_size=28)
        n_math = MathTex("n", font_size=30).set_color(WHITE)
        desc_4_2 = Text("可唯一分解为质因数之积。", font="KaiTi", font_size=28)
        desc_4 = VGroup(desc_4_1, n_math, desc_4_2).arrange(RIGHT, buff=0.1)
        desc_4.next_to(eq_prod, DOWN, buff=0.6)
        self.play(Write(desc_4))

        desc_5 = Text("展开上述乘积，恰好能遍历所有正整数的倒数：", font="KaiTi", font_size=28)
        desc_5.next_to(desc_4, DOWN, buff=0.3)
        self.play(Write(desc_5))

        eq_euler = MathTex(r"\prod_{p} \frac{1}{1 - \frac{1}{p}} = \sum_{n=1}^{\infty} \frac{1}{n}")
        eq_euler.scale(1.1).set_color(GREEN).next_to(desc_5, DOWN, buff=0.4)
        self.play(Write(eq_euler))
        
        rect_euler = SurroundingRectangle(eq_euler, color=GREEN, buff=0.15)
        self.play(Create(rect_euler))
        self.wait(2)

        # 整理屏幕，仅保留核心等式
        euler_group = VGroup(eq_euler, rect_euler)
        self.play(
            FadeOut(desc_3), FadeOut(eq_prod), FadeOut(desc_4), FadeOut(desc_5)
        )
        self.play(euler_group.animate.to_edge(UP, buff=0.8))

        # ==================== 第三幕：反证法与收尾 ====================
        desc_6_1 = Text("利用反证法。假设质数仅有有限的", font="KaiTi", font_size=28)
        k_math = MathTex("k", font_size=30).set_color(YELLOW)
        desc_6_2 = Text("个，", font="KaiTi", font_size=28)
        desc_6 = VGroup(desc_6_1, k_math, desc_6_2).arrange(RIGHT, buff=0.1)
        desc_6.next_to(euler_group, DOWN, buff=0.8)
        self.play(Write(desc_6))

        desc_7 = Text("则等号左侧为有限项乘积，结果必然为一个有限常数。", font="KaiTi", font_size=28)
        desc_7.next_to(desc_6, DOWN, buff=0.4)
        self.play(Write(desc_7))

        desc_8 = Text("然而，等号右侧为调和级数，其和趋于无穷大。", font="KaiTi", font_size=28)
        desc_8.next_to(desc_7, DOWN, buff=0.4)
        self.play(Write(desc_8))

        # 中文与数学符号的简单结合，保证字体正确
        eq_contradiction_1 = Text("有限常数", font="KaiTi", font_size=32).set_color(RED)
        eq_contradiction_2 = MathTex(r"\neq \infty", font_size=35).set_color(RED)
        eq_contradiction = VGroup(eq_contradiction_1, eq_contradiction_2).arrange(RIGHT, buff=0.2)
        eq_contradiction.next_to(desc_8, DOWN, buff=0.6)
        self.play(FadeIn(eq_contradiction, shift=UP))
        self.wait(1.5)

        desc_9 = Text("产生矛盾，故原假设不成立，质数必然有无穷多个。", font="KaiTi", font_size=30)
        desc_9.next_to(eq_contradiction, DOWN, buff=0.6)
        self.play(Write(desc_9))
        self.wait(3)

        # 大清场
        self.play(
            FadeOut(euler_group), FadeOut(desc_6), FadeOut(desc_7), 
            FadeOut(desc_8), FadeOut(eq_contradiction), FadeOut(desc_9)
        )

        # ==================== 第四幕：历史意义 ====================
        # 移除了大标题，直接将第一句话作为起始点定位在屏幕上方
        hist_1 = Text("1737年，欧拉在极限概念尚未严格建立的时代写下此恒等式。", font="KaiTi", font_size=28)
        hist_1.to_edge(UP, buff=1.5)
        self.play(Write(hist_1))

        # 引入相关历史事实，丰富知识深度
        hist_2_1 = Text("不仅如同他解决巴塞尔问题", font="KaiTi", font_size=28)
        eq_basel = MathTex(r"\sum \frac{1}{n^2} = \frac{\pi^2}{6}", font_size=30).set_color(BLUE)
        hist_2_2 = Text("般展现了高超的级数技巧，", font="KaiTi", font_size=28)
        hist_2 = VGroup(hist_2_1, eq_basel, hist_2_2).arrange(RIGHT, buff=0.1)
        hist_2.next_to(hist_1, DOWN, buff=0.3)
        self.play(Write(hist_2))

        hist_3 = Text("更是首次将数论中的离散问题与分析学中的连续级数相连。", font="KaiTi", font_size=28)
        hist_3.next_to(hist_2, DOWN, buff=0.3)
        self.play(Write(hist_3))
        self.wait(1)

        hist_4_1 = Text("后来，黎曼将公式中的指数推广至复数域", font="KaiTi", font_size=28)
        s_math = MathTex("s", font_size=30).set_color(YELLOW)
        hist_4_2 = Text("，定义了：", font="KaiTi", font_size=28)
        hist_4 = VGroup(hist_4_1, s_math, hist_4_2).arrange(RIGHT, buff=0.1)
        hist_4.next_to(hist_3, DOWN, buff=0.6)
        self.play(Write(hist_4))

        eq_zeta = MathTex(r"\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_{p} \frac{1}{1 - p^{-s}}")
        eq_zeta.scale(1.1).set_color(YELLOW).next_to(hist_4, DOWN, buff=0.4)
        self.play(FadeIn(eq_zeta, shift=UP))
        self.wait(1)

        hist_5 = Text("著名的黎曼猜想正是由此而来，这也为现代解析数论打下了基础。", font="KaiTi", font_size=28)
        hist_5.next_to(eq_zeta, DOWN, buff=0.6)
        self.play(Write(hist_5))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)