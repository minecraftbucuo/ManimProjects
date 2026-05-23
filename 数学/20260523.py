from manim import *

import manimpango

manimpango.register_font("simkai.ttf")

# === 字体自动映射补丁开始 ===
_original_text_init = Text.__init__

def _patched_text_init(self, text, *args, **kwargs):
    # 如果检测到请求 KaiTi，自动重定向到 楷体
    if kwargs.get('font') == 'KaiTi':
        kwargs['font'] = '楷体'
    _original_text_init(self, text, *args, **kwargs)

Text.__init__ = _patched_text_init
# === 字体自动映射补丁结束 ===

class CyclicEquationSystem(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("解轮换对称方程组", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"\begin{cases} x^2 + 2yz = x \\ y^2 + 2zx = y \\ z^2 + 2xy = z \end{cases}",
            font_size=45
        ).set_color(BLUE)

        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))
        
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

        # ==================== 第一幕：整体相加 ====================
        desc_1 = Text("首先，将方程组的三个等式相加：", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_add_1 = MathTex(r"x^2 + y^2 + z^2 + 2yz + 2zx + 2xy = x + y + z").set_color(BLUE).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(eq_add_1))
        self.wait(1.5)

        desc_2 = Text("等式左侧利用完全平方公式进行化简：", font="KaiTi", font_size=28).next_to(eq_add_1, DOWN, buff=0.5)
        self.play(Write(desc_2))

        eq_add_2 = MathTex(r"(x+y+z)^2", r" = ", r"x+y+z")
        eq_add_2[0].set_color(YELLOW)
        eq_add_2[2].set_color(YELLOW)
        eq_add_2.next_to(desc_2, DOWN, buff=0.3)
        self.play(Write(eq_add_2))
        self.wait(1)

        desc_3 = Text("由此可得关于变量总和的两个前提条件：", font="KaiTi", font_size=28).next_to(eq_add_2, DOWN, buff=0.5)
        self.play(Write(desc_3))

        eq_case_1 = MathTex(r"x+y+z = 0").set_color(GREEN)
        eq_case_or = Text("或", font="KaiTi", font_size=28)
        eq_case_2 = MathTex(r"x+y+z = 1").set_color(GREEN)
        cases_group = VGroup(eq_case_1, eq_case_or, eq_case_2).arrange(RIGHT, buff=0.5).next_to(desc_3, DOWN, buff=0.4)
        
        self.play(FadeIn(cases_group, shift=UP))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(desc_1), FadeOut(eq_add_1), FadeOut(desc_2), FadeOut(eq_add_2), FadeOut(desc_3)
        )
        self.play(cases_group.animate.to_edge(UP, buff=0.5))

        # ==================== 第二幕：两式相减 ====================
        desc_4_text1 = Text("接着，将第一式减去第二式：", font="KaiTi", font_size=30)
        desc_4_text1.next_to(cases_group, DOWN, buff=0.6)
        self.play(Write(desc_4_text1))

        eq_sub_1 = MathTex(r"(x^2 - y^2) + 2z(y - x) = x - y").set_color(BLUE).next_to(desc_4_text1, DOWN, buff=0.4)
        self.play(Write(eq_sub_1))
        self.wait(1.5)

        desc_5 = Text("利用平方差公式，并提取公因式：", font="KaiTi", font_size=28).next_to(eq_sub_1, DOWN, buff=0.5)
        self.play(Write(desc_5))

        eq_sub_2 = MathTex(r"(x - y)(x + y) - 2z(x - y) - (x - y) = 0").set_color(YELLOW).next_to(desc_5, DOWN, buff=0.3)
        self.play(Write(eq_sub_2))
        self.wait(1)

        eq_sub_3 = MathTex(r"(x - y)(x + y - 2z - 1) = 0").scale(1.1).set_color(GREEN).next_to(eq_sub_2, DOWN, buff=0.3)
        self.play(TransformMatchingTex(eq_sub_2.copy(), eq_sub_3))

        rect_sub = SurroundingRectangle(eq_sub_3, color=GREEN, buff=0.15)
        self.play(Create(rect_sub))
        self.wait(2)

        # 再次整理屏幕
        self.play(
            FadeOut(desc_4_text1), FadeOut(eq_sub_1), FadeOut(desc_5), FadeOut(eq_sub_2)
        )
        sub_group = VGroup(eq_sub_3, rect_sub)
        self.play(sub_group.animate.next_to(cases_group, DOWN, buff=0.5))

        # ==================== 第三幕：情况一 ====================
        desc_7_text = Text("讨论情况一：当", font="KaiTi", font_size=28)
        desc_7_math = MathTex(r"x+y+z=0", font_size=30).set_color(YELLOW)
        desc_7_text2 = Text("时，代入上式：", font="KaiTi", font_size=28)
        desc_7 = VGroup(desc_7_text, desc_7_math, desc_7_text2).arrange(RIGHT, buff=0.1).next_to(sub_group, DOWN, buff=0.6)
        self.play(Write(desc_7))

        eq_case1_1 = MathTex(r"(x - y)(-z - 2z - 1) = 0").set_color(BLUE).next_to(desc_7, DOWN, buff=0.4)
        self.play(Write(eq_case1_1))

        eq_case1_2 = MathTex(r"(x - y)(3z + 1) = 0").set_color(YELLOW).next_to(eq_case1_1, DOWN, buff=0.3)
        self.play(TransformMatchingTex(eq_case1_1.copy(), eq_case1_2))
        self.wait(1.5)

        desc_8 = Text("结合方程组的轮换对称性，可得出解：", font="KaiTi", font_size=28).next_to(eq_case1_2, DOWN, buff=0.5)
        self.play(Write(desc_8))

        ans_case1_1 = MathTex(r"(0, 0, 0)")
        ans_case1_text = Text("与", font="KaiTi", font_size=28)
        ans_case1_2 = MathTex(r"(-\frac{1}{3}, -\frac{1}{3}, \frac{2}{3})")
        ans_case1_text2 = Text("及其轮换式", font="KaiTi", font_size=28)
        ans_c1_group = VGroup(ans_case1_1, ans_case1_text, ans_case1_2, ans_case1_text2).arrange(RIGHT, buff=0.2).set_color(GREEN).next_to(desc_8, DOWN, buff=0.3)
        self.play(Write(ans_c1_group))
        self.wait(2.5)

        # ==================== 第四幕：情况二 ====================
        # 大清场
        self.play(
            FadeOut(desc_7), FadeOut(eq_case1_1), FadeOut(eq_case1_2), FadeOut(desc_8), FadeOut(ans_c1_group)
        )

        desc_9_text = Text("讨论情况二：当", font="KaiTi", font_size=28)
        desc_9_math = MathTex(r"x+y+z=1", font_size=30).set_color(YELLOW)
        desc_9_text2 = Text("时，同理代入关系式：", font="KaiTi", font_size=28)
        desc_9 = VGroup(desc_9_text, desc_9_math, desc_9_text2).arrange(RIGHT, buff=0.1).next_to(sub_group, DOWN, buff=0.6)
        self.play(Write(desc_9))

        eq_case2_1 = MathTex(r"(x - y)(1 - z - 2z - 1) = 0").set_color(BLUE).next_to(desc_9, DOWN, buff=0.4)
        self.play(Write(eq_case2_1))

        eq_case2_2 = MathTex(r"z(x - y) = 0").set_color(YELLOW).next_to(eq_case2_1, DOWN, buff=0.3)
        self.play(TransformMatchingTex(eq_case2_1.copy(), eq_case2_2))
        self.wait(1.5)

        desc_10 = Text("结合对称性，得出另一部分的解：", font="KaiTi", font_size=28).next_to(eq_case2_2, DOWN, buff=0.5)
        self.play(Write(desc_10))

        ans_case2_1 = MathTex(r"(\frac{1}{3}, \frac{1}{3}, \frac{1}{3})")
        ans_case2_text = Text("与", font="KaiTi", font_size=28)
        ans_case2_2 = MathTex(r"(1, 0, 0)")
        ans_case2_text2 = Text("及其轮换式", font="KaiTi", font_size=28)
        ans_c2_group = VGroup(ans_case2_1, ans_case2_text, ans_case2_2, ans_case2_text2).arrange(RIGHT, buff=0.2).set_color(GREEN).next_to(desc_10, DOWN, buff=0.3)
        self.play(Write(ans_c2_group))
        self.wait(2.5)

        # ==================== 第五幕：总结 ====================
        # 全屏清场
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        desc_11 = Text("综上所述，原方程组的完整解集为：", font="KaiTi", font_size=35).to_edge(UP, buff=1.5)
        self.play(Write(desc_11))

        # 绝对居中定位
        final_ans_1 = MathTex(r"(0, 0, 0), \quad (\frac{1}{3}, \frac{1}{3}, \frac{1}{3})").scale(1.2).set_color(YELLOW).move_to(UP * 0.5)
        
        final_ans_2_math = MathTex(r"(1, 0, 0), \quad (-\frac{1}{3}, -\frac{1}{3}, \frac{2}{3})").scale(1.2).set_color(YELLOW)
        final_ans_2_text = Text("及其轮换式", font="KaiTi", font_size=30).set_color(YELLOW)
        final_ans_2 = VGroup(final_ans_2_math, final_ans_2_text).arrange(RIGHT, buff=0.5).move_to(DOWN * 0.8)

        self.play(FadeIn(final_ans_1, shift=UP))
        self.play(FadeIn(final_ans_2, shift=UP))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)