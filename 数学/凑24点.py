from manimlib import *


class Game24Fluid(Scene):
    def construct(self):
        frame = self.camera.frame

        # ==================== 强制色彩设定 ====================
        TEXT_C = YELLOW  # 所有中文字统一黄色
        MATH_C = BLUE  # 所有数学公式统一蓝色
        EMPH_C = ORANGE  # 强调数字用橙色
        RSLT_C = GREEN  # 最终结果高亮用绿色

        # ==================== 智能摄像机跟随系统 ====================
        def write_sync_camera(mob):
            # 将目标Y值设定在物体底部上方2.0单位处，使得物体始终停留在画面中偏下的黄金视觉区
            target_cam_y = mob.get_bottom()[1] + 2.0
            if target_cam_y < frame.get_y():
                self.play(
                    Write(mob),
                    frame.animate.set_y(target_cam_y),
                    run_time=2.0
                )
            else:
                self.play(Write(mob), run_time=2.0)
            self.wait(1.0)  # 稍微缩短单句停顿，让叙事更连贯

        # ==================== 封面与标题 ====================
        title = Text("如何用这四个数字凑 24 点？", font="KaiTi", font_size=70)
        title.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE)

        integral = Tex(r"5,\ 5,\ 5,\ 1 \Rightarrow 24", font_size=60).set_color(MATH_C)

        cover = VGroup(title, integral).arrange(DOWN, buff=2)
        self.play(Write(cover), run_time=2.0)

        self.wait(1.0)

        # ==================== 3秒高燃倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=180)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.move_to(frame.get_center())
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)

        self.play(FadeOut(title), FadeOut(integral))

        # ==================== 叙事段落 A：打破定势 ====================
        # 初始位置基于摄像机中心偏上，靠左对齐
        p1_t1 = Text("常规的整数因数分解在这里失效，必须打破思维定势，", font="KaiTi", font_size=35).set_color(TEXT_C)
        p1_t2 = Text("尝试寻找非整数的突破口。", font="KaiTi", font_size=35).set_color(TEXT_C)

        p1_t3 = VGroup(
            Text("既然手边有多个 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"5").set_color(MATH_C),
            Text("，不妨锁定其中一个作为最终的乘数。", font="KaiTi", font_size=35).set_color(TEXT_C)
        ).arrange(RIGHT, buff=0.1)

        p1_t4 = Text("这样一来，我们的目标就变成了凑出一个分数：", font="KaiTi", font_size=35).set_color(TEXT_C)

        p1_eq = Tex(r"24 = 5 \times \frac{24}{5}").set_color(MATH_C).scale(1.2)

        group_A = VGroup(p1_t1, p1_t2, p1_t3, p1_t4, p1_eq)
        group_A.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        group_A.move_to(frame.get_center() + UP * 1.5).to_edge(LEFT, buff=1)

        for mob in group_A:
            write_sync_camera(mob)
        self.wait(1.5)

        # ==================== 叙事段落 B：分数拆解 ====================
        p2_t1 = VGroup(
            Text("现在的核心任务转移了：如何用剩下的 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"5, 5, 1").set_color(MATH_C),
            Text(" 凑出 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"\frac{24}{5}").set_color(EMPH_C),
            Text(" ？", font="KaiTi", font_size=35).set_color(TEXT_C)
        ).arrange(RIGHT, buff=0.1)

        p2_t2 = VGroup(
            Text("观察这个分数，它距离整数 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"5").set_color(MATH_C),
            Text(" 非常近，可以顺势将其拆解：", font="KaiTi", font_size=35).set_color(TEXT_C)
        ).arrange(RIGHT, buff=0.1)

        p2_eq = Tex(r"\frac{24}{5} = 5 - \frac{1}{5}").set_color(MATH_C).scale(1.2)

        group_B = VGroup(p2_t1, p2_t2, p2_eq)
        group_B.arrange(DOWN, buff=0.6, aligned_edge=LEFT).next_to(group_A, DOWN, buff=1.5).align_to(group_A, LEFT)

        for mob in group_B:
            write_sync_camera(mob)
        self.wait(1.5)

        # ==================== 叙事段落 C：完美拼图 ====================
        p3_t1 = VGroup(
            Text("为了完成这个减法，我们需要 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"\frac{1}{5}").set_color(MATH_C),
            Text("。", font="KaiTi", font_size=35).set_color(TEXT_C)
        ).arrange(RIGHT, buff=0.1)

        p3_t2 = VGroup(
            Text("而我们手头恰好只剩下最后两个数字：", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"1").set_color(MATH_C),
            Text(" 和 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"5").set_color(MATH_C),
            Text("，完美匹配：", font="KaiTi", font_size=35).set_color(TEXT_C)
        ).arrange(RIGHT, buff=0.1)

        p3_eq = VGroup(
            Text("直接组合为：", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"\frac{1}{5}").set_color(MATH_C)
        ).arrange(RIGHT, buff=0.5).scale(1.2)

        group_C = VGroup(p3_t1, p3_t2, p3_eq)
        group_C.arrange(DOWN, buff=0.6, aligned_edge=LEFT).next_to(group_B, DOWN, buff=1.5).align_to(group_A, LEFT)

        for mob in group_C:
            write_sync_camera(mob)
        self.wait(1.5)

        # ==================== 叙事段落 D：终极回代 ====================
        p4_t1 = Text("最后，将这个精妙的思维链条逆向连接起来，代回原式：", font="KaiTi", font_size=35).set_color(TEXT_C)

        final_eq = Tex(
            r"5 \times \left( 5 - \frac{1}{5} \right) = 24"
        ).set_color(RSLT_C).scale(1.5)

        group_D = VGroup(p4_t1, final_eq)
        group_D.arrange(DOWN, buff=1.0, aligned_edge=LEFT).next_to(group_C, DOWN, buff=1.5).align_to(group_A, LEFT)

        # 把大公式居中显示
        final_eq.set_x(0)

        write_sync_camera(p4_t1)
        write_sync_camera(final_eq)
        self.wait(1)

        # ==================== 强调与收尾 ====================
        # 外框特效
        rect = SurroundingRectangle(final_eq, buff=0.4).set_color(YELLOW)
        self.play(Write(rect), run_time=1.5)

        self.play(
            final_eq.animate.scale(1.2).set_color_by_gradient(BLUE, YELLOW, RED),
            rect.animate.scale(1.2).set_color(PINK),
            frame.animate.scale(1.1),  # 镜头稍微拉远，显得有张力
            run_time=2.0
        )
        self.wait(3)

        # 清屏准备结尾
        all_mobs = Group(*self.mobjects)
        all_mobs.remove(frame)
        self.play(FadeOut(all_mobs), run_time=1.5)

        xiexie = Text("感谢观看", font="KaiTi", font_size=100)
        xiexie.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE)
        xiexie.fix_in_frame()  # 确保结尾在屏幕正中央

        self.play(FadeIn(xiexie, scale=0.8), run_time=2.0)
        self.wait(3)