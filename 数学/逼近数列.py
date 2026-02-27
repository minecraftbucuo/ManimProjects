from manim import *

class ApproximateSequence(Scene):
    def construct(self):
        definition = MathTex(r"""
        \begin{cases}
            \alpha_{\scriptscriptstyle{2k-1}}^{\scriptscriptstyle{(a,b)}} 
                &= \quad \left[ \alpha_{\scriptscriptstyle{2k-3}}^{\scriptscriptstyle{(a,b)}} \right]^2 
                + (a^2+b)\left[ \alpha_{\scriptscriptstyle{2k-2}}^{\scriptscriptstyle{(a,b)}} \right]^2 \\
            \alpha_{\scriptscriptstyle{2k}}^{\scriptscriptstyle{(a,b)}} 
                &= \quad 2\alpha_{\scriptscriptstyle{2k-2}}^{\scriptscriptstyle{(a,b)}}
                  \alpha_{\scriptscriptstyle{2k-3}}^{\scriptscriptstyle{(a,b)}} \\
            \alpha_{\scriptscriptstyle{1}}^{\scriptscriptstyle{(a,b)}} &= \quad a,
            \alpha_{\scriptscriptstyle{2}}^{\scriptscriptstyle{(a,b)}} = 1,
            a,k \in \mathbb{N}_{\scriptscriptstyle+} ~ , k \ge 2 ~ , b \in \mathbb{Z}
        \end{cases}
        """).set_color_by_gradient(BLUE, GREEN, YELLOW)

        # definition.set_color(BLUE)
        arrow = MathTex(r"\Updownarrow").set_color_by_gradient(BLUE, GREEN, YELLOW)

        sequence = MathTex(r"""
        \begin{cases}
            \alpha_{\scriptscriptstyle{2k-1}}^{\scriptscriptstyle{(a,b)}} &= \quad \frac
            {\left( a + \sqrt{a^2 + b} \right)^{2^{\scriptscriptstyle{k-1}}} +
             \left( a - \sqrt{a^2 + b} \right)^{2^{\scriptscriptstyle{k-1}}}}
            {2} \\
            \alpha_{\scriptscriptstyle{2k}}^{\scriptscriptstyle{(a,b)}} &= \quad \frac
            {\sqrt{a^2 + b} \left[
                \left( a + \sqrt{a^2 + b} \right)^{2^{\scriptscriptstyle{k-1}}} -
                \left( a - \sqrt{a^2 + b} \right)^{2^{\scriptscriptstyle{k-1}}}
            \right]}
            {2(a^2 + b)}
        \end{cases}
        """).set_color_by_gradient(YELLOW, GREEN, BLUE)

        # sequence.set_color(BLUE)

        group1 = VGroup(definition, arrow, sequence).arrange(DOWN)
        self.add(group1)
