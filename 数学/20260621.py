from manim import *

# 强制设置竖屏分辨率和自适应帧大小
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 8.0
config.frame_height = 14.22

class MinimumIntegerWith21Divisors(Scene):
    def construct(self):
        # ==================== 封面 ====================
        # 第一行：求具有
        title_part1 = Text("求具有 ", font="KaiTi", font_size=35)
        title_math_n = MathTex(r"21", font_size=40).set_color(YELLOW)
        title_part2 = Text(" 个正因数的", font="KaiTi", font_size=35)
        title_line1 = VGroup(title_part1, title_math_n, title_part2).arrange(RIGHT, buff=0.1)

        # 第二行：最小正整数（突出显示）
        title_line2 = Text("最小正整数", font="KaiTi", font_size=50).set_color(BLUE)

        # 将两行垂直组合，作为整体封面
        cover = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.6)
        cover.move_to(UP * 2)
        
        # 依次播放封面动画
        self.play(Write(title_line1))
        self.play(FadeIn(title_line2, shift=UP))
        self.wait(0.5)
        
        # ==================== 3秒高燃倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=160)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            # 定位在封面的正下方，避免遮挡
            countdown_text.next_to(cover, DOWN, buff=1.5)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：约数个数定理 ====================
        part_1_title = Text("第一部分：约数个数定理", font="KaiTi", font_size=32).to_edge(UP, buff=1.5)
        self.play(Write(part_1_title))

        desc_1_text1 = Text("设正整数", font="KaiTi", font_size=26)
        desc_1_math1 = MathTex(r"N", font_size=30).set_color(YELLOW)
        desc_1_text2 = Text("的标准素因数分解为：", font="KaiTi", font_size=26)
        desc_1 = VGroup(desc_1_text1, desc_1_math1, desc_1_text2).arrange(RIGHT, buff=0.1).next_to(part_1_title, DOWN, buff=0.8)
        self.play(Write(desc_1))

        eq_1 = MathTex(r"N = p_1^{a_1} \cdot p_2^{a_2} \cdots p_k^{a_k}", font_size=36).set_color(BLUE).next_to(desc_1, DOWN, buff=0.4)
        self.play(Write(eq_1))
        self.wait(1)

        desc_2_text1 = Text("其正因数个数", font="KaiTi", font_size=26)
        desc_2_math1 = MathTex(r"d(N)", font_size=30).set_color(YELLOW)
        desc_2_text2 = Text("的计算公式为：", font="KaiTi", font_size=26)
        desc_2 = VGroup(desc_2_text1, desc_2_math1, desc_2_text2).arrange(RIGHT, buff=0.1).next_to(eq_1, DOWN, buff=0.8)
        self.play(Write(desc_2))

        eq_2 = MathTex(r"d(N) = (a_1 + 1)(a_2 + 1) \cdots (a_k + 1)", font_size=34).set_color(BLUE).next_to(desc_2, DOWN, buff=0.4)
        self.play(Write(eq_2))
        self.wait(1)

        desc_3_text1 = Text("已知题目要求", font="KaiTi", font_size=26)
        desc_3_math1 = MathTex(r"d(N) = 21", font_size=30).set_color(YELLOW)
        desc_3_text2 = Text("，需要对此进行逆推。", font="KaiTi", font_size=26)
        desc_3 = VGroup(desc_3_text1, desc_3_math1, desc_3_text2).arrange(RIGHT, buff=0.1).next_to(eq_2, DOWN, buff=0.8)
        self.play(Write(desc_3))
        self.wait(2)

        # 暴力清场，准备第二部分
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 第二幕：分解目标值 ====================
        part_2_title = Text("第二部分：分解目标值", font="KaiTi", font_size=32).to_edge(UP, buff=1.5)
        self.play(Write(part_2_title))

        desc_4_text1 = Text("将数字", font="KaiTi", font_size=26)
        desc_4_math1 = MathTex(r"21", font_size=30).set_color(YELLOW)
        desc_4_text2 = Text("分解为大于", font="KaiTi", font_size=26)
        desc_4_math2 = MathTex(r"1", font_size=30).set_color(YELLOW)
        desc_4_text3 = Text("的整数乘积：", font="KaiTi", font_size=26)
        desc_4 = VGroup(desc_4_text1, desc_4_math1, desc_4_text2, desc_4_math2, desc_4_text3).arrange(RIGHT, buff=0.1).next_to(part_2_title, DOWN, buff=0.8)
        self.play(Write(desc_4))

        eq_3_text1 = Text("情况一（单因子）：", font="KaiTi", font_size=26)
        eq_3_math1 = MathTex(r"21 = 21", font_size=36).set_color(GREEN)
        eq_3 = VGroup(eq_3_text1, eq_3_math1).arrange(RIGHT, buff=0.3).next_to(desc_4, DOWN, buff=0.6)
        self.play(Write(eq_3))

        eq_4_text1 = Text("情况二（双因子）：", font="KaiTi", font_size=26)
        eq_4_math1 = MathTex(r"21 = 7 \times 3", font_size=36).set_color(GREEN)
        eq_4 = VGroup(eq_4_text1, eq_4_math1).arrange(RIGHT, buff=0.3).next_to(eq_3, DOWN, buff=0.5)
        self.play(Write(eq_4))
        self.wait(1.5)

        # 断行处理，防止超出边界
        desc_5_line1_t1 = Text("对应的", font="KaiTi", font_size=26)
        desc_5_line1_m1 = MathTex(r"N", font_size=30).set_color(YELLOW)
        desc_5_line1_t2 = Text("的素因子结构", font="KaiTi", font_size=26)
        desc_5_line1 = VGroup(desc_5_line1_t1, desc_5_line1_m1, desc_5_line1_t2).arrange(RIGHT, buff=0.1)
        
        desc_5_line2 = Text("必然为以下两种形态：", font="KaiTi", font_size=26)
        
        desc_5 = VGroup(desc_5_line1, desc_5_line2).arrange(DOWN, buff=0.2).next_to(eq_4, DOWN, buff=0.8)
        self.play(Write(desc_5))

        eq_5_text1 = Text("形态一：", font="KaiTi", font_size=26)
        eq_5_math1 = MathTex(r"N = p_1^{20}", font_size=36).set_color(BLUE)
        eq_5 = VGroup(eq_5_text1, eq_5_math1).arrange(RIGHT, buff=0.3).next_to(desc_5, DOWN, buff=0.5)
        self.play(Write(eq_5))

        eq_6_text1 = Text("形态二：", font="KaiTi", font_size=26)
        eq_6_math1 = MathTex(r"N = p_1^6 \cdot p_2^2", font_size=36).set_color(BLUE)
        eq_6 = VGroup(eq_6_text1, eq_6_math1).arrange(RIGHT, buff=0.3).next_to(eq_5, DOWN, buff=0.5)
        self.play(Write(eq_6))
        self.wait(2)

        # 清场
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 第三幕：最小值分析 ====================
        part_3_title = Text("第三部分：求最小值分析", font="KaiTi", font_size=32).to_edge(UP, buff=1.5)
        self.play(Write(part_3_title))

        # 断行处理：为使 N 尽可能小...
        desc_6_line1_t1 = Text("为使", font="KaiTi", font_size=26)
        desc_6_line1_m1 = MathTex(r"N", font_size=30).set_color(YELLOW)
        desc_6_line1_t2 = Text("尽可能小，", font="KaiTi", font_size=26)
        desc_6_line1 = VGroup(desc_6_line1_t1, desc_6_line1_m1, desc_6_line1_t2).arrange(RIGHT, buff=0.1)
        
        desc_6_line2 = Text("应将较大的指数分配给较小的素数。", font="KaiTi", font_size=26)
        
        desc_6 = VGroup(desc_6_line1, desc_6_line2).arrange(DOWN, buff=0.2).next_to(part_3_title, DOWN, buff=0.8)
        self.play(Write(desc_6))

        desc_7_text1 = Text("正整数从小到大的素数依次为：", font="KaiTi", font_size=24)
        desc_7_math1 = MathTex(r"2, 3, 5, \dots", font_size=30).set_color(BLUE)
        desc_7 = VGroup(desc_7_text1, desc_7_math1).arrange(RIGHT, buff=0.1).next_to(desc_6, DOWN, buff=0.6)
        self.play(Write(desc_7))
        self.wait(1)

        # 形态一计算
        desc_8_text1 = Text("对于形态一", font="KaiTi", font_size=26)
        desc_8_math1 = MathTex(r"N = p_1^{20}", font_size=30).set_color(YELLOW)
        desc_8_text2 = Text("，取最小素数", font="KaiTi", font_size=26)
        desc_8_math2 = MathTex(r"2", font_size=30).set_color(YELLOW)
        desc_8_text3 = Text("：", font="KaiTi", font_size=26)
        # 这句不长，可以单行
        desc_8 = VGroup(desc_8_text1, desc_8_math1, desc_8_text2, desc_8_math2, desc_8_text3).arrange(RIGHT, buff=0.1).next_to(desc_7, DOWN, buff=0.8)
        self.play(Write(desc_8))

        eq_7 = MathTex(r"N = 2^{20} = 1048576", font_size=36).set_color(GREEN).next_to(desc_8, DOWN, buff=0.4)
        self.play(Write(eq_7))
        self.wait(1)

        # 形态二计算
        desc_9_text1 = Text("对于形态二", font="KaiTi", font_size=26)
        desc_9_math1 = MathTex(r"N = p_1^6 \cdot p_2^2", font_size=30).set_color(YELLOW)
        desc_9_text2 = Text("：", font="KaiTi", font_size=26)
        desc_9 = VGroup(desc_9_text1, desc_9_math1, desc_9_text2).arrange(RIGHT, buff=0.1).next_to(eq_7, DOWN, buff=0.8)
        self.play(Write(desc_9))

        # 断行处理：将指数分配给素数...
        desc_10_line1_t1 = Text("将指数", font="KaiTi", font_size=26)
        desc_10_line1_m1 = MathTex(r"6", font_size=30).set_color(YELLOW)
        desc_10_line1_t2 = Text("和", font="KaiTi", font_size=26)
        desc_10_line1_m2 = MathTex(r"2", font_size=30).set_color(YELLOW)
        desc_10_line1 = VGroup(desc_10_line1_t1, desc_10_line1_m1, desc_10_line1_t2, desc_10_line1_m2).arrange(RIGHT, buff=0.1)

        desc_10_line2_t1 = Text("分别分配给素数", font="KaiTi", font_size=26)
        desc_10_line2_m1 = MathTex(r"2", font_size=30).set_color(YELLOW)
        desc_10_line2_t2 = Text("和", font="KaiTi", font_size=26)
        desc_10_line2_m2 = MathTex(r"3", font_size=30).set_color(YELLOW)
        desc_10_line2 = VGroup(desc_10_line2_t1, desc_10_line2_m1, desc_10_line2_t2, desc_10_line2_m2).arrange(RIGHT, buff=0.1)
        
        desc_10 = VGroup(desc_10_line1, desc_10_line2).arrange(DOWN, buff=0.2).next_to(desc_9, DOWN, buff=0.4)
        self.play(Write(desc_10))

        eq_8 = MathTex(r"N = 2^6 \cdot 3^2", font_size=36).set_color(GREEN).next_to(desc_10, DOWN, buff=0.4)
        self.play(Write(eq_8))
        
        eq_9 = MathTex(r"N = 64 \times 9 = 576", font_size=36).set_color(GREEN).next_to(desc_10, DOWN, buff=0.4)
        self.play(ReplacementTransform(eq_8, eq_9))
        self.wait(2)

        # 清场
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 第四幕：最终结论 ====================
        outro_1 = Text("对比两种形态取得的极小值：", font="KaiTi", font_size=28).move_to(UP * 1.5)
        self.play(Write(outro_1))

        eq_10 = MathTex(r"576 < 1048576", font_size=45).set_color(YELLOW).next_to(outro_1, DOWN, buff=0.8)
        self.play(Write(eq_10))
        self.wait(1)

        outro_2 = Text("因此，满足条件的最小正整数为：", font="KaiTi", font_size=28).next_to(eq_10, DOWN, buff=1.2)
        self.play(Write(outro_2))

        final_ans = MathTex(r"576", font_size=80).set_color_by_gradient(YELLOW, GREEN).next_to(outro_2, DOWN, buff=0.8)
        self.play(FadeIn(final_ans, shift=UP))
        self.wait(3)

        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(1)