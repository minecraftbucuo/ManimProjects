# 2026.2.27 冒泡排序可视化 AI

from manim import *
import numpy as np


class BubbleSortIntro(Scene):
    def construct(self):
        # ========== 1. 动态标题：居中 → 左上角 ==========
        main_title = Text("冒泡排序", font="KaiTi", font_size=84, weight=BOLD)
        main_title.set_color_by_gradient(BLUE, GREEN, YELLOW)
        self.play(Write(main_title, run_time=1.5))
        self.wait(0.8)

        corner_title = Text("冒泡排序", font="KaiTi", font_size=32, weight=BOLD)
        corner_title.set_color_by_gradient(BLUE, GREEN)
        corner_title.to_edge(UL, buff=0.6)
        self.play(Transform(main_title, corner_title), run_time=1.5)

        # ========== 2. 核心知识卡片（数学符号用 LaTeX）==========
        card_data = [
            ("算法流程", BLUE, "重复遍历序列\n比较相邻元素\n交换逆序对\n大元素浮至末尾"),
            ("算法特点", GREEN, "简单直观\n原地排序\n稳定排序"),
            ("时间复杂度", YELLOW,
             VGroup(
                 VGroup(
                     Text("最好（已排序）: ", font="KaiTi", font_size=19),
                     MathTex(r"O(n)", font_size=22, color=YELLOW)
                 ).arrange(RIGHT, buff=0.1),
                 VGroup(
                     Text("平均/最坏: ", font="KaiTi", font_size=19),
                     MathTex(r"O(n^2)", font_size=22, color=RED)
                 ).arrange(RIGHT, buff=0.1)
             ).arrange(DOWN, buff=0.15)),
            ("适用场景", RED, "小规模数据\n教学演示\n近似有序数据")
        ]

        cards = VGroup()
        card_width = 3.5
        card_height = 2.0

        for i, (title_text, color, content) in enumerate(card_data):
            card_bg = RoundedRectangle(
                width=card_width,
                height=card_height,
                corner_radius=0.15,
                fill_color=BLACK,
                fill_opacity=0.92,
                stroke_color=color,
                stroke_width=2.2
            )

            title_obj = Text(title_text, font="KaiTi", font_size=26, weight=BOLD, color=color)
            title_obj.next_to(card_bg.get_top(), DOWN, buff=0.2).align_to(card_bg, LEFT).shift(RIGHT * 0.3)

            if isinstance(content, str):
                content_obj = Text(content, font="KaiTi", font_size=20, color=WHITE, line_spacing=0.6)
                content_obj.next_to(title_obj, DOWN, buff=0.15).align_to(title_obj, LEFT)
            else:
                content.next_to(title_obj, DOWN, buff=0.12).align_to(title_obj, LEFT)
                content_obj = content

            card = VGroup(card_bg, title_obj, content_obj)
            cards.add(card)

        cards.arrange_in_grid(rows=2, cols=2, buff=(0.4, 0.3))
        cards.move_to(UP * 0.7)

        for card in cards:
            self.play(FadeIn(card, shift=DOWN * 0.2, scale=0.97), run_time=0.7)
            self.wait(0.3)
        self.wait(0.6)

        # ========== 3. 示例代码（Code类 + 严格兼容0.18.1）==========
        code = Code(
            code="""# Bubble Sort with Optimization
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):      # Outer loop
        swapped = False       # Optimization flag
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:       # Terminate early if no swap
            break
    return arr""",
            tab_width=4,
            language="python",
            font="Consolas",
            style="monokai",
            font_size=18,
            line_spacing=0.6,
            insert_line_no=True,  # ✅ 开启行号
            line_no_from=1,
            line_no_buff=0.25,  # 增大间距防贴边
            background="rectangle",
            background_stroke_width=1.5,
            background_stroke_color=BLUE_E,
        )
        code.background_mobject.set_fill("#0f172a", opacity=0.93)
        # 🔑 关键修复1：创建后立即强化行号（必须在动画前！）
        code.line_numbers.set_color(WHITE).set_opacity(1.0)  # opacity=1.0 是救命稻草！

        # 🔑 关键修复2：将行号纳入初始动画（不再遗漏！）
        self.play(
            FadeIn(code.background_mobject, scale=0.95),
            FadeIn(code.line_numbers),  # ✨ 行号同步淡入
            run_time=0.6
        )
        self.play(Write(code.code), run_time=1.8)  # 代码逐行写入
        self.wait(1.0)

        # ========== 4. 收尾过渡 ==========
        separator = Line(LEFT * 3.4, RIGHT * 3.4, color=GREY, stroke_width=1.0, stroke_opacity=0.5)
        separator.next_to(code, DOWN, buff=0.5)

        footer = Text("→ 算法动态可视化演示即将开始", font="KaiTi", font_size=24, color=BLUE_A)
        footer.next_to(separator, DOWN, buff=0.3)

        self.play(Create(separator), run_time=0.6)
        self.play(Write(footer), run_time=0.8)
        self.wait(1.2)

        # 淡出
        all_elements = VGroup(cards, code, separator, footer)
        self.play(all_elements.animate.set_opacity(0.05).scale(0.93), run_time=1.2)
        self.wait(0.3)

        final_hint = Text("可视化演示加载中...", font="KaiTi", font_size=30, color=GREEN_B)
        final_hint.move_to(ORIGIN)
        self.play(FadeIn(final_hint, scale=1.15), run_time=0.6)
        self.wait(1.3)
        self.play(FadeOut(final_hint), run_time=0.5)
        self.wait(0.2)


