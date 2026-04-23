from manim import *
import numpy as np


class InsertionSortFinal(Scene):
    def construct(self):
        # ====================
        # 0. 顶部标题
        # ====================
        title = Text("插入排序可视化", font="KaiTi", font_size=40).to_edge(UP)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW)
        self.play(Write(title))

        # ====================
        # 1. 左侧：代码与精确高亮框
        # ====================
        # 注意：这里每一行行尾绝对不能有空格，否则 Manim 的边框会包裹住那些看不见的空格
        code_str = """void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}""".replace('\r', '').replace('\t', '    ')
        # 下移一点避开顶部的标题
        code = Code(
            code=code_str,
            tab_width=4,
            background="window",
            language="cpp",
            font="Monospace",
            style="monokai"
        ).scale(0.55).to_edge(LEFT, buff=0.3).shift(DOWN * 0.5)

        # # 动态高亮框：精确包裹单行字符的 VGroup，buff 设小一点让它紧贴代码
        # pointer_box = SurroundingRectangle(code.code[0], color=YELLOW, buff=0.00)
        #
        # def move_box(line_index):
        #     # SurroundingRectangle 会自动自适应目标文字真实的物理长宽，实现“精确框住”
        #     return Transform(pointer_box, SurroundingRectangle(code.code[line_index], color=YELLOW, buff=0.00))
        # 初始高亮框
        pointer_box = SurroundingRectangle(code.code[0], color=YELLOW, buff=0.05)
        # 记录下第一行的绝对高度，作为全局标准
        standard_height = pointer_box.height

        def move_box(line_index):
            # 1. 先生成贴合目标行的初始框
            target_box = SurroundingRectangle(code.code[line_index], color=YELLOW, buff=0.05)
            # 2. 暴力修正：宽度顺其自然，但高度必须拉伸/压缩到标准高度
            target_box.stretch_to_fit_height(standard_height)
            # 3. 重新对齐，防止拉伸后中心偏移
            target_box.move_to(code.code[line_index].get_center())

            return Transform(pointer_box, target_box)

        # ====================
        # 2. 右侧：数据与防重叠布局
        # ====================
        arr = [7, 3, 8, 5, 9, 4, 2, 6, 1]
        n = len(arr)

        x_offset = 3.5  # 整体向右偏移
        data_baseline_y = -1.5  # 柱状图基准线
        key_buffer_y = -3.2  # 底部缓冲区（防止移位时重叠）

        unique_vals = set(arr)
        positions = {}
        for idx in range(n):
            for val in unique_vals:
                x_pos = (idx - n / 2 + 0.5) * 0.75 + x_offset
                y_pos = data_baseline_y + (val * 0.25) / 2
                positions[(idx, val)] = np.array([x_pos, y_pos, 0])

        rectangles = []
        labels = []
        value_groups = []

        for i, value in enumerate(arr):
            rect = Rectangle(
                width=0.6,
                height=value * 0.25,
                fill_color=BLUE,
                fill_opacity=0.8,
                stroke_color=WHITE,
                stroke_width=1.5
            )
            rect.move_to(positions[(i, value)])
            # 沿用你之前喜欢的字体和居中方式
            label = Text(str(value), font="KaiTi", font_size=20).move_to(rect.get_center())
            group = VGroup(rect, label)

            rectangles.append(rect)
            labels.append(label)
            value_groups.append(group)

        # ====================
        # 3. 动画执行流程
        # ====================
        self.play(Create(code), Create(pointer_box))
        self.play(*[Create(group) for group in value_groups])
        self.wait(0.5)

        # 默认第 0 个元素处于已排序状态（变绿）
        self.play(rectangles[0].animate.set_fill(GREEN, 0.8), run_time=0.2)

        for i in range(1, n):
            self.play(move_box(1), run_time=0.3)
            self.wait(0.2)

            key_val = arr[i]
            key_group = value_groups[i]
            key_rect = rectangles[i]
            key_label = labels[i]

            self.play(move_box(2), run_time=0.3)
            self.play(key_rect.animate.set_fill(YELLOW, 0.8), run_time=0.2)
            # 移入缓冲区
            key_buffer_pos = np.array([key_group.get_x(), key_buffer_y, 0])
            self.play(key_group.animate.move_to(key_buffer_pos), run_time=0.4)

            self.play(move_box(3), run_time=0.3)
            j = i - 1
            self.wait(0.2)

            while j >= 0:
                self.play(move_box(4), run_time=0.3)
                self.play(rectangles[j].animate.set_fill(RED, 0.8), run_time=0.2)
                self.wait(0.1)

                if arr[j] > key_val:
                    self.play(move_box(5), run_time=0.3)

                    target_j1_pos = positions[(j + 1, arr[j])]
                    self.play(value_groups[j].animate.move_to(target_j1_pos), run_time=0.4)

                    arr[j + 1] = arr[j]
                    value_groups[j + 1] = value_groups[j]
                    rectangles[j + 1] = rectangles[j]
                    labels[j + 1] = labels[j]

                    self.play(rectangles[j + 1].animate.set_fill(GREEN, 0.8), run_time=0.2)

                    self.play(move_box(6), run_time=0.3)
                    j -= 1
                else:
                    self.play(rectangles[j].animate.set_fill(GREEN, 0.8), run_time=0.2)
                    break

            # 再次指向 while 判断，确认退出
            self.play(move_box(4), run_time=0.3)
            self.wait(0.1)

            self.play(move_box(8), run_time=0.3)

            arr[j + 1] = key_val
            value_groups[j + 1] = key_group
            rectangles[j + 1] = key_rect
            labels[j + 1] = key_label

            # 从下方缓冲区精准落入目标空位
            final_pos = positions[(j + 1, key_val)]
            self.play(key_group.animate.move_to(final_pos), run_time=0.5)
            self.play(key_rect.animate.set_fill(GREEN, 0.8), run_time=0.2)
            self.wait(0.2)

        # 循环结束收尾
        self.play(move_box(10), run_time=0.3)
        self.play(Uncreate(pointer_box))
        self.play(*[rect.animate.set_fill(GREEN, 0.8) for rect in rectangles], run_time=0.5)
        self.wait(2)