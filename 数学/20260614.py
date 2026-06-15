from manim import *


class AlgebraicGeometryProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("代数式极值问题的几何解法", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        cond_text = Text("已知条件：", font="KaiTi", font_size=35)
        cond_math = MathTex(r"a^2 + b^2 = 4", font_size=40).set_color(GREEN)
        cond_group = VGroup(cond_text, cond_math).arrange(RIGHT, buff=0.2)

        target_text1 = Text("求代数式", font="KaiTi", font_size=35)
        target_math = MathTex(r"\sqrt{20 - 8a} + \sqrt{8 + 4b}", font_size=40).set_color_by_gradient(YELLOW, ORANGE)
        target_text2 = Text("的最小值", font="KaiTi", font_size=35)
        target_group = VGroup(target_text1, target_math, target_text2).arrange(RIGHT, buff=0.2)

        cover = VGroup(title, cond_group, target_group).arrange(DOWN, buff=0.8)
        cover.to_edge(UP, buff=1.0)

        self.play(Write(title))
        self.play(FadeIn(cond_group, shift=UP), FadeIn(target_group, shift=UP))
        self.wait(1)

        # ==================== 倒计时 ====================
        # 放置在标题和题目下方，避免遮挡
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=120)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.next_to(cover, DOWN, buff=1.0)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：第一个根式的配方 ====================
        desc_1 = Text("首先，对第一个根式进行代数变形：", font="KaiTi", font_size=30).to_edge(UP, buff=1.0)
        self.play(Write(desc_1))

        eq_1_orig = MathTex(r"\sqrt{20 - 8a}").set_color(YELLOW).next_to(desc_1, DOWN, buff=0.6)
        self.play(Write(eq_1_orig))
        self.wait(1)

        desc_2_t1 = Text("代入已知条件", font="KaiTi", font_size=28)
        desc_2_m1 = MathTex(r"a^2 + b^2 = 4", font_size=30).set_color(GREEN)
        desc_2_t2 = Text("，展开常数项：", font="KaiTi", font_size=28)
        desc_2 = VGroup(desc_2_t1, desc_2_m1, desc_2_t2).arrange(RIGHT, buff=0.1).next_to(eq_1_orig, DOWN, buff=0.6)
        self.play(Write(desc_2))

        # 对公式进行切片以实现局部上色
        eq_1_sub = MathTex(r"=", r"\sqrt{(", r"a^2 + b^2", r") + 16 - 8a}")
        eq_1_sub[2].set_color(GREEN)
        eq_1_sub.next_to(desc_2, DOWN, buff=0.4)
        self.play(Write(eq_1_sub))
        self.wait(1)

        desc_3 = Text("进行完全平方配方：", font="KaiTi", font_size=28).next_to(eq_1_sub, DOWN, buff=0.6)
        self.play(Write(desc_3))

        eq_1_final = MathTex(r"=", r"\sqrt{", r"(a-4)^2", r"+", r"b^2", r"}")
        eq_1_final[2].set_color(TEAL)
        eq_1_final[4].set_color(TEAL)
        eq_1_final.next_to(desc_3, DOWN, buff=0.4)
        self.play(Write(eq_1_final))
        self.wait(1.5)

        # 整理屏幕，保留最终结论
        self.play(
            FadeOut(desc_1), FadeOut(eq_1_orig), FadeOut(desc_2), FadeOut(eq_1_sub), FadeOut(desc_3)
        )

        geo_1_t1 = Text("这表示点", font="KaiTi", font_size=30)
        geo_1_m1 = MathTex(r"P(a, b)", font_size=32).set_color(BLUE)
        geo_1_t2 = Text("到定点", font="KaiTi", font_size=30)
        geo_1_m2 = MathTex(r"A(4, 0)", font_size=32).set_color(RED)
        geo_1_t3 = Text("的距离", font="KaiTi", font_size=30)
        geo_1 = VGroup(geo_1_t1, geo_1_m1, geo_1_t2, geo_1_m2, geo_1_t3).arrange(RIGHT, buff=0.1)

        self.play(eq_1_final.animate.to_edge(UP, buff=1.0))
        geo_1.next_to(eq_1_final, DOWN, buff=0.5)
        self.play(Write(geo_1))
        self.wait(2)

        self.play(FadeOut(eq_1_final), FadeOut(geo_1))

        # ==================== 第二幕：第二个根式的配方 ====================
        desc_4 = Text("同理，对第二个根式进行处理：", font="KaiTi", font_size=30).to_edge(UP, buff=1.0)
        self.play(Write(desc_4))

        eq_2_orig = MathTex(r"\sqrt{8 + 4b}").set_color(ORANGE).next_to(desc_4, DOWN, buff=0.6)
        self.play(Write(eq_2_orig))
        self.wait(1)

        eq_2_sub = MathTex(r"=", r"\sqrt{(", r"a^2 + b^2", r") + 4 + 4b}")
        eq_2_sub[2].set_color(GREEN)
        eq_2_sub.next_to(eq_2_orig, DOWN, buff=0.6)
        self.play(Write(eq_2_sub))
        self.wait(1)

        eq_2_final = MathTex(r"=", r"\sqrt{", r"a^2", r"+", r"(b+2)^2", r"}")
        eq_2_final[2].set_color(PURPLE)
        eq_2_final[4].set_color(PURPLE)
        eq_2_final.next_to(eq_2_sub, DOWN, buff=0.6)
        self.play(Write(eq_2_final))
        self.wait(1.5)

        self.play(
            FadeOut(desc_4), FadeOut(eq_2_orig), FadeOut(eq_2_sub)
        )

        geo_2_t1 = Text("这表示点", font="KaiTi", font_size=30)
        geo_2_m1 = MathTex(r"P(a, b)", font_size=32).set_color(BLUE)
        geo_2_t2 = Text("到定点", font="KaiTi", font_size=30)
        geo_2_m2 = MathTex(r"B(0, -2)", font_size=32).set_color(RED)
        geo_2_t3 = Text("的距离", font="KaiTi", font_size=30)
        geo_2 = VGroup(geo_2_t1, geo_2_m1, geo_2_t2, geo_2_m2, geo_2_t3).arrange(RIGHT, buff=0.1)

        self.play(eq_2_final.animate.to_edge(UP, buff=1.0))
        geo_2.next_to(eq_2_final, DOWN, buff=0.5)
        self.play(Write(geo_2))
        self.wait(2)

        self.play(FadeOut(eq_2_final), FadeOut(geo_2))

        # ==================== 第三幕：建立几何模型 ====================
        desc_5 = Text("至此，原代数式转化为几何模型：", font="KaiTi", font_size=30).to_edge(UP, buff=1.0)
        self.play(Write(desc_5))

        model_m1 = MathTex(r"|PA|", r"+", r"|PB|")
        model_m1[0].set_color(TEAL)
        model_m1[2].set_color(PURPLE)
        model_m1.next_to(desc_5, DOWN, buff=0.8)
        self.play(Write(model_m1))

        model_t1_1 = Text("其中动点", font="KaiTi", font_size=28)
        model_t1_2 = MathTex(r"P", font_size=30).set_color(BLUE)
        model_t1_3 = Text("在圆", font="KaiTi", font_size=28)
        model_t1_4 = MathTex(r"a^2 + b^2 = 4", font_size=30).set_color(GREEN)
        model_t1_5 = Text("上", font="KaiTi", font_size=28)
        model_t1 = VGroup(model_t1_1, model_t1_2, model_t1_3, model_t1_4, model_t1_5).arrange(RIGHT, buff=0.1)
        model_t1.next_to(model_m1, DOWN, buff=0.8)
        self.play(Write(model_t1))

        model_t2_1 = Text("根据三角形两边之和大于第三边，当", font="KaiTi", font_size=28)
        model_t2_2 = MathTex(r"P", font_size=30).set_color(BLUE)
        model_t2_3 = Text("在线段", font="KaiTi", font_size=28)
        model_t2_4 = MathTex(r"AB", font_size=30).set_color(RED)
        model_t2_5 = Text("上时：", font="KaiTi", font_size=28)
        model_t2 = VGroup(model_t2_1, model_t2_2, model_t2_3, model_t2_4, model_t2_5).arrange(RIGHT, buff=0.1)
        model_t2.next_to(model_t1, DOWN, buff=0.6)
        self.play(Write(model_t2))

        model_m2 = MathTex(r"|PA| + |PB|", r"\ge", r"|AB|")
        model_m2[0].set_color_by_gradient(TEAL, PURPLE)
        model_m2[2].set_color(RED)
        model_m2.next_to(model_t2, DOWN, buff=0.6)
        self.play(Write(model_m2))
        self.wait(2.5)

        self.play(
            FadeOut(desc_5), FadeOut(model_m1), FadeOut(model_t1), FadeOut(model_t2), FadeOut(model_m2)
        )

        # ==================== 第四幕：验证与求解 ====================
        desc_6 = Text("验证定点与圆的位置关系：", font="KaiTi", font_size=30).to_edge(UP, buff=1.0)
        self.play(Write(desc_6))

        check_t1_1 = Text("定点", font="KaiTi", font_size=28)
        check_t1_2 = MathTex(r"B(0, -2)", font_size=30).set_color(RED)
        check_t1_3 = Text("代入方程成立，在圆上；", font="KaiTi", font_size=28)
        check_1 = VGroup(check_t1_1, check_t1_2, check_t1_3).arrange(RIGHT, buff=0.1).next_to(desc_6, DOWN, buff=0.6)
        self.play(Write(check_1))

        check_t2_1 = Text("定点", font="KaiTi", font_size=28)
        check_t2_2 = MathTex(r"A(4, 0)", font_size=30).set_color(RED)
        check_t2_3 = Text("在圆外。线段必与圆相交。", font="KaiTi", font_size=28)
        check_2 = VGroup(check_t2_1, check_t2_2, check_t2_3).arrange(RIGHT, buff=0.1).next_to(check_1, DOWN, buff=0.6)
        self.play(Write(check_2))
        self.wait(1.5)

        desc_7 = Text("故最小值为线段的长度：", font="KaiTi", font_size=30).next_to(check_2, DOWN, buff=0.8)
        self.play(Write(desc_7))

        final_eq_1 = MathTex(r"|AB|", r"=", r"\sqrt{(4-0)^2 + (0-(-2))^2}")
        final_eq_1[0].set_color(RED)
        final_eq_1.next_to(desc_7, DOWN, buff=0.4)

        final_eq_2 = MathTex(r"=", r"\sqrt{20}", r"=", r"2\sqrt{5}")
        final_eq_2[3].set_color_by_gradient(YELLOW, RED)
        final_eq_2.next_to(final_eq_1, DOWN, buff=0.4)

        self.play(Write(final_eq_1))
        self.wait(0.5)
        self.play(Write(final_eq_2))

        # 加一个强调框
        rect_final = SurroundingRectangle(final_eq_2[3], color=YELLOW, buff=0.15)
        self.play(Create(rect_final))
        self.wait(3)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)