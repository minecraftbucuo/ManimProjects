# -*- coding: utf-8 -*-
# @Time    : 2026/3/26 22:31
# @Author  : MINEC
# @File    : 莱布尼茨公式证明.py
# @Software: PyCharm
from manim import *


class MathTexColor(MathTex):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_color_by_gradient(GREEN, BLUE, YELLOW)


class TextColor(Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_color_by_gradient(GREEN, BLUE, YELLOW)


class LeibnizFormulaProof(MovingCameraScene):
    def construct(self):
        # 设置边距
        LEFT_MARGIN = 1.2

        # ==========================================
        # 1. 开场标题
        # ==========================================
        title = Text("莱布尼茨公式的证明", font="KaiTi", font_size=50)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        title.to_edge(UP, buff=3)


        formula = MathTexColor(
            r"\frac{d}{dx} \int_{\alpha(x)}^{\beta(x)} f(x,y) \, dy = ",
            r"\int_{\alpha(x)}^{\beta(x)} f_x(x,y) \, dy + ",
            r"f(x,\beta(x))\beta'(x) - ",
            r"f(x,\alpha(x))\alpha'(x)",
            font_size=32
        )
        formula.next_to(title, DOWN, buff=2)

        # 初始镜头位置
        self.play(Write(title), run_time=0.8)
        self.play(Write(formula), run_time=1.5)
        self.wait(0.5)

        # 移动到第一步
        self.play(
            self.camera.frame.animate.move_to(DOWN),
            FadeOut(title, shift=UP * 0.5),
            FadeOut(formula, shift=UP * 0.5),
            run_time=1.5
        )

        # ==========================================
        # 2. 步骤1：函数定义与增量分析
        # ==========================================
        step1_title = TextColor("步骤1：函数定义与增量分析", font="KaiTi", font_size=28, color=BLUE)
        step1_title.to_edge(UP, buff=2).to_edge(LEFT, buff=LEFT_MARGIN)

        self.play(Write(step1_title))

        # 函数定义
        func_def = MathTexColor(
            r"\Phi(x) = \int_{\alpha(x)}^{\beta(x)} f(x,y) \, dy",
            font_size=30
        )
        func_def.next_to(step1_title, DOWN, buff=0.4).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(func_def))

        # 增量表达式
        delta_def = MathTexColor(
            r"\Delta\Phi = \Phi(x+\Delta x) - \Phi(x)",
            font_size=30
        )
        delta_def.next_to(func_def, DOWN, buff=0.3).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(delta_def))

        # 增量展开
        delta_expand = MathTexColor(
            r"= \int_{\alpha(x+\Delta x)}^{\beta(x+\Delta x)} f(x+\Delta x,y) \, dy - ",
            r"\int_{\alpha(x)}^{\beta(x)} f(x,y) \, dy",
            font_size=28
        )
        delta_expand.next_to(delta_def, DOWN, buff=0.3).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(delta_expand))

        # 移动到拆分为三部分的位置
        self.wait(0.5)
        self.play(
            self.camera.frame.animate.shift(DOWN * 1.5),
            run_time=1
        )

        # 拆分为三部分说明
        split_text = TextColor("将积分拆分为三部分：", font="KaiTi", font_size=24, color=YELLOW)
        split_text.next_to(delta_expand, DOWN, buff=0.5).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(split_text))

        # 拆分为三部分公式
        delta_parts = MathTexColor(
            r"\Delta\Phi = ",
            r"\underbrace{\int_{\alpha(x)}^{\beta(x)} [f(x+\Delta x,y)-f(x,y)]\,dy}_{(I)}",
            r"+",
            r"\underbrace{\int_{\beta(x)}^{\beta(x+\Delta x)} f(x+\Delta x,y)\,dy}_{(II)}",
            r"-",
            r"\underbrace{\int_{\alpha(x)}^{\alpha(x+\Delta x)} f(x+\Delta x,y)\,dy}_{(III)}",
            font_size=26
        )
        delta_parts.next_to(split_text, DOWN, buff=0.3).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(delta_parts))

        # 高亮三部分
        part1_box = SurroundingRectangle(delta_parts[1], color=GREEN, buff=0.05)
        part2_box = SurroundingRectangle(delta_parts[3], color=YELLOW, buff=0.05)
        part3_box = SurroundingRectangle(delta_parts[5], color=RED, buff=0.05)

        self.play(Create(part1_box), run_time=0.8)
        self.play(Create(part2_box), run_time=0.8)
        self.play(Create(part3_box), run_time=0.8)
        self.wait(0.5)

        # 清除第一部分内容
        self.play(
            FadeOut(step1_title),
            FadeOut(func_def),
            FadeOut(delta_def),
            FadeOut(delta_expand),
            FadeOut(split_text),
            FadeOut(part1_box),
            FadeOut(part2_box),
            FadeOut(part3_box),
            delta_parts.animate.move_to(UP * 1.5),
            run_time=1
        )

        # 镜头跟随第一部分
        self.play(
            self.camera.frame.animate.move_to(DOWN * 1),
            run_time=1
        )

        # ==========================================
        # 3. 步骤2：处理第一部分 (I)
        # ==========================================
        part1_title = TextColor("第一部分 (I)：被积函数的增量", font="KaiTi", font_size=26, color=GREEN)
        part1_title.next_to(delta_parts, DOWN, buff=1.5).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(part1_title))

        part1_eq1 = MathTexColor(
            r"\frac{(I)}{\Delta x} = \frac{1}{\Delta x}",
            r"\int_{\alpha(x)}^{\beta(x)} [f(x+\Delta x,y)-f(x,y)]\,dy",
            font_size=28
        )
        part1_eq1.next_to(part1_title, DOWN, buff=0.3).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(part1_eq1))

        # 镜头下移
        self.play(
            self.camera.frame.animate.shift(DOWN * 0.8),
            run_time=0.8
        )

        # 拉格朗日中值定理
        lagrange_text = TextColor("由拉格朗日中值定理：", font="KaiTi", font_size=22, color=WHITE)
        lagrange_text.next_to(part1_eq1, DOWN, buff=0.4).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(lagrange_text))

        lagrange_eq = MathTexColor(
            r"f(x+\Delta x,y)-f(x,y) = f_x(\xi,y)\Delta x",
            font_size=28
        )
        lagrange_eq.next_to(lagrange_text, DOWN, buff=0.2).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(lagrange_eq))

        where_text = TextColor("其中", font="KaiTi", font_size=20, color=WHITE)
        where_eq = MathTexColor(r"\xi \in (x, x+\Delta x)", font_size=24)
        where_group = VGroup(where_text, where_eq).arrange(RIGHT, buff=0.2)
        where_group.next_to(lagrange_eq, DOWN, buff=0.2).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(where_group))

        # 镜头下移
        self.play(
            self.camera.frame.animate.shift(DOWN * 0.6),
            run_time=0.8
        )

        # 代入并取极限
        part1_eq2 = MathTexColor(
            r"\Rightarrow \frac{(I)}{\Delta x} = ",
            r"\int_{\alpha(x)}^{\beta(x)} f_x(\xi, y) \, dy",
            font_size=28
        )
        part1_eq2.next_to(where_group, DOWN, buff=0.4).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(part1_eq2))

        part1_limit = MathTexColor(
            r"\lim_{\Delta x \to 0} \frac{(I)}{\Delta x} = ",
            r"\int_{\alpha(x)}^{\beta(x)} f_x(x, y) \, dy",
            font_size=28, color=ORANGE
        )
        part1_limit.next_to(part1_eq2, DOWN, buff=0.3).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(part1_limit))

        self.wait(0.5)

        # 清除第一部分，镜头移动到第二部分
        self.play(
            FadeOut(part1_title),
            FadeOut(part1_eq1),
            FadeOut(lagrange_text),
            FadeOut(lagrange_eq),
            FadeOut(where_group),
            FadeOut(part1_eq2),
            FadeOut(part1_limit),
            self.camera.frame.animate.move_to(DOWN * 1.5),
            delta_parts.animate.move_to(UP * 1.5),
            run_time=1
        )

        # ==========================================
        # 4. 步骤2：处理第二部分 (II)
        # ==========================================
        part2_title = TextColor("第二部分 (II)：上积分限的增量", font="KaiTi", font_size=26, color=YELLOW)
        part2_title.next_to(delta_parts, DOWN, buff=1.5).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(part2_title))

        part2_eq1 = MathTexColor(
            r"\frac{(II)}{\Delta x} = \frac{1}{\Delta x}",
            r"\int_{\beta(x)}^{\beta(x+\Delta x)} f(x+\Delta x,y)\,dy",
            font_size=28
        )
        part2_eq1.next_to(part2_title, DOWN, buff=0.3).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(part2_eq1))

        # 镜头下移
        self.play(
            self.camera.frame.animate.shift(DOWN * 0.8),
            run_time=0.8
        )

        # 积分中值定理
        integral_mean_text = TextColor("由积分中值定理：", font="KaiTi", font_size=22, color=WHITE)
        integral_mean_text.next_to(part2_eq1, DOWN, buff=0.4).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(integral_mean_text))

        integral_mean_eq = MathTexColor(
            r"= f(x+\Delta x, \eta) \cdot \frac{\beta(x+\Delta x) - \beta(x)}{\Delta x}",
            font_size=28
        )
        integral_mean_eq.next_to(integral_mean_text, DOWN, buff=0.2).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(integral_mean_eq))

        where_text2 = TextColor("其中", font="KaiTi", font_size=20, color=WHITE)
        where_eq2 = MathTexColor(r"\eta \in [\beta(x), \beta(x+\Delta x)]", font_size=24)
        where_group2 = VGroup(where_text2, where_eq2).arrange(RIGHT, buff=0.2)
        where_group2.next_to(integral_mean_eq, DOWN, buff=0.2).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(where_group2))

        # 镜头下移
        self.play(
            self.camera.frame.animate.shift(DOWN * 0.6),
            run_time=0.8
        )

        # 取极限
        part2_limit = MathTexColor(
            r"\lim_{\Delta x \to 0} \frac{(II)}{\Delta x} = ",
            r"f(x, \beta(x)) \cdot \beta'(x)",
            font_size=28, color=ORANGE
        )
        part2_limit.next_to(where_group2, DOWN, buff=0.4).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(part2_limit))

        self.wait(0.5)

        # 清除第二部分，镜头移动到第三部分
        self.play(
            FadeOut(part2_title),
            FadeOut(part2_eq1),
            FadeOut(integral_mean_text),
            FadeOut(integral_mean_eq),
            FadeOut(where_group2),
            FadeOut(part2_limit),
            self.camera.frame.animate.move_to(DOWN * 1.5),
            delta_parts.animate.move_to(UP * 1.5),
            run_time=1
        )

        # ==========================================
        # 5. 步骤2：处理第三部分 (III)
        # ==========================================
        part3_title = TextColor("第三部分 (III)：下积分限的增量", font="KaiTi", font_size=26, color=RED)
        part3_title.next_to(delta_parts, DOWN, buff=1.5).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(part3_title))

        part3_eq1 = MathTexColor(
            r"\frac{(III)}{\Delta x} = \frac{1}{\Delta x}",
            r"\int_{\alpha(x)}^{\alpha(x+\Delta x)} f(x+\Delta x,y)\,dy",
            font_size=28
        )
        part3_eq1.next_to(part3_title, DOWN, buff=0.3).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(part3_eq1))

        # 镜头下移
        self.play(
            self.camera.frame.animate.shift(DOWN * 0.8),
            run_time=0.8
        )

        # 积分中值定理
        integral_mean_text2 = TextColor("由积分中值定理：", font="KaiTi", font_size=22, color=WHITE)
        integral_mean_text2.next_to(part3_eq1, DOWN, buff=0.4).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(integral_mean_text2))

        integral_mean_eq2 = MathTexColor(
            r"= f(x+\Delta x, \zeta) \cdot \frac{\alpha(x+\Delta x) - \alpha(x)}{\Delta x}",
            font_size=28
        )
        integral_mean_eq2.next_to(integral_mean_text2, DOWN, buff=0.2).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(integral_mean_eq2))

        where_text3 = TextColor("其中", font="KaiTi", font_size=20, color=WHITE)
        where_eq3 = MathTexColor(r"\zeta \in [\alpha(x), \alpha(x+\Delta x)]", font_size=24)
        where_group3 = VGroup(where_text3, where_eq3).arrange(RIGHT, buff=0.2)
        where_group3.next_to(integral_mean_eq2, DOWN, buff=0.2).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(where_group3))

        # 镜头下移
        self.play(
            self.camera.frame.animate.shift(DOWN * 0.6),
            run_time=0.8
        )

        # 取极限
        part3_limit = MathTexColor(
            r"\lim_{\Delta x \to 0} \frac{(III)}{\Delta x} = ",
            r"f(x, \alpha(x)) \cdot \alpha'(x)",
            font_size=28, color=ORANGE
        )
        part3_limit.next_to(where_group3, DOWN, buff=0.4).to_edge(LEFT, buff=LEFT_MARGIN)
        self.play(Write(part3_limit))

        self.wait(0.5)

        # 清除所有内容，回到中心
        self.play(
            FadeOut(part3_title),
            FadeOut(part3_eq1),
            FadeOut(integral_mean_text2),
            FadeOut(integral_mean_eq2),
            FadeOut(where_group3),
            FadeOut(part3_limit),
            FadeOut(delta_parts),
            self.camera.frame.animate.move_to(ORIGIN).set_height(config["frame_height"]),
            run_time=1.5
        )

        # ==========================================
        # 6. 步骤3：合并结果
        # ==========================================
        step3_title = TextColor("步骤3：合并三部分结果", font="KaiTi", font_size=32, color=BLUE)
        step3_title.to_edge(UP, buff=0.5)

        self.play(Write(step3_title))

        # 导数定义
        derivative_def = MathTexColor(
            r"\Phi'(x) = \lim_{\Delta x\to 0} \frac{\Delta\Phi}{\Delta x}",
            font_size=34
        )
        derivative_def.next_to(step3_title, DOWN, buff=0.5)
        self.play(Write(derivative_def))

        # 合并公式
        combined_formula = MathTexColor(
            r"= \lim_{\Delta x\to 0} \frac{(I)}{\Delta x}",
            r"+ \lim_{\Delta x\to 0} \frac{(II)}{\Delta x}",
            r"- \lim_{\Delta x\to 0} \frac{(III)}{\Delta x}",
            font_size=30
        )
        combined_formula.next_to(derivative_def, DOWN, buff=0.3)
        self.play(Write(combined_formula))

        # 镜头下移
        self.play(
            self.camera.frame.animate.shift(DOWN * 1.2),
            run_time=1
        )

        # 代入三部分的结果
        result = MathTexColor(
            r"= \int_{\alpha(x)}^{\beta(x)} f_x(x,y)\,dy",
            r"+ f(x,\beta(x))\beta'(x)",
            r"- f(x,\alpha(x))\alpha'(x)",
            font_size=34, color=GREEN
        )
        result.next_to(combined_formula, DOWN, buff=0.5)
        self.play(Write(result), run_time=1.5)
        self.wait(0.5)

        # 镜头回到中心
        self.play(
            self.camera.frame.animate.move_to(ORIGIN).set_height(config["frame_height"]),
            run_time=1
        )

        # 清除合并步骤
        self.play(
            FadeOut(step3_title),
            FadeOut(derivative_def),
            FadeOut(combined_formula),
            FadeOut(result),
            run_time=0.8
        )

        # ==========================================
        # 7. 最终公式
        # ==========================================
        final_title = TextColor("莱布尼茨公式", font="KaiTi", font_size=40, color=YELLOW)
        final_title.to_edge(UP, buff=0.5)

        self.play(Write(final_title))

        # 7. 最终公式
        # ==========================================
        final_title = Text("莱布尼茨公式", font="KaiTi", font_size=40, color=YELLOW)
        final_title.to_edge(UP, buff=0.5)

        self.play(Write(final_title))

        # 最终公式（写在一行）
        final_formula = MathTexColor(
            r"\frac{d}{dx} \int_{\alpha(x)}^{\beta(x)} f(x,y) \, dy = ",
            r"\int_{\alpha(x)}^{\beta(x)} \frac{\partial f}{\partial x}(x,y) \, dy + ",
            r"f(x,\beta(x))\beta'(x) - f(x,\alpha(x))\alpha'(x)",
            font_size=36
        )
        final_formula.next_to(final_title, DOWN, buff=0.5)

        # 条件公式（用TextColor和MathTexColor组合）
        # 中文部分
        cond_chinese1 = TextColor("条件：", font="KaiTi", font_size=30, color=GRAY)
        cond_chinese2 = TextColor(" 连续, ", font="KaiTi", font_size=30, color=GRAY)
        cond_chinese3 = TextColor(" 可导", font="KaiTi", font_size=30, color=GRAY)

        # 公式部分
        cond_math1 = MathTexColor(r"f_x(x,y)", font_size=30, color=GRAY)
        cond_math2 = MathTexColor(r"\alpha(x), \beta(x)", font_size=30, color=GRAY)

        # 用VGroup组合
        conditions_tex = VGroup(
            cond_chinese1,
            cond_math1,
            cond_chinese2,
            cond_math2,
            cond_chinese3
        ).arrange(RIGHT, buff=0.1)
        conditions_tex.next_to(final_formula, DOWN, buff=0.3)

        # 用VGroup组合公式和条件
        final_group = VGroup(final_formula, conditions_tex)

        self.play(Write(final_formula), run_time=2)
        self.wait(0.5)
        self.play(Write(conditions_tex), run_time=1.5)

        # 用框框出最终公式和条件
        final_box = SurroundingRectangle(final_group, color=YELLOW, buff=0.3, corner_radius=0.1)
        self.play(Create(final_box), run_time=1)

        # 镜头放大公式
        self.play(
            self.camera.frame.animate.move_to(final_group.get_center()).scale(1.1),
            run_time=1.5
        )
        self.wait(1)

        self.wait(2)