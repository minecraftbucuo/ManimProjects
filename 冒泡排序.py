from manim import *
import numpy as np


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