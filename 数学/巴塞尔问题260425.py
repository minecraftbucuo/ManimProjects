from manimlib import *


class BaselProblemProof(Scene):
    def construct(self):
        # ==================== 封面与倒计时 ====================
        title = Text("如何用初等方法证明巴塞尔问题？", font="KaiTi", font_size=60)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW)

        series = Tex(
            r"\sum_{n=1}^{\infty} \frac{1}{n^2} = 1 + \frac{1}{4} + \frac{1}{9} + \cdots = \frac{\pi^2}{6}",
            font_size=50
        )
        series.set_color_by_gradient(GREEN, BLUE, YELLOW)

        cover = VGroup(title, series).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(Write(series))
        self.wait(2)

        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=180)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.move_to(ORIGIN)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)

        self.play(FadeOut(cover))

        # ==================== 场景一：复数展开与虚部提取 ====================
        hint_1 = VGroup(
            Text("我们先从", font="KaiTi", font_size=32),
            Text("棣莫弗公式", font="KaiTi", font_size=32).set_color(YELLOW),
            Text("出发：", font="KaiTi", font_size=32)
        ).arrange(RIGHT, buff=0.1).to_edge(UP, buff=0.6)
        self.play(Write(hint_1))

        eq_demoivre = Tex(
            r"(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)"
        ).set_color(BLUE).next_to(hint_1, DOWN, buff=0.4)
        self.play(Write(eq_demoivre))
        self.wait(1)

        hint_2 = Text("利用二项式定理，将左边完全展开：", font="KaiTi", font_size=30).next_to(eq_demoivre, DOWN, buff=0.6)
        self.play(Write(hint_2))

        eq_expand = Tex(
            r"(\cos\theta + i\sin\theta)^n = \cos^n\theta + i\binom{n}{1}\cos^{n-1}\theta\sin\theta - \binom{n}{2}\cos^{n-2}\theta\sin^2\theta - \cdots"
        ).set_color(BLUE).scale(0.7).next_to(hint_2, DOWN, buff=0.4)
        self.play(Write(eq_expand))
        self.wait(1.5)

        # 【排版控制 1】：淡出前两句文本，把公式往上移，腾出下方空间
        self.play(FadeOut(hint_1), FadeOut(hint_2))
        self.play(
            VGroup(eq_demoivre, eq_expand).animate.to_edge(UP, buff=0.5)
        )

        hint_3 = VGroup(
            Text("对比等式两边，我们只提取", font="KaiTi", font_size=30),
            Text("虚部", font="KaiTi", font_size=30).set_color(GREEN),
            Text("（带有奇数个 ", font="KaiTi", font_size=30),
            Tex("i", font_size=35),  # 这里用 Tex 渲染数学符号 i
            Text(" 的项）：", font="KaiTi", font_size=30)
        ).arrange(RIGHT, buff=0.1).next_to(eq_expand, DOWN, buff=0.6)

        self.play(Write(hint_3))

        eq_sin_exp = Tex(
            r"\sin(n\theta) = \binom{n}{1}\cos^{n-1}\theta \sin\theta - \binom{n}{3}\cos^{n-3}\theta \sin^3\theta + \cdots"
        ).set_color(BLUE).scale(0.8).next_to(hint_3, DOWN, buff=0.4)
        self.play(Write(eq_sin_exp))
        self.wait(1.5)

        hint_4 = Text("在右侧提取公因式：", font="KaiTi", font_size=30).next_to(eq_sin_exp, DOWN,
                                                                                                buff=0.5)
        self.play(Write(hint_4))

        eq_sin_cot = Tex(
            r"\sin(n\theta) = \sin^n\theta \left[ \binom{n}{1}\cot^{n-1}\theta - \binom{n}{3}\cot^{n-3}\theta + \cdots \right]"
        ).set_color(YELLOW).scale(0.8).next_to(hint_4, DOWN, buff=0.4)
        self.play(TransformMatchingTex(eq_sin_exp.copy(), eq_sin_cot))
        self.wait(2)

        # 清空屏幕，只保留最终核心公式置顶
        self.play(FadeOut(VGroup(eq_demoivre, eq_expand, hint_3, eq_sin_exp, hint_4)))
        self.play(eq_sin_cot.animate.to_edge(UP, buff=0.6))

        # ==================== 场景二：构造方程与召唤韦达定理 ====================
        hint_5 = VGroup(
            Text("令 ", font="KaiTi", font_size=32),
            Tex(r"n = 2m + 1", font_size=32).set_color(GREEN)
        ).arrange(RIGHT, buff=0.1).next_to(eq_sin_cot, DOWN, buff=0.6)

        hint_6 = VGroup(
            Text("此时再令等式左边 ", font="KaiTi", font_size=32),
            Tex(r"\sin((2m+1)\theta) = 0", font_size=35).set_color(RED),
            Text("，寻找能让等式成立的角度：", font="KaiTi", font_size=32)
        ).arrange(RIGHT, buff=0.1).next_to(hint_5, DOWN, buff=0.3)
        self.play(Write(hint_5), Write(hint_6))

        eq_roots = Tex(
            r"\theta_k = \frac{k\pi}{2m+1} \quad (k = 1, 2, \dots, m)"
        ).set_color(BLUE).scale(0.9).next_to(hint_6, DOWN, buff=0.3)
        self.play(Write(eq_roots))
        self.wait(1.5)

        # 【排版控制 2】：擦掉文字，把根的公式推上去
        self.play(FadeOut(hint_5), FadeOut(hint_6))
        self.play(eq_roots.animate.next_to(eq_sin_cot, DOWN, buff=0.5))

        hint_7 = VGroup(
            Text("在区间 ", font="KaiTi", font_size=30),
            Tex(r"\left(0, \frac{\pi}{2}\right)", font_size=35).set_color(GREEN),
            Text(" 内正弦值不为 0，既然整体等于 0，必定是", font="KaiTi", font_size=30),
            Text("方括号内为 0", font="KaiTi", font_size=30).set_color(YELLOW)
        ).arrange(RIGHT, buff=0.1).next_to(eq_roots, DOWN, buff=0.5)
        self.play(Write(hint_7))

        eq_poly = Tex(
            r"\binom{2m+1}{1} (\cot^2\theta)^m - \binom{2m+1}{3} (\cot^2\theta)^{m-1} + \dots = 0"
        ).set_color(BLUE).scale(0.85).next_to(hint_7, DOWN, buff=0.3)
        self.play(Write(eq_poly))
        self.wait(1.5)

        # 【排版控制 3】：再次擦掉文字，把多项式推上去
        self.play(FadeOut(hint_7))
        self.play(eq_poly.animate.next_to(eq_roots, DOWN, buff=0.5))

        # 此时屏幕下方有广阔的空间，绝对不会溢出
        hint_8 = VGroup(
            Text("将其看作关于 ", font="KaiTi", font_size=30),
            Tex(r"x = \cot^2\theta", font_size=35).set_color(GREEN),
            Text(" 的 m 次多项式，由", font="KaiTi", font_size=30),
            Text("韦达定理", font="KaiTi", font_size=30).set_color(YELLOW),
            Text("得根之和：", font="KaiTi", font_size=30)
        ).arrange(RIGHT, buff=0.1).next_to(eq_poly, DOWN, buff=0.5)
        self.play(Write(hint_8))

        eq_vieta_step1 = Tex(
            r"\sum_{k=1}^m \cot^2(\theta_k) = \frac{\binom{2m+1}{3}}{\binom{2m+1}{1}}"
        ).set_color(GREEN).scale(0.9).next_to(hint_8, DOWN, buff=0.3)
        self.play(Write(eq_vieta_step1))
        self.wait(1.5)

        eq_vieta_step2 = Tex(
            r"\sum_{k=1}^m \cot^2(\theta_k) = \frac{m(2m-1)}{3}"
        ).set_color(GREEN).scale(0.9).move_to(eq_vieta_step1)
        self.play(TransformMatchingTex(eq_vieta_step1, eq_vieta_step2))
        self.wait(2)

        # 清场
        self.play(FadeOut(VGroup(eq_sin_cot, eq_roots, eq_poly, hint_8)))
        self.play(eq_vieta_step2.animate.to_edge(UP, buff=0.6))

        # ==================== 场景三：几何放缩搭建桥梁 ====================
        hint_9 = Text("代数推导暂告段落，我们需要建立不等关系：", font="KaiTi", font_size=30).next_to(
            eq_vieta_step2, DOWN, buff=0.6)
        self.play(Write(hint_9))

        eq_ineq_1 = Tex(
            r"\sin x < x < \tan x \quad \Rightarrow \quad \sin^2 x < x^2 < \tan^2 x \quad \left( x \in \left(0, \frac{\pi}{2}\right) \right)"
        ).set_color(BLUE).scale(0.85).next_to(hint_9, DOWN, buff=0.4)
        self.play(Write(eq_ineq_1))
        self.wait(1.5)

        hint_10 = Text("取倒数导致不等号反向，并使用三角恒等式化简：", font="KaiTi", font_size=30).next_to(eq_ineq_1,
                                                                                                         DOWN, buff=0.5)
        self.play(Write(hint_10))

        eq_ineq_2 = Tex(
            r"\frac{1}{\sin^2 x} > \frac{1}{x^2} > \frac{1}{\tan^2 x} \quad \Rightarrow \quad 1 + \cot^2 x > \frac{1}{x^2} > \cot^2 x"
        ).set_color(BLUE).scale(0.85).next_to(hint_10, DOWN, buff=0.4)
        self.play(Write(eq_ineq_2))
        self.wait(1.5)

        # 【排版控制 4】：擦除上面的推导说明，把核心不等式向上提
        self.play(FadeOut(hint_9), FadeOut(hint_10), FadeOut(eq_ineq_1))
        self.play(eq_ineq_2.animate.next_to(eq_vieta_step2, DOWN, buff=0.5))

        eq_ineq_3 = Tex(
            r"\cot^2 x < \frac{1}{x^2} < 1 + \cot^2 x"
        ).set_color(YELLOW).scale(1.0).next_to(eq_ineq_2, DOWN, buff=0.4)
        self.play(Write(eq_ineq_3))
        self.wait(2)

        self.play(FadeOut(eq_ineq_2))
        self.play(eq_ineq_3.animate.next_to(eq_vieta_step2, DOWN, buff=0.6))

        # ==================== 场景四：夹逼定理与最终极限 ====================
        hint_11 = Text("将之前求出的根代入这个不等式，并进行累加：", font="KaiTi", font_size=30).next_to(eq_ineq_3, DOWN,
                                                                                                       buff=0.5)
        self.play(Write(hint_11))

        eq_sum_ineq = Tex(
            r"\sum_{k=1}^m \cot^2(\theta_k) < \sum_{k=1}^m \frac{(2m+1)^2}{k^2\pi^2} < m + \sum_{k=1}^m \cot^2(\theta_k)"
        ).set_color(BLUE).scale(0.8).next_to(hint_11, DOWN, buff=0.4)
        self.play(Write(eq_sum_ineq))
        self.wait(1.5)

        # 【排版控制 5】：抹去累加文本，公式上移
        self.play(FadeOut(hint_11))
        self.play(eq_sum_ineq.animate.next_to(eq_ineq_3, DOWN, buff=0.5))

        hint_12 = Text("代入顶部的引理结果，并孤立中间的平方倒数和：", font="KaiTi", font_size=30).next_to(eq_sum_ineq,
                                                                                                         DOWN, buff=0.5)
        self.play(Write(hint_12))

        # 【极其关键的修复】：彻底抛弃 Tex 内部切片，直接建立 3 个独立的物体拼装！
        part_left = Tex(r"\frac{m(2m-1)\pi^2}{3(2m+1)^2}").set_color(BLUE)
        part_mid = Tex(r" < \sum_{k=1}^m \frac{1}{k^2} < ").set_color(BLUE)
        part_right = Tex(r"\frac{m\pi^2}{(2m+1)^2} + \frac{m(2m-1)\pi^2}{3(2m+1)^2}").set_color(BLUE)

        # 用 VGroup 像积木一样把它们排在一起
        eq_final_ineq = VGroup(part_left, part_mid, part_right).arrange(RIGHT, buff=0.2).scale(0.8).next_to(hint_12,
                                                                                                            DOWN,
                                                                                                            buff=0.4)

        self.play(ReplacementTransform(eq_sum_ineq.copy(), eq_final_ineq))
        self.wait(2)

        # 最终推导：大清场，把终极不等式移到屏幕正中央
        self.play(FadeOut(VGroup(eq_vieta_step2, eq_ineq_3, eq_sum_ineq, hint_12)))
        self.play(eq_final_ineq.animate.move_to(ORIGIN))

        hint_13 = VGroup(
            Text("最后一步：让 ", font="KaiTi", font_size=35),
            Tex(r"m \to \infty", font_size=40).set_color(GREEN),
            Text("，观察两端多项式的极限。", font="KaiTi", font_size=35)
        ).arrange(RIGHT, buff=0.1).next_to(eq_final_ineq, UP, buff=0.8)
        self.play(Write(hint_13))
        self.wait(1)

        eq_limit_calc = Tex(
            r"\lim_{m\to\infty} \frac{2m^2\pi^2 - \dots}{12m^2 + \dots} = \frac{2\pi^2}{12} = \frac{\pi^2}{6}"
        ).set_color(GREEN).scale(0.9).next_to(eq_final_ineq, DOWN, buff=0.8)
        self.play(FadeIn(eq_limit_calc, shift=UP))
        self.wait(2)

        # 【极其关键的修复】：因为是独立物体，这里可以实现极其纯净的 ReplacementTransform
        limit_left = Tex(r"\frac{\pi^2}{6}").scale(1.2).set_color(GREEN).move_to(part_left)
        limit_right = Tex(r"\frac{\pi^2}{6}").scale(1.2).set_color(GREEN).move_to(part_right)

        self.play(
            ReplacementTransform(part_left, limit_left),
            ReplacementTransform(part_right, limit_right)
        )
        self.wait(1.5)

        final_eq = Tex(
            r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}"
        ).scale(1.5).set_color(YELLOW)

        # 将屏幕上剩下的 3 个积木直接转化为最终的巴塞尔等式
        self.play(
            FadeOut(hint_13),
            FadeOut(eq_limit_calc),
            ReplacementTransform(VGroup(limit_left, part_mid, limit_right), final_eq)
        )

        rect = SurroundingRectangle(final_eq, buff=0.4, color=YELLOW)
        self.play(Write(rect))
        self.play(
            final_eq.animate.set_color_by_gradient(BLUE, YELLOW, RED),
            rect.animate.set_color_by_gradient(BLUE, YELLOW, RED)
        )
        self.wait(4)

        # ==================== 尾声 ====================
        self.play(FadeOut(final_eq), FadeOut(rect))

        xiexie = Text("谢谢观看", font="KaiTi", font_size=100).set_color_by_gradient(BLUE, YELLOW, RED)

        self.play(Write(xiexie))
        self.wait(3)