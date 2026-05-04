# 还没发布

from manim import *
import numpy as np
import itertools


class CircleDivisionProof(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("骗死人的圆的分割", font="KaiTi", font_size=50)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover_text1 = Text("圆上", font="KaiTi", font_size=40)
        eq_cover_math1 = MathTex(r"n", font_size=45).set_color(YELLOW)
        eq_cover_text2 = Text("个点，最多分出几个区域？", font="KaiTi", font_size=40)
        eq_cover = VGroup(eq_cover_text1, eq_cover_math1, eq_cover_text2).arrange(RIGHT, buff=0.05)

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

        # ==================== 辅助函数：生成圆上的点和线 ====================
        def get_circle_elements(n, radius=2.2):
            # 生成圆上的点坐标
            points = [
                radius * np.array([np.cos(i * TAU / n + TAU / 4), np.sin(i * TAU / n + TAU / 4), 0])
                for i in range(n)
            ]
            dots = VGroup(*[Dot(p, radius=0.06, color=YELLOW) for p in points])

            lines = VGroup()
            # 两两连线
            for i in range(n):
                for j in range(i + 1, n):
                    lines.add(Line(points[i], points[j], stroke_width=2, color=BLUE_C))

            return dots, lines, points

        # ==================== 第一幕：直觉陷阱 ====================
        desc_1_text1 = Text("在圆上任取", font="KaiTi", font_size=30)
        desc_1_math1 = MathTex(r"n", font_size=32).set_color(YELLOW)
        desc_1_text2 = Text("个点，两两相连。", font="KaiTi", font_size=30)
        desc_1 = VGroup(desc_1_text1, desc_1_math1, desc_1_text2).arrange(RIGHT, buff=0.05).to_edge(UP, buff=0.8)
        self.play(Write(desc_1))

        desc_2 = Text("直觉告诉我们，区域数似乎在翻倍增长：", font="KaiTi", font_size=28).next_to(desc_1, DOWN, buff=0.5)
        self.play(Write(desc_2))

        # 演示 n=4
        circle_4 = Circle(radius=2.2, color=WHITE)
        dots_4, lines_4, _ = get_circle_elements(4)
        group_4 = VGroup(circle_4, lines_4, dots_4).shift(LEFT * 3.5)

        num_4_text = Text("4个点", font="KaiTi", font_size=26).next_to(group_4, DOWN, buff=0.3)
        num_4_regions = MathTex(r"8", font_size=40).set_color(GREEN).next_to(num_4_text, DOWN, buff=0.2)

        self.play(Create(circle_4), Create(lines_4), FadeIn(dots_4), Write(num_4_text), run_time=1.5)
        self.play(Write(num_4_regions))
        self.wait(0.5)

        # 演示 n=5
        circle_5 = Circle(radius=2.2, color=WHITE)
        dots_5, lines_5, _ = get_circle_elements(5)
        group_5 = VGroup(circle_5, lines_5, dots_5).shift(RIGHT * 3.5)

        num_5_text = Text("5个点", font="KaiTi", font_size=26).next_to(group_5, DOWN, buff=0.3)
        num_5_regions = MathTex(r"16", font_size=40).set_color(GREEN).next_to(num_5_text, DOWN, buff=0.2)

        self.play(Create(circle_5), Create(lines_5), FadeIn(dots_5), Write(num_5_text), run_time=1.5)
        self.play(Write(num_5_regions))
        self.wait(1)

        # 总结规律
        self.play(
            FadeOut(group_4), FadeOut(num_4_text), FadeOut(num_4_regions),
            FadeOut(group_5), FadeOut(num_5_text), FadeOut(num_5_regions),
            FadeOut(desc_1), FadeOut(desc_2)
        )

        desc_3_text1 = Text("1, 2, 4, 8, 16... 规律太明显了，下一个肯定是", font="KaiTi", font_size=30).to_edge(UP,
                                                                                                               buff=0.8)
        desc_3_math1 = MathTex(r"2^{n-1}", font_size=34).set_color(YELLOW)
        desc_3 = VGroup(desc_3_text1, desc_3_math1).arrange(RIGHT, buff=0.05)
        self.play(Write(desc_3))

        desc_4_text1 = Text("6个点的时候，一定是", font="KaiTi", font_size=30)
        desc_4_math1 = MathTex(r"32", font_size=36).set_color(RED)
        desc_4_text2 = Text("个区域！", font="KaiTi", font_size=30)
        desc_4 = VGroup(desc_4_text1, desc_4_math1, desc_4_text2).arrange(RIGHT, buff=0.05).next_to(desc_3, DOWN,
                                                                                                    buff=0.5)
        self.play(Write(desc_4))
        self.wait(2)

        self.play(FadeOut(desc_3), FadeOut(desc_4))

        # ==================== 第二幕：残酷的真相 ====================
        desc_5 = Text("真的是这样吗？我们老老实实画出来看看：", font="KaiTi", font_size=30).to_edge(UP, buff=0.8)
        self.play(Write(desc_5))

        # 演示 n=6
        circle_6 = Circle(radius=2.5, color=WHITE)
        dots_6, lines_6, pts_6 = get_circle_elements(6, radius=2.5)
        group_6 = VGroup(circle_6, lines_6, dots_6).move_to(LEFT * 2)

        self.play(Create(circle_6), run_time=0.5)
        self.play(Create(lines_6), FadeIn(dots_6), run_time=2)
        self.wait(1)

        # 寻找并高亮内部的15个交点 (这是规律断裂的根源)
        # 简单寻找交点的逻辑：对线段两两求交，保留圆内部的点
        intersections = []
        for l1, l2 in itertools.combinations(lines_6, 2):
            p1, p2 = l1.get_start_and_end()
            p3, p4 = l2.get_start_and_end()
            # 排除在圆上同一点相交的情况
            if np.allclose(p1, p3) or np.allclose(p1, p4) or np.allclose(p2, p3) or np.allclose(p2, p4):
                continue
            # 粗略计算交点 (Manim的line_intersection)
            try:
                inter = line_intersection(p1[:2], p2[:2], p3[:2], p4[:2])
                inter_3d = np.array([inter[0], inter[1], 0])
                # 确保交点在圆内
                if np.linalg.norm(inter_3d) < 2.4:
                    intersections.append(inter_3d)
            except:
                pass

        inter_dots = VGroup(*[Dot(p, radius=0.06, color=RED) for p in intersections])
        self.play(FadeIn(inter_dots, run_time=1.5))
        self.wait(1)

        desc_6_text1 = Text("看到中间这些红点了吗？它们让区域暴增！", font="KaiTi", font_size=28).next_to(group_6, RIGHT,
                                                                                                        buff=0.8).align_to(
            group_6, UP)
        self.play(Write(desc_6_text1))
        self.wait(1)

        num_6_text = Text("6个点的真实区域数：", font="KaiTi", font_size=28).next_to(desc_6_text1, DOWN, buff=0.8)
        self.play(Write(num_6_text))

        num_6_regions = MathTex(r"31", font_size=80).set_color(RED).next_to(num_6_text, DOWN, buff=0.3)
        self.play(Write(num_6_regions))
        self.wait(2)

        self.play(FadeOut(desc_5), FadeOut(group_6), FadeOut(inter_dots), FadeOut(desc_6_text1), FadeOut(num_6_text),
                  FadeOut(num_6_regions))

        # ==================== 第三幕：组合真相 ====================
        desc_7 = Text("直觉被打破了！真正的规律是什么？", font="KaiTi", font_size=30).to_edge(UP, buff=0.8)
        self.play(Write(desc_7))

        desc_8_text1 = Text("区域的产生，完全取决于三个独立事件：", font="KaiTi", font_size=28).next_to(desc_7, DOWN,
                                                                                                      buff=0.5)
        self.play(Write(desc_8_text1))

        event_1_text1 = Text("1. 最原始的圆：", font="KaiTi", font_size=28)
        event_1_math1 = MathTex(r"1", font_size=30).set_color(YELLOW)
        event_1 = VGroup(event_1_text1, event_1_math1).arrange(RIGHT, buff=0.05).next_to(desc_8_text1, DOWN, buff=0.3)
        self.play(Write(event_1))

        event_2_text1 = Text("2. 每一条连线，穿过已有区域，增加", font="KaiTi", font_size=28)
        event_2_math1 = MathTex(r"1", font_size=30).set_color(YELLOW)
        event_2_text2 = Text("个区域。连线数：", font="KaiTi", font_size=28)
        event_2_math2 = MathTex(r"\binom{n}{2}", font_size=30).set_color(GREEN)
        event_2 = VGroup(event_2_text1, event_2_math1, event_2_text2, event_2_math2).arrange(RIGHT, buff=0.05).next_to(
            event_1, DOWN, buff=0.2)
        self.play(Write(event_2))

        event_3_text1 = Text("3. 每一个内部交点，都会额外再增加", font="KaiTi", font_size=28)
        event_3_math1 = MathTex(r"1", font_size=30).set_color(RED)
        event_3_text2 = Text("个区域。交点数：", font="KaiTi", font_size=28)
        event_3_math2 = MathTex(r"\binom{n}{4}", font_size=30).set_color(RED)
        event_3 = VGroup(event_3_text1, event_3_math1, event_3_text2, event_3_math2).arrange(RIGHT, buff=0.05).next_to(
            event_2, DOWN, buff=0.2)
        self.play(Write(event_3))
        self.wait(1.5)

        desc_9 = Text("把它们全部加起来，才是真正的通项公式：", font="KaiTi", font_size=28).next_to(event_3, DOWN,
                                                                                                  buff=0.5)
        self.play(Write(desc_9))

        eq_formula = MathTex(r"a_n = 1 + \binom{n}{2} + \binom{n}{4}").scale(1.2).set_color(YELLOW).next_to(desc_9,
                                                                                                            DOWN,
                                                                                                            buff=0.5)
        self.play(Write(eq_formula))
        self.wait(2)

        # 大清场
        self.play(
            FadeOut(desc_7), FadeOut(desc_8_text1), FadeOut(event_1),
            FadeOut(event_2), FadeOut(event_3), FadeOut(desc_9), FadeOut(eq_formula)
        )

        # ==================== 第四幕：验证与散场 ====================
        desc_10_text1 = Text("验证一下", font="KaiTi", font_size=30)
        desc_10_math1 = MathTex(r"n=6", font_size=32).set_color(YELLOW)
        desc_10 = VGroup(desc_10_text1, desc_10_math1).arrange(RIGHT, buff=0.05).to_edge(UP, buff=1)
        self.play(Write(desc_10))

        eq_verify = MathTex(r"1 + \binom{6}{2} + \binom{6}{4} = 1 + 15 + 15 = 31").scale(1.1).set_color(GREEN).next_to(
            desc_10, DOWN, buff=0.8)
        self.play(Write(eq_verify))
        self.wait(2)

        # 全屏暴力清场
        self.play(FadeOut(desc_10), FadeOut(eq_verify))

        outro_1 = Text("归纳法是会骗人的", font="KaiTi", font_size=50).set_color_by_gradient(RED, YELLOW).move_to(
            UP * 0.5)
        self.play(Write(outro_1))
        self.wait(1.5)

        outro_2_text1 = Text("没有严格证明的规律，都是耍流氓", font="KaiTi", font_size=35).set_color(BLUE).next_to(
            outro_1, DOWN, buff=0.8)
        self.play(Write(outro_2_text1))
        self.wait(3)

        self.play(
            *[FadeOut(m) for m in self.mobjects]
        )
        self.wait(1)