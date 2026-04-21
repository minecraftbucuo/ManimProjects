from manimlib import *


class ClausenMosleyIdentity(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("如何求这个函数的傅里叶级数？", font="KaiTi", font_size=70)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW)

        identity = Tex(
            r"\ln(1 - 2\alpha \cos x + \alpha^2) \quad (|\alpha| < 1)",
            font_size=50
        )
        identity.set_color_by_gradient(GREEN, BLUE, YELLOW)

        cover = VGroup(title, identity).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(Write(identity))
        self.wait(2)

        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=180)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.move_to(ORIGIN)

            # 完美卡点：0.3出场 + 0.4停留 + 0.3退场 = 精准1秒钟
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(1)

        # 【修复 1】：直接淡出封面，把屏幕空间完全腾给推导过程，杜绝角落重叠
        self.play(FadeOut(cover))

        # ==================== 1. 观察真数项 ====================
        hint_text1 = VGroup(
            Text("观察对数真数，利用", font="KaiTi", font_size=35),
            Text("欧拉公式", font="KaiTi", font_size=35),
            Text("将其视为复数乘积", font="KaiTi", font_size=35)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)

        self.play(Write(hint_text1))

        eq1_1 = Tex(
            r"1 - 2\alpha \cos x + \alpha^2"
        ).set_color(BLUE)

        self.play(Write(eq1_1))
        self.wait(1.5)

        eq1_2 = Tex(
            r"1 - \alpha ", r"\Big(", r"2\cos x", r"\Big)", r" + \alpha^2"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq1_1, eq1_2))
        self.wait(1.5)

        eq1_3 = Tex(
            r"1 - \alpha ", r"\Big(", r"e^{ix} + e^{-ix}", r"\Big)", r" + \alpha^2"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq1_2, eq1_3))
        self.wait(1.5)

        eq1_4 = Tex(
            r"1 - \alpha e^{ix} - \alpha e^{-ix} + \alpha^2 e^{ix} e^{-ix}"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq1_3, eq1_4))
        self.wait(1.5)

        eq1_5 = Tex(
            r"(1 - \alpha e^{ix})", r"(1 - \alpha e^{-ix})"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq1_4, eq1_5))
        self.wait(2)

        # 整理第一步的结果放上去暂存
        step1_result = Tex(r"1 - 2\alpha \cos x + \alpha^2", r"=",
                           r"(1 - \alpha e^{ix})(1 - \alpha e^{-ix})").set_color(BLUE).scale(0.8).to_edge(UP, buff=0.8)
        self.play(Transform(eq1_5, step1_result))

        # ==================== 2. 取对数 ====================
        hint_text2 = Text("代回原式，并利用对数性质拆解", font="KaiTi", font_size=35).set_color(BLUE).to_edge(
            DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text1, hint_text2))

        eq2_1 = Tex(
            r"\ln", r"\Big(", r"1 - 2\alpha \cos x + \alpha^2", r"\Big)"
        ).set_color(BLUE)

        self.play(Write(eq2_1))
        self.wait(1.5)

        eq2_2 = Tex(
            r"\ln", r"\Big[", r"(1 - \alpha e^{ix})", r"(1 - \alpha e^{-ix})", r"\Big]"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq2_1, eq2_2))
        self.wait(1.5)

        eq2_3 = Tex(
            r"\ln", r"(1 - \alpha e^{ix})", r"+", r"\ln", r"(1 - \alpha e^{-ix})"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq2_2, eq2_3))
        self.wait(2)

        self.play(eq2_3.animate.scale(0.8).next_to(step1_result, DOWN, buff=0.4))

        # ==================== 3. 泰勒级数展开 ====================
        hint_text3 = VGroup(
            Text("利用泰勒展开 ", font="KaiTi", font_size=35),
            Tex(r"\ln(1-u) = -\sum \frac{u^n}{n}", font_size=35)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)

        self.play(ReplacementTransform(hint_text2, hint_text3))

        eq3_1 = Tex(
            r"\ln", r"(1 - \alpha e^{ix})", r"=", r"-\sum_{n=1}^{\infty}", r"\frac{(\alpha e^{ix})^n}{n}", r"=",
            r"-\sum_{n=1}^{\infty}", r"\frac{\alpha^n}{n}", r"e^{inx}"
        ).set_color(BLUE).scale(0.85)

        eq3_2 = Tex(
            r"\ln", r"(1 - \alpha e^{-ix})", r"=", r"-\sum_{n=1}^{\infty}", r"\frac{(\alpha e^{-ix})^n}{n}", r"=",
            r"-\sum_{n=1}^{\infty}", r"\frac{\alpha^n}{n}", r"e^{-inx}"
        ).set_color(BLUE).scale(0.85)

        VGroup(eq3_1, eq3_2).arrange(DOWN, buff=0.5).move_to(ORIGIN).shift(DOWN * 0.2)

        self.play(Write(eq3_1))
        self.wait(1.5)
        self.play(Write(eq3_2))
        self.wait(2)

        # 清除上方暂存，准备合并
        self.play(FadeOut(step1_result), FadeOut(eq2_3), FadeOut(eq1_5))
        self.play(VGroup(eq3_1, eq3_2).animate.to_edge(UP, buff=1.0))

        # ==================== 4. 合并两项 ====================
        hint_text4 = Text("两项相加(记原式为S)，提取公因式", font="KaiTi", font_size=35).set_color(BLUE).to_edge(
            DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text3, hint_text4))

        eq4_1 = Tex(
            r"S", r"=", r"\Big(", r"-\sum_{n=1}^{\infty} \frac{\alpha^n}{n} e^{inx}", r"\Big)", r"+", r"\Big(",
            r"-\sum_{n=1}^{\infty} \frac{\alpha^n}{n} e^{-inx}", r"\Big)"
        ).set_color(BLUE).scale(0.85)
        eq4_1.next_to(eq3_2, DOWN, buff=0.8)

        self.play(Write(eq4_1))
        self.wait(1.5)

        self.play(FadeOut(eq3_1), FadeOut(eq3_2))
        self.play(eq4_1.animate.move_to(ORIGIN))

        eq4_2 = Tex(
            r"S", r"=", r"-\sum_{n=1}^{\infty} \frac{\alpha^n}{n}", r"\Big(", r"e^{inx} + e^{-inx}", r"\Big)"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq4_1, eq4_2))
        self.wait(1.5)

        eq4_3 = Tex(
            r"S", r"=", r"-\sum_{n=1}^{\infty} \frac{\alpha^n}{n}", r"\Big(", r"2\cos(nx)", r"\Big)"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq4_2, eq4_3))
        self.wait(1.5)

        eq4_4 = Tex(
            r"S", r"=", r"-2 \sum_{n=1}^{\infty} \frac{\alpha^n}{n} \cos(nx)"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq4_3, eq4_4))
        self.wait(2)

        # ==================== 5. 结论与终极展示 ====================
        self.play(FadeOut(hint_text4))

        final_eq = Tex(
            r"\ln(1 - 2\alpha \cos x + \alpha^2)",
            r"=",
            r"-2 \sum_{n=1}^{\infty} \frac{\alpha^n}{n} \cos(nx)"
        ).set_color(BLUE)

        self.play(
            TransformMatchingTex(
                eq4_4, final_eq,
                key_map={
                    r"S": r"\ln(1 - 2\alpha \cos x + \alpha^2)"
                }
            )
        )
        self.wait(2)

        rect = SurroundingRectangle(final_eq, buff=0.3, color=YELLOW)
        self.play(Write(rect))

        self.play(
            final_eq.animate.scale(1.3).set_color_by_gradient(BLUE, YELLOW, RED),
            rect.animate.scale(1.3)
        )
        self.wait(4)

        # 【修复 2】：使用强制 FadeOut 确保残留公式消失，然后再淡入“谢谢观看”
        self.play(
            FadeOut(final_eq),
            FadeOut(rect)
        )

        xiexie = Text("谢谢观看", font="KaiTi", font_size=100).set_color_by_gradient(BLUE, YELLOW, RED)
        self.play(Write(xiexie))
        self.wait(3)