from manimlib import *

class GuoShu(Scene):
    def construct(self):
        title = Text("勾股数生成公式", font="KaiTi", font_size=90)
        title.set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.move_to(1.5*UP))

        gongshi = Tex(r"a^2 + b^2 = c^2")
        gongshi.move_to(1.3*DOWN)
        gongshi.set_color_by_gradient(GREEN, BLUE, YELLOW, RED, PURPLE, ORANGE, TEAL)
        self.play(Write(gongshi))
        self.wait(1)

        self.play(title.animate.scale(0.45).to_corner(UL), FadeOut(gongshi, shift=DOWN))

        zhuyili = Tex(r"(2n+1)^2+(2n^2+2n)^2=(2n^2+2n+1)^2")
        zhuyili.set_color(BLUE)
        self.play(Write(zhuyili))

        self.wait(1)
        self.play(FadeOut(zhuyili, shift=DOWN))

        group1 = VGroup(
            Tex(r"|z^2| \, = \, {|z|}^2"),
            Tex(r"|(x+yi)^2| \, = \, {|x+yi|}^2"),
            Tex(r"|x^2-y^2+2xyi| \, = \, x^2+y^2"),
            Tex(r"\sqrt {(x^2-y^2)^2+(2xy)^2} \,=\,x^2+y^2"),
            Tex(r"(x^2-y^2)^2+(2xy)^2 \,=\,(x^2+y^2)^2")
        ).set_color(BLUE)

        self.play(Write(group1[0]))
        self.wait(2)

        for i in range(1, len(group1)):
            if i == 2:
                self.play(Transform(group1[i-1], group1[i]))
            else:
                self.remove(group1[1])
                self.play(TransformMatchingTex(group1[i-1], group1[i]))
            self.wait(2)

        self.wait(1)
        zhuyili1 = Tex(r"((n+1)^2-n^2)^2+(2n(n+1))^2 \,=\,((n+1)^2+n^2)^2").set_color(BLUE)
        self.play(TransformMatchingTex(group1[-1], zhuyili1))
        self.wait(1)
        self.play(Transform(zhuyili1, zhuyili))

        self.wait(1)
        self.play(FadeOut(zhuyili1))

        xiexie = Text("谢谢观看", font="KaiTi", font_size=140).set_color_by_gradient(BLUE, YELLOW, RED)
        self.play(
            Write(xiexie),
            FadeOut(title)
        )

