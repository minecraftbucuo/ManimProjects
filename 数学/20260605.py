from manim import *

class ExtremumMultiPerspective(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("条件极值问题的多维视角", font="KaiTi", font_size=45)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cond = VGroup(
            Text("已知", font="KaiTi", font_size=30),
            MathTex(r"x, y > 0", font_size=35).set_color(YELLOW),
            Text("且", font="KaiTi", font_size=30),
            MathTex(r"x^3 + y^3 = 2", font_size=35).set_color(YELLOW)
        ).arrange(RIGHT, buff=0.2)

        eq_target = VGroup(
            Text("求", font="KaiTi", font_size=30),
            MathTex(r"x+y", font_size=35).set_color(BLUE),
            Text("的最大值", font="KaiTi", font_size=30)
        ).arrange(RIGHT, buff=0.2)

        cover = VGroup(title, eq_cond, eq_target).arrange(DOWN, buff=0.8)
        
        self.play(Write(title))
        self.play(FadeIn(eq_cond, shift=UP))
        self.play(FadeIn(eq_target, shift=UP))
        self.wait(1.5)

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

        # ==================== 第一幕：代数视角 (对称多项式) ====================
        act1_title = Text("视角一：代数视角的降维", font="KaiTi", font_size=35).to_edge(UP, buff=0.8)
        self.play(Write(act1_title))

        desc_1 = VGroup(
            Text("对于对称式，引入基本对称多项式：令", font="KaiTi", font_size=28),
            MathTex(r"s = x+y", font_size=30).set_color(BLUE),
            Text("，", font="KaiTi", font_size=28),
            MathTex(r"p = xy", font_size=30).set_color(BLUE)
        ).arrange(RIGHT, buff=0.1).next_to(act1_title, DOWN, buff=0.6)
        self.play(Write(desc_1))

        desc_2 = Text("对原方程进行因式分解与代换：", font="KaiTi", font_size=28).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(desc_2))

        eq_alg_1 = MathTex(r"x^3 + y^3 = (x+y)[(x+y)^2 - 3xy]").next_to(desc_2, DOWN, buff=0.3)
        eq_alg_2 = MathTex(r"s(s^2 - 3p) = 2").set_color(YELLOW).next_to(eq_alg_1, DOWN, buff=0.3)
        self.play(Write(eq_alg_1))
        self.play(Write(eq_alg_2))
        self.wait(2)

        # 整理屏幕 1
        self.play(FadeOut(desc_1), FadeOut(desc_2), FadeOut(eq_alg_1))
        self.play(eq_alg_2.animate.next_to(act1_title, DOWN, buff=0.5))

        desc_3 = VGroup(
            Text("为了求", font="KaiTi", font_size=28),
            MathTex(r"s", font_size=30).set_color(BLUE),
            Text("的最值，从上式解出", font="KaiTi", font_size=28),
            MathTex(r"p", font_size=30).set_color(BLUE),
            Text("：", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1).next_to(eq_alg_2, DOWN, buff=0.5)
        self.play(Write(desc_3))

        eq_alg_3 = MathTex(r"p = \frac{s^3 - 2}{3s}").set_color(YELLOW).next_to(desc_3, DOWN, buff=0.3)
        self.play(Write(eq_alg_3))
        self.wait(1.5)

        desc_4 = VGroup(
            Text("根据完全平方式非负性质", font="KaiTi", font_size=28),
            MathTex(r"(x-y)^2 \ge 0", font_size=30).set_color(GREEN),
            Text("可得基本不等式：", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1).next_to(eq_alg_3, DOWN, buff=0.5)
        self.play(Write(desc_4))

        eq_alg_4 = MathTex(r"s^2 \ge 4p").set_color(GREEN).next_to(desc_4, DOWN, buff=0.3)
        self.play(Write(eq_alg_4))
        self.wait(2)

        # 整理屏幕 2 (修复越界问题：将两个公式横向排列以节省垂直空间)
        self.play(FadeOut(eq_alg_2), FadeOut(desc_3), FadeOut(desc_4))
        kept_group = VGroup(eq_alg_3, eq_alg_4).arrange(RIGHT, buff=1.5)
        self.play(kept_group.animate.next_to(act1_title, DOWN, buff=0.6))

        desc_5 = VGroup(
            Text("将", font="KaiTi", font_size=28),
            MathTex(r"p", font_size=30).set_color(BLUE),
            Text("代入不等式中，转化为关于", font="KaiTi", font_size=28),
            MathTex(r"s", font_size=30).set_color(BLUE),
            Text("的一元不等式：", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1).next_to(kept_group, DOWN, buff=0.6)
        self.play(Write(desc_5))

        eq_alg_5 = MathTex(r"s^2 \ge 4 \left( \frac{s^3 - 2}{3s} \right)").next_to(desc_5, DOWN, buff=0.4)
        self.play(Write(eq_alg_5))
        self.wait(1.5)

        # 整理屏幕 3 (再次腾出空间给最终计算)
        self.play(FadeOut(kept_group), FadeOut(desc_5))
        self.play(eq_alg_5.animate.next_to(act1_title, DOWN, buff=0.6))

        desc_6 = VGroup(
            Text("因为", font="KaiTi", font_size=28),
            MathTex(r"s > 0", font_size=30).set_color(BLUE),
            Text("，两边同乘", font="KaiTi", font_size=28),
            MathTex(r"3s", font_size=30).set_color(BLUE),
            Text("并化简：", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1).next_to(eq_alg_5, DOWN, buff=0.6)
        self.play(Write(desc_6))

        eq_alg_6 = MathTex(r"3s^3 \ge 4s^3 - 8 \implies s^3 \le 8 \implies s \le 2").set_color(YELLOW).next_to(desc_6, DOWN, buff=0.5)
        self.play(Write(eq_alg_6))
        self.wait(2.5)

        # 全屏清场，准备第二幕
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 第二幕：分析视角 (凸函数) ====================
        act2_title = Text("视角二：分析视角的凸凹性", font="KaiTi", font_size=35).to_edge(UP, buff=0.8)
        self.play(Write(act2_title))

        desc_7 = VGroup(
            Text("构造函数", font="KaiTi", font_size=28),
            MathTex(r"f(t) = t^3 \quad (t > 0)", font_size=30).set_color(BLUE)
        ).arrange(RIGHT, buff=0.1).next_to(act2_title, DOWN, buff=0.6)
        self.play(Write(desc_7))

        desc_8 = VGroup(
            Text("求二阶导数知", font="KaiTi", font_size=28),
            MathTex(r"f''(t) = 6t > 0", font_size=30).set_color(GREEN),
            Text("，故该函数为严格下凸函数。", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1).next_to(desc_7, DOWN, buff=0.5)
        self.play(Write(desc_8))
        self.wait(1.5)

        desc_9 = Text("根据琴生不等式 (Jensen's Inequality) 的性质：", font="KaiTi", font_size=28).next_to(desc_8, DOWN, buff=0.6)
        self.play(Write(desc_9))

        eq_calc_1 = MathTex(r"\frac{f(x) + f(y)}{2} \ge f\left(\frac{x+y}{2}\right)").set_color(YELLOW).next_to(desc_9, DOWN, buff=0.3)
        self.play(Write(eq_calc_1))
        self.wait(2)

        # 整理屏幕 4 (防止第二幕越界)
        self.play(FadeOut(desc_7), FadeOut(desc_8), FadeOut(desc_9))
        self.play(eq_calc_1.animate.next_to(act2_title, DOWN, buff=0.5))

        desc_10 = VGroup(
            Text("将", font="KaiTi", font_size=28),
            MathTex(r"f(t) = t^3", font_size=30).set_color(BLUE),
            Text("代入不等式中：", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1).next_to(eq_calc_1, DOWN, buff=0.5)
        self.play(Write(desc_10))

        eq_calc_2 = MathTex(r"\frac{x^3 + y^3}{2} \ge \left(\frac{x+y}{2}\right)^3").next_to(desc_10, DOWN, buff=0.3)
        self.play(Write(eq_calc_2))
        self.wait(1)

        desc_11 = VGroup(
            Text("代入已知条件", font="KaiTi", font_size=28),
            MathTex(r"x^3 + y^3 = 2", font_size=30).set_color(GREEN),
            Text("：", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1).next_to(eq_calc_2, DOWN, buff=0.5)
        self.play(Write(desc_11))

        eq_calc_3 = MathTex(r"\frac{2}{2} \ge \frac{(x+y)^3}{8} \implies (x+y)^3 \le 8").set_color(YELLOW).next_to(desc_11, DOWN, buff=0.3)
        self.play(Write(eq_calc_3))
        self.wait(1.5)
        
        # 整理屏幕 5 (突出最终结果)
        self.play(FadeOut(desc_10), FadeOut(eq_calc_2), FadeOut(desc_11))
        self.play(eq_calc_3.animate.next_to(eq_calc_1, DOWN, buff=0.8))

        eq_calc_4 = MathTex(r"x+y \le 2").scale(1.2).set_color(RED).next_to(eq_calc_3, DOWN, buff=0.6)
        self.play(TransformMatchingTex(eq_calc_3.copy(), eq_calc_4))
        self.wait(2.5)

        # 全屏清场，准备第三幕
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 第三幕：本质推广 (幂平均不等式) ====================
        act3_title = Text("举一反三：通用的幂平均不等式", font="KaiTi", font_size=35).to_edge(UP, buff=0.8)
        self.play(Write(act3_title))

        desc_12 = VGroup(
            Text("定义正实数", font="KaiTi", font_size=28),
            MathTex(r"x, y", font_size=30).set_color(BLUE),
            Text("的", font="KaiTi", font_size=28),
            MathTex(r"p", font_size=30).set_color(BLUE),
            Text("阶幂平均数为：", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1).next_to(act3_title, DOWN, buff=0.6)
        self.play(Write(desc_12))

        eq_mean_1 = MathTex(r"M_p = \left( \frac{x^p + y^p}{2} \right)^{\frac{1}{p}}").set_color(YELLOW).next_to(desc_12, DOWN, buff=0.4)
        self.play(Write(eq_mean_1))
        self.wait(1.5)

        desc_13 = VGroup(
            Text("核心定理：当", font="KaiTi", font_size=28),
            MathTex(r"p > q", font_size=30).set_color(GREEN),
            Text("时，总有", font="KaiTi", font_size=28),
            MathTex(r"M_p \ge M_q", font_size=30).set_color(GREEN),
            Text("。", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1).next_to(eq_mean_1, DOWN, buff=0.5)
        self.play(Write(desc_13))
        self.wait(1.5)

        # 整理屏幕 6
        self.play(FadeOut(desc_12), FadeOut(desc_13))
        self.play(eq_mean_1.animate.next_to(act3_title, DOWN, buff=0.5))

        desc_14 = VGroup(
            Text("回到原题，由", font="KaiTi", font_size=28),
            MathTex(r"3 > 1", font_size=30).set_color(GREEN),
            Text("，直接运用", font="KaiTi", font_size=28),
            MathTex(r"M_3 \ge M_1", font_size=30).set_color(GREEN),
            Text("：", font="KaiTi", font_size=28)
        ).arrange(RIGHT, buff=0.1).next_to(eq_mean_1, DOWN, buff=0.6)
        self.play(Write(desc_14))

        eq_mean_2 = MathTex(r"\left(\frac{x^3+y^3}{2}\right)^{\frac{1}{3}} \ge \frac{x+y}{2}").next_to(desc_14, DOWN, buff=0.4)
        self.play(Write(eq_mean_2))
        self.wait(1)

        eq_mean_3 = MathTex(r"\left(\frac{2}{2}\right)^{\frac{1}{3}} \ge \frac{x+y}{2} \implies 1 \ge \frac{x+y}{2}").set_color(YELLOW).next_to(eq_mean_2, DOWN, buff=0.4)
        self.play(Write(eq_mean_3))
        self.wait(1.5)
        
        # 整理屏幕 7 (收尾特写)
        self.play(FadeOut(desc_14), FadeOut(eq_mean_2))
        self.play(eq_mean_3.animate.next_to(eq_mean_1, DOWN, buff=0.8))

        eq_final = MathTex(r"x+y \le 2").scale(1.2).set_color(RED).next_to(eq_mean_3, DOWN, buff=0.6)
        self.play(TransformMatchingTex(eq_mean_3.copy(), eq_final))
        self.wait(3)

        # ==================== 散场 ====================
        self.play(*[FadeOut(m) for m in self.mobjects])
        
        outro = Text("看透数学本质，方能举一反三", font="KaiTi", font_size=45).set_color(BLUE)
        self.play(Write(outro))
        self.wait(2)
        self.play(FadeOut(outro))
        self.wait(1)