# 2025.8.22
from manimlib import *

def myTex(text):
    mytex = Tex(text)
    mytex.set_color_by_gradient(GREEN, BLUE, YELLOW)
    return mytex

class SummationProblems3(Scene):
    def show_title(self):
        self.title = Tex(r"\sum_{i=0}^{n}{C_{n + i}^{i} 2^{n-i}} =  \space ?", font_size=90)
        self.title.set_color_by_gradient(GREEN, BLUE, YELLOW)
        self.play(Write(self.title))
        self.wait(1)

        self.play(self.title.animate.scale(0.45).to_corner(UL))
        self.wait(1)

    def show_end(self, last):
        xiexie = Text("谢谢观看", font="KaiTi", font_size=140).set_color_by_gradient(BLUE, YELLOW, RED)
        self.play(
            ReplacementTransform(last, xiexie),
        )
        self.wait(2)

    def construct(self):
        self.show_title()
        self.wait(1)
        daizhi = VGroup(
            myTex(r"\sum_{i=0}^{0}{C_{0 + i}^{i} 2^{0-i}} = 1"),
            myTex(r"\sum_{i=0}^{1}{C_{1 + i}^{i} 2^{1-i}} = 2 + 2"),
            myTex(r"\sum_{i=0}^{1}{C_{1 + i}^{i} 2^{1-i}} = 4"),
            myTex(r"\sum_{i=0}^{2}{C_{2 + i}^{i} 2^{2-i}} = 4 + 6 + 6"),
            myTex(r"\sum_{i=0}^{2}{C_{2 + i}^{i} 2^{2-i}} = 16"),
        )

        self.play(Write(daizhi[0]))
        self.wait(1)
        for i in range(1, len(daizhi)):
            self.play(TransformMatchingTex(daizhi[i - 1], daizhi[i]))
            self.wait(1)

        caixiang = myTex(r"\sum_{i=0}^{n}{C_{n + i}^{i} 2^{n-i}} = 4^n")
        self.play(TransformMatchingTex(daizhi[-1], caixiang))
        self.wait(2)

        tuidao = myTex(r"\sum_{i=0}^{n}{C_{n + i}^{i} 2^{n-i}} = 2^n \sum_{i=0}^{n}{C_{n + i}^{i} \frac{1}{2^i}}")
        self.play(TransformMatchingTex(caixiang, tuidao))
        self.wait(1)

        s_n = myTex(r"S_n = \sum_{i=0}^{n}{C_{n + i}^{i} \frac{1}{2^i}}")
        s_n.shift(UP * 1.5)
        self.play(Write(s_n))
        self.play(s_n.animate.scale(0.83).to_corner(UR))

        tuidao2 = myTex(r"\sum_{i=0}^{n}{C_{n + i}^{i} 2^{n-i}} = 2^n S_n")
        self.play(TransformMatchingTex(tuidao, tuidao2))
        self.play(tuidao2.animate.shift(UP * 1.7))
        self.wait(1)

        tuidao3 = VGroup(
            myTex(r"S_{n + 1} = 2S_n \quad ?"),
            myTex(r"S_{n + 1} = \sum_{i=0}^{n + 1}{C_{n + 1 + i}^{i} \frac{1}{2^i}}"),
            myTex(r"S_{n + 1} = \sum_{i=0}^{n + 1}({C_{n + i}^{i} + C_{n + i}^{i - 1}) \frac{1}{2^i}}"),
            myTex(r"S_{n + 1} = \sum_{i=0}^{n + 1}{C_{n + i}^{i} \frac{1}{2^i}} + \sum_{i=0}^{n + 1}{C_{n + i}^{i - 1} \frac{1}{2^i}}"),

            myTex(r"S_{n + 1} = S_n + C_{2n+1}^{n+1}\frac{1}{2^{n+1}} + \sum_{i=0}^{n + 1}{C_{n + i}^{i - 1} \frac{1}{2^i}}"),

            myTex(r"S_{n + 1} = S_n + C_{2n+1}^{n+1}\frac{1}{2^{n+1}} + \frac{1}{2} \left( S_{n + 1} - C_{2n+2}^{n+1}\frac{1}{2^{n + 1}} \right)"),
            myTex(r"S_{n + 1} = S_n + \frac{1}{2}S_{n+1} + \frac{1}{2^{n+1}} \left( C_{2n+1}^{n+1} - \frac{1}{2}C_{2n+2}^{n+1} \right)"),
            myTex(r"S_{n + 1} = S_n + \frac{1}{2}S_{n+1}"),
            myTex(r"S_{n + 1} = 2S_n"),
            myTex(r"S_n=2^n"),
        )
        self.play(Write(tuidao3[0]))
        self.wait(1)
        for i in range(1, 4):
            self.play(TransformMatchingTex(tuidao3[i - 1], tuidao3[i]))
            self.wait(1)

        zuo = VGroup(
            myTex(r"\sum_{i=0}^{n + 1}{C_{n + i}^{i} \frac{1}{2^i}}"),
            myTex(r"\sum_{i=0}^{n + 1}{C_{n + i}^{i} \frac{1}{2^i}}=\sum_{i=0}^{n}{C_{n + i}^{i} \frac{1}{2^i}} + C_{2n+1}^{n+1}\frac{1}{2^{n+1}}"),
            myTex(r"\sum_{i=0}^{n + 1}{C_{n + i}^{i} \frac{1}{2^i}} = S_n + C_{2n+1}^{n+1}\frac{1}{2^{n+1}}")
        )
        zuo.shift(DOWN * 1.6)
        self.play(Write(zuo[0]))
        self.wait(1)
        for i in range(1, len(zuo)):
            self.play(TransformMatchingTex(zuo[i - 1], zuo[i]))
            self.wait(1)

        self.play(TransformMatchingTex(tuidao3[3], tuidao3[4]))
        self.wait(1)

        you = VGroup(
            myTex(r"\sum_{i=0}^{n + 1}{C_{n + i}^{i - 1} \frac{1}{2^i}}"),
            myTex(r"\sum_{i=0}^{n + 1}{C_{n + i}^{i - 1} \frac{1}{2^i}} = \frac{1}{2} \sum_{i=0}^{n + 1}{C_{n + i}^{i - 1} \frac{1}{2^{i - 1}}}"),
            myTex(r"\sum_{i=0}^{n + 1}{C_{n + i}^{i - 1} \frac{1}{2^i}} = \frac{1}{2} \sum_{i=0}^{n}{C_{n + 1 + i}^{i} \frac{1}{2^{i}}}"),
            myTex(r"\sum_{i=0}^{n + 1}{C_{n + i}^{i - 1} \frac{1}{2^i}} = \frac{1}{2} \left( \sum_{i=0}^{n + 1}{C_{n + 1 + i}^{i} \frac{1}{2^{i}}} - C_{2n+2}^{n+1}\frac{1}{2^{n + 1}} \right)"),
            myTex(r"\sum_{i=0}^{n + 1}{C_{n + i}^{i - 1} \frac{1}{2^i}} = \frac{1}{2} \left( S_{n + 1} - C_{2n+2}^{n+1}\frac{1}{2^{n + 1}} \right)"),
        )
        you.shift(DOWN * 1.6)
        self.play(TransformMatchingTex(zuo[-1], you[0]))
        self.wait(1)
        for i in range(1, len(you)):
            self.play(TransformMatchingTex(you[i - 1], you[i]))
            self.wait(1)

        self.play(TransformMatchingTex(tuidao3[4], tuidao3[5]))
        self.play(FadeOut(you[-1]))
        self.wait(1)
        for i in range(6, len(tuidao3)):
            self.play(TransformMatchingTex(tuidao3[i - 1], tuidao3[i]))
            self.wait(1)

        tuidao2_ = myTex(r"\sum_{i=0}^{n}{C_{n + i}^{i} 2^{n-i}} = 4^n")
        tuidao2_.move_to(tuidao2.get_center())
        self.play(TransformMatchingTex(tuidao2, tuidao2_))
        self.wait(1)

        new_title = myTex(r"\sum_{i=0}^{n}{C_{n + i}^{i} 2^{n-i}} = 4^n").scale(0.83)
        new_title.move_to(self.title.get_center())
        self.play(TransformMatchingTex(self.title, new_title))
        rect = SurroundingRectangle(self.title, buff=0.05, color=YELLOW)
        rect.scale(1.2)
        self.play(ShowCreation(rect))
        self.wait(1)
        self.play(
            FadeOut(s_n),
            FadeOut(tuidao3[-1]),
            new_title.animate.scale(2).move_to(ORIGIN),
            FadeOut(tuidao2_),
            rect.animate.scale(3).move_to(ORIGIN),
        )
        self.wait(1)

        self.show_end(new_title)











