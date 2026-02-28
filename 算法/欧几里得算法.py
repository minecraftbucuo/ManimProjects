# -*- coding: utf-8 -*-
# @Time    : 2026/2/28 16:02
# @Author  : MINEC + AI
# @File    : 欧几里得算法.py
# @Software: PyCharm
import math

from manim import *


class CppEuclideanCode(Scene):
    def construct(self):
        title = Text("算法实现代码（C++）", font_size=36).to_edge(UP)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)
        self.play(Write(title))

        # 非递归版本
        iterative_code = Code(
            code="""int gcd_iterative(int a, int b) {
    while (b != 0) {
        int temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}""",
            tab_width=4,
            background="window",
            language="cpp",
            font="Consolas",
            font_size=20
        )
        iterative_code.next_to(title, DOWN, buff=0.5)

        # 递归版本
        recursive_code = Code(
            code="""int gcd_recursive(int a, int b) {
    if (b == 0) return a;
    return gcd_recursive(b, a % b);
}""",
            tab_width=4,
            background="window",
            language="cpp",
            font="Consolas",
            font_size=20
        )
        recursive_code.next_to(iterative_code, DOWN, buff=1)

        self.play(Create(iterative_code))
        self.wait(2)
        self.play(Create(recursive_code))
        self.wait(3)

        self.play(
            FadeOut(title),
            FadeOut(iterative_code),
            FadeOut(recursive_code)
        )


