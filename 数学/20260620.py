from manim import *

# 强制设置竖屏分辨率和自适应帧大小
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 8.0
config.frame_height = 14.22

class PerfectSquareProofVertical(Scene):
    def construct(self):
        # ==================== 封面 ====================
        # 第一行：求所有正整数 n 使
        title_part1 = Text("求所有正整数 ", font="KaiTi", font_size=35)
        title_math_n = MathTex(r"n", font_size=40).set_color(YELLOW)
        title_part2 = Text(" 使", font="KaiTi", font_size=35)
        title_line1 = VGroup(title_part1, title_math_n, title_part2).arrange(RIGHT, buff=0.1)

        # 第二行：表达式（突出显示）
        title_math_eq = MathTex(r"n^2 + 2n + 12", font_size=55).set_color(BLUE)
        
        # 第三行：为完全平方数
        title_line3 = Text("为完全平方数", font="KaiTi", font_size=35)

        # 将三行垂直组合，作为整体封面
        cover = VGroup(title_line1, title_math_eq, title_line3).arrange(DOWN, buff=0.6)
        cover.move_to(UP * 2)
        
        # 依次播放封面动画
        self.play(Write(title_line1))
        self.play(FadeIn(title_math_eq, shift=UP))
        self.play(Write(title_line3))
        self.wait(0.5)
        
        # ==================== 3秒高燃倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=160)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            # 定位在封面的正下方
            countdown_text.next_to(cover, DOWN, buff=1.5)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：配方与因式分解 ====================
        method_1_title = Text("解法一：配方与因式分解法", font="KaiTi", font_size=32).to_edge(UP, buff=1.5)
        self.play(Write(method_1_title))

        desc_1_text1 = Text("首先，假设该式等于正整数", font="KaiTi", font_size=26)
        desc_1_math1 = MathTex(r"m", font_size=30).set_color(YELLOW)
        desc_1_text2 = Text("的平方：", font="KaiTi", font_size=26)
        desc_1 = VGroup(desc_1_text1, desc_1_math1, desc_1_text2).arrange(RIGHT, buff=0.1).next_to(method_1_title, DOWN, buff=0.8)
        self.play(Write(desc_1))

        eq_sq_orig = MathTex(r"n^2 + 2n + 12 = m^2", font_size=40).set_color(BLUE).next_to(desc_1, DOWN, buff=0.4)
        self.play(Write(eq_sq_orig))
        self.wait(1)

        desc_2 = Text("对等式左边的前两项进行配方：", font="KaiTi", font_size=26).next_to(eq_sq_orig, DOWN, buff=0.8)
        self.play(Write(desc_2))

        eq_sq_1 = MathTex(r"(n^2 + 2n + 1) + 11 = m^2", font_size=40).set_color(BLUE).next_to(desc_2, DOWN, buff=0.4)
        self.play(Write(eq_sq_1))
        
        eq_sq_2 = MathTex(r"(n+1)^2 + 11 = m^2", font_size=40).set_color(BLUE).next_to(desc_2, DOWN, buff=0.4)
        self.play(ReplacementTransform(eq_sq_1, eq_sq_2))
        self.wait(1)

        desc_3 = Text("移项并利用平方差公式展开：", font="KaiTi", font_size=26).next_to(eq_sq_2, DOWN, buff=0.8)
        self.play(Write(desc_3))

        eq_sq_3 = MathTex(r"m^2 - (n+1)^2 = 11", font_size=40).set_color(YELLOW).next_to(desc_3, DOWN, buff=0.4)
        self.play(Write(eq_sq_3))

        eq_sq_final = MathTex(r"(m - n - 1)(m + n + 1) = 11", font_size=36).set_color(YELLOW).next_to(desc_3, DOWN, buff=0.4)
        self.play(ReplacementTransform(eq_sq_3, eq_sq_final))
        self.wait(2)

        # 整理屏幕，保留核心方程
        self.play(
            FadeOut(method_1_title), FadeOut(desc_1), FadeOut(eq_sq_orig), 
            FadeOut(desc_2), FadeOut(eq_sq_2), FadeOut(desc_3)
        )
        self.play(eq_sq_final.animate.to_edge(UP, buff=1.5).scale(1.1))

        # ==================== 第二幕：素数性质与求解 ====================
        desc_4_text1 = Text("因为", font="KaiTi", font_size=26)
        desc_4_math1 = MathTex(r"11", font_size=30).set_color(YELLOW)
        desc_4_text2 = Text("是质数，且各字母均为正整数", font="KaiTi", font_size=26)
        desc_4 = VGroup(desc_4_text1, desc_4_math1, desc_4_text2).arrange(RIGHT, buff=0.1).next_to(eq_sq_final, DOWN, buff=0.8)
        self.play(Write(desc_4))

        desc_5 = Text("所以两因式只能分别对应 1 和 11：", font="KaiTi", font_size=26).next_to(desc_4, DOWN, buff=0.3)
        self.play(Write(desc_5))

        sys_eq = MathTex(
            r"\begin{cases} m - n - 1 = 1 \\ m + n + 1 = 11 \end{cases}", 
            font_size=40
        ).set_color(GREEN).next_to(desc_5, DOWN, buff=0.6)
        self.play(Write(sys_eq))
        self.wait(1.5)

        desc_6_text1 = Text("两式相减，消去", font="KaiTi", font_size=26)
        desc_6_math1 = MathTex(r"m", font_size=30).set_color(YELLOW)
        desc_6_text2 = Text("，可解得", font="KaiTi", font_size=26)
        desc_6_math2 = MathTex(r"n", font_size=30).set_color(YELLOW)
        desc_6_text3 = Text("的值：", font="KaiTi", font_size=26)
        desc_6 = VGroup(desc_6_text1, desc_6_math1, desc_6_text2, desc_6_math2, desc_6_text3).arrange(RIGHT, buff=0.1).next_to(sys_eq, DOWN, buff=0.8)
        self.play(Write(desc_6))

        ans_eq_1 = MathTex(r"2n + 2 = 10", font_size=40).set_color(YELLOW).next_to(desc_6, DOWN, buff=0.5)
        ans_eq_2 = MathTex(r"n = 4", font_size=50).set_color(YELLOW).next_to(desc_6, DOWN, buff=0.5)
        self.play(Write(ans_eq_1))
        self.wait(1)
        self.play(ReplacementTransform(ans_eq_1, ans_eq_2))
        self.wait(2)

        # 暴力清场，准备下一种方法
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 第三幕：放缩与夹逼法 ====================
        method_2_title = Text("解法二：放缩与夹逼法", font="KaiTi", font_size=32).to_edge(UP, buff=1.5)
        self.play(Write(method_2_title))

        desc_8_text1 = Text("观察原式", font="KaiTi", font_size=26)
        desc_8_math = MathTex(r"n^2 + 2n + 12", font_size=30).set_color(BLUE)
        desc_8_text2 = Text("的大小范围：", font="KaiTi", font_size=26)
        desc_8 = VGroup(desc_8_text1, desc_8_math, desc_8_text2).arrange(RIGHT, buff=0.1).next_to(method_2_title, DOWN, buff=0.8)
        self.play(Write(desc_8))

        desc_9 = Text("显然，它存在一个严密的下界：", font="KaiTi", font_size=26).next_to(desc_8, DOWN, buff=0.6)
        self.play(Write(desc_9))

        eq_bound_1 = MathTex(r"n^2 + 2n + 12 > (n+1)^2", font_size=38).set_color(GREEN).next_to(desc_9, DOWN, buff=0.4)
        self.play(Write(eq_bound_1))
        self.wait(1.5)

        desc_10 = Text("接下来寻找上界，考察后续平方数：", font="KaiTi", font_size=26).next_to(eq_bound_1, DOWN, buff=0.8)
        self.play(Write(desc_10))

        eq_bound_2 = MathTex(r"n^2 + 2n + 12 < (n+3)^2", font_size=38).set_color(GREEN).next_to(desc_10, DOWN, buff=0.4)
        self.play(Write(eq_bound_2))
        self.wait(1)

        desc_11 = Text("（展开为 4n > 3，对正整数恒成立）", font="KaiTi", font_size=22, color=GRAY).next_to(eq_bound_2, DOWN, buff=0.3)
        self.play(Write(desc_11))
        self.wait(2)

        # 清理下半部分屏幕，防止溢出
        self.play(
            FadeOut(desc_8), FadeOut(desc_9), FadeOut(eq_bound_1), 
            FadeOut(desc_10), FadeOut(eq_bound_2), FadeOut(desc_11)
        )

        # ==================== 第四幕：得出唯一解 ====================
        desc_12 = Text("由此可知，原式被夹在\n两个次邻的完全平方数之间：", font="KaiTi", font_size=26, line_spacing=1.2).next_to(method_2_title, DOWN, buff=1)
        self.play(Write(desc_12))

        eq_squeeze = MathTex(r"(n+1)^2 < n^2 + 2n + 12 < (n+3)^2", font_size=32).set_color(YELLOW).next_to(desc_12, DOWN, buff=0.6)
        self.play(Write(eq_squeeze))
        self.wait(1.5)

        desc_13 = Text("要使其本身成为完全平方数，\n它只能等于中间唯一的那个值：", font="KaiTi", font_size=26, line_spacing=1.2).next_to(eq_squeeze, DOWN, buff=0.8)
        self.play(Write(desc_13))

        eq_final_2 = MathTex(r"n^2 + 2n + 12 = (n+2)^2", font_size=40).set_color(BLUE).next_to(desc_13, DOWN, buff=0.6)
        self.play(Write(eq_final_2))
        self.wait(1)

        eq_final_3 = MathTex(r"n^2 + 2n + 12 = n^2 + 4n + 4", font_size=40).set_color(BLUE).next_to(desc_13, DOWN, buff=0.6)
        self.play(ReplacementTransform(eq_final_2, eq_final_3))
        self.wait(1)
        
        eq_final_4 = MathTex(r"2n = 8 \implies n = 4", font_size=45).set_color(YELLOW).next_to(eq_final_3, DOWN, buff=0.8)
        self.play(Write(eq_final_4))
        self.wait(3)

        # 清场
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 散场总结 ====================
        outro_1 = Text("两种方法殊途同归，最终结果均为：", font="KaiTi", font_size=28).move_to(UP * 1)
        self.play(Write(outro_1))

        final_ans = MathTex(r"n = 4").scale(2.5).set_color_by_gradient(YELLOW, GREEN).next_to(outro_1, DOWN, buff=1)
        self.play(FadeIn(final_ans, shift=UP))
        self.wait(3)

        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(1)