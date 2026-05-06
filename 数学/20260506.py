from manim import *


class NestedFunctionFluidProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("如何求解这个嵌套根式方程？", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"\sqrt{6+\sqrt{6+x}} - x = 0",
            font_size=60
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

        # ==================== 第一幕：常规解法 ====================
        desc_1 = Text("首先按常规代数步骤求解：", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.5)
        self.play(Write(desc_1))

        eq_orig = MathTex(r"\sqrt{6+\sqrt{6+x}} - x = 0", font_size=38).set_color(BLUE)
        eq_orig.next_to(desc_1, DOWN, buff=0.4)
        self.play(Write(eq_orig))
        self.wait(1)

        desc_2 = Text("移项得：", font="KaiTi", font_size=28)
        desc_2.next_to(eq_orig, DOWN, buff=0.3)
        self.play(Write(desc_2))

        # 直接在原位置替换，不往下堆
        eq_move = MathTex(r"\sqrt{6+\sqrt{6+x}} = x", font_size=38)
        eq_move.move_to(eq_orig)
        self.play(TransformMatchingTex(eq_orig, eq_move))
        self.wait(0.8)
        self.play(FadeOut(desc_2))

        # 定义域说明，单独占一行
        desc_3_text1 = Text("确定定义域：外层结果为", font="KaiTi", font_size=26)
        desc_3_math1 = MathTex(r"x", font_size=26).set_color(YELLOW)
        desc_3_text2 = Text("，且内层要求", font="KaiTi", font_size=26)
        desc_3_math2 = MathTex(r"x \ge -6", font_size=26).set_color(YELLOW)
        desc_3_text3 = Text("，综合可得", font="KaiTi", font_size=26)
        desc_3_math3 = MathTex(r"x \ge 0", font_size=26).set_color(YELLOW)
        desc_3_text4 = Text("。", font="KaiTi", font_size=26)
        desc_3 = VGroup(desc_3_text1, desc_3_math1, desc_3_text2, desc_3_math2, desc_3_text3, desc_3_math3, desc_3_text4).arrange(RIGHT, buff=0.1)
        desc_3.next_to(eq_move, DOWN, buff=0.4)
        self.play(Write(desc_3))
        self.wait(1.5)
        self.play(FadeOut(desc_3))

        # 平方过程替换
        desc_4 = Text("两边平方并整理：", font="KaiTi", font_size=28)
        desc_4.next_to(eq_move, DOWN, buff=0.3)
        self.play(Write(desc_4))

        eq_sq1 = MathTex(r"\sqrt{6+x} = x^2 - 6", font_size=38)
        eq_sq1.move_to(eq_move)
        self.play(TransformMatchingTex(eq_move, eq_sq1))
        self.wait(0.8)
        self.play(FadeOut(desc_4))

        desc_5 = Text("再次平方，展开并移项：", font="KaiTi", font_size=28)
        desc_5.next_to(eq_sq1, DOWN, buff=0.3)
        self.play(Write(desc_5))

        eq_sq2 = MathTex(r"x^4 - 12x^2 - x + 30 = 0", font_size=38).set_color(RED)
        eq_sq2.move_to(eq_sq1)
        self.play(TransformMatchingTex(eq_sq1, eq_sq2))
        self.wait(0.8)
        self.play(FadeOut(desc_5))

        # 结论
        desc_6 = Text("得到一元四次方程，求解繁琐且易产生增根，需另寻方法。", font="KaiTi", font_size=26).set_color(RED)
        desc_6.next_to(eq_sq2, DOWN, buff=0.5)
        self.play(Write(desc_6))
        self.wait(2)

        # 大清场
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        # ==================== 第二幕：洞察本质 ====================
        desc_7_text1 = Text("从函数嵌套的角度重新审视，令", font="KaiTi", font_size=30)
        desc_7_math = MathTex(r"f(t) = \sqrt{6+t}", font_size=32).set_color(BLUE)
        desc_7_text2 = Text("，则原方程化为：", font="KaiTi", font_size=30)
        desc_7 = VGroup(desc_7_text1, desc_7_math, desc_7_text2).arrange(RIGHT, buff=0.1)
        desc_7.to_edge(UP, buff=0.5)
        self.play(Write(desc_7))

        eq_iter = MathTex(r"f(f(x)) = x", font_size=50).set_color(BLUE)
        eq_iter.next_to(desc_7, DOWN, buff=0.5)
        self.play(FadeIn(eq_iter, shift=UP))
        self.wait(1.5)

        # 定理说明
        th_text1 = Text("根据相关定理：若函数", font="KaiTi", font_size=24)
        th_math1 = MathTex(r"f(x)", font_size=24).set_color(GREEN)
        th_text2 = Text("在区间上严格单调递增，", font="KaiTi", font_size=24)
        th_line1 = VGroup(th_text1, th_math1, th_text2).arrange(RIGHT, buff=0.1)
        th_line1.next_to(eq_iter, DOWN, buff=0.5)

        th_text3 = Text("则方程", font="KaiTi", font_size=24)
        th_math2 = MathTex(r"f(f(x)) = x", font_size=24).set_color(GREEN)
        th_text4 = Text("的解等价于", font="KaiTi", font_size=24)
        th_math3 = MathTex(r"f(x) = x", font_size=24).set_color(GREEN)
        th_text5 = Text("的解。", font="KaiTi", font_size=24)
        th_line2 = VGroup(th_text3, th_math2, th_text4, th_math3, th_text5).arrange(RIGHT, buff=0.1)
        th_line2.next_to(th_line1, DOWN, buff=0.2)

        self.play(Write(th_line1))
        self.play(Write(th_line2))
        self.wait(1)

        # 简要证明
        pf_text1 = Text("简要证明（反证法）：若", font="KaiTi", font_size=22)
        pf_math1 = MathTex(r"f(x) > x", font_size=22).set_color(ORANGE)
        pf_text2 = Text("，由递增性作用", font="KaiTi", font_size=22)
        pf_math2 = MathTex(r"f", font_size=22).set_color(ORANGE)
        pf_text3 = Text("得", font="KaiTi", font_size=22)
        pf_math3 = MathTex(r"f(f(x)) > f(x)", font_size=22).set_color(ORANGE)
        pf_line1 = VGroup(pf_text1, pf_math1, pf_text2, pf_math2, pf_text3, pf_math3).arrange(RIGHT, buff=0.1)
        pf_line1.next_to(th_line2, DOWN, buff=0.4)

        pf_text4 = Text("代入原式即", font="KaiTi", font_size=22)
        pf_math4 = MathTex(r"x > f(x)", font_size=22).set_color(ORANGE)
        pf_text5 = Text("，与假设矛盾，故仅有", font="KaiTi", font_size=22)
        pf_math5 = MathTex(r"f(x) = x", font_size=22).set_color(ORANGE)
        pf_text6 = Text("。", font="KaiTi", font_size=22)
        pf_line2 = VGroup(pf_text4, pf_math4, pf_text5, pf_math5, pf_text6).arrange(RIGHT, buff=0.1)
        pf_line2.next_to(pf_line1, DOWN, buff=0.2)

        self.play(Write(pf_line1))
        self.play(Write(pf_line2))
        self.wait(1.5)

        # 淡出证明部分
        self.play(
            FadeOut(th_line1), FadeOut(th_line2),
            FadeOut(pf_line1), FadeOut(pf_line2)
        )

        # 结论应用
        app_text1 = Text("本题中", font="KaiTi", font_size=28)
        app_math = MathTex(r"f(t) = \sqrt{6+t}", font_size=28).set_color(BLUE)
        app_text2 = Text("在定义域内显然严格单调递增。", font="KaiTi", font_size=28)
        app_desc = VGroup(app_text1, app_math, app_text2).arrange(RIGHT, buff=0.1)
        app_desc.next_to(eq_iter, DOWN, buff=0.6)
        self.play(Write(app_desc))
        self.wait(2)

        # 大清场
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        # ==================== 第三幕：等价化简 ====================
        desc_11 = Text("因此，原方程可等价化简为：", font="KaiTi", font_size=32)
        desc_11.to_edge(UP, buff=0.5)
        self.play(Write(desc_11))

        eq_reduce = MathTex(r"\sqrt{6+x} = x", font_size=50).set_color(GREEN)
        eq_reduce.next_to(desc_11, DOWN, buff=0.5)
        self.play(FadeIn(eq_reduce, shift=UP))
        self.wait(1.5)

        desc_12 = Text("两边平方并整理得：", font="KaiTi", font_size=28)
        desc_12.next_to(eq_reduce, DOWN, buff=0.3)
        self.play(Write(desc_12))

        eq_quad = MathTex(r"x^2 - x - 6 = 0", font_size=45)
        eq_quad.move_to(eq_reduce)
        self.play(TransformMatchingTex(eq_reduce, eq_quad))
        self.wait(0.8)
        self.play(FadeOut(desc_12))

        desc_13 = Text("因式分解：", font="KaiTi", font_size=28)
        desc_13.next_to(eq_quad, DOWN, buff=0.3)
        self.play(Write(desc_13))

        eq_fact = MathTex(r"(x-3)(x+2) = 0", font_size=45)
        eq_fact.move_to(eq_quad)
        self.play(TransformMatchingTex(eq_quad, eq_fact))
        self.wait(0.8)
        self.play(FadeOut(desc_13))

        # 结论得出
        fin_text1 = Text("结合定义域", font="KaiTi", font_size=28)
        fin_math = MathTex(r"x \ge 0", font_size=28).set_color(YELLOW)
        fin_text2 = Text("，舍去负根，最终解为：", font="KaiTi", font_size=28)
        fin_desc = VGroup(fin_text1, fin_math, fin_text2).arrange(RIGHT, buff=0.1)
        fin_desc.next_to(eq_fact, DOWN, buff=0.5)
        self.play(Write(fin_desc))

        eq_final = MathTex(r"x = 3", font_size=60).set_color(YELLOW)
        eq_final.next_to(fin_desc, DOWN, buff=0.4)
        self.play(FadeIn(eq_final, shift=UP))
        self.wait(3)

        # 大清场
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        # ==================== 第四幕：举一反三 ====================
        desc_15 = Text("此方法可推广至一类嵌套问题：", font="KaiTi", font_size=30)
        desc_15.to_edge(UP, buff=0.5)
        self.play(Write(desc_15))

        # 变式一
        v1_text1 = Text("变式一：无限嵌套结构", font="KaiTi", font_size=24)
        v1_eq = MathTex(r"\sqrt{6+\sqrt{6+\sqrt{6+\dots}}} = x", font_size=26).set_color(BLUE)
        v1_text2 = Text("直接解", font="KaiTi", font_size=24)
        v1_eq2 = MathTex(r"\sqrt{6+x} = x", font_size=26).set_color(GREEN)
        v1 = VGroup(v1_text1, v1_eq, v1_text2, v1_eq2).arrange(RIGHT, buff=0.3)
        v1.next_to(desc_15, DOWN, buff=0.5)
        self.play(Write(v1))
        self.wait(1.5)

        # 变式二
        v2_text1 = Text("变式二：改变底层数字", font="KaiTi", font_size=24)
        v2_eq = MathTex(r"\sqrt{2+\sqrt{2+\sqrt{2+x}}} = x", font_size=26).set_color(BLUE)
        v2_text2 = Text("直接解", font="KaiTi", font_size=24)
        v2_eq2 = MathTex(r"\sqrt{2+x} = x", font_size=26).set_color(GREEN)
        v2 = VGroup(v2_text1, v2_eq, v2_text2, v2_eq2).arrange(RIGHT, buff=0.3)
        v2.next_to(v1, DOWN, buff=0.4)
        self.play(Write(v2))
        self.wait(1.5)

        # 警告/易错点
        warn_text1 = Text("注意：若函数为递减函数，如", font="KaiTi", font_size=24)
        warn_eq = MathTex(r"\sqrt{6 - \sqrt{6 - x}} = x", font_size=26).set_color(RED)
        warn_text2 = Text("，则不满足等价条件，强行化简会导致漏解。", font="KaiTi", font_size=24).set_color(RED)
        warn = VGroup(warn_text1, warn_eq, warn_text2).arrange(RIGHT, buff=0.2)
        warn.next_to(v2, DOWN, buff=0.5)
        self.play(Write(warn))
        self.wait(4)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)