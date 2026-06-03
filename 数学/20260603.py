from manim import *

class NestedFunctionIsomorphism(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("求解分式线性嵌套方程", font="KaiTi", font_size=45)
        title.set_color_by_gradient(BLUE, GREEN)

        eq_cover = MathTex(
            r"f(f(x)) = \frac{x-1}{x+1}",
            font_size=60
        ).set_color(BLUE)

        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))
        
        # ==================== 倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=180)
            countdown_text.set_color_by_gradient(GRAY, LIGHT_GRAY)
            countdown_text.move_to(ORIGIN)
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 第一幕：代数结构的观察与假设 ====================
        desc_1 = Text("首先，观察等号右侧已知函数的代数结构：", font="KaiTi", font_size=30)
        desc_1.to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        eq_g = MathTex(r"g(x) = \frac{x-1}{x+1}").set_color(BLUE).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(eq_g))
        self.wait(1.5)

        desc_2_t1 = Text("此函数属于标准的", font="KaiTi", font_size=28)
        desc_2_m1 = Text("分式线性变换", font="KaiTi", font_size=28).set_color(YELLOW)
        desc_2_t2 = Text("。", font="KaiTi", font_size=28)
        desc_2 = VGroup(desc_2_t1, desc_2_m1, desc_2_t2).arrange(RIGHT, buff=0.1).next_to(eq_g, DOWN, buff=0.5)
        self.play(Write(desc_2))

        desc_3_t1 = Text("基于函数复合运算的封闭性，合理假设未知函数", font="KaiTi", font_size=28)
        desc_3_m1 = MathTex(r"f(x)", font_size=30).set_color(GREEN)
        desc_3 = VGroup(desc_3_t1, desc_3_m1).arrange(RIGHT, buff=0.1).next_to(desc_2, DOWN, buff=0.3)
        
        desc_4 = Text("具有完全相同的分子分母线性结构：", font="KaiTi", font_size=28).next_to(desc_3, DOWN, buff=0.2)
        self.play(Write(desc_3), Write(desc_4))

        eq_f = MathTex(r"f(x) = \frac{ax+b}{cx+d}").set_color(GREEN).next_to(desc_4, DOWN, buff=0.4)
        self.play(Write(eq_f))
        self.wait(2)

        # 【全面清屏 1】防止拥挤
        self.play(
            FadeOut(desc_1), FadeOut(eq_g), FadeOut(desc_2), 
            FadeOut(desc_3), FadeOut(desc_4), FadeOut(eq_f)
        )

        # ==================== 第二幕：引入矩阵同构理论 ====================
        desc_5_t1 = Text("在处理此类函数时，若直接将", font="KaiTi", font_size=30)
        desc_5_m1 = MathTex(r"f(x)", font_size=32).set_color(GREEN)
        desc_5_t2 = Text("代入展开，计算将极其繁琐。", font="KaiTi", font_size=30)
        desc_5 = VGroup(desc_5_t1, desc_5_m1, desc_5_t2).arrange(RIGHT, buff=0.1).to_edge(UP, buff=0.8)
        self.play(Write(desc_5))

        desc_6 = Text("因此，我们引入同构理论：分式线性变换的复合运算，", font="KaiTi", font_size=28).next_to(desc_5, DOWN, buff=0.6)
        desc_7 = Text("在数学上严格等价于其对应系数矩阵的乘法运算。", font="KaiTi", font_size=28).next_to(desc_6, DOWN, buff=0.2)
        self.play(Write(desc_6), Write(desc_7))
        self.wait(1.5)

        desc_8_t1 = Text("提取已知函数", font="KaiTi", font_size=28)
        desc_8_m1 = MathTex(r"g(x)", font_size=30).set_color(BLUE)
        desc_8_t2 = Text("的各项系数，构造对应的变换矩阵", font="KaiTi", font_size=28)
        desc_8_m2 = MathTex(r"G", font_size=30).set_color(BLUE)
        desc_8_t3 = Text("：", font="KaiTi", font_size=28)
        desc_8 = VGroup(desc_8_t1, desc_8_m1, desc_8_t2, desc_8_m2, desc_8_t3).arrange(RIGHT, buff=0.1)
        desc_8.next_to(desc_7, DOWN, buff=0.6)
        self.play(Write(desc_8))

        eq_matrix_G = MathTex(
            r"g(x) = \frac{1 \cdot x - 1}{1 \cdot x + 1} \implies G = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}"
        ).set_color(BLUE).next_to(desc_8, DOWN, buff=0.4)
        self.play(Write(eq_matrix_G))
        self.wait(2)

        # 【全面清屏 2】保持矩阵 G，置于顶部
        self.play(
            FadeOut(desc_5), FadeOut(desc_6), FadeOut(desc_7), FadeOut(desc_8)
        )
        self.play(eq_matrix_G.animate.to_edge(UP, buff=0.8))

        # ==================== 第三幕：方程降维与常数因子的讨论 ====================
        desc_9_t1 = Text("令未知函数", font="KaiTi", font_size=28)
        desc_9_m1 = MathTex(r"f(x)", font_size=30).set_color(GREEN)
        desc_9_t2 = Text("对应的矩阵为", font="KaiTi", font_size=28)
        desc_9_m2 = MathTex(r"F", font_size=30).set_color(GREEN)
        desc_9_t3 = Text("。", font="KaiTi", font_size=28)
        desc_9 = VGroup(desc_9_t1, desc_9_m1, desc_9_t2, desc_9_m2, desc_9_t3).arrange(RIGHT, buff=0.1)
        desc_9.next_to(eq_matrix_G, DOWN, buff=0.5)
        self.play(Write(desc_9))

        desc_10 = Text("注意：分式的分子分母同时乘以非零常数，函数本身不改变。", font="KaiTi", font_size=28).next_to(desc_9, DOWN, buff=0.4)
        desc_11 = Text("这就意味着，在矩阵域中，两个矩阵即便相差一个纯量倍数，", font="KaiTi", font_size=28).next_to(desc_10, DOWN, buff=0.2)
        desc_12 = Text("它们依然表示同一个分式变换。", font="KaiTi", font_size=28).next_to(desc_11, DOWN, buff=0.2)
        self.play(Write(desc_10))
        self.play(Write(desc_11), Write(desc_12))

        desc_13_t1 = Text("于是，原方程", font="KaiTi", font_size=28)
        desc_13_m1 = MathTex(r"f(f(x)) = g(x)", font_size=30).set_color(BLUE)
        desc_13_t2 = Text("被降维转化为矩阵方程：", font="KaiTi", font_size=28)
        desc_13 = VGroup(desc_13_t1, desc_13_m1, desc_13_t2).arrange(RIGHT, buff=0.1).next_to(desc_12, DOWN, buff=0.5)
        self.play(Write(desc_13))

        eq_matrix_F2 = MathTex(r"F^2 = k \cdot G \quad (k \neq 0)").set_color(YELLOW).next_to(desc_13, DOWN, buff=0.3)
        rect_F2 = SurroundingRectangle(eq_matrix_F2, color=YELLOW, buff=0.15)
        self.play(Write(eq_matrix_F2), Create(rect_F2))
        self.wait(2)

        # 【全面清屏 3】准备进入几何视角的深度解析
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        # ==================== 第四幕：几何视角的旋转解析 ====================
        desc_14_t1 = Text("为了解出矩阵", font="KaiTi", font_size=30)
        desc_14_m1 = MathTex(r"F", font_size=32).set_color(GREEN)
        desc_14_t2 = Text("，我们需要探究矩阵", font="KaiTi", font_size=30)
        desc_14_m2 = MathTex(r"G", font_size=32).set_color(BLUE)
        desc_14_t3 = Text("的几何意义。", font="KaiTi", font_size=30)
        desc_14 = VGroup(desc_14_t1, desc_14_m1, desc_14_t2, desc_14_m2, desc_14_t3).arrange(RIGHT, buff=0.1)
        desc_14.to_edge(UP, buff=0.8)
        self.play(Write(desc_14))

        desc_15 = Text("提出模长因子后，它可以化为标准的二维旋转矩阵形式：", font="KaiTi", font_size=28).next_to(desc_14, DOWN, buff=0.4)
        self.play(Write(desc_15))

        eq_geom_G = MathTex(
            r"G = \sqrt{2} \begin{pmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{pmatrix} = \sqrt{2} \begin{pmatrix} \cos(\frac{\pi}{4}) & -\sin(\frac{\pi}{4}) \\ \sin(\frac{\pi}{4}) & \cos(\frac{\pi}{4}) \end{pmatrix}"
        ).scale(0.85).next_to(desc_15, DOWN, buff=0.5)
        self.play(Write(eq_geom_G))
        self.wait(1.5)

        desc_16_t1 = Text("这说明，该变换本质上是对平面进行", font="KaiTi", font_size=28)
        desc_16_m1 = MathTex(r"\frac{\pi}{4} \ (45^{\circ})", font_size=30).set_color(YELLOW)
        desc_16_t2 = Text("的旋转。", font="KaiTi", font_size=28)
        desc_16 = VGroup(desc_16_t1, desc_16_m1, desc_16_t2).arrange(RIGHT, buff=0.1).next_to(eq_geom_G, DOWN, buff=0.5)
        
        desc_17 = Text("前面的缩放常数可以在分式中被约去，不必关注。", font="KaiTi", font_size=26).set_color(LIGHT_GRAY).next_to(desc_16, DOWN, buff=0.2)
        self.play(Write(desc_16), Write(desc_17))
        self.wait(2)

        # 【全面清屏 4】过渡到 F 的推导
        self.play(
            FadeOut(desc_14), FadeOut(desc_15), FadeOut(eq_geom_G), 
            FadeOut(desc_16), FadeOut(desc_17)
        )

        # ==================== 第五幕：推导 F 矩阵 ====================
        desc_18_t1 = Text("既然矩阵", font="KaiTi", font_size=30)
        desc_18_m1 = MathTex(r"F", font_size=32).set_color(GREEN)
        desc_18_t2 = Text("连续作用两次（平方）等效于旋转", font="KaiTi", font_size=30)
        desc_18_m2 = MathTex(r"\frac{\pi}{4}", font_size=32).set_color(YELLOW)
        desc_18_t3 = Text("，", font="KaiTi", font_size=30)
        desc_18 = VGroup(desc_18_t1, desc_18_m1, desc_18_t2, desc_18_m2, desc_18_t3).arrange(RIGHT, buff=0.1)
        desc_18.to_edge(UP, buff=0.8)
        self.play(Write(desc_18))

        desc_19 = Text("那么它自身作用一次，理应代表旋转一半的角度：", font="KaiTi", font_size=28).next_to(desc_18, DOWN, buff=0.3)
        self.play(Write(desc_19))

        eq_F_rot = MathTex(
            r"F \sim \begin{pmatrix} \cos(\frac{\pi}{8}) & -\sin(\frac{\pi}{8}) \\ \sin(\frac{\pi}{8}) & \cos(\frac{\pi}{8}) \end{pmatrix}"
        ).set_color(GREEN).scale(0.9).next_to(desc_19, DOWN, buff=0.5)
        self.play(Write(eq_F_rot))
        self.wait(1.5)

        desc_20 = Text("为了便于化简为代数式，我们提取余弦项作为常数因子：", font="KaiTi", font_size=28).next_to(eq_F_rot, DOWN, buff=0.5)
        self.play(Write(desc_20))

        eq_F_tan = MathTex(
            r"F \sim \cos(\frac{\pi}{8}) \begin{pmatrix} 1 & -\tan(\frac{\pi}{8}) \\ \tan(\frac{\pi}{8}) & 1 \end{pmatrix} \sim \begin{pmatrix} 1 & -\tan(\frac{\pi}{8}) \\ \tan(\frac{\pi}{8}) & 1 \end{pmatrix}"
        ).set_color(GREEN).scale(0.9).next_to(desc_20, DOWN, buff=0.4)
        self.play(Write(eq_F_tan))
        self.wait(2)

        # 【全面清屏 5】准备纯净的计算环境
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        # ==================== 第六幕：最终的数值计算与还原 ====================
        desc_21 = Text("现在的任务是求出正切值。利用三角半角公式：", font="KaiTi", font_size=30).to_edge(UP, buff=0.8)
        self.play(Write(desc_21))

        eq_tan = MathTex(
            r"\frac{2\tan(\frac{\pi}{8})}{1-\tan^2(\frac{\pi}{8})} = \tan(\frac{\pi}{4}) = 1"
        ).next_to(desc_21, DOWN, buff=0.5)
        
        # 修复点：严格分离 LaTeX 公式和中文 Text，不再把中文放入 MathTex
        eq_tan_ans_math = MathTex(
            r"\implies \tan(\frac{\pi}{8}) = \sqrt{2} - 1"
        )
        eq_tan_ans_text = Text("(取正根)", font="KaiTi", font_size=26)
        eq_tan_ans = VGroup(eq_tan_ans_math, eq_tan_ans_text).arrange(RIGHT, buff=0.3).set_color(YELLOW).next_to(eq_tan, DOWN, buff=0.4)
        
        self.play(Write(eq_tan))
        self.play(Write(eq_tan_ans))
        self.wait(1.5)

        desc_22 = Text("将数值代回矩阵结构中，我们得到了目标系数矩阵：", font="KaiTi", font_size=28).next_to(eq_tan_ans, DOWN, buff=0.6)
        self.play(Write(desc_22))

        eq_F_final = MathTex(
            r"F' = \begin{pmatrix} 1 & 1-\sqrt{2} \\ \sqrt{2}-1 & 1 \end{pmatrix}"
        ).set_color(GREEN).next_to(desc_22, DOWN, buff=0.4)
        self.play(Write(eq_F_final))
        self.wait(2)

        # 【全面清屏 6】展示最终解
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )

        desc_23 = Text("最后一步，将矩阵重新翻译为分式线性函数的代数表达：", font="KaiTi", font_size=32).to_edge(UP, buff=1.2)
        self.play(Write(desc_23))

        eq_func_f1 = MathTex(
            r"f_1(x) = \frac{x + 1 - \sqrt{2}}{(\sqrt{2}-1)x + 1}"
        ).scale(1.3).set_color(YELLOW).next_to(desc_23, DOWN, buff=1.0)
        rect_f1 = SurroundingRectangle(eq_func_f1, color=YELLOW, buff=0.25)
        self.play(Write(eq_func_f1), Create(rect_f1))
        self.wait(3)

        # ==================== 第七幕：多解的补充说明与退场 ====================
        self.play(
            FadeOut(desc_23)
        )
        grp_ans = VGroup(eq_func_f1, rect_f1)
        self.play(grp_ans.animate.to_edge(UP, buff=1.0))

        desc_24_t1 = Text("值得补充的是，考虑三角函数的周期性，", font="KaiTi", font_size=28)
        desc_24_m1 = MathTex(r"\frac{5\pi}{8}", font_size=30).set_color(BLUE)
        desc_24_t2 = Text("旋转两倍后", font="KaiTi", font_size=28)
        desc_24 = VGroup(desc_24_t1, desc_24_m1, desc_24_t2).arrange(RIGHT, buff=0.1).next_to(grp_ans, DOWN, buff=0.8)
        
        desc_25_t1 = Text("与原角度相差", font="KaiTi", font_size=28)
        desc_25_m1 = MathTex(r"2\pi", font_size=30).set_color(BLUE)
        desc_25_t2 = Text("，因此同样满足方程的代数约束。", font="KaiTi", font_size=28)
        desc_25 = VGroup(desc_25_t1, desc_25_m1, desc_25_t2).arrange(RIGHT, buff=0.1).next_to(desc_24, DOWN, buff=0.2)
        self.play(Write(desc_24), Write(desc_25))
        self.wait(1)

        desc_26 = Text("依此同理可求得另一个有效的解答：", font="KaiTi", font_size=28).next_to(desc_25, DOWN, buff=0.5)
        self.play(Write(desc_26))

        eq_func_f2 = MathTex(
            r"f_2(x) = \frac{x + 1 + \sqrt{2}}{-(1+\sqrt{2})x + 1}"
        ).scale(1.2).set_color(YELLOW).next_to(desc_26, DOWN, buff=0.5)
        self.play(FadeIn(eq_func_f2, shift=UP))
        self.wait(3.5)

        # ==================== 散场 ====================
        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)