class EuclideanAlgorithm(Scene):
    def construct(self):
        # ========== 顶部标题区（全程保留）==========
        self.title = Text("欧几里得算法（辗转相除法）", font_size=36, color=BLUE)
        self.title.to_edge(UP, buff=0.3)
        self.subtitle = Text("几何演示：最大公约数计算", font_size=26, color=YELLOW)
        self.subtitle.next_to(self.title, DOWN, buff=0.1)
        self.play(Write(self.title), Write(self.subtitle))
        self.wait(1.5)

        # ========== 初始化数据 ==========
        a, b = 48, 18
        gcd_val = math.gcd(a, b)
        scale = 0.15  # 适配16:9屏幕

        # ========== 步骤1：a ÷ b = q ... r ==========
        # 清理区：确保无残留
        self.clear_step_elements()

        # 数字显示（标题下方安全区）
        nums = VGroup(
            Text(f"a = {a}", color=RED, font_size=32),
            Text(f"b = {b}", color=GREEN, font_size=32)
        ).arrange(RIGHT, buff=2).next_to(self.subtitle, DOWN, buff=0.8)
        self.play(FadeIn(nums))
        self.wait(0.8)

        # 可视化区（严格居中，预留上下空间）
        rect_a = Rectangle(height=0.7, width=a * scale, color=RED, fill_opacity=0.3)
        rect_b = Rectangle(height=0.7, width=b * scale, color=GREEN, fill_opacity=0.3)
        rects = VGroup(rect_a, rect_b).arrange(DOWN, buff=1.0).move_to(ORIGIN)

        labels = VGroup(
            Text(str(a), color=RED, font_size=28).next_to(rect_a, LEFT, buff=0.4),
            Text(str(b), color=GREEN, font_size=28).next_to(rect_b, LEFT, buff=0.4)
        )

        self.play(Create(rects), Write(labels))
        self.wait(0.7)

        # 步骤说明（底部安全区）
        step1_txt = Text("用 b 量 a", font_size=28, color=YELLOW).to_edge(DOWN, buff=1.0)
        self.play(Write(step1_txt))
        self.wait(0.5)

        # 测量动画（仅高亮块，无数字标签防重叠）
        remainder = a % b
        full_copies = a // b
        measure_group = VGroup()

        for i in range(full_copies):
            mr = Rectangle(
                height=0.85, width=b * scale,
                color=GREEN, fill_opacity=0.15, stroke_width=1
            ).next_to(rect_a.get_left() + RIGHT * i * b * scale, RIGHT, buff=0)
            measure_group.add(mr)
            self.play(Create(mr), run_time=0.3)

        # 余数高亮
        if remainder > 0:
            rem_rect = Rectangle(
                height=0.85, width=remainder * scale,
                color=YELLOW, fill_opacity=0.6
            ).next_to(rect_a.get_left() + RIGHT * full_copies * b * scale, RIGHT, buff=0)
            rem_label = Text(f"余数: {remainder}", color=YELLOW, font_size=26).next_to(rem_rect, RIGHT, buff=0.3)
            self.play(Create(rem_rect), Write(rem_label))
            self.wait(1)

            # 更新步骤说明
            new_step = Text(f"{a} = {b}×{full_copies} + {remainder}", font_size=28, color=WHITE)
            self.play(Transform(step1_txt, new_step.to_edge(DOWN, buff=1.0)))
            self.wait(1.5)

        # ========== 严格清除本步骤所有元素 ==========
        clear_group = VGroup(nums, rects, labels, step1_txt, measure_group)
        if remainder > 0:
            clear_group.add(rem_rect, rem_label)
        self.play(FadeOut(clear_group), run_time=1)
        self.wait(0.5)

        # ========== 步骤2：b ÷ remainder = ...（仅当余数>0）==========
        if remainder > 0:
            self.clear_step_elements()  # 确保干净

            # 新数字显示
            nums2 = VGroup(
                Text(f"新被除数 = {b}", color=GREEN, font_size=30),
                Text(f"新除数 = {remainder}", color=YELLOW, font_size=30)
            ).arrange(RIGHT, buff=1.5).next_to(self.subtitle, DOWN, buff=0.8)
            self.play(FadeIn(nums2))
            self.wait(0.7)

            # 新矩形
            rect_b2 = Rectangle(height=0.7, width=b * scale, color=GREEN, fill_opacity=0.3)
            rect_r = Rectangle(height=0.7, width=remainder * scale, color=YELLOW, fill_opacity=0.3)
            rects2 = VGroup(rect_b2, rect_r).arrange(DOWN, buff=1.0).move_to(ORIGIN)

            labels2 = VGroup(
                Text(str(b), color=GREEN, font_size=28).next_to(rect_b2, LEFT, buff=0.4),
                Text(str(remainder), color=YELLOW, font_size=28).next_to(rect_r, LEFT, buff=0.4)
            )

            self.play(Create(rects2), Write(labels2))
            self.wait(0.7)

            step2_txt = Text("用余数量 b", font_size=28, color=YELLOW).to_edge(DOWN, buff=1.0)
            self.play(Write(step2_txt))
            self.wait(0.5)

            # 测量
            remainder2 = b % remainder
            full_copies2 = b // remainder
            measure_group2 = VGroup()

            for i in range(full_copies2):
                mr2 = Rectangle(
                    height=0.85, width=remainder * scale,
                    color=YELLOW, fill_opacity=0.15, stroke_width=1
                ).next_to(rect_b2.get_left() + RIGHT * i * remainder * scale, RIGHT, buff=0)
                measure_group2.add(mr2)
                self.play(Create(mr2), run_time=0.3)

            if remainder2 > 0:
                rem_rect2 = Rectangle(
                    height=0.85, width=remainder2 * scale,
                    color=PURPLE, fill_opacity=0.6
                ).next_to(rect_b2.get_left() + RIGHT * full_copies2 * remainder * scale, RIGHT, buff=0)
                rem_label2 = Text(f"新余数: {remainder2}", color=PURPLE, font_size=26).next_to(rem_rect2, RIGHT, buff=0.3)
                self.play(Create(rem_rect2), Write(rem_label2))
                self.wait(1)

                new_step2 = Text(f"{b} = {remainder}×{full_copies2} + {remainder2}", font_size=28, color=WHITE)
                self.play(Transform(step2_txt, new_step2.to_edge(DOWN, buff=1.0)))
                self.wait(1.5)

            # 严格清除
            clear_group2 = VGroup(nums2, rects2, labels2, step2_txt, measure_group2)
            if remainder2 > 0:
                clear_group2.add(rem_rect2, rem_label2)
            self.play(FadeOut(clear_group2), run_time=1)
            self.wait(0.5)

        # ========== 最终结果（全新区域，无任何残留）==========
        self.clear()  # 彻底清空（保留标题）
        self.add(self.title, self.subtitle)

        result = Text(f"最大公约数 gcd({a}, {b}) = {gcd_val}",
                      font_size=42, color=GOLD, weight=BOLD)
        result.move_to(ORIGIN).shift(UP)

        geo = VGroup(
            Text("几何意义：", font_size=30, color=BLUE, weight=BOLD),
            Text(f"长度为 {gcd_val} 的线段可", font_size=26),
            Text(f"无剩余地量尽 {a} 和 {b}", font_size=26)
        ).arrange(DOWN, buff=0.4).next_to(result, DOWN, buff=1.2)

        summary = Text("辗转相除：余数为0时，除数即为最大公约数",
                       font_size=26, color=YELLOW).to_edge(DOWN, buff=0.8)

        self.play(Write(result), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(geo))
        self.wait(1)
        self.play(Write(summary))
        self.wait(3)

    def clear_step_elements(self):
        """辅助方法：清除除标题外的所有元素"""
        mobs = self.mobjects[:]
        for m in mobs:
            if m not in [self.title, self.subtitle] and isinstance(m, (Mobject, VMobject)):
                self.remove(m)