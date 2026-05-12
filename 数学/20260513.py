from manim import *


class AlgebraicIdentityProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("如何注意到：", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"\sqrt{\frac{1}{m^2} + \frac{1}{n^2} + \frac{1}{(m+n)^2}} = \frac{1}{m} + \frac{1}{n} - \frac{1}{m+n}",
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

        # ==================== 第一幕：展开验证 ====================
        desc_1 = Text("首先验证等式右侧项的完全平方：", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_orig = MathTex(
            r"\left(\frac{1}{m} + \frac{1}{n} - \frac{1}{m+n}\right)^2"
        ).set_color(BLUE).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(eq_orig))
        self.wait(1.5)

        desc_2 = Text("将其展开为平方项与交叉项：", font="KaiTi", font_size=28).next_to(eq_orig, DOWN, buff=0.5)
        self.play(Write(desc_2))

        eq_sq_1 = MathTex(
            r"= \frac{1}{m^2} + \frac{1}{n^2} + \frac{1}{(m+n)^2} + ",
            r"2\left(\frac{1}{mn} - \frac{1}{m(m+n)} - \frac{1}{n(m+n)}\right)"
        )
        eq_sq_1[1].set_color(YELLOW)
        eq_sq_1.next_to(desc_2, DOWN, buff=0.3)
        self.play(Write(eq_sq_1))
        self.wait(1.5)

        desc_3 = Text("提取交叉项的公分母进行化简：", font="KaiTi", font_size=28).next_to(eq_sq_1, DOWN, buff=0.5)
        self.play(Write(desc_3))

        eq_cross = MathTex(
            r"\frac{1}{mn} - \frac{1}{m(m+n)} - \frac{1}{n(m+n)} = \frac{(m+n) - n - m}{mn(m+n)} = 0"
        ).set_color(YELLOW).next_to(desc_3, DOWN, buff=0.3)
        self.play(Write(eq_cross))
        self.wait(2)

        # 整理屏幕
        self.play(
            FadeOut(desc_1), FadeOut(eq_orig), FadeOut(desc_2), FadeOut(eq_sq_1), FadeOut(desc_3), FadeOut(eq_cross)
        )

        # ==================== 第二幕：结构化抽象 ====================
        desc_4 = Text("为揭示该结论的代数普适性，引入对称代换：", font="KaiTi", font_size=30).to_edge(UP, buff=0.8)
        self.play(Write(desc_4))

        eq_sub = MathTex(r"a = m, \quad b = n, \quad c = -(m+n)").set_color(GREEN).next_to(desc_4, DOWN, buff=0.5)
        self.play(Write(eq_sub))
        self.wait(1)

        desc_5 = Text("由此构造出核心的前置约束条件：", font="KaiTi", font_size=28).next_to(eq_sub, DOWN, buff=0.5)
        self.play(Write(desc_5))

        eq_cond = MathTex(r"a + b + c = 0").set_color(GREEN).scale(1.2).next_to(desc_5, DOWN, buff=0.3)
        rect_cond = SurroundingRectangle(eq_cond, color=GREEN, buff=0.15)
        cond_group = VGroup(eq_cond, rect_cond)

        self.play(Write(eq_cond))
        self.play(Create(rect_cond))
        self.wait(2)

        # 再次整理屏幕
        self.play(
            FadeOut(desc_4), FadeOut(eq_sub), FadeOut(desc_5)
        )
        self.play(cond_group.animate.to_edge(UP, buff=0.5))

        # ==================== 第三幕：本质推演 ====================
        desc_6_text = Text("此时原根号内部的表达式转化为：", font="KaiTi", font_size=28)
        desc_6 = VGroup(desc_6_text).next_to(cond_group, DOWN, buff=0.6)
        self.play(Write(desc_6))

        eq_sym = MathTex(r"\frac{1}{a^2} + \frac{1}{b^2} + \frac{1}{c^2}").set_color(BLUE).next_to(desc_6, DOWN,
                                                                                                   buff=0.4)
        self.play(Write(eq_sym))
        self.wait(1.5)

        desc_7 = Text("联想三个变量倒数和的完全平方展开公式：", font="KaiTi", font_size=28).next_to(eq_sym, DOWN,
                                                                                                   buff=0.6)
        self.play(Write(desc_7))

        eq_general = MathTex(
            r"\left( \frac{1}{a} + \frac{1}{b} + \frac{1}{c} \right)^2 = \frac{1}{a^2} + \frac{1}{b^2} + \frac{1}{c^2} + ",
            r"2 \left( \frac{a+b+c}{abc} \right)"
        ).next_to(desc_7, DOWN, buff=0.4)
        eq_general[0].set_color(BLUE)
        eq_general[1].set_color(YELLOW)
        self.play(Write(eq_general))
        self.wait(2)

        # 清理多余项，准备展示结论
        self.play(
            FadeOut(desc_6), FadeOut(eq_sym), FadeOut(desc_7)
        )
        self.play(eq_general.animate.next_to(cond_group, DOWN, buff=1))

        # ==================== 第四幕：得出结论 ====================
        desc_8_t1 = Text("代入约束条件", font="KaiTi", font_size=28)
        desc_8_m1 = MathTex(r"a+b+c=0", font_size=30).set_color(GREEN)
        desc_8_t2 = Text("，交叉项整体为零：", font="KaiTi", font_size=28)
        desc_8 = VGroup(desc_8_t1, desc_8_m1, desc_8_t2).arrange(RIGHT, buff=0.1).next_to(eq_general, DOWN, buff=0.5)
        self.play(Write(desc_8))

        eq_final_abs = MathTex(
            r"\frac{1}{a^2} + \frac{1}{b^2} + \frac{1}{c^2} = \left( \frac{1}{a} + \frac{1}{b} + \frac{1}{c} \right)^2"
        ).set_color(BLUE).next_to(desc_8, DOWN, buff=0.4)
        self.play(Write(eq_final_abs))
        self.wait(1.5)

        # 终场清理
        self.play(
            FadeOut(cond_group), FadeOut(eq_general), FadeOut(desc_8), FadeOut(eq_final_abs)
        )

        desc_9 = Text("两端同时开平方，并恢复原变量，即得证明：", font="KaiTi", font_size=35).to_edge(UP, buff=2)
        self.play(Write(desc_9))

        final_ans = MathTex(
            r"\sqrt{\frac{1}{m^2} + \frac{1}{n^2} + \frac{1}{(m+n)^2}} = \left| \frac{1}{m} + \frac{1}{n} - \frac{1}{m+n} \right|"
        ).scale(1.2).set_color(YELLOW).next_to(desc_9, DOWN, buff=1)

        self.play(FadeIn(final_ans, shift=UP))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)