from manimlib import *


class CauchyFactorialLimit(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("柯 西 定 理 求 解 阶 乘 极 限", font="KaiTi", font_size=80).shift(UP * 2)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW)

        integral = Tex(
            r"\lim_{n \to \infty} \frac{\sqrt[n]{n!}}{n} = ?",
            font_size=60
        ).shift(DOWN)
        integral.set_color_by_gradient(GREEN, BLUE, YELLOW)

        self.play(Write(title))
        self.play(Write(integral))
        self.wait(2)

        # 缩小并移至角落，腾出顶部中间位置
        self.play(
            title.animate.scale(0.45).to_corner(UL, buff=0.4),
            integral.animate.scale(0.55).to_corner(UR, buff=0.4),
        )
        self.wait(1)

        # ==================== 0. 定理引入并常驻 ====================
        hint_text0 = Text("回顾 Cauchy 第二极限定理：", font="KaiTi", font_size=35).set_color(
            BLUE).to_edge(DOWN, buff=0.8)
        self.play(Write(hint_text0))

        # 初始放在中央展示
        thm_eq = Tex(
            r"\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = A \implies \lim_{n \to \infty} \sqrt[n]{a_n} = A",
            font_size=45
        ).set_color(YELLOW)

        thm_box = SurroundingRectangle(thm_eq, color=YELLOW, buff=0.2, stroke_width=2)
        thm_group = VGroup(thm_eq, thm_box)

        self.play(FadeIn(thm_group, shift=UP))
        self.wait(2)

        # 核心改动：将定理移动到顶部中间，常驻显示
        self.play(
            thm_group.animate.scale(0.6).shift(UP * 2.3),
        )
        self.wait(1)

        # ==================== 1. 构造数列 ====================
        hint_text1 = VGroup(
            Text("构造数列 ", font="KaiTi", font_size=35),
            Tex(r"a_n", font_size=35),
            Text("，将分母放入根号内：", font="KaiTi", font_size=35)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)

        self.play(ReplacementTransform(hint_text0, hint_text1))

        eq1 = Tex(
            r"\frac{\sqrt[n]{n!}}{n}", r"=", r"\sqrt[n]{\frac{n!}{n^n}}"
        ).set_color(BLUE)
        self.play(Write(eq1))
        self.wait(2)

        eq2 = Tex(
            r"a_n", r"=", r"\frac{n!}{n^n}"
        ).set_color(BLUE)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(2)

        # ==================== 2. 列出比值 ====================
        hint_text2 = Text("计算相邻项的比值：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text1, hint_text2))

        # 将 an 移到侧边位置展示，不影响主推导区
        self.play(eq2.animate.scale(0.6).to_edge(LEFT, buff=0.5))

        eq4 = Tex(
            r"\frac{a_{n+1}}{a_n}", r"=", r"\frac{(n+1)!}{(n+1)^{n+1}}", r"\cdot", r"\frac{n^n}{n!}"
        ).set_color(BLUE)
        self.play(Write(eq4))
        self.wait(2)

        # ==================== 3. 展开与约分 ====================
        hint_text3 = Text("展开并约分：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text2, hint_text3))

        eq5 = Tex(
            r"\frac{a_{n+1}}{a_n}", r"=", r"\frac{(n+1) \cdot n!}{(n+1) \cdot (n+1)^n}", r"\cdot", r"\frac{n^n}{n!}"
        ).set_color(BLUE)
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait(1.5)

        self.play(
            eq5[2][0:5].animate.set_color(RED),
            eq5[2][6:8].animate.set_color(YELLOW),
            eq5[2][9:14].animate.set_color(RED),
            eq5[4][3:5].animate.set_color(YELLOW)
        )
        self.wait(1.5)

        eq7 = Tex(
            r"\frac{a_{n+1}}{a_n}", r"=", r"\frac{n^n}{(n+1)^n}"
        ).set_color(BLUE)
        self.play(TransformMatchingTex(eq5, eq7))
        self.wait(2)

        # ==================== 4. 凑重要极限 ====================
        hint_text5 = Text("倒写分式凑成重要极限：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text3, hint_text5))

        eq9 = Tex(
            r"\frac{a_{n+1}}{a_n}", r"=", r"\frac{1}{\Big( 1 + \frac{1}{n} \Big)^n}"
        ).set_color(BLUE)
        self.play(TransformMatchingTex(eq7, eq9))
        self.wait(2)

        # ==================== 5. 求极限 ====================
        hint_text6 = Text("求比值极限：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text5, hint_text6))

        eq11 = Tex(
            r"\lim_{n \to \infty} \frac{a_{n+1}}{a_n}", r"=", r"\frac{1}{e}"
        ).set_color(BLUE)
        self.play(TransformMatchingTex(eq9, eq11))
        self.wait(2)

        # ==================== 6. 得出结论 ====================
        # 此时引导观众看上方的常驻定理
        hint_text7 = Text("对照上方 Cauchy 定理，比值极限 = 根值极限：", font="KaiTi", font_size=35).set_color(
            YELLOW).to_edge(DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text6, hint_text7))

        # 定理闪烁提醒一下
        self.play(thm_box.animate.set_stroke(width=6), run_time=0.5)
        self.play(thm_box.animate.set_stroke(width=2), run_time=0.5)

        eq12 = Tex(
            r"\lim_{n \to \infty} \sqrt[n]{a_n}", r"=", r"\frac{1}{e}"
        ).set_color(BLUE)
        self.play(TransformMatchingTex(eq11, eq12))
        self.wait(2)

        # ==================== 终极完整展开 ====================
        self.play(FadeOut(hint_text7), FadeOut(eq2), FadeOut(thm_group))

        final_eq = Tex(
            r"\lim_{n \to \infty} \frac{\sqrt[n]{n!}}{n}",
            r"=",
            r"\frac{1}{e}"
        ).set_color(BLUE)

        self.play(
            TransformMatchingTex(
                eq12, final_eq,
                key_map={
                    r"\lim_{n \to \infty} \sqrt[n]{a_n}": r"\lim_{n \to \infty} \frac{\sqrt[n]{n!}}{n}"
                }
            )
        )
        self.wait(2)

        rect = SurroundingRectangle(final_eq, buff=0.25, color=YELLOW)
        self.play(Write(rect))

        self.play(
            final_eq.animate.scale(1.5).set_color_by_gradient(BLUE, YELLOW, RED),
            rect.animate.scale(1.5),
            FadeOut(integral),
            FadeOut(title)
        )
        self.wait(4)

        xiexie = Text("谢谢观看", font="KaiTi", font_size=120).set_color_by_gradient(BLUE, YELLOW, RED)
        self.play(
            ReplacementTransform(final_eq, xiexie),
            FadeOut(rect)
        )
        self.wait(3)