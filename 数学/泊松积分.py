from manimlib import *

class PoissonIntegralRigorous(Scene):
    def construct(self):
        # ==================== 封面 ====================
        title = Text("泊 松 积 分 的 推 导", font="KaiTi", font_size=80).shift(UP * 2)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW)

        integral = Tex(
            r"I = \int_{-\infty}^{+\infty} e^{-x^2} dx = ?",
            font_size=60
        ).shift(DOWN)
        integral.set_color_by_gradient(GREEN, BLUE, YELLOW)

        self.play(Write(title))
        self.play(Write(integral))
        self.wait(2)

        # 缩小并移至角落，腾出主舞台
        self.play(
            title.animate.scale(0.45).to_corner(UL, buff=0.4),
            integral.animate.scale(0.55).to_corner(UR, buff=0.4),
        )
        self.wait(1)
        title.fix_in_frame()
        integral.fix_in_frame()

        # ==================== 0. 一维与升维 ====================
        hint_text0 = Text("目标：求解一维高斯曲线下方的面积", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN,
                                                                                                                 buff=0.8)
        self.play(Write(hint_text0))

        eq1 = Tex(r"I", r"=", r"\int_{-\infty}^{+\infty} e^{-x^2} dx").set_color(BLUE)
        self.play(Write(eq1))
        self.wait(1)

        hint_text1 = Text("技巧：将其自身相乘，升维构造二重积分", font="KaiTi", font_size=35).set_color(BLUE).to_edge(
            DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text0, hint_text1))

        eq2 = Tex(r"I^2", r"=", r"\iint_{\mathbb{R}^2}", r"e^{-(x^2+y^2)}", r"dx dy").set_color(BLUE)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(2)

        self.play(FadeOut(eq2))

        # ==================== 1. 三维空间展示 (缩小视野) ====================
        hint_text2 = Text("在三维空间中，对应一个旋转对称的钟形曲面", font="KaiTi", font_size=35).set_color(
            BLUE).to_edge(DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text1, hint_text2))
        hint_text2.fix_in_frame()

        # 缩小 3D 场景比例，显得更精致
        self.play(self.camera.frame.animate.set_euler_angles(theta=-30 * DEGREES, phi=70 * DEGREES).scale(1.3),
                  run_time=1.5)

        axes3d = ThreeDAxes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[0, 1.5, 0.5],
            width=6, height=6, depth=6
        )

        surface = ParametricSurface(
            lambda u, v: axes3d.c2p(u, v, np.exp(-(u ** 2 + v ** 2))),
            u_range=(-3, 3), v_range=(-3, 3),
            resolution=(40, 40), color=TEAL, opacity=0.7
        )

        self.play(ShowCreation(axes3d))
        self.play(ShowCreation(surface), run_time=2)

        self.play(self.camera.frame.animate.increment_theta(120 * DEGREES), run_time=3, rate_func=linear)
        self.wait(1)

        self.play(
            self.camera.frame.animate.set_euler_angles(theta=0, phi=0).scale(1 / 1.3),
            FadeOut(axes3d), FadeOut(surface), run_time=1.5
        )

        # ==================== 2. 雅可比行列式推导 ====================
        hint_text3 = Text("利用旋转对称性，引入极坐标代换：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN,
                                                                                                                buff=0.8)
        hint_text2.unfix_from_frame()
        self.play(ReplacementTransform(hint_text2, hint_text3))

        eq3 = Tex(r"x = r\cos\theta, \quad y = r\sin\theta").set_color(YELLOW).shift(UP * 1)

        eq4 = Tex(r"dx dy", r"=",
                  r"\begin{vmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{vmatrix}", r"dr d\theta")
        eq4.next_to(eq3, DOWN, buff=0.5)

        eq5 = Tex(r"dx dy", r"=", r"(r\cos^2\theta + r\sin^2\theta)", r"dr d\theta")
        eq5.next_to(eq3, DOWN, buff=0.5)

        eq6 = Tex(r"dx dy", r"=", r"r", r"dr d\theta").set_color(YELLOW)
        eq6.next_to(eq3, DOWN, buff=0.5)

        self.play(Write(eq3))
        self.wait(1)
        self.play(Write(eq4))
        self.wait(1)
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait(1)
        self.play(TransformMatchingTex(eq5, eq6))
        self.wait(2)

        self.play(FadeOut(eq3))

        # 将 dxdy = r dr d\theta 悬浮在左下角
        hud_box = SurroundingRectangle(eq6, color=YELLOW, buff=0.15, stroke_width=2)
        hud_group = VGroup(eq6, hud_box)

        self.play(hud_group.animate.scale(0.7).to_corner(DL, buff=0.5))
        hud_group.fix_in_frame()
        self.wait(1)

        # ==================== 3. 极其详细的代入与计算 ====================

        # 步骤 3.1: 将原公式请回来，准备代换
        hint_text4 = Text("回到二重积分，将变量代换进去：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN,
                                                                                                                  buff=0.8)
        self.play(ReplacementTransform(hint_text3, hint_text4))

        eq_base = Tex(r"I^2", r"=", r"\iint_{\mathbb{R}^2}", r"e^{-(x^2+y^2)}", r"dx dy").set_color(BLUE)
        self.play(Write(eq_base))
        self.wait(1)

        # # 染色预警
        # self.play(
        #     eq_base[3].animate.set_color(RED),
        #     eq_base[4].animate.set_color(YELLOW)
        # )
        # self.wait(1)

        # 呼应左下角 HUD 闪烁
        self.play(hud_box.animate.set_stroke(width=6), run_time=0.4)
        self.play(hud_box.animate.set_stroke(width=2), run_time=0.4)

        hint_text4_1 = VGroup(
            Text("将 ", font="KaiTi", font_size=35),
            Tex(r"x, y", font_size=35),
            Text(" 和面积元替换为极坐标表达式：", font="KaiTi", font_size=35)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text4, hint_text4_1))

        # 【核心新增】：明确展示原始 x y 的代入过程，不直接跳步到 r^2
        eq_sub0 = Tex(r"I^2", r"=", r"\int_{0}^{2\pi} \int_{0}^{+\infty}", r"e^{-\left((r\cos\theta)^2 + (r\sin\theta)^2\right)}", r"r dr d\theta").set_color(BLUE)
        # eq_sub0[3].set_color(RED)
        # eq_sub0[4].set_color(YELLOW)
        self.play(TransformMatchingTex(eq_base, eq_sub0))
        self.wait(2.5)

        hint_text4_1_5 = Text("提取公因式，利用三角恒等式化简：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text4_1, hint_text4_1_5))

        # 视觉上演化：化简完成
        eq_sub1 = Tex(r"I^2", r"=", r"\int_{0}^{2\pi} \int_{0}^{+\infty}", r"e^{-r^2}", r"r dr d\theta").set_color(BLUE)
        # eq_sub1[3].set_color(RED)
        # eq_sub1[4].set_color(YELLOW)
        self.play(TransformMatchingTex(eq_sub0, eq_sub1))
        self.wait(2)

        # 步骤 3.2: 分离变量计算 theta
        hint_text4_2 = Text("将双重积分拆分，先计算极角部分：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN,
                                                                                                                  buff=0.8)
        self.play(ReplacementTransform(hint_text4_1_5, hint_text4_2))

        eq_sep = Tex(r"I^2", r"=", r"\left( \int_{0}^{2\pi} d\theta \right)", r"\cdot",
                     r"\left( \int_{0}^{+\infty} e^{-r^2} r dr \right)").set_color(BLUE)
        self.play(TransformMatchingTex(eq_sub1, eq_sep))
        self.wait(1.5)

        eq_sep2 = Tex(r"I^2", r"=", r"2\pi", r"\cdot", r"\int_{0}^{+\infty} e^{-r^2}", r"r dr").set_color(BLUE)
        self.play(TransformMatchingTex(eq_sep, eq_sep2))
        self.wait(2)

        # 步骤 3.3: 凑微分换元
        hint_text5 = VGroup(
            Text("对径向积分使用换元法：令 ", font="KaiTi", font_size=35),
            Tex("u = r^2", font_size=35, color=GREEN),
            Text("，则 ", font="KaiTi", font_size=35),
            Tex(r"r dr = \frac{1}{2} du", font_size=35, color=GREEN)
        ).arrange(RIGHT, buff=0.1).set_color(BLUE).to_edge(DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text4_2, hint_text5))
        self.wait(1)

        # 将 r dr 染色，准备替换
        self.play(eq_sep2[5].animate.set_color(GREEN))
        self.wait(1)

        # 明确展示替换结果
        eq_sub2 = Tex(r"I^2", r"=", r"2\pi", r"\cdot", r"\int_{0}^{+\infty} e^{-u}", r"\frac{1}{2} du").set_color(BLUE)
        # eq_sub2[4].set_color(GREEN)
        # eq_sub2[5].set_color(GREEN)
        self.play(TransformMatchingTex(eq_sep2, eq_sub2))
        self.wait(2)

        # 步骤 3.4: 提取常数与求原函数
        hint_text5_2 = Text("常数抵消并求出原函数：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text5, hint_text5_2))

        eq_int = Tex(r"I^2", r"=", r"\pi", r"\cdot", r"\left[ -e^{-u} \right]_{0}^{+\infty}").set_color(BLUE)
        self.play(TransformMatchingTex(eq_sub2, eq_int))
        self.wait(2)

        # 步骤 3.5: 代入上下限
        hint_text5_3 = Text("代入上下限：", font="KaiTi", font_size=35).set_color(BLUE).to_edge(DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text5_2, hint_text5_3))

        eq_calc = Tex(r"I^2", r"=", r"\pi", r"\cdot", r"(0 - (-1))").set_color(BLUE)
        self.play(TransformMatchingTex(eq_int, eq_calc))
        self.wait(1.5)

        eq_res = Tex(r"I^2", r"=", r"\pi").set_color(BLUE)
        self.play(TransformMatchingTex(eq_calc, eq_res))
        self.wait(2)

        # ==================== 4. 得出结论 ====================
        hint_text6 = Text("开平方得出最终结论：", font="KaiTi", font_size=35).set_color(YELLOW).to_edge(DOWN, buff=0.8)
        self.play(ReplacementTransform(hint_text5_3, hint_text6))

        self.play(
            FadeOut(hint_text6),
            FadeOut(hud_group, shift=DOWN),
            integral.animate.unfix_from_frame(),
            title.animate.unfix_from_frame()
        )

        final_eq = Tex(
            r"I = \int_{-\infty}^{+\infty} e^{-x^2} dx",
            r"=",
            r"\sqrt{\pi}"
        ).set_color(BLUE)

        self.play(
            TransformMatchingTex(
                eq_res, final_eq,
                key_map={r"I^2": r"I = \int_{-\infty}^{+\infty} e^{-x^2} dx", r"\pi": r"\sqrt{\pi}"}
            )
        )
        self.wait(1)

        rect = SurroundingRectangle(final_eq, buff=0.25, color=YELLOW)
        self.play(Write(rect))

        self.play(
            final_eq.animate.scale(1.5).set_color_by_gradient(BLUE, YELLOW, RED),
            rect.animate.scale(1.5),
            FadeOut(integral),
            FadeOut(title)
        )
        self.wait(3)

        xiexie = Text("谢谢观看", font="KaiTi", font_size=120).set_color_by_gradient(BLUE, YELLOW, RED)
        self.play(
            ReplacementTransform(final_eq, xiexie),
            FadeOut(rect)
        )
        self.wait(3)