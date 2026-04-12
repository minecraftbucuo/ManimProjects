from manimlib import *


class FactorialRootLimit(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("化 连 乘 为 积 分 : 阶 乘 极 限", font="KaiTi", font_size=80)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW)

        integral = Tex(
            r"\lim_{n \to \infty} \frac{\sqrt[n]{n!}}{n} = ?",
            font_size=60
        )
        integral.set_color_by_gradient(GREEN, BLUE, YELLOW)

        cover = VGroup(title, integral).arrange(DOWN, buff=0.8)
        self.play(Write(title))
        self.play(Write(integral))
        self.wait(2)

        self.play(
            title.animate.scale(0.5).to_corner(UL),
            integral.animate.scale(0.6).to_corner(UR),
        )
        self.wait(1.5)

        # ==================== 1. 取对数 ====================

        hint_text1 = VGroup(
            Text("令 ", font="KaiTi", font_size=35),
            Tex(r"L", font_size=35),
            Text(" 为原极限，并对其两边取自然对数：", font="KaiTi", font_size=35)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)

        self.play(Write(hint_text1))

        # 【修复点】：使用 \Bigg( 和 \Bigg) 替代 \left( 和 \right)
        eq1 = Tex(
            r"\ln L", r"=", r"\lim_{n \to \infty}", r"\ln", r"\Bigg(", r"\frac{(n!)^{\frac{1}{n}}}{n}", r"\Bigg)"
        ).set_color(BLUE)

        self.play(Write(eq1))
        self.wait(2)

        # 【修复点】：使用 \Bigg[ 和 \Bigg] 替代 \left[ 和 \right]
        eq2 = Tex(
            r"\ln L", r"=", r"\lim_{n \to \infty}", r"\Bigg[", r"\frac{1}{n} \ln(n!)", r"-", r"\ln n", r"\Bigg]"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(2)

        # ==================== 2. 展开并整理 ====================

        hint_text2 = VGroup(
            Text("由于 ", font="KaiTi", font_size=35),
            Tex(r"\ln(n!) = \sum_{i=1}^n \ln i", font_size=35),
            Text("，代入并展开求和式：", font="KaiTi", font_size=35)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)

        self.play(ReplacementTransform(hint_text1, hint_text2))

        # 【修复点】：使用 \Bigg[ 和 \Bigg] 替代 \left[ 和 \right]
        eq3 = Tex(
            r"\ln L", r"=", r"\lim_{n \to \infty}", r"\Bigg[",
            r"\frac{1}{n} \sum_{i=1}^n \ln i", r"-", r"\frac{1}{n} \sum_{i=1}^n \ln n",
            r"\Bigg]"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(2)

        hint_text3 = Text("合并同类项，凑成标准形式：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN,
                                                                                                          buff=0.8)
        self.play(ReplacementTransform(hint_text2, hint_text3))

        # 【修复点】：使用 \Big( 和 \Big) 替代 \left( 和 \right)
        eq4 = Tex(
            r"\ln L", r"=", r"\lim_{n \to \infty}", r"\frac{1}{n}", r"\sum_{i=1}^n", r"\ln", r"\Big(", r"\frac{i}{n}",
            r"\Big)"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(2)

        # ==================== 3. 转化为定积分 ====================

        hint_text4 = VGroup(
            Text("识别为区间 ", font="KaiTi", font_size=35),
            Tex(r"[0, 1]", font_size=35),
            Text(" 上的黎曼和：", font="KaiTi", font_size=35)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)

        self.play(ReplacementTransform(hint_text3, hint_text4))

        eq5 = Tex(
            r"\ln L", r"=", r"\int_0^1", r"\ln x", r"\, dx"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq4, eq5))
        self.wait(2)

        # ==================== 4. 计算积分 ====================

        hint_text5 = Text("使用分部积分法计算定积分：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN,
                                                                                                           buff=0.8)
        self.play(ReplacementTransform(hint_text4, hint_text5))

        # 完美切分以避免渲染冲突
        eq6 = Tex(
            r"\ln L", r"=", r"\Big(", r"x \ln x", r"-", r"x", r"\Big)", r"\Big|_0^1"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq5, eq6))
        self.wait(2)

        eq7 = Tex(
            r"\ln L", r"=", r"\Big(", r"1 \cdot \ln 1 - 1", r"\Big)", r"-", r"\lim_{x \to 0^+}", r"(x \ln x - x)"
        ).set_color(BLUE).scale(0.9)

        self.play(TransformMatchingTex(eq6, eq7))
        self.wait(2)

        eq8 = Tex(
            r"\ln L", r"=", r"-1", r"-", r"0"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq7, eq8))
        self.wait(1.5)

        eq9 = Tex(
            r"\ln L", r"=", r"-1"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq8, eq9))
        self.wait(1.5)

        # ==================== 5. 得出结论 ====================

        hint_text6 = Text("还原对数，得出最终的极限值：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN,
                                                                                                            buff=0.8)
        self.play(ReplacementTransform(hint_text5, hint_text6))

        eq10 = Tex(
            r"L", r"=", r"e^{-1}", r"=", r"\frac{1}{e}"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq9, eq10))
        self.wait(2)

        # ==================== 终极完整展开 ====================
        self.play(FadeOut(hint_text6))

        final_eq = Tex(
            r"\lim_{n \to \infty} \frac{\sqrt[n]{n!}}{n}",
            r"=",
            r"\frac{1}{e}"
        ).set_color(BLUE)

        self.play(
            TransformMatchingTex(
                eq10, final_eq,
                key_map={
                    "L": r"\lim_{n \to \infty} \frac{\sqrt[n]{n!}}{n}"
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