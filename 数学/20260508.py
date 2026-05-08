from manim import *


class StructureMappingProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("如何求解此类复合结构函数方程？", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"f\left(x + \frac{1}{x}\right) = x^3 + \frac{1}{x^3}",
            font_size=60
        ).set_color(BLUE)

        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))
        # ==================== 3秒倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=180)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.move_to(ORIGIN)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：观察与代数恒等式 ====================
        desc_1 = Text("首先观察等式两边的结构特征：", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_orig = MathTex(r"f\left(x + \frac{1}{x}\right) = x^3 + \frac{1}{x^3}").set_color(BLUE).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(eq_orig))
        self.wait(1.5)

        desc_2_text = Text("输入端与输出端存在代数恒等式联系，即完全立方公式：", font="KaiTi", font_size=28)
        desc_2_math = MathTex(r"(a+b)^3 = a^3 + b^3 + 3ab(a+b)", font_size=30).set_color(YELLOW)
        desc_2 = VGroup(desc_2_text, desc_2_math).arrange(DOWN, buff=0.2).next_to(eq_orig, DOWN, buff=0.5)
        self.play(Write(desc_2_text))
        self.play(Write(desc_2_math))
        self.wait(1)

        desc_3 = Text("将其代入本题的结构：", font="KaiTi", font_size=28).next_to(desc_2, DOWN, buff=0.5)
        self.play(Write(desc_3))

        eq_expand = MathTex(r"\left(x + \frac{1}{x}\right)^3 = x^3 + \frac{1}{x^3} + 3\left(x + \frac{1}{x}\right)")
        eq_expand.set_color_by_tex(r"x^3 + \frac{1}{x^3}", BLUE)
        eq_expand.next_to(desc_3, DOWN, buff=0.3)
        self.play(Write(eq_expand))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(desc_1), FadeOut(eq_orig), FadeOut(desc_2), FadeOut(desc_3)
        )
        self.play(eq_expand.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：换元与核心求解 ====================
        desc_4_text1 = Text("此时引入换元法，令", font="KaiTi", font_size=30)
        desc_4_math1 = MathTex(r"t = x + \frac{1}{x}", font_size=32).set_color(YELLOW)
        desc_4 = VGroup(desc_4_text1, desc_4_math1).arrange(RIGHT, buff=0.1).next_to(eq_expand, DOWN, buff=0.6)
        self.play(Write(desc_4))

        desc_5 = Text("原恒等式可改写为：", font="KaiTi", font_size=28).next_to(desc_4, DOWN, buff=0.5)
        self.play(Write(desc_5))

        eq_sub = MathTex(r"t^3 = f(t) + 3t").set_color(GREEN).next_to(desc_5, DOWN, buff=0.4)
        self.play(ReplacementTransform(eq_expand.copy(), eq_sub))
        self.wait(1)

        desc_6 = Text("将目标函数孤立，移项得到：", font="KaiTi", font_size=28).next_to(eq_sub, DOWN, buff=0.5)
        self.play(Write(desc_6))

        eq_solve = MathTex(r"f(t) = t^3 - 3t").set_color(GREEN).scale(1.1).next_to(desc_6, DOWN, buff=0.3)
        self.play(TransformMatchingTex(eq_sub.copy(), eq_solve))

        rect_solve = SurroundingRectangle(eq_solve, color=GREEN, buff=0.15)
        self.play(Create(rect_solve))
        self.wait(2)

        # 再次整理屏幕
        self.play(
            FadeOut(desc_4), FadeOut(desc_5), FadeOut(eq_sub), FadeOut(desc_6)
        )
        solve_group = VGroup(eq_solve, rect_solve)
        self.play(solve_group.animate.next_to(eq_expand, DOWN, buff=0.5))

        # ==================== 第三幕：还原函数与定义域 ====================
        desc_7_text1 = Text("将自变量", font="KaiTi", font_size=28)
        desc_7_math1 = MathTex(r"t", font_size=30).set_color(YELLOW)
        desc_7_text2 = Text("还原为", font="KaiTi", font_size=28)
        desc_7_math2 = MathTex(r"x", font_size=30).set_color(YELLOW)
        desc_7 = VGroup(desc_7_text1, desc_7_math1, desc_7_text2, desc_7_math2).arrange(RIGHT, buff=0.1).next_to(solve_group, DOWN, buff=0.6)
        self.play(Write(desc_7))

        eq_restore = MathTex(r"f(x) = x^3 - 3x").set_color(BLUE).next_to(desc_7, DOWN, buff=0.4)
        self.play(Write(eq_restore))
        self.wait(1.5)

        desc_8 = Text("同时需确定定义域，由基本不等式：", font="KaiTi", font_size=28).next_to(eq_restore, DOWN, buff=0.5)
        self.play(Write(desc_8))

        eq_domain_cond = MathTex(r"\left| x + \frac{1}{x} \right| \ge 2 \implies |t| \ge 2").set_color(YELLOW).next_to(desc_8, DOWN, buff=0.3)
        self.play(Write(eq_domain_cond))
        self.wait(2)

        # 全屏清场
        self.play(
            FadeOut(eq_expand), FadeOut(solve_group), FadeOut(desc_7), FadeOut(eq_restore), FadeOut(desc_8), FadeOut(eq_domain_cond)
        )

        desc_9 = Text("综合解析式与定义域，得到最终结果：", font="KaiTi", font_size=35).to_edge(UP, buff=1.5)
        self.play(Write(desc_9))

        final_ans = MathTex(r"f(x) = x^3 - 3x \quad (|x| \ge 2)").scale(1.2).set_color(YELLOW).move_to(ORIGIN)
        self.play(FadeIn(final_ans, shift=UP))
        self.wait(3)

        # ==================== 第四幕：举一反三 ====================
        # 全屏清空
        self.play(
            FadeOut(desc_9), FadeOut(final_ans)
        )

        desc_10 = Text("此方法可推广至同类结构，例如：", font="KaiTi", font_size=35).to_edge(UP, buff=1.5)
        self.play(Write(desc_10))

        desc_11_text = Text("已知", font="KaiTi", font_size=30)
        desc_11_math = MathTex(r"f\left(x + \frac{1}{x}\right) = x^2 + \frac{1}{x^2}", font_size=36).set_color(BLUE)
        desc_11 = VGroup(desc_11_text, desc_11_math).arrange(RIGHT, buff=0.1).next_to(desc_10, DOWN, buff=0.8)
        self.play(Write(desc_11))
        self.wait(1)

        desc_12_text = Text("利用完全平方公式", font="KaiTi", font_size=28)
        desc_12_math = MathTex(r"(a+b)^2 = a^2 + b^2 + 2ab", font_size=28).set_color(YELLOW)
        desc_12 = VGroup(desc_12_text, desc_12_math).arrange(RIGHT, buff=0.1).next_to(desc_11, DOWN, buff=0.5)
        self.play(Write(desc_12))
        self.wait(1)

        desc_13_text = Text("同理可得：", font="KaiTi", font_size=30)
        desc_13_math = MathTex(r"f(x) = x^2 - 2 \quad (|x| \ge 2)", font_size=36).set_color(GREEN)
        desc_13 = VGroup(desc_13_text, desc_13_math).arrange(RIGHT, buff=0.1).next_to(desc_12, DOWN, buff=0.5)
        self.play(Write(desc_13))
        self.wait(2)

        # 清场准备总结
        self.play(
            FadeOut(desc_10), FadeOut(desc_11), FadeOut(desc_12), FadeOut(desc_13)
        )

        outro_1 = Text("核心思想在于：", font="KaiTi", font_size=40).to_edge(UP, buff=2)
        self.play(Write(outro_1))
        self.wait(1)

        outro_2_text1 = Text("不直接求解", font="KaiTi", font_size=35)
        outro_2_math1 = MathTex(r"x", font_size=35).set_color(YELLOW)
        outro_2_text2 = Text("，而是利用恒等式建立结构映射", font="KaiTi", font_size=35)
        outro_2 = VGroup(outro_2_text1, outro_2_math1, outro_2_text2).arrange(RIGHT, buff=0.1).next_to(outro_1, DOWN, buff=0.8)
        self.play(Write(outro_2))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)