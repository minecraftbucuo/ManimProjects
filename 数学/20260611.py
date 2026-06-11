from manim import *


class ConditionExtremumProof(Scene):
    def construct(self):
        # ==================== 全局参数设置 ====================
        # 统一调小字号，增加屏幕容纳空间
        text_sz = 26
        math_sz = 36
        line_buff = 0.5  # 统一行间距

        # ==================== 封面 ====================
        title = Text("", font="KaiTi", font_size=40)

        eq_cover_1_m1 = MathTex(r"x, y > 0,", font_size=math_sz)
        eq_cover_1_t = Text("且", font="KaiTi", font_size=text_sz)
        eq_cover_1_m2 = MathTex(r"\frac{1}{2x+y} + \frac{1}{y+1} = 1", font_size=math_sz)
        eq_cover_1 = VGroup(eq_cover_1_m1, eq_cover_1_t, eq_cover_1_m2).arrange(RIGHT, buff=0.15)

        eq_cover_2_t1 = Text("求", font="KaiTi", font_size=text_sz)
        eq_cover_2_m = MathTex(r"x+2y", font_size=math_sz)
        eq_cover_2_t2 = Text("的最小值", font="KaiTi", font_size=text_sz)
        eq_cover_2 = VGroup(eq_cover_2_t1, eq_cover_2_m, eq_cover_2_t2).arrange(RIGHT, buff=0.15)

        eq_cover = VGroup(eq_cover_1, eq_cover_2).arrange(DOWN, buff=line_buff).set_color(BLUE)
        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1).to_edge(UP, buff=1.2)

        # self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))

        # ==================== 倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=100)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.next_to(cover, DOWN, buff=0.8)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：换元法 (同屏最大行数: 5) ====================
        # 行 1
        desc_1 = Text("已知条件分母较复杂，首先采用换元法化简：", font="KaiTi", font_size=text_sz).to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        # 行 2
        eq_sub_t = Text("令", font="KaiTi", font_size=text_sz)
        eq_sub_m = MathTex(r"a = 2x+y, \quad b = y+1", font_size=math_sz).set_color(BLUE)
        eq_sub = VGroup(eq_sub_t, eq_sub_m).arrange(RIGHT, buff=0.15).next_to(desc_1, DOWN, buff=line_buff)
        self.play(Write(eq_sub))
        self.wait(1)

        # 行 3
        desc_2_t1 = Text("由于", font="KaiTi", font_size=text_sz)
        desc_2_m1 = MathTex(r"x, y > 0", font_size=math_sz).set_color(YELLOW)
        desc_2_t2 = Text("，推断出", font="KaiTi", font_size=text_sz)
        desc_2_m2 = MathTex(r"a > 0, b > 1", font_size=math_sz).set_color(YELLOW)
        desc_2 = VGroup(desc_2_t1, desc_2_m1, desc_2_t2, desc_2_m2).arrange(RIGHT, buff=0.1).next_to(eq_sub, DOWN,
                                                                                                     buff=line_buff)
        self.play(Write(desc_2))
        self.wait(1)

        # 行 4
        desc_3 = Text("此时，原已知条件转化为标准形式：", font="KaiTi", font_size=text_sz).next_to(desc_2, DOWN,
                                                                                                 buff=line_buff)
        self.play(Write(desc_3))

        # 行 5
        eq_cond_new = MathTex(r"\frac{1}{a} + \frac{1}{b} = 1", font_size=40).set_color(GREEN).next_to(desc_3, DOWN,
                                                                                                       buff=line_buff)
        self.play(Write(eq_cond_new))
        self.wait(2)

        # 清除不必要的信息，仅保留核心条件
        self.play(FadeOut(desc_1), FadeOut(eq_sub), FadeOut(desc_2), FadeOut(desc_3))
        self.play(eq_cond_new.animate.to_edge(UP, buff=0.8))

        # ==================== 第二幕：重构目标函数 (同屏最大行数: 5) ====================
        # 行 1 (eq_cond_new 已在顶部)

        # 行 2
        desc_4 = Text("将目标函数用新变量表示：", font="KaiTi", font_size=text_sz).next_to(eq_cond_new, DOWN,
                                                                                          buff=line_buff)
        self.play(Write(desc_4))

        # 行 3
        eq_xy = MathTex(r"y = b-1, \quad x = \frac{a-b+1}{2}", font_size=math_sz).set_color(BLUE).next_to(desc_4, DOWN,
                                                                                                          buff=line_buff)
        self.play(Write(eq_xy))
        self.wait(1)

        # 行 4
        desc_5 = Text("代入目标函数并化简：", font="KaiTi", font_size=text_sz).next_to(eq_xy, DOWN, buff=line_buff)
        self.play(Write(desc_5))

        # 行 5
        eq_target = MathTex(r"x + 2y = \frac{a-b+1}{2} + 2(b-1) = \frac{a+3b-3}{2}", font_size=math_sz).next_to(desc_5,
                                                                                                                DOWN,
                                                                                                                buff=line_buff)
        self.play(Write(eq_target))
        self.wait(2)

        # 全屏清场，准备核心计算
        self.play(FadeOut(eq_cond_new), FadeOut(desc_4), FadeOut(eq_xy), FadeOut(desc_5), FadeOut(eq_target))

        # ==================== 第三幕：相乘与展开 (同屏最大行数: 5) ====================
        # 行 1：重申已知与目标
        top_cond_t = Text("已知：", font="KaiTi", font_size=text_sz)
        top_cond_m = MathTex(r"\frac{1}{a} + \frac{1}{b} = 1", font_size=math_sz).set_color(GREEN)
        top_cond = VGroup(top_cond_t, top_cond_m).arrange(RIGHT, buff=0.2)

        top_goal_t = Text("目标：求", font="KaiTi", font_size=text_sz)
        top_goal_m = MathTex(r"a+3b", font_size=math_sz).set_color(YELLOW)
        top_goal_t2 = Text("的最小值", font="KaiTi", font_size=text_sz)
        top_goal = VGroup(top_goal_t, top_goal_m, top_goal_t2).arrange(RIGHT, buff=0.1)

        top_group = VGroup(top_cond, top_goal).arrange(DOWN, buff=line_buff).to_edge(UP, buff=0.8)
        self.play(FadeIn(top_group))

        # 行 3
        desc_7 = Text("将核心目标乘以常数 1 (即已知条件) 进行配凑：", font="KaiTi", font_size=text_sz).next_to(top_group,
                                                                                                              DOWN,
                                                                                                              buff=line_buff)
        self.play(Write(desc_7))

        # 行 4
        eq_mul = MathTex(r"a+3b = (a+3b) \times 1 = (a+3b)\left(\frac{1}{a} + \frac{1}{b}\right)",
                         font_size=math_sz).set_color(BLUE).next_to(desc_7, DOWN, buff=line_buff)
        self.play(Write(eq_mul))
        self.wait(1.5)

        # 替换行 3 的文字，腾出空间展示行 5
        desc_8 = Text("展开多项式，构造出互为倒数的结构：", font="KaiTi", font_size=text_sz).move_to(desc_7.get_center())
        self.play(ReplacementTransform(desc_7, desc_8))

        # 行 5
        eq_expand = MathTex(r"= 1 + \frac{a}{b} + \frac{3b}{a} + 3 = 4 + \left(\frac{a}{b} + \frac{3b}{a}\right)",
                            font_size=math_sz).next_to(eq_mul, DOWN, buff=line_buff)
        self.play(Write(eq_expand))
        self.wait(2)

        # 大清场
        self.play(FadeOut(top_group), FadeOut(desc_8), FadeOut(eq_mul))

        # 把推导出的核心等式置顶
        eq_core_func = MathTex(r"a+3b = 4 + \left(\frac{a}{b} + \frac{3b}{a}\right)", font_size=math_sz).set_color(
            YELLOW).to_edge(UP, buff=1)
        self.play(ReplacementTransform(eq_expand, eq_core_func))

        # ==================== 第四幕：基本不等式 (同屏最大行数: 5) ====================
        # 行 1 (eq_core_func 已在顶部)

        # 行 2
        desc_9 = Text("利用基本不等式求解最小边界：", font="KaiTi", font_size=text_sz).next_to(eq_core_func, DOWN,
                                                                                              buff=line_buff)
        self.play(Write(desc_9))

        # 行 3
        eq_amgm = MathTex(r"\frac{a}{b} + \frac{3b}{a} \ge 2\sqrt{\frac{a}{b} \cdot \frac{3b}{a}} = 2\sqrt{3}",
                          font_size=math_sz).set_color(BLUE).next_to(desc_9, DOWN, buff=line_buff)
        self.play(Write(eq_amgm))
        self.wait(1.5)

        # 行 4
        desc_10 = Text("代回原目标函数得出结果：", font="KaiTi", font_size=text_sz).next_to(eq_amgm, DOWN,
                                                                                           buff=line_buff)
        self.play(Write(desc_10))

        # 行 5
        eq_final_calc = MathTex(r"x+2y = \frac{a+3b-3}{2} \ge \frac{4+2\sqrt{3}-3}{2} = \frac{1+2\sqrt{3}}{2}",
                                font_size=math_sz).next_to(desc_10, DOWN, buff=line_buff)
        self.play(Write(eq_final_calc))
        self.wait(2)

        # 清场
        self.play(FadeOut(eq_core_func), FadeOut(desc_9), FadeOut(eq_amgm), FadeOut(desc_10), FadeOut(eq_final_calc))

        # ==================== 第五幕：取等条件验证 (同屏最大行数: 5) ====================
        # 行 1
        desc_11 = Text("最后，必须验证等号成立的条件：", font="KaiTi", font_size=text_sz).to_edge(UP, buff=1)
        self.play(Write(desc_11))

        # 行 2
        eq_equality = MathTex(r"\frac{a}{b} = \frac{3b}{a} \implies a = \sqrt{3}b", font_size=math_sz).set_color(
            BLUE).next_to(desc_11, DOWN, buff=line_buff)
        self.play(Write(eq_equality))
        self.wait(1)

        # 行 3
        desc_12 = Text("结合已知条件可解得相应的变量值：", font="KaiTi", font_size=text_sz).next_to(eq_equality, DOWN,
                                                                                                   buff=line_buff)
        self.play(Write(desc_12))

        # 行 4
        eq_vars = MathTex(r"b = 1 + \frac{\sqrt{3}}{3}, \quad a = \sqrt{3} + 1", font_size=math_sz).next_to(desc_12,
                                                                                                            DOWN,
                                                                                                            buff=line_buff)
        self.play(Write(eq_vars))
        self.wait(1)

        # 行 5
        desc_13_t1 = Text("此时", font="KaiTi", font_size=text_sz)
        desc_13_m1 = MathTex(r"x, y", font_size=math_sz).set_color(YELLOW)
        desc_13_t2 = Text("均大于零，满足初始定义域条件。", font="KaiTi", font_size=text_sz)
        desc_13 = VGroup(desc_13_t1, desc_13_m1, desc_13_t2).arrange(RIGHT, buff=0.1).next_to(eq_vars, DOWN,
                                                                                              buff=line_buff)
        self.play(Write(desc_13))
        self.wait(2)

        # 散场与结果展示
        self.play(FadeOut(desc_11), FadeOut(eq_equality), FadeOut(desc_12), FadeOut(eq_vars), FadeOut(desc_13))

        final_title = Text("因此，最小值为：", font="KaiTi", font_size=32).move_to(UP * 0.8)
        final_answer = MathTex(r"\frac{1+2\sqrt{3}}{2}", font_size=50).set_color(YELLOW).next_to(final_title, DOWN,
                                                                                                 buff=0.8)

        self.play(Write(final_title))
        self.play(FadeIn(final_answer, shift=UP))
        self.wait(3)

        # ==================== 剧终 ====================
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(1)