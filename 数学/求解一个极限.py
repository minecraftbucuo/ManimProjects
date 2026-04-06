from manimlib import *


class RiemannSumLimit(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("经 典 极 限 ： 黎 曼 和 误 差", font="KaiTi", font_size=80)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW)

        integral = Tex(
            r"\lim_{n \to \infty} n \left( \frac{\pi}{4} - \sum_{i=1}^{n} \frac{n}{n^2 + i^2} \right) = ?",
            font_size=50
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

        # ==================== 1. 构造函数与定积分 ====================

        eq1 = Tex(
            r"L", r"=", r"\lim_{n \to \infty}", r"n", r"\Bigg(", r"\frac{\pi}{4}", r"-",
            r"\sum_{i=1}^{n} \frac{n}{n^2 + i^2}", r"\Bigg)"
        ).set_color(BLUE)

        self.play(Write(eq1))
        self.wait(2)

        eq2 = Tex(
            r"L", r"=", r"\lim_{n \to \infty}", r"n", r"\Bigg(", r"\frac{\pi}{4}", r"-",
            r"\frac{1}{n}\sum_{i=1}^{n} \frac{1}{1 + (\frac{i}{n})^2}", r"\Bigg)"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(2)

        # 【修复点】：Text 和 Tex 组合，公式渲染为原生 LaTeX
        hint_text = VGroup(
            Text("令 ", font="KaiTi", font_size=35),
            Tex(r"f(x) = \frac{1}{1+x^2}", font_size=35),
            Text("，将各项化为积分与黎曼和：", font="KaiTi", font_size=35)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)

        self.play(Write(hint_text))
        self.wait(1.5)

        eq3 = Tex(
            r"L", r"=", r"\lim_{n \to \infty}", r"n", r"\Bigg(", r"\int_0^1 f(x) dx", r"-",
            r"\frac{1}{n}\sum_{i=1}^{n} f\left(\frac{i}{n}\right)", r"\Bigg)"
        ).set_color(BLUE)

        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(3)

        # 【修复点】：文字混排公式
        hint_text2 = VGroup(
            Text("引入 ", font="KaiTi", font_size=35),
            Tex(r"F(x) = \int_0^x f(t) dt", font_size=35),
            Text("，将误差拆分到每个小区间：", font="KaiTi", font_size=35)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)

        eq4 = Tex(
            r"L", r"=", r"\lim_{n \to \infty}", r"n", r"\sum_{i=1}^{n}", r"\Bigg[",
            r"\left( F\left(\frac{i}{n}\right) - F\left(\frac{i-1}{n}\right) \right)", r"-",
            r"\frac{1}{n} f\left(\frac{i}{n}\right)", r"\Bigg]"
        ).set_color(BLUE).scale(0.9)

        self.play(
            ReplacementTransform(hint_text, hint_text2),
            TransformMatchingTex(eq3, eq4)
        )
        self.wait(3)

        # ==================== 2. 利用泰勒公式分析区间误差 ====================

        self.play(eq4.animate.shift(UP * 1.5))

        # 【修复点】：文字混排公式
        hint_text3 = VGroup(
            Text("对 ", font="KaiTi", font_size=35),
            Tex(r"F\left(\frac{i-1}{n}\right)", font_size=35),
            Text(" 在 ", font="KaiTi", font_size=35),
            Tex(r"\frac{i}{n}", font_size=35),
            Text(" 处进行泰勒展开 (步长 ", font="KaiTi", font_size=35),
            Tex(r"-\frac{1}{n}", font_size=35),
            Text(")：", font="KaiTi", font_size=35)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)

        self.play(ReplacementTransform(hint_text2, hint_text3))

        taylor_eq = Tex(
            r"F\left(\frac{i-1}{n}\right)", r"=", r"F\left(\frac{i}{n}\right)", r"-",
            r"\frac{1}{n} f\left(\frac{i}{n}\right)", r"+", r"\frac{1}{2n^2} f'\left(\frac{i}{n}\right)", r"-",
            r"\frac{1}{6n^3} f''(\theta_i)"
        ).set_color(BLUE).scale(0.8).shift(DOWN * 0.5)

        self.play(Write(taylor_eq))
        self.wait(3)

        hint_text4 = Text("移项整理，得到每个小区间上的精确误差：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(
            DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text3, hint_text4))

        error_eq = Tex(
            r"F\left(\frac{i}{n}\right)", r"-", r"F\left(\frac{i-1}{n}\right)", r"-",
            r"\frac{1}{n} f\left(\frac{i}{n}\right)", r"=", r"-\frac{1}{2n^2} f'\left(\frac{i}{n}\right)", r"+",
            r"\frac{1}{6n^3} f''(\theta_i)"
        ).set_color(BLUE).scale(0.8).shift(DOWN * 0.5)

        self.play(TransformMatchingTex(taylor_eq, error_eq))
        self.wait(3)

        # ==================== 3. 求和并计算极限 ====================

        # 【修复点】：文字混排公式
        hint_text5 = VGroup(
            Text("代回原极限 ", font="KaiTi", font_size=35),
            Tex(r"L", font_size=35),
            Text(" 的求和式中：", font="KaiTi", font_size=35)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)

        self.play(ReplacementTransform(hint_text4, hint_text5))

        eq5 = Tex(
            r"L", r"=", r"\lim_{n \to \infty}", r"n", r"\sum_{i=1}^{n}", r"\Bigg[",
            r"-\frac{1}{2n^2} f'\left(\frac{i}{n}\right)", r"+", r"\frac{1}{6n^3} f''(\theta_i)", r"\Bigg]"
        ).set_color(BLUE).scale(0.9).move_to(ORIGIN)

        self.play(
            ReplacementTransform(VGroup(eq4, error_eq), eq5)
        )
        self.wait(3)

        # 【修复点】：文字混排公式
        hint_text6 = VGroup(
            Text("将外侧的 ", font="KaiTi", font_size=35),
            Tex(r"n", font_size=35),
            Text(" 乘入括号：", font="KaiTi", font_size=35)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)

        self.play(ReplacementTransform(hint_text5, hint_text6))

        eq6 = Tex(
            r"L", r"=", r"\lim_{n \to \infty}", r"\Bigg[", r"-\frac{1}{2n} \sum_{i=1}^{n} f'\left(\frac{i}{n}\right)",
            r"+", r"\frac{1}{6n^2} \sum_{i=1}^{n} f''(\theta_i)", r"\Bigg]"
        ).set_color(BLUE).scale(0.9)

        self.play(TransformMatchingTex(eq5, eq6))
        self.wait(2.5)

        # 【修复点】：文字混排公式，完美夹逼定理渲染
        hint_text7 = VGroup(
            Text("二阶导数 ", font="KaiTi", font_size=35),
            Tex(r"f''(x)", font_size=35),
            Text(" 有界，由夹逼定理可知：", font="KaiTi", font_size=35),
            Tex(r"\lim_{n \to \infty} \frac{1}{6n^2} \sum_{i=1}^{n} f''(\theta_i) = 0", font_size=35)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)

        self.play(ReplacementTransform(hint_text6, hint_text7))
        self.wait(3)

        eq7 = Tex(
            r"L", r"=", r"\lim_{n \to \infty}", r"\Bigg[", r"-\frac{1}{2n} \sum_{i=1}^{n} f'\left(\frac{i}{n}\right)",
            r"\Bigg]"
        ).set_color(BLUE).scale(0.9)

        self.play(TransformMatchingTex(eq6, eq7))
        self.wait(2)

        # ==================== 4. 最终结果 ====================

        hint_text8 = Text("提取常数，并将主部极限转化为定积分：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(
            DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text7, hint_text8))

        eq8 = Tex(
            r"L", r"=", r"-\frac{1}{2}", r"\int_0^1 f'(x) dx"
        ).set_color(BLUE).scale(0.9)

        self.play(TransformMatchingTex(eq7, eq8))
        self.wait(2)

        hint_text9 = Text("由牛顿-莱布尼茨公式：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text8, hint_text9))

        eq9 = Tex(
            r"L", r"=", r"-\frac{1}{2}", r"\Big(", r"f(1)", r"-", r"f(0)", r"\Big)"
        ).set_color(BLUE).scale(0.9)

        self.play(TransformMatchingTex(eq8, eq9))
        self.wait(2)

        # 【修复点】：文字混排公式
        hint_text10 = VGroup(
            Text("代入端点值 ", font="KaiTi", font_size=35),
            Tex(r"f(1)=\frac{1}{2}", font_size=35),
            Text(", ", font="KaiTi", font_size=35),
            Tex(r"f(0)=1", font_size=35),
            Text("：", font="KaiTi", font_size=35)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)

        self.play(ReplacementTransform(hint_text9, hint_text10))

        # 【极其关键修复】：将原来的 \left( 换成了 \Big( 彻底消除 LaTeX 切片编译报错
        eq10 = Tex(
            r"L", r"=", r"-\frac{1}{2}", r"\Big(", r"\frac{1}{2}", r"-", r"1", r"\Big)"
        ).set_color(BLUE).scale(0.9)

        self.play(TransformMatchingTex(eq9, eq10))
        self.wait(2)

        eq11 = Tex(
            r"L", r"=", r"\frac{1}{4}"
        ).set_color(BLUE).scale(0.9)

        self.play(TransformMatchingTex(eq10, eq11))
        self.wait(1.5)

        # ==================== 终极完整展开 ====================
        self.play(FadeOut(hint_text10))

        final_eq = Tex(
            r"\lim_{n \to \infty} n \left( \frac{\pi}{4} - \sum_{i=1}^{n} \frac{n}{n^2 + i^2} \right)",
            r"=",
            r"\frac{1}{4}"
        ).set_color(BLUE)

        self.play(
            TransformMatchingTex(
                eq11, final_eq,
                key_map={
                    "L": r"\lim_{n \to \infty} n \left( \frac{\pi}{4} - \sum_{i=1}^{n} \frac{n}{n^2 + i^2} \right)"}
            )
        )
        self.wait(2)

        rect = SurroundingRectangle(final_eq, buff=0.25, color=YELLOW)
        self.play(Write(rect))

        self.play(
            final_eq.animate.scale(1.2).set_color_by_gradient(BLUE, YELLOW, RED),
            rect.animate.scale(1.2),
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