from manim import *

class DeepMathSimplification(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("", font="KaiTi", font_size=40)
        
        # 拆分中文与公式，使用VGroup组合避免LaTeX中文编译错误
        cover_text = Text("化简：", font="KaiTi", font_size=32).set_color(BLUE)
        cover_math = MathTex(
            r"\sqrt{4 - \sqrt{10 + 2\sqrt{5}}} + \sqrt{4 + \sqrt{10 + 2\sqrt{5}}}",
            font_size=40
        ).set_color(BLUE)
        eq_cover = VGroup(cover_text, cover_math).arrange(RIGHT, buff=0.2)

        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1).to_edge(UP, buff=1.5)
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))

        # ==================== 倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=120)
            countdown_text.set_color_by_gradient(BLUE, YELLOW)
            countdown_text.next_to(cover, DOWN, buff=1.5)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：识别结构与降维 ====================
        desc_1 = Text("首先观察算式的结构特征：", font="KaiTi", font_size=30).to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_orig = MathTex(
            r"x = \sqrt{4 - \sqrt{10 + 2\sqrt{5}}} + \sqrt{4 + \sqrt{10 + 2\sqrt{5}}}", 
            font_size=35
        ).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(eq_orig))
        self.wait(1.5)

        desc_2 = Text("两项呈现共轭结构，直接化简内部根号较为困难。", font="KaiTi", font_size=28).next_to(eq_orig, DOWN, buff=0.5)
        self.play(Write(desc_2))

        desc_3 = Text("可以考虑采用“整体平方法”，利用平方差公式进行化简。", font="KaiTi", font_size=28).next_to(desc_2, DOWN, buff=0.3)
        self.play(Write(desc_3))
        self.wait(1.5)

        # 展开计算
        eq_sq_1 = MathTex(
            r"x^2 = \left(4 - \sqrt{\cdots}\right) + \left(4 + \sqrt{\cdots}\right) + 2\sqrt{4^2 - (\sqrt{10 + 2\sqrt{5}})^2}", 
            font_size=30
        ).next_to(desc_3, DOWN, buff=0.5).set_color(YELLOW)
        self.play(Write(eq_sq_1))
        self.wait(2)

        eq_sq_2 = MathTex(
            r"x^2 = 8 + 2\sqrt{16 - (10 + 2\sqrt{5})}", 
            font_size=35
        ).next_to(eq_sq_1, DOWN, buff=0.3)
        self.play(Write(eq_sq_2))
        
        eq_sq_final = MathTex(
            r"x^2 = 8 + 2\sqrt{6 - 2\sqrt{5}}", 
            font_size=35
        ).next_to(eq_sq_2, DOWN, buff=0.3).set_color(BLUE)
        self.play(ReplacementTransform(eq_sq_2.copy(), eq_sq_final))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(desc_1), FadeOut(eq_orig), FadeOut(desc_2), 
            FadeOut(desc_3), FadeOut(eq_sq_1), FadeOut(eq_sq_2)
        )
        self.play(eq_sq_final.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：解构双重根号 ====================
        desc_4_text1 = Text("此时问题的核心转化为化简：", font="KaiTi", font_size=30)
        desc_4_math1 = MathTex(r"\sqrt{6 - 2\sqrt{5}}", font_size=35).set_color(YELLOW)
        desc_4 = VGroup(desc_4_text1, desc_4_math1).arrange(RIGHT, buff=0.2).next_to(eq_sq_final, DOWN, buff=0.6)
        self.play(Write(desc_4))

        desc_5 = Text("基本思路：逆向构造完全平方式", font="KaiTi", font_size=28).next_to(desc_4, DOWN, buff=0.5)
        self.play(Write(desc_5))

        eq_form = MathTex(
            r"(a - b)^2 = (a^2 + b^2) - 2ab", 
            font_size=35
        ).next_to(desc_5, DOWN, buff=0.3)
        self.play(Write(eq_form))
        self.wait(1.5)

        desc_6 = Text("对比系数，我们需要寻找满足以下条件的两个数：", font="KaiTi", font_size=28).next_to(eq_form, DOWN, buff=0.5)
        self.play(Write(desc_6))

        # 拆分韦达定理这部分的中文与公式
        vieta_text1 = Text("两数之和为", font="KaiTi", font_size=28).set_color(GREEN)
        vieta_math1 = MathTex("6", font_size=35).set_color(GREEN)
        vieta_text2 = Text("，乘积为", font="KaiTi", font_size=28).set_color(GREEN)
        vieta_math2 = MathTex(r"5 \implies a^2=5, b^2=1", font_size=35).set_color(GREEN)
        
        eq_vieta = VGroup(vieta_text1, vieta_math1, vieta_text2, vieta_math2).arrange(RIGHT, buff=0.15).next_to(desc_6, DOWN, buff=0.3)
        self.play(Write(eq_vieta))
        self.wait(2)

        eq_inner_final = MathTex(
            r"\sqrt{6 - 2\sqrt{5}} = \sqrt{(\sqrt{5} - 1)^2} = \sqrt{5} - 1", 
            font_size=35
        ).next_to(eq_vieta, DOWN, buff=0.4).set_color(YELLOW)
        self.play(Write(eq_inner_final))
        self.wait(2)

        # 再次整理屏幕
        self.play(
            FadeOut(desc_4), FadeOut(desc_5), FadeOut(eq_form), 
            FadeOut(desc_6), FadeOut(eq_vieta)
        )
        self.play(eq_inner_final.animate.next_to(eq_sq_final, DOWN, buff=0.8))

        # ==================== 第三幕：代回与结论 ====================
        desc_7 = Text("将双重根号的化简结果代回原方程：", font="KaiTi", font_size=28).next_to(eq_inner_final, DOWN, buff=0.6)
        self.play(Write(desc_7))

        eq_sub_1 = MathTex(
            r"x^2 = 8 + 2(\sqrt{5} - 1)", 
            font_size=35
        ).next_to(desc_7, DOWN, buff=0.4)
        self.play(Write(eq_sub_1))

        eq_sub_2 = MathTex(
            r"x^2 = 6 + 2\sqrt{5}", 
            font_size=35
        ).next_to(eq_sub_1, DOWN, buff=0.3).set_color(BLUE)
        self.play(ReplacementTransform(eq_sub_1.copy(), eq_sub_2))
        self.wait(1.5)

        # 全屏清场，留下最后冲刺
        self.play(
            FadeOut(eq_sq_final), FadeOut(eq_inner_final), 
            FadeOut(desc_7), FadeOut(eq_sub_1)
        )
        self.play(eq_sub_2.animate.to_edge(UP, buff=1.5))

        desc_8 = Text("使用相同的方法再次进行配方，同理可得：", font="KaiTi", font_size=28).next_to(eq_sub_2, DOWN, buff=0.6)
        self.play(Write(desc_8))

        eq_sub_3 = MathTex(
            r"x^2 = (\sqrt{5} + 1)^2", 
            font_size=35
        ).next_to(desc_8, DOWN, buff=0.4)
        self.play(Write(eq_sub_3))
        self.wait(1.5)

        desc_9 = Text("由于原式中两项均为正数，故其和必定为正数，直接开方：", font="KaiTi", font_size=28).next_to(eq_sub_3, DOWN, buff=0.6)
        self.play(Write(desc_9))

        final_ans = MathTex(
            r"x = \sqrt{5} + 1", 
            font_size=50
        ).set_color(YELLOW).next_to(desc_9, DOWN, buff=0.6)
        self.play(Write(final_ans))

        rect_ans = SurroundingRectangle(final_ans, color=YELLOW, buff=0.2)
        self.play(Create(rect_ans))
        self.wait(3)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)