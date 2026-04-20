from manimlib import *


class PoissonIntegral(Scene):
    def construct(self):
        frame = self.camera.frame

        # ==================== 强制色彩设定 ====================
        TEXT_C = YELLOW  # 所有中文字统一黄色
        MATH_C = BLUE  # 所有数学公式统一蓝色
        EMPH_C = ORANGE  # 强调数字（如0、1）用橙色
        RSLT_C = GREEN  # 最终结果高亮用绿色

        # ==================== 智能摄像机跟随系统 ====================
        def write_sync_camera(mob):
            target_cam_y = mob.get_y() + 1.5
            if target_cam_y < frame.get_y():
                self.play(
                    Write(mob),
                    frame.animate.set_y(target_cam_y),
                    run_time=2.0  # 【放慢】写字和摄像机平移的速度
                )
            else:
                self.play(Write(mob), run_time=2.0)  # 【放慢】写字速度
            self.wait(1.5)  # 【加长】每一行写完后的阅读停顿时间

        # ==================== 封面与标题 ====================
        title = Text("如何求这个积分？", font="KaiTi", font_size=80)
        title.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        integral = Tex(r"\int_0^\pi \ln(1 - 2\alpha\cos x + \alpha^2) dx \,=\, ?", font_size=60).set_color(MATH_C)

        cover = VGroup(title, integral).arrange(DOWN, buff=0.8)
        self.play(Write(title), run_time=2.0)
        self.play(Write(integral), run_time=2.0)
        self.wait(2)  # 【加长】封面展示时间

        self.play(
            title.animate.scale(0.6).to_edge(UP, buff=0.5),
            integral.animate.scale(0.8).next_to(title, DOWN, buff=0.5),
            run_time=1.5
        )
        self.wait(1.5)

        # ==================== 3秒高燃倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=180)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.move_to(frame.get_center())

            # 完美卡点：0.3出场 + 0.4停留 + 0.3退场 = 精准1秒钟
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(1)

        # ==================== 1. 当 |α| < 1 时 ====================
        case1_title = VGroup(
            Text("1. 当 ", font="KaiTi", font_size=40).set_color(TEXT_C),
            Tex(r"|\alpha| < 1", font_size=45).set_color(MATH_C),
            Text(" 时", font="KaiTi", font_size=40).set_color(TEXT_C)
        ).arrange(RIGHT, buff=0.1)
        case1_title.next_to(integral, DOWN, buff=1.5).to_edge(LEFT, buff=1)

        write_sync_camera(case1_title)

        c1_step1 = Text("利用著名的傅里叶级数展开式：", font="KaiTi", font_size=35).set_color(TEXT_C)
        c1_eq1 = Tex(
            r"\ln(1 - 2\alpha \cos x + \alpha^2) = -2 \sum_{n=1}^{\infty} \frac{\alpha^n}{n} \cos(nx)").set_color(
            MATH_C)

        c1_step2 = Text("将其代入积分中，并在满足收敛条件时交换积分与求和顺序：", font="KaiTi", font_size=35).set_color(
            TEXT_C)
        c1_eq2 = Tex(
            r"I(\alpha) = \int_0^\pi \left( -2 \sum_{n=1}^{\infty} \frac{\alpha^n}{n} \cos(nx) \right) dx").set_color(
            MATH_C)
        c1_eq3 = Tex(r"I(\alpha) = -2 \sum_{n=1}^{\infty} \frac{\alpha^n}{n} \int_0^\pi \cos(nx) \, dx").set_color(
            MATH_C)

        c1_step3 = Text("计算内部积分：", font="KaiTi", font_size=35).set_color(TEXT_C)
        c1_eq4 = Tex(
            r"\int_0^\pi \cos(nx) \, dx = \left[ \frac{\sin(nx)}{n} \right]_0^\pi = \frac{\sin(n\pi) - \sin(0)}{n}").set_color(
            MATH_C)

        c1_step4 = VGroup(
            Text("因为 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"n").set_color(MATH_C),
            Text(" 是整数，所以对所有 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"n \ge 1").set_color(MATH_C),
            Text("，该积分等于 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"0").set_color(EMPH_C),
            Text("。", font="KaiTi", font_size=35).set_color(TEXT_C)
        ).arrange(RIGHT, buff=0.1)

        c1_eq5 = Tex(r"I(\alpha) = -2 \sum_{n=1}^{\infty} \frac{\alpha^n}{n} \cdot 0 = 0").set_color(RSLT_C)

        group_c1 = VGroup(c1_step1, c1_eq1, c1_step2, c1_eq2, c1_eq3, c1_step3, c1_eq4, c1_step4, c1_eq5)
        group_c1.arrange(DOWN, buff=0.6, aligned_edge=LEFT).next_to(case1_title, DOWN, buff=0.8).align_to(case1_title,
                                                                                                          LEFT)

        for mob in group_c1:
            write_sync_camera(mob)
        self.wait(3)  # 【加长】情况1结束后的消化时间

        # ==================== 2. 当 |α| > 1 时 ====================
        case2_title = VGroup(
            Text("2. 当 ", font="KaiTi", font_size=40).set_color(TEXT_C),
            Tex(r"|\alpha| > 1", font_size=45).set_color(MATH_C),
            Text(" 时", font="KaiTi", font_size=40).set_color(TEXT_C)
        ).arrange(RIGHT, buff=0.1)
        case2_title.next_to(group_c1, DOWN, buff=2).align_to(case1_title, LEFT)

        write_sync_camera(case2_title)

        c2_step1 = Text("首先对被积函数进行巧妙的代数变形：", font="KaiTi", font_size=35).set_color(TEXT_C)
        c2_eq1 = Tex(
            r"1 - 2\alpha \cos x + \alpha^2 = \alpha^2 \left( 1 - 2\left(\frac{1}{\alpha}\right) \cos x + \left(\frac{1}{\alpha}\right)^2 \right)").set_color(
            MATH_C)

        c2_step2 = VGroup(
            Text("代回积分并利用对数性质 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"\ln(ab) = \ln(a) + \ln(b)").set_color(MATH_C),
            Text("：", font="KaiTi", font_size=35).set_color(TEXT_C)
        ).arrange(RIGHT, buff=0.1)

        c2_eq2 = Tex(
            r"I(\alpha) = \int_0^\pi \left[ \ln(\alpha^2) + \ln\left( 1 - 2\left(\frac{1}{\alpha}\right) \cos x + \left(\frac{1}{\alpha}\right)^2 \right) \right] dx").set_color(
            MATH_C)
        c2_eq3 = Tex(
            r"I(\alpha) = \int_0^\pi \ln(\alpha^2) \, dx + \int_0^\pi \ln\left( 1 - 2\left(\frac{1}{\alpha}\right) \cos x + \left(\frac{1}{\alpha}\right)^2 \right) dx").set_color(
            MATH_C)

        c2_step3 = Text("分解为两个积分：", font="KaiTi", font_size=35).set_color(TEXT_C)

        c2_eq4 = VGroup(
            Text("第一部分：", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"\int_0^\pi 2\ln|\alpha| \, dx = 2\pi \ln|\alpha|").set_color(MATH_C)
        ).arrange(RIGHT, buff=0.1)

        c2_eq5 = VGroup(
            Text("第二部分：因为 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"|\alpha| > 1 \Rightarrow \left|\frac{1}{\alpha}\right| < 1").set_color(MATH_C),
            Text("，符合情况 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex("1").set_color(EMPH_C),
            Text("，积分值为 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex("0").set_color(EMPH_C),
            Text("。", font="KaiTi", font_size=35).set_color(TEXT_C)
        ).arrange(RIGHT, buff=0.1)

        c2_eq6 = Tex(r"I(\alpha) = 2\pi \ln|\alpha|").set_color(RSLT_C)

        group_c2 = VGroup(c2_step1, c2_eq1, c2_step2, c2_eq2, c2_eq3, c2_step3, c2_eq4, c2_eq5, c2_eq6)
        group_c2.arrange(DOWN, buff=0.6, aligned_edge=LEFT).next_to(case2_title, DOWN, buff=0.8).align_to(case1_title,
                                                                                                          LEFT)

        for mob in group_c2:
            write_sync_camera(mob)
        self.wait(3)  # 【加长】情况2结束后的消化时间

        # ==================== 3. 当 |α| = 1 时 ====================
        case3_title = VGroup(
            Text("3. 当 ", font="KaiTi", font_size=40).set_color(TEXT_C),
            Tex(r"|\alpha| = 1", font_size=45).set_color(MATH_C),
            Text(" 时", font="KaiTi", font_size=40).set_color(TEXT_C)
        ).arrange(RIGHT, buff=0.1)
        case3_title.next_to(group_c2, DOWN, buff=2).align_to(case1_title, LEFT)

        write_sync_camera(case3_title)

        c3_eq1 = VGroup(
            Text("当 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"\alpha = 1").set_color(MATH_C),
            Text(" 时，被积函数变为 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"\ln(2(1-\cos x))").set_color(MATH_C)
        ).arrange(RIGHT, buff=0.1)

        c3_eq2 = VGroup(
            Text("当 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"\alpha = -1").set_color(MATH_C),
            Text(" 时，被积函数变为 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex(r"\ln(2(1+\cos x))").set_color(MATH_C)
        ).arrange(RIGHT, buff=0.1)

        c3_text1 = VGroup(
            Text("这两种情况都是广义积分，但均收敛，计算结果同为 ", font="KaiTi", font_size=35).set_color(TEXT_C),
            Tex("0").set_color(EMPH_C),
            Text("。", font="KaiTi", font_size=35).set_color(TEXT_C)
        ).arrange(RIGHT, buff=0.1)

        group_c3 = VGroup(c3_eq1, c3_eq2, c3_text1)
        group_c3.arrange(DOWN, buff=0.6, aligned_edge=LEFT).next_to(case3_title, DOWN, buff=0.8).align_to(case1_title,
                                                                                                          LEFT)

        for mob in group_c3:
            write_sync_camera(mob)
        self.wait(3)  # 【加长】情况3结束后的消化时间

        # ==================== 最终答案 ====================
        final_title = Text("综上所有情况，最终答案：", font="KaiTi", font_size=45).set_color(TEXT_C)
        final_title.next_to(group_c3, DOWN, buff=2).align_to(case1_title, LEFT)

        final_cases = Tex(
            r"\int_0^\pi \ln(1 - 2\alpha \cos x + \alpha^2) \, dx = \begin{cases} 0, & |\alpha| \le 1 \\ 2\pi \ln|\alpha|, & |\alpha| > 1 \end{cases}"
        ).set_color(MATH_C).scale(1.2)

        final_cases.next_to(final_title, DOWN, buff=1).set_x(0)

        write_sync_camera(final_title)
        write_sync_camera(final_cases)
        self.wait(2)  # 【加长】画框前的停顿

        # 外框特效
        rect = SurroundingRectangle(final_cases, buff=0.3).set_color(YELLOW)
        self.play(Write(rect), run_time=1.5)

        self.play(
            final_cases.animate.scale(1.2).set_color_by_gradient(BLUE, YELLOW, RED),
            rect.animate.scale(1.2).set_color(PINK),
            frame.animate.scale(1.1),
            run_time=2.0
        )
        self.wait(3)  # 【加长】大总结停留时间

        # ==================== 终极霸气炫彩居中收尾 ====================
        xiexie = Text("谢谢观看", font="KaiTi", font_size=140)
        xiexie.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        xiexie.fix_in_frame()

        all_mobs = Group(*self.mobjects)
        all_mobs.remove(frame)
        self.play(FadeOut(all_mobs), run_time=1.5)

        self.play(FadeIn(xiexie, scale=0.8), run_time=2.0)
        self.wait(4)  # 【加长】全剧终留白