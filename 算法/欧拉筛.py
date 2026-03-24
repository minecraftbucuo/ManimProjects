# -*- coding: utf-8 -*-
# @Time    : 2026/3/24 19:39
# @Author  : MINEC + AI
# @File    : 欧拉筛.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
from manim import *


class EulerSieveVisualization(MovingCameraScene):
    def construct(self):
        # ==================== 配置参数 ====================
        N = 30  # 筛的范围
        FAST_RUN = 0.3
        SLOW_RUN = 0.8
        PAUSE_TIME = 0.5

        # 颜色定义
        COLOR_UNVISITED = WHITE
        COLOR_PRIME = GREEN
        COLOR_COMPOSITE = RED
        COLOR_CURRENT_I = BLUE
        COLOR_CURRENT_PRODUCT = ORANGE
        COLOR_HIGHLIGHT = YELLOW

        # ==================== 代码模块 ====================
        code_str = """vector<int> primes;
vector<bool> is_prime(n+1, true);
is_prime[0] = is_prime[1] = false;
for (int i = 2; i <= n; i++) {
    if (is_prime[i])
        primes.push_back(i);
    for (int p : primes) {
        if (i * p > n) break;
        is_prime[i * p] = false;
        if (i % p == 0) break;
    }
}"""

        # 创建代码对象
        code_obj = Code(
            code=code_str,
            language="cpp",
            font_size=24,
            background="rectangle",
            background_stroke_color="#3c3c3c",
            background_stroke_width=1,
            corner_radius=0.1,
            insert_line_no=True,
            style="monokai",
        )

        # 定位到左上角
        code_obj.to_corner(UL, buff=0.5)

        # ==================== 高亮框 ====================
        highlight_box = Rectangle(
            fill_color=COLOR_HIGHLIGHT,
            fill_opacity=0.3,
            stroke_width=0,
            z_index=1
        )

        # 高亮函数
        def get_highlight_anim(line_idx):
            target_line = code_obj.code[line_idx]
            h = target_line.height
            w = code_obj.width
            return AnimationGroup(
                highlight_box.animate.stretch_to_fit_height(h).stretch_to_fit_width(w).move_to(
                    target_line.get_center()),
                run_time=0.1
            )

        # ==================== 数字网格 (右侧) ====================
        numbers = VGroup()
        number_rects = {}
        number_texts = {}

        cols = 6
        rows = (N + 1) // cols + (1 if (N + 1) % cols else 0)

        for num in range(N + 1):
            rect = Square(side_length=0.55, fill_opacity=0.2, stroke_width=2)
            rect.set_stroke(COLOR_UNVISITED)
            rect.set_fill("#1a1a2e", opacity=0.5)

            txt = Text(str(num), font="Arial", font_size=18, color=COLOR_UNVISITED)

            cell = VGroup(rect, txt)
            numbers.add(cell)
            number_rects[num] = rect
            number_texts[num] = txt

        numbers.arrange_in_grid(rows=rows, cols=cols, buff=0.08)
        numbers.to_edge(RIGHT, buff=0.5).to_edge(UP, buff=0.8)

        # 数字标题
        num_title = Text(f"欧拉筛 (n={N})", font="Microsoft YaHei", font_size=24, color=WHITE)
        num_title.next_to(numbers, UP, buff=0.2)

        # ==================== 质数列表 (移至左侧，代码下方) ====================
        primes_display_title = Text("primes: []", font="Consolas", font_size=20, color=GREEN)
        # 放在代码块下方，左对齐
        primes_display_title.next_to(code_obj, DOWN, buff=0.3, aligned_edge=LEFT)

        # ==================== 图例 (底部中间) ====================
        legend_items = VGroup()
        legends = [
            ("未访问", COLOR_UNVISITED),
            ("质数", COLOR_PRIME),
            ("合数", COLOR_COMPOSITE),
            ("当前i", COLOR_CURRENT_I),
            ("当前乘积", COLOR_CURRENT_PRODUCT),
        ]
        for name, color in legends:
            sq = Square(side_length=0.25, fill_opacity=0.5, stroke_color=color)
            lb = Text(name, font="Microsoft YaHei", font_size=14, color=WHITE)
            item = VGroup(sq, lb).arrange(RIGHT, buff=0.1)
            legend_items.add(item)

        legend_items.arrange(RIGHT, buff=0.3)
        legend_items.to_edge(DOWN, buff=0.3)

        # ==================== 初始化动画 ====================
        self.play(FadeIn(code_obj))
        self.play(FadeIn(numbers), FadeIn(num_title))
        self.play(FadeIn(primes_display_title), FadeIn(legend_items))

        # 初始化高亮框状态
        self.play(get_highlight_anim(0), FadeIn(highlight_box))

        # ==================== 辅助函数 ====================
        def highlight_code_line(line_idx):
            return get_highlight_anim(line_idx)

        def flash_code_line(line_idx, color=COLOR_HIGHLIGHT):
            target = code_obj.code[line_idx]
            flash_rect = SurroundingRectangle(target, color=color, buff=0.1)
            flash_rect.set_stroke(width=3)
            return flash_rect

        def mark_as_prime(num):
            rect = number_rects[num]
            txt = number_texts[num]
            new_rect = rect.copy().set_stroke(COLOR_PRIME, width=3)
            new_rect.set_fill(GREEN, opacity=0.3)
            new_txt = txt.copy().set_color(COLOR_PRIME)
            return Transform(rect, new_rect), Transform(txt, new_txt)

        def mark_as_composite(num):
            rect = number_rects[num]
            txt = number_texts[num]
            new_rect = rect.copy().set_stroke(COLOR_COMPOSITE, width=2)
            new_rect.set_fill(RED, opacity=0.3)
            new_txt = txt.copy().set_color(COLOR_COMPOSITE)
            return Transform(rect, new_rect), Transform(txt, new_txt)

        def highlight_current_i(num):
            rect = number_rects[num]
            new_rect = rect.copy().set_stroke(COLOR_CURRENT_I, width=4)
            return Transform(rect, new_rect)

        def pulse_product(num):
            rect = number_rects[num]
            pulse = SurroundingRectangle(rect, color=COLOR_CURRENT_PRODUCT, buff=0.05)
            pulse.set_stroke(width=4)
            return pulse

        def create_min_factor_effect(i_val, p_val):
            i_rect = number_rects[i_val]
            p_rect = number_rects[p_val]

            line = Line(i_rect.get_center(), p_rect.get_center(), color=YELLOW, stroke_width=3)

            label = Text(f"{p_val}是{i_val}的最小质因子", font="Microsoft YaHei", font_size=16, color=YELLOW)
            label.next_to(line.get_center(), UP, buff=0.1)

            i_rect_zoom = SurroundingRectangle(i_rect, color=YELLOW, buff=0.05)
            p_rect_zoom = SurroundingRectangle(p_rect, color=YELLOW, buff=0.05)

            return VGroup(line, label, i_rect_zoom, p_rect_zoom)

        # ==================== 算法执行 ====================
        primes_list = []
        is_prime = [True] * (N + 1)
        is_prime[0] = is_prime[1] = False

        # 初始化 is_prime[0] = is_prime[1] = false (Line 2)
        self.play(highlight_code_line(2), run_time=FAST_RUN)

        self.play(*mark_as_composite(0), *mark_as_composite(1), run_time=FAST_RUN)
        self.wait(PAUSE_TIME)

        # 主循环
        for i in range(2, N + 1):
            # for loop (Line 3)
            self.play(highlight_code_line(3), run_time=FAST_RUN)

            # 高亮当前 i
            self.play(highlight_current_i(i), run_time=FAST_RUN)

            # if (is_prime[i]) (Line 4)
            self.play(highlight_code_line(4), run_time=FAST_RUN)

            if is_prime[i]:
                # 闪烁效果
                flash = flash_code_line(4, GREEN)
                self.play(FadeIn(flash), run_time=0.2)
                self.play(FadeOut(flash), run_time=0.2)

                # primes.push_back(i) (Line 5)
                self.play(highlight_code_line(5), run_time=SLOW_RUN)

                primes_list.append(i)
                self.play(*mark_as_prime(i), run_time=SLOW_RUN)

                # 更新质数列表显示
                new_primes_display = Text(
                    f"primes: [{', '.join(map(str, primes_list))}]",
                    font="Consolas", font_size=20, color=GREEN
                )
                # 保持位置在左侧代码下方
                new_primes_display.next_to(code_obj, DOWN, buff=0.3, aligned_edge=LEFT)
                # new_primes_display.move_to(primes_display_title.get_center())
                self.play(Transform(primes_display_title, new_primes_display), run_time=FAST_RUN)

                self.wait(PAUSE_TIME)

            # for (int p : primes) (Line 6)
            self.play(highlight_code_line(6), run_time=FAST_RUN)

            for j, p in enumerate(primes_list):
                # if (i * p > n) break (Line 7)
                self.play(highlight_code_line(7), run_time=FAST_RUN)

                product = i * p
                if product > N:
                    flash = flash_code_line(7, RED)
                    self.play(FadeIn(flash), run_time=0.2)
                    self.play(FadeOut(flash), run_time=0.2)
                    self.wait(PAUSE_TIME)
                    break

                # 显示乘积位置
                pulse = pulse_product(product)
                self.play(FadeIn(pulse), run_time=FAST_RUN)

                # is_prime[i * p] = false (Line 8)
                self.play(highlight_code_line(8), run_time=FAST_RUN)

                is_prime[product] = False
                self.play(*mark_as_composite(product), FadeOut(pulse), run_time=FAST_RUN)

                # if (i % p == 0) break (Line 9)
                self.play(highlight_code_line(9), run_time=SLOW_RUN)

                if i % p == 0:
                    # 最小质因子特效
                    flash = flash_code_line(9, YELLOW)
                    self.play(FadeIn(flash), run_time=0.2)

                    min_factor_effect = create_min_factor_effect(i, p)
                    self.play(FadeIn(min_factor_effect), run_time=SLOW_RUN)
                    self.wait(PAUSE_TIME + 0.3)
                    self.play(FadeOut(flash), FadeOut(min_factor_effect), run_time=FAST_RUN)
                    break
                else:
                    self.play(FadeOut(pulse), run_time=FAST_RUN)

            # 恢复 i 的显示颜色
            if is_prime[i]:
                self.play(*mark_as_prime(i), run_time=FAST_RUN)
            else:
                rect = number_rects[i]
                new_rect = rect.copy().set_stroke(COLOR_COMPOSITE, width=2)
                self.play(Transform(rect, new_rect), run_time=FAST_RUN)

        # 结束循环
        self.play(highlight_code_line(11), run_time=FAST_RUN)

        # 最终结果展示
        result_text = Text(
            f"筛选完成！共 {len(primes_list)} 个质数",
            font="Microsoft YaHei", font_size=24, color=GREEN
        )
        result_text.next_to(legend_items, UP, buff=0.2)
        self.play(FadeIn(result_text), run_time=SLOW_RUN)
        self.wait(2)