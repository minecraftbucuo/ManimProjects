from manim import *

# 强制设置竖屏分辨率和自适应帧大小
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 8.0
config.frame_height = 14.22


class ErdosPrimeDivergence(Scene):

    def construct(self):
        # ==================== 封面 ====================
        title = Text("Erdos的证明:质数倒数和发散", font="KaiTi", font_size=40)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)

        eq_cover = MathTex(
            r"\sum_{p \in \mathbb{P}} \frac{1}{p} = \infty", font_size=55
        ).set_color(BLUE)

        # 加大封面核心间距
        cover = VGroup(title, eq_cover).arrange(DOWN, buff=1.2).move_to(UP * 2)
        self.play(Write(title))
        self.play(FadeIn(eq_cover, shift=UP))
        self.wait(0.5)

        # ==================== 3秒倒计时 ====================
        for i in ["3", "2", "1"]:
            countdown_text = Text(i, font="KaiTi", font_size=150)
            countdown_text.set_color_by_gradient(RED, ORANGE, YELLOW)
            countdown_text.next_to(cover, DOWN, buff=2.0)  # 加大倒计时下移距离
            self.play(FadeIn(countdown_text, scale=0.5), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(countdown_text, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(cover))

        # ==================== 建立反证假设 ====================
        desc_1 = Text(
            "假设全体质数的倒数之和收敛：", font="KaiTi", font_size=26
        ).to_edge(UP, buff=1.5)
        eq_hyp = (
            MathTex(r"\sum_{i=1}^{\infty} \frac{1}{p_i} < \infty", font_size=32)
            .set_color(BLUE)
            .next_to(desc_1, DOWN, buff=0.8)  # 加大间距
        )
        self.play(Write(desc_1), Write(eq_hyp))
        self.wait(1.5)

        desc_2 = Text(
            "由级数的收敛性，其余项必可任意小。", font="KaiTi", font_size=26
        ).next_to(eq_hyp, DOWN, buff=0.9)  # 加大间距
        desc_3 = Text("由此，必然存在一个正整数", font="KaiTi", font_size=26)
        t_k = MathTex(r"k", font_size=28).set_color(YELLOW)
        desc_3_end = Text("满足：", font="KaiTi", font_size=26)
        g_k = (
            VGroup(desc_3, t_k, desc_3_end)
            .arrange(RIGHT, buff=0.05)
            .next_to(desc_2, DOWN, buff=0.5)  # 加大间距
        )

        eq_tail = (
            MathTex(r"\sum_{i=k+1}^{\infty} \frac{1}{p_i} < \frac{1}{2}", font_size=32)
            .set_color(YELLOW)
            .next_to(g_k, DOWN, buff=0.8)  # 加大间距
        )
        self.play(Write(desc_2), Write(g_k), Write(eq_tail))
        self.wait(2)

        desc_4 = Text(
            "基于此项，将全体质数划分为两类：", font="KaiTi", font_size=26
        ).next_to(eq_tail, DOWN, buff=0.9)  # 加大间距

        t_small = Text("小质数集合：", font="KaiTi", font_size=24)
        m_small = MathTex(
            r"S = \{p_1, p_2, \dots, p_k\}", font_size=26
        ).set_color(GREEN)
        g_small = (
            VGroup(t_small, m_small)
            .arrange(RIGHT, buff=0.1)
            .next_to(desc_4, DOWN, buff=0.6)  # 加大间距
        )

        t_large = Text("大质数集合：", font="KaiTi", font_size=24)
        m_large = MathTex(
            r"L = \{p_{k+1}, p_{k+2}, \dots\}", font_size=26
        ).set_color(ORANGE)
        g_large = (
            VGroup(t_large, m_large)
            .arrange(RIGHT, buff=0.1)
            .next_to(g_small, DOWN, buff=0.5)  # 加大间距
        )

        self.play(Write(desc_4), Write(g_small), Write(g_large))
        self.wait(3)

        # 清场释放空间
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 引入变量并分类 ====================
        desc_5 = Text("任取一个正整数", font="KaiTi", font_size=26)
        m_n = MathTex(r"N", font_size=28).set_color(YELLOW)
        desc_5_end = Text("，并考查以下两类整数计数：", font="KaiTi", font_size=26)
        g_n = (
            VGroup(desc_5, m_n, desc_5_end)
            .arrange(RIGHT, buff=0.05)
            .to_edge(UP, buff=1.5)
        )
        self.play(Write(g_n))

        m_nb_sym = MathTex(r"N_b", font_size=28).set_color(ORANGE)
        t_nb = Text("：在 ", font="KaiTi", font_size=24)
        m_nb_range = MathTex(r"1 \le n \le N", font_size=26)
        t_nb_end = Text(" 中，含大质数因子的整数个数。", font="KaiTi", font_size=24)
        g_nb_def = (
            VGroup(m_nb_sym, t_nb, m_nb_range, t_nb_end)
            .arrange(RIGHT, buff=0.05)
            .next_to(g_n, DOWN, buff=1.0)  # 加大间距
        )

        m_ns_sym = MathTex(r"N_s", font_size=28).set_color(GREEN)
        t_ns = Text("：在 ", font="KaiTi", font_size=24)
        m_ns_range = MathTex(r"1 \le n \le N", font_size=26)
        t_ns_end = Text(" 中，只含小质数因子的整数个数。", font="KaiTi", font_size=24)
        g_ns_def = (
            VGroup(m_ns_sym, t_ns, m_ns_range, t_ns_end)
            .arrange(RIGHT, buff=0.05)
            .next_to(g_nb_def, DOWN, buff=0.8)  # 加大间距
        )

        self.play(Write(g_nb_def), Write(g_ns_def))
        self.wait(2)

        desc_6 = Text(
            "显然，任何小于等于 N 的正整数必居其一：", font="KaiTi", font_size=26
        ).next_to(g_ns_def, DOWN, buff=1.0)  # 加大间距
        eq_sum = (
            MathTex(r"N_b + N_s \ge N", font_size=34)
            .set_color(BLUE)
            .next_to(desc_6, DOWN, buff=0.8)  # 加大间距
        )
        self.play(Write(desc_6), Write(eq_sum))

        rect_sum = SurroundingRectangle(eq_sum, color=BLUE, buff=0.2)
        self.play(Create(rect_sum))
        self.wait(3)

        # 清场
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 估计大质数贡献 Nb ====================
        desc_7 = Text("对于任意一个大质数", font="KaiTi", font_size=26)
        m_pi = MathTex(r"p_i", font_size=28).set_color(ORANGE)
        desc_7_end = Text("其在目标区间内的倍数个数为：", font="KaiTi", font_size=26)
        g_pi = (
            VGroup(desc_7, m_pi, desc_7_end)
            .arrange(DOWN, buff=0.5)
            .to_edge(UP, buff=1.5)
        )

        eq_floor = (
            MathTex(r"\lfloor \frac{N}{p_i} \rfloor \le \frac{N}{p_i}", font_size=30)
            .next_to(g_pi, DOWN, buff=0.8)  # 加大间距
        )
        self.play(Write(g_pi), Write(eq_floor))
        self.wait(1.5)

        desc_8 = Text(
            "对所有大质数因子的贡献进行放大求和：", font="KaiTi", font_size=26
        ).next_to(eq_floor, DOWN, buff=0.9)  # 加大间距

        eq_nb_1 = (
            MathTex(
                r"N_b \le \sum_{i=k+1}^{\infty} \lfloor \frac{N}{p_i} \rfloor",
                font_size=30,
            )
            .set_color(ORANGE)
            .next_to(desc_8, DOWN, buff=0.8)  # 加大间距
        )
        eq_nb_2 = (
            MathTex(
                r"\le \sum_{i=k+1}^{\infty} \frac{N}{p_i} = N \sum_{i=k+1}^{\infty} \frac{1}{p_i}",
                font_size=30,
            )
            .set_color(ORANGE)
            .next_to(eq_nb_1, DOWN, buff=0.5)  # 加大间距
        )

        self.play(Write(desc_8), Write(eq_nb_1))
        self.play(Write(eq_nb_2))
        self.wait(1.5)

        desc_9 = Text("代入先前得到的尾项假设：", font="KaiTi", font_size=26).next_to(
            eq_nb_2, DOWN, buff=0.9
        )  # 加大间距
        m_tail_ref = (
            MathTex(r"\sum_{i=k+1}^{\infty} \frac{1}{p_i} < \frac{1}{2}", font_size=28)
            .set_color(YELLOW)
            .next_to(desc_9, DOWN, buff=0.5)  # 加大间距
        )
        self.play(Write(desc_9), Write(m_tail_ref))

        eq_nb_final = (
            MathTex(r"N_b < N \cdot \frac{1}{2} = \frac{N}{2}", font_size=32)
            .set_color(RED)
            .next_to(m_tail_ref, DOWN, buff=0.8)  # 加大间距
        )
        self.play(Write(eq_nb_final))

        rect_nb = SurroundingRectangle(eq_nb_final, color=RED, buff=0.2)
        self.play(Create(rect_nb))
        self.wait(3)

        # 清场
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 估计小质数贡献 Ns ====================
        desc_10 = Text("对于只含小质数因子的任何整数", font="KaiTi", font_size=26)
        m_n2 = MathTex(r"n \le N", font_size=28).set_color(GREEN)
        desc_10_end = Text("均可唯一写为：", font="KaiTi", font_size=26)
        g_n2 = (
            VGroup(desc_10, m_n2, desc_10_end)
            .arrange(DOWN, buff=0.5)
            .to_edge(UP, buff=1.5)
        )

        eq_ab = (
            MathTex(r"n = a_n \cdot b_n^2", font_size=32)
            .set_color(GREEN)
            .next_to(g_n2, DOWN, buff=0.8)  # 加大间距
        )
        self.play(Write(g_n2), Write(eq_ab))
        self.wait(1.5)

        desc_11 = Text("其中", font="KaiTi", font_size=26)
        m_an = MathTex(r"a_n", font_size=28).set_color(YELLOW)
        desc_11_end = Text("为无平方因子数。其质因子", font="KaiTi", font_size=26)
        g_an_desc = (
            VGroup(desc_11, m_an, desc_11_end)
            .arrange(RIGHT, buff=0.05)
            .next_to(eq_ab, DOWN, buff=0.8)  # 加大间距
        )
        desc_11_sub = Text(
            "只能来自小质数集合，根据组合计数：", font="KaiTi", font_size=26
        ).next_to(g_an_desc, DOWN, buff=0.5)  # 加大间距
        self.play(Write(g_an_desc), Write(desc_11_sub))

        t_an_1 = Text("不同的 ", font="KaiTi", font_size=26)
        m_an_sym = MathTex(r"a_n", font_size=28)
        t_an_2 = Text(" 最多有 ", font="KaiTi", font_size=26)
        m_an_pow = MathTex(r"2^k", font_size=28)
        t_an_3 = Text(" 种", font="KaiTi", font_size=26)
        eq_an_count = (
            VGroup(t_an_1, m_an_sym, t_an_2, m_an_pow, t_an_3)
            .arrange(RIGHT, buff=0.05)
            .set_color(YELLOW)
            .next_to(desc_11_sub, DOWN, buff=0.6)  # 加大间距
        )
        self.play(Write(eq_an_count))
        self.wait(1.5)

        desc_12 = Text("同时，由不等式关系显然可得：", font="KaiTi", font_size=26).next_to(
            eq_an_count, DOWN, buff=0.8)  # 加大间距
        m_bn_ineq = (
            MathTex(r"b_n^2 \le n \le N \implies b_n \le \sqrt{N}", font_size=28)
            .set_color(YELLOW)
            .next_to(desc_12, DOWN, buff=0.5)  # 加大间距
        )
        self.play(Write(desc_12), Write(m_bn_ineq))

        t_bn_1 = Text("不同的 ", font="KaiTi", font_size=26)
        m_bn_sym = MathTex(r"b_n", font_size=28)
        t_bn_2 = Text(" 最多有 ", font="KaiTi", font_size=26)
        m_bn_sqrt = MathTex(r"\sqrt{N}", font_size=28)
        t_bn_3 = Text(" 种", font="KaiTi", font_size=26)
        eq_bn_count = (
            VGroup(t_bn_1, m_bn_sym, t_bn_2, m_bn_sqrt, t_bn_3)
            .arrange(RIGHT, buff=0.05)
            .set_color(YELLOW)
            .next_to(m_bn_ineq, DOWN, buff=0.6)  # 加大间距
        )
        self.play(Write(eq_bn_count))
        self.wait(1.5)

        desc_13 = Text("结合两部分的选法，可得上限：", font="KaiTi", font_size=26).next_to(
            eq_bn_count, DOWN, buff=0.8)  # 加大间距
        eq_ns_final = (
            MathTex(r"N_s \le 2^k \cdot \sqrt{N}", font_size=32)
            .set_color(GREEN)
            .next_to(desc_13, DOWN, buff=0.8)  # 加大间距
        )
        self.play(Write(desc_13), Write(eq_ns_final))

        rect_ns = SurroundingRectangle(eq_ns_final, color=GREEN, buff=0.2)
        self.play(Create(rect_ns))
        self.wait(3)

        # 清场
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ==================== 导出矛盾 ====================
        desc_14 = Text("将两部分的估计值代回原不等式：", font="KaiTi", font_size=26).to_edge(
            UP, buff=1.5)
        eq_comb_1 = (
            MathTex(r"N \le N_b + N_s", font_size=30)
            .set_color(BLUE)
            .next_to(desc_14, DOWN, buff=0.8)  # 加大间距
        )
        eq_comb_2 = (
            MathTex(r"N < \frac{N}{2} + 2^k \sqrt{N}", font_size=30)
            .set_color(RED)
            .next_to(eq_comb_1, DOWN, buff=0.5)  # 加大间距
        )
        self.play(Write(desc_14), Write(eq_comb_1))
        self.play(Write(eq_comb_2))
        self.wait(2)

        desc_15 = Text("移项化简，两边同时减去", font="KaiTi", font_size=26)
        m_half_n = MathTex(r"\frac{N}{2}", font_size=28).set_color(YELLOW)
        g_simplify = (
            VGroup(desc_15, m_half_n)
            .arrange(RIGHT, buff=0.05)
            .next_to(eq_comb_2, DOWN, buff=0.8)  # 加大间距
        )
        self.play(Write(g_simplify))

        eq_sim_1 = (
            MathTex(r"\frac{N}{2} < 2^k \sqrt{N}", font_size=30)
            .next_to(g_simplify, DOWN, buff=0.8)  # 加大间距
        )
        eq_sim_2 = (
            MathTex(r"\sqrt{N} < 2^{k+1} \implies N < 2^{2k+2}", font_size=30)
            .set_color(YELLOW)
            .next_to(eq_sim_1, DOWN, buff=0.5)  # 加大间距
        )
        self.play(Write(eq_sim_1))
        self.play(Write(eq_sim_2))
        self.wait(2.5)

        # 释放下半部分空间
        self.play(
            FadeOut(desc_14),
            FadeOut(eq_comb_1),
            FadeOut(eq_comb_2),
            FadeOut(g_simplify),
            FadeOut(eq_sim_1),
            FadeOut(eq_sim_2),
        )

        desc_16 = Text("此处关键在于：常数", font="KaiTi", font_size=26)
        m_k_fixed = MathTex(r"k", font_size=28).set_color(YELLOW)
        desc_16_end = Text(" 是固定不变的。", font="KaiTi", font_size=26)
        g_k_fixed = (
            VGroup(desc_16, m_k_fixed, desc_16_end)
            .arrange(RIGHT, buff=0.05)
            .to_edge(UP, buff=2.0)  # 精准定位顶部
        )

        desc_17 = Text("而上述关于 ", font="KaiTi", font_size=26)
        m_n_any = MathTex(r"N", font_size=28).set_color(YELLOW)
        desc_17_end = Text(" 的不等式必须对任意整数成立。", font="KaiTi", font_size=26)
        g_n_any = (
            VGroup(desc_17, m_n_any, desc_17_end)
            .arrange(RIGHT, buff=0.05)
            .next_to(g_k_fixed, DOWN, buff=0.9)  # 加大间距
        )

        self.play(Write(g_k_fixed), Write(g_n_any))
        self.wait(2)

        desc_18 = Text("如果我们选取足够大的整数", font="KaiTi", font_size=26)
        m_n_large = MathTex(r"N = 2^{2k+2}", font_size=28).set_color(RED)
        g_contradict = (
            VGroup(desc_18, m_n_large)
            .arrange(RIGHT, buff=0.05)
            .next_to(g_n_any, DOWN, buff=1.0)  # 加大间距
        )

        t_contradict = Text(
            "当 N 足够大时，此不等式不再成立。", font="KaiTi", font_size=28
        ).set_color(RED)
        t_contradict.next_to(g_contradict, DOWN, buff=0.8)  # 加大间距

        self.play(Write(g_contradict))
        self.play(Write(t_contradict))
        self.wait(3.5)

        # ==================== 最终结论 ====================
        self.play(*[FadeOut(m) for m in self.mobjects])

        desc_final = Text(
            "由此断定，原收敛假设不成立。", font="KaiTi", font_size=30
        ).to_edge(UP, buff=2.5)
        self.play(Write(desc_final))
        self.wait(1)

        outro_1 = (
            Text("全体质数的倒数之和必然发散", font="KaiTi", font_size=38)
            .set_color_by_gradient(RED, YELLOW)
            .next_to(desc_final, DOWN, buff=1.5)  # 加大间距
        )
        self.play(Write(outro_1))
        self.wait(1)

        eq_final_stat = (
            MathTex(r"\sum_{p \in \mathbb{P}} \frac{1}{p} = \infty", font_size=52)
            .set_color(BLUE)
            .next_to(outro_1, DOWN, buff=1.2)  # 加大间距
        )
        self.play(FadeIn(eq_final_stat, shift=UP))
        self.wait(2)

        outro_2 = Text("该结果表明：质数的分布", font="KaiTi", font_size=28).next_to(
            eq_final_stat, DOWN, buff=2.0)  # 加大底部收尾跨度
        outro_3 = (
            Text("比平方数序列要稠密得多。", font="KaiTi", font_size=32)
            .set_color(BLUE)
            .next_to(outro_2, DOWN, buff=0.8)  # 加大间距
        )
        self.play(Write(outro_2), Write(outro_3))
        self.wait(4)

        # 渐隐退出
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(1)