class BubbleSortManim(Scene):
    def construct(self):
        # 初始化数组
        arr = [7, 3, 8, 5, 9, 4, 2, 6, 1]
        n = len(arr)
        baseline_y = -2.5  # 所有矩形底部对齐的y坐标

        # 预计算所有(索引, 数值)的位置
        unique_vals = set(arr)
        positions = {}
        for idx in range(n):
            for val in unique_vals:
                x_pos = (idx - n / 2 + 0.5) * 1.2
                y_pos = baseline_y + (val * 0.3) / 2
                positions[(idx, val)] = np.array([x_pos, y_pos, 0])

        # 创建矩形和标签
        rectangles = []
        labels = []
        value_groups = []

        for i, value in enumerate(arr):
            rect = Rectangle(
                width=0.8,
                height=value * 0.3,
                fill_color=BLUE,
                fill_opacity=0.8,
                stroke_color=WHITE,
                stroke_width=2
            )
            rect.move_to(positions[(i, value)])
            label = Text(str(value), font="KaiTi", font_size=24).move_to(rect.get_center())
            group = VGroup(rect, label)

            rectangles.append(rect)
            labels.append(label)
            value_groups.append(group)

        # 显示初始数组
        self.play(*[Create(group) for group in value_groups])
        self.wait(0.5)

        # 标题
        title = Text("冒泡排序可视化", font="KaiTi", font_size=45).to_edge(UP)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW)
        self.play(Write(title))
        self.wait(0.5)

        # 交换计数器
        swap_count = 0
        swap_text = Text(f"交换次数: 0", font="KaiTi", font_size=24).next_to(title, DOWN)
        swap_text.set_color_by_gradient(GREEN, BLUE, YELLOW)
        self.play(Write(swap_text))

        # 冒泡排序主循环
        for i in range(n - 1):
            for j in range(n - i - 1):
                # 高亮当前比较元素
                self.play(
                    rectangles[j].animate.set_fill(RED, 0.8),
                    rectangles[j + 1].animate.set_fill(RED, 0.8),
                    run_time=0.3
                )
                self.wait(0.2)

                if arr[j] > arr[j + 1]:
                    # 交换数组值
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

                    # 更新交换计数
                    swap_count += 1
                    new_swap = Text(f"交换次数: {swap_count}", font="KaiTi", font_size=24).move_to(
                        swap_text.get_center())
                    new_swap.set_color_by_gradient(GREEN, BLUE, YELLOW)
                    self.play(Transform(swap_text, new_swap), run_time=0.3)

                    # 获取预计算的目标位置
                    target_j = positions[(j, arr[j])]
                    target_j1 = positions[(j + 1, arr[j + 1])]

                    # 交换位置（VGroup包含矩形和标签）
                    self.play(
                        value_groups[j].animate.move_to(target_j1),
                        value_groups[j + 1].animate.move_to(target_j),
                        run_time=0.6
                    )

                    # 交换列表引用
                    value_groups[j], value_groups[j + 1] = value_groups[j + 1], value_groups[j]
                    rectangles[j], rectangles[j + 1] = rectangles[j + 1], rectangles[j]
                    labels[j], labels[j + 1] = labels[j + 1], labels[j]

                    # 交换后恢复为原色（蓝色）
                    self.play(
                        rectangles[j].animate.set_fill(BLUE, 0.8),
                        rectangles[j + 1].animate.set_fill(BLUE, 0.8),
                        run_time=0.2
                    )
                    self.wait(0.1)
                else:
                    # 无需交换：恢复蓝色
                    self.play(
                        rectangles[j].animate.set_fill(BLUE, 0.8),
                        rectangles[j + 1].animate.set_fill(BLUE, 0.8),
                        run_time=0.2
                    )

            # 标记本轮新确定的元素（位置 n-i-1）为绿色
            if 0 <= n - i - 1 < n:
                self.play(
                    rectangles[n - i - 1].animate.set_fill(GREEN, 0.8),
                    run_time=0.25
                )
            self.wait(0.2)

        # 排序完成：清理交换计数器
        self.play(
            FadeOut(swap_text),
            run_time=0.6
        )

        # 确保所有方块为绿色（最终排序状态）
        self.play(
            *[rect.animate.set_fill(GREEN, 0.8) for rect in rectangles],
            run_time=0.5
        )

        # 显示完成信息
        completion_text = Text("排序完成!", font="KaiTi", font_size=36, color=GREEN).next_to(title, DOWN)
        self.play(Write(completion_text))

        final_text = Text("排序结果: " + " ".join(map(str, arr)), font="KaiTi", font_size=24).next_to(completion_text,
                                                                                                      DOWN)
        final_text.set_color_by_gradient(GREEN, BLUE, YELLOW)
        self.play(Write(final_text))

        self.wait(2)