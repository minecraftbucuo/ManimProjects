# codex gpt-5.5

from __future__ import annotations

from dataclasses import dataclass

from manim import *


FONT = "Microsoft YaHei"
BG = "#10131A"
PANEL = "#1A1F2B"
INK = "#E8ECF1"
MUTED = "#8892A6"
NODE_FILL = "#202636"
EDGE = "#596275"
YELLOW = "#F6C85F"
GREEN = "#4CC38A"
ORANGE = "#FF9F43"
RED = "#FF6B6B"
BLUE = "#6CA8FF"


@dataclass
class TreeNode:
    left: int
    right: int
    value: int
    depth: int
    x: float = 0
    y: float = 0
    left_child: "TreeNode | None" = None
    right_child: "TreeNode | None" = None
    circle: Circle | None = None
    label: Text | None = None
    mob: VGroup | None = None
    edge_left: Line | None = None
    edge_right: Line | None = None


class SegmentTreeDemo(Scene):
    def construct(self):
        self.camera.background_color = BG
        values = [2, 1, 5, 3, 4, 7, 6, 8]
        root = self.build_model(values)
        nodes = self.collect_nodes(root)
        nodes_by_depth = self.group_by_depth(nodes)
        self.place_tree(root)
        self.attach_tree_mobjects(nodes)

        self.play_cover(values)

        title = Text("线段树：区间和的快速维护", font=FONT, font_size=30, color=INK)
        title.to_edge(UP, buff=0.12)
        subtitle = Text(
            "把数组切成层层区间：查询只拿完整覆盖的块，更新只改一条路径",
            font=FONT,
            font_size=17,
            color=MUTED,
        )
        subtitle.next_to(title, DOWN, buff=0.06)
        rule = Line(LEFT * 6.5, RIGHT * 6.5, color="#2C3446", stroke_width=2)
        rule.next_to(subtitle, DOWN, buff=0.12)

        array_bar, array_cells = self.make_array_bar(values)
        self.play(FadeIn(title, shift=DOWN * 0.15), FadeIn(subtitle), Create(rule))
        self.play(FadeIn(array_bar, shift=UP * 0.2), run_time=0.8)
        self.wait(0.4)

        self.play_build_sequence(nodes_by_depth, array_cells)
        self.play_query_sequence(root, array_cells)
        self.play_update_sequence(root, array_cells)
        self.play_final_query(root, array_cells)
        self.play_code_outro()


    def play_cover(self, values: list[int]):
        grid = self.make_cover_grid()
        tree = self.make_cover_tree()
        array_strip = self.make_cover_array(values)

        frame = Rectangle(width=12.6, height=6.55, stroke_color="#2E384D", stroke_width=1.4)
        frame.set_fill(opacity=0)
        frame.set_z_index(1)

        kicker = Text("RANGE QUERY DATA STRUCTURE", font=FONT, font_size=15, color=BLUE)
        kicker.set_opacity(0.9)
        kicker.move_to([-3.7, 1.28, 0])

        title = Text("SEGMENT TREE", font=FONT, font_size=54, weight=BOLD, color=INK)
        title.move_to([-2.45, 0.58, 0])
        title_glow = title.copy().set_color(BLUE).set_opacity(0.22).scale(1.018)

        cn_title = Text("线段树演示动画", font=FONT, font_size=31, color=INK)
        cn_title.move_to([-3.0, -0.08, 0])

        subtitle = Text("建树 · 区间查询 · 单点更新", font=FONT, font_size=19, color=MUTED)
        subtitle.move_to([-3.1, -0.62, 0])

        chips = VGroup(
            self.make_cover_chip("区间和"),
            self.make_cover_chip("O(log n)"),
            self.make_cover_chip("Point Update"),
        )
        chips.arrange(RIGHT, buff=0.16)
        chips.move_to([-3.18, -1.16, 0])

        accent = VGroup(
            Line([-5.92, 1.72, 0], [-4.05, 1.72, 0], color=GREEN, stroke_width=3),
            Line([-5.92, 1.58, 0], [-5.2, 1.58, 0], color=ORANGE, stroke_width=3),
            Line([-5.92, 1.44, 0], [-4.72, 1.44, 0], color=BLUE, stroke_width=3),
        )

        scan = Line([-6.1, -2.75, 0], [-6.1, 2.75, 0], color=GREEN, stroke_width=2)
        scan.set_opacity(0.35)

        cover = VGroup(
            grid,
            tree,
            array_strip,
            frame,
            title_glow,
            kicker,
            title,
            cn_title,
            subtitle,
            chips,
            accent,
            scan,
        )

        self.play(FadeIn(grid), Create(frame), run_time=0.8)
        self.play(
            LaggedStart(Create(accent), FadeIn(kicker, shift=RIGHT * 0.18), lag_ratio=0.18),
            run_time=0.7,
        )
        self.play(
            FadeIn(title_glow),
            FadeIn(title, shift=UP * 0.18),
            FadeIn(cn_title, shift=UP * 0.12),
            run_time=0.9,
        )
        self.play(FadeIn(subtitle), LaggedStart(*[FadeIn(chip, shift=UP * 0.08) for chip in chips], lag_ratio=0.15))
        self.play(LaggedStart(Create(tree), FadeIn(array_strip, shift=UP * 0.12), lag_ratio=0.12), run_time=1.2)
        self.play(scan.animate.shift(RIGHT * 12.2), run_time=1.2, rate_func=linear)
        self.wait(0.45)
        self.play(FadeOut(cover, shift=UP * 0.12), run_time=0.8)

    def make_cover_grid(self) -> VGroup:
        grid = VGroup()
        for x in [i * 0.5 for i in range(-13, 14)]:
            line = Line([x, -3.3, 0], [x, 3.3, 0], color="#222A3A", stroke_width=0.7)
            line.set_opacity(0.33 if abs(x) % 1 else 0.5)
            grid.add(line)
        for y in [i * 0.5 for i in range(-7, 8)]:
            line = Line([-6.7, y, 0], [6.7, y, 0], color="#222A3A", stroke_width=0.7)
            line.set_opacity(0.33 if abs(y) % 1 else 0.5)
            grid.add(line)

        diagonals = VGroup(
            Line([-6.5, -2.4, 0], [-2.5, 3.1, 0], color="#1F6FEB", stroke_width=1),
            Line([2.2, -3.0, 0], [6.6, 2.1, 0], color="#26A269", stroke_width=1),
        )
        diagonals.set_opacity(0.18)
        grid.add(diagonals)
        return grid

    def make_cover_tree(self) -> VGroup:
        positions = {
            "root": [3.45, 1.75, 0],
            "l": [2.1, 0.78, 0],
            "r": [4.8, 0.78, 0],
            "ll": [1.45, -0.18, 0],
            "lr": [2.75, -0.18, 0],
            "rl": [4.15, -0.18, 0],
            "rr": [5.45, -0.18, 0],
            "a": [1.12, -1.12, 0],
            "b": [1.78, -1.12, 0],
            "c": [2.42, -1.12, 0],
            "d": [3.08, -1.12, 0],
            "e": [3.82, -1.12, 0],
            "f": [4.48, -1.12, 0],
            "g": [5.12, -1.12, 0],
            "h": [5.78, -1.12, 0],
        }
        edges = [
            ("root", "l"),
            ("root", "r"),
            ("l", "ll"),
            ("l", "lr"),
            ("r", "rl"),
            ("r", "rr"),
            ("ll", "a"),
            ("ll", "b"),
            ("lr", "c"),
            ("lr", "d"),
            ("rl", "e"),
            ("rl", "f"),
            ("rr", "g"),
            ("rr", "h"),
        ]
        labels = {
            "root": "[0,7]",
            "l": "[0,3]",
            "r": "[4,7]",
            "ll": "[0,1]",
            "lr": "[2,3]",
            "rl": "[4,5]",
            "rr": "[6,7]",
        }

        group = VGroup()
        for start, end in edges:
            line = Line(positions[start], positions[end], color="#596275", stroke_width=1.8)
            line.set_opacity(0.72)
            group.add(line)

        for key, point in positions.items():
            radius = 0.25 if key in "abcdefgh" else 0.28
            circle = Circle(radius=radius, stroke_color="#6CA8FF", stroke_width=1.7)
            circle.set_fill("#171D2A", opacity=0.96)
            circle.move_to(point)
            if key in {"lr", "rl", "g"}:
                circle.set_stroke(GREEN, width=2.6)
                circle.set_fill("#19342E", opacity=0.95)
            group.add(circle)
            if key in labels:
                label = Text(labels[key], font=FONT, font_size=10, color=INK)
                label.move_to(point)
                group.add(label)

        badge = Text("query [2,6]", font=FONT, font_size=14, color=GREEN)
        badge.move_to([4.25, -1.78, 0])
        underline = Line([3.4, -1.98, 0], [5.12, -1.98, 0], color=GREEN, stroke_width=2.2)
        group.add(badge, underline)
        return group

    def make_cover_array(self, values: list[int]) -> VGroup:
        group = VGroup()
        cells = VGroup()
        for index, value in enumerate(values):
            box = RoundedRectangle(
                width=0.38,
                height=0.38,
                corner_radius=0.035,
                stroke_color=GREEN if 2 <= index <= 6 else "#3B465C",
                stroke_width=1.6,
                fill_color="#151B26",
                fill_opacity=1,
            )
            value_text = Text(str(value), font=FONT, font_size=12, color=INK)
            value_text.move_to(box)
            cells.add(VGroup(box, value_text))
        cells.arrange(RIGHT, buff=0.08)
        cells.move_to([4.35, -2.45, 0])

        left_bracket = Text("[", font=FONT, font_size=28, color=GREEN)
        right_bracket = Text("]", font=FONT, font_size=28, color=GREEN)
        left_bracket.next_to(cells[2], LEFT, buff=0.01)
        right_bracket.next_to(cells[6], RIGHT, buff=0.01)

        label = Text("array blocks", font=FONT, font_size=12, color=MUTED)
        label.next_to(cells, DOWN, buff=0.16)
        group.add(cells, left_bracket, right_bracket, label)
        return group

    def make_cover_chip(self, text: str) -> VGroup:
        label = Text(text, font=FONT, font_size=13, color=INK)
        box = RoundedRectangle(
            width=max(1.0, label.width + 0.32),
            height=0.34,
            corner_radius=0.08,
            stroke_color="#3B465C",
            stroke_width=1.2,
            fill_color="#171D2A",
            fill_opacity=0.88,
        )
        label.move_to(box)
        return VGroup(box, label)

    def build_model(self, values: list[int]) -> TreeNode:
        def build(left: int, right: int, depth: int) -> TreeNode:
            if left == right:
                return TreeNode(left, right, values[left], depth)
            mid = (left + right) // 2
            left_child = build(left, mid, depth + 1)
            right_child = build(mid + 1, right, depth + 1)
            return TreeNode(
                left,
                right,
                left_child.value + right_child.value,
                depth,
                left_child=left_child,
                right_child=right_child,
            )

        return build(0, len(values) - 1, 0)

    def collect_nodes(self, root: TreeNode) -> list[TreeNode]:
        result: list[TreeNode] = []

        def walk(node: TreeNode):
            result.append(node)
            if node.left_child:
                walk(node.left_child)
            if node.right_child:
                walk(node.right_child)

        walk(root)
        return result

    def group_by_depth(self, nodes: list[TreeNode]) -> dict[int, list[TreeNode]]:
        grouped: dict[int, list[TreeNode]] = {}
        for node in nodes:
            grouped.setdefault(node.depth, []).append(node)
        for level in grouped.values():
            level.sort(key=lambda item: item.left)
        return grouped

    def place_tree(self, root: TreeNode):
        root_y = 2.0
        depth_gap = 0.98
        leaf_gap = 1.12

        leaves: list[TreeNode] = []

        def gather_leaves(node: TreeNode):
            if node.left == node.right:
                leaves.append(node)
                return
            gather_leaves(node.left_child)
            gather_leaves(node.right_child)

        gather_leaves(root)
        center = (len(leaves) - 1) / 2
        for index, leaf in enumerate(leaves):
            leaf.x = (index - center) * leaf_gap
            leaf.y = root_y - leaf.depth * depth_gap

        def place_internal(node: TreeNode):
            if node.left == node.right:
                return
            place_internal(node.left_child)
            place_internal(node.right_child)
            node.x = (node.left_child.x + node.right_child.x) / 2
            node.y = root_y - node.depth * depth_gap

        place_internal(root)

    def attach_tree_mobjects(self, nodes: list[TreeNode]):
        for node in nodes:
            circle = Circle(radius=0.36, color=EDGE, stroke_width=2.5)
            circle.set_fill(NODE_FILL, opacity=0.95)
            circle.move_to([node.x, node.y, 0])
            circle.set_z_index(2)
            label = self.make_node_label(node)
            label.move_to(circle.get_center())
            label.set_z_index(3)
            node.circle = circle
            node.label = label
            node.mob = VGroup(circle, label)

        for node in nodes:
            if node.left_child:
                node.edge_left = self.make_edge(node, node.left_child)
            if node.right_child:
                node.edge_right = self.make_edge(node, node.right_child)

    def make_edge(self, parent: TreeNode, child: TreeNode) -> Line:
        edge = Line(parent.circle.get_center(), child.circle.get_center())
        edge.set_stroke(EDGE, width=2.2, opacity=0.85)
        edge.set_z_index(0)
        return edge

    def make_node_label(self, node: TreeNode) -> Text:
        return Text(
            f"[{node.left},{node.right}]\n{node.value}",
            font=FONT,
            font_size=12,
            line_spacing=0.55,
            color=INK,
        )

    def make_array_bar(self, values: list[int]):
        group = VGroup()
        cells = []
        cell_w = 0.62
        gap = 0.1
        total_w = len(values) * cell_w + (len(values) - 1) * gap
        start_x = -total_w / 2 + cell_w / 2
        y = -3.28

        caption = Text("原数组 a", font=FONT, font_size=17, color=INK)
        caption.move_to([-5.55, y + 0.05, 0])
        caption.set_z_index(6)
        group.add(caption)

        for index, value in enumerate(values):
            x = start_x + index * (cell_w + gap)
            box = RoundedRectangle(
                width=cell_w,
                height=0.62,
                corner_radius=0.04,
                stroke_color="#3B465C",
                stroke_width=2,
                fill_color="#171C27",
                fill_opacity=1,
            )
            box.move_to([x, y, 0])
            box.set_z_index(2)
            value_text = Text(str(value), font=FONT, font_size=18, color=INK)
            value_text.move_to(box.get_center())
            value_text.set_z_index(8)
            index_text = Text(str(index), font=FONT, font_size=12, color=MUTED)
            index_text.next_to(box, DOWN, buff=0.08)
            index_text.set_z_index(8)
            cell = VGroup(box, value_text, index_text)
            group.add(cell)
            cells.append({"box": box, "value": value_text, "index": index_text, "group": cell})

        return group, cells

    def play_build_sequence(self, nodes_by_depth, array_cells):
        leaves = nodes_by_depth[3]
        self.show_stage("1. 建树：叶子就是单个数组元素")
        leaf_anims = []
        for leaf in leaves:
            leaf_anims.append(FadeIn(leaf.mob, shift=UP * 0.18))
            leaf_anims.append(array_cells[leaf.left]["box"].animate.set_stroke(BLUE, width=3))
        self.play(LaggedStart(*leaf_anims, lag_ratio=0.08), run_time=2.2)
        self.play(*[cell["box"].animate.set_stroke("#3B465C", width=2) for cell in array_cells])

        descriptions = {
            2: "相邻叶子合并：长度 2 的区间",
            1: "继续向上合并：长度 4 的区间",
            0: "根节点保存整个数组的区间和",
        }
        for depth in [2, 1, 0]:
            nodes = nodes_by_depth[depth]
            note = Text(descriptions[depth], font=FONT, font_size=17, color=INK)
            note.move_to([0, 2.88, 0])
            formulas = VGroup(
                *[
                    Text(
                        f"[{n.left},{n.right}] = {n.left_child.value} + {n.right_child.value} = {n.value}",
                        font=FONT,
                        font_size=12 if depth == 2 else 13,
                        color=MUTED,
                    )
                    for n in nodes
                ]
            )
            formulas.arrange(RIGHT, buff=0.28)
            formulas.move_to([0, 2.56, 0])
            if formulas.width > 11:
                formulas.scale_to_fit_width(11)

            edge_anims = []
            node_anims = []
            for node in nodes:
                edge_anims.extend([Create(node.edge_left), Create(node.edge_right)])
                node_anims.append(FadeIn(node.mob, shift=UP * 0.14))
                node_anims.append(Indicate(node.left_child.mob, color=YELLOW, scale_factor=1.08))
                node_anims.append(Indicate(node.right_child.mob, color=YELLOW, scale_factor=1.08))
            self.play(FadeIn(note), FadeIn(formulas), run_time=0.5)
            self.play(LaggedStart(*edge_anims, lag_ratio=0.04), run_time=0.8)
            self.play(LaggedStart(*node_anims, lag_ratio=0.05), run_time=1.5)
            self.wait(0.25)
            self.play(FadeOut(note), FadeOut(formulas), run_time=0.45)

        root = nodes_by_depth[0][0]
        total = Text(f"数组总和 = 根节点 [{root.left},{root.right}] = {root.value}", font=FONT, font_size=18, color=GREEN)
        total.move_to([0, 2.88, 0])
        self.play(Indicate(root.mob, color=GREEN, scale_factor=1.08), FadeIn(total))
        self.wait(0.8)
        self.play(FadeOut(total))

    def play_query_sequence(self, root: TreeNode, array_cells):
        self.show_stage("2. 区间查询：sum(2, 6)")
        self.reset_array_cells(array_cells)
        self.reset_tree(root)

        for index in range(2, 7):
            self.play(
                array_cells[index]["box"].animate.set_fill("#243A33", opacity=1).set_stroke(GREEN, width=3),
                array_cells[index]["index"].animate.set_color(GREEN),
                run_time=0.12,
            )

        panel = self.make_panel("查询目标", ["sum(2, 6)", "只取完整覆盖的节点"])
        self.play(FadeIn(panel, shift=LEFT * 0.2))

        partial = [root, self.find_node(root, 0, 3), self.find_node(root, 4, 7), self.find_node(root, 6, 7)]
        skipped = [self.find_node(root, 0, 1), self.find_node(root, 7, 7)]
        hits = [self.find_node(root, 2, 3), self.find_node(root, 4, 5), self.find_node(root, 6, 6)]

        self.play(*[self.node_color_animation(n, YELLOW, 4) for n in partial], run_time=0.75)
        self.play(*[self.node_dim_animation(n) for n in skipped], run_time=0.55)

        running = 0
        lines = ["命中节点："]
        for hit in hits:
            running += hit.value
            lines.append(f"[{hit.left},{hit.right}] = {hit.value}")
            lines.append(f"当前答案 = {running}")
            new_panel = self.make_panel("查询目标", ["sum(2, 6)", *lines])
            self.play(
                self.node_color_animation(hit, GREEN, 5),
                Transform(panel, new_panel),
                run_time=0.75,
            )
            self.wait(0.25)
            lines.pop()

        answer_panel = self.make_panel("查询结果", ["8 + 11 + 6", "答案 = 25"])
        self.play(Transform(panel, answer_panel), run_time=0.6)
        self.wait(1)
        self.play(FadeOut(panel))

    def play_update_sequence(self, root: TreeNode, array_cells):
        self.show_stage("3. 单点更新：a[3] 从 3 改成 9")
        self.reset_tree(root)
        self.reset_array_cells(array_cells)

        update_panel = self.make_panel("更新", ["a[3] = 9", "差值 delta = +6", "只影响一条根到叶路径"])
        self.play(FadeIn(update_panel, shift=LEFT * 0.2))

        for index, cell in enumerate(array_cells):
            target = ORANGE if index == 3 else "#3B465C"
            width = 3 if index == 3 else 2
            self.play(cell["box"].animate.set_stroke(target, width=width), run_time=0.06)

        new_value = Text("9", font=FONT, font_size=18, color=ORANGE)
        new_value.move_to(array_cells[3]["value"].get_center())
        new_value.set_z_index(8)
        self.play(Transform(array_cells[3]["value"], new_value), run_time=0.6)

        path = [
            self.find_node(root, 3, 3),
            self.find_node(root, 2, 3),
            self.find_node(root, 0, 3),
            root,
        ]
        new_values = [9, 14, 17, 42]

        for node, value in zip(path, new_values):
            self.play(self.node_color_animation(node, ORANGE, 5), run_time=0.35)
            replacement = Text(
                f"[{node.left},{node.right}]\n{value}",
                font=FONT,
                font_size=12,
                line_spacing=0.55,
                color=INK,
            )
            replacement.move_to(node.circle.get_center())
            node.value = value
            self.play(Transform(node.label, replacement), run_time=0.5)
            self.wait(0.15)

        changed = Text("只有包含下标 3 的区间需要重算", font=FONT, font_size=18, color=ORANGE)
        changed.move_to([0, 2.86, 0])
        self.play(FadeIn(changed), run_time=0.45)
        self.wait(0.8)
        self.play(FadeOut(changed), FadeOut(update_panel))

    def play_final_query(self, root: TreeNode, array_cells):
        self.show_stage("4. 更新后再次查询：sum(2, 6)")
        self.reset_tree(root)
        self.reset_array_cells(array_cells)

        for index in range(2, 7):
            self.play(
                array_cells[index]["box"].animate.set_fill("#243A33", opacity=1).set_stroke(GREEN, width=3),
                array_cells[index]["index"].animate.set_color(GREEN),
                run_time=0.08,
            )

        hits = [self.find_node(root, 2, 3), self.find_node(root, 4, 5), self.find_node(root, 6, 6)]
        panel = self.make_panel("更新后结果", ["命中节点不变", "[2,3] = 14", "[4,5] = 11", "[6,6] = 6", "答案 = 31"])
        self.play(FadeIn(panel, shift=LEFT * 0.2), *[self.node_color_animation(n, GREEN, 5) for n in hits], run_time=1.0)

        insight = Text("查询路径复用，答案自动反映最新数组", font=FONT, font_size=18, color=GREEN)
        insight.move_to([0, 2.86, 0])
        self.play(FadeIn(insight))
        self.wait(1.2)
        self.play(FadeOut(insight), FadeOut(panel))

    def play_code_outro(self):
        existing = list(self.mobjects)
        if existing:
            self.play(*[FadeOut(mob, shift=DOWN * 0.08) for mob in existing], run_time=0.8)

        title = Text("代码落地：三段核心逻辑", font=FONT, font_size=28, color=INK)
        title.to_edge(UP, buff=0.32)
        subtitle = Text(
            "建树合并左右区间，查询收集完整覆盖，更新沿一条路径回溯重算",
            font=FONT,
            font_size=16,
            color=MUTED,
        )
        subtitle.next_to(title, DOWN, buff=0.12)

        snippets = [
            (
                "build",
                GREEN,
                [
                    "def build(o, l, r):",
                    "    if l == r:",
                    "        tree[o] = a[l]",
                    "        return",
                    "    m = (l + r) // 2",
                    "    build(o*2, l, m)",
                    "    build(o*2+1, m+1, r)",
                    "    tree[o] = tree[o*2] + tree[o*2+1]",
                ],
            ),
            (
                "query",
                BLUE,
                [
                    "def query(o, l, r, ql, qr):",
                    "    if ql <= l and r <= qr:",
                    "        return tree[o]",
                    "    m, ans = (l + r) // 2, 0",
                    "    if ql <= m:",
                    "        ans += query(o*2, l, m, ql, qr)",
                    "    if qr > m:",
                    "        ans += query(o*2+1, m+1, r, ql, qr)",
                    "    return ans",
                ],
            ),
            (
                "update",
                ORANGE,
                [
                    "def update(o, l, r, i, x):",
                    "    if l == r:",
                    "        tree[o] = x",
                    "        return",
                    "    m = (l + r) // 2",
                    "    if i <= m:",
                    "        update(o*2, l, m, i, x)",
                    "    else:",
                    "        update(o*2+1, m+1, r, i, x)",
                    "    tree[o] = tree[o*2] + tree[o*2+1]",
                ],
            ),
        ]

        code_card = self.make_code_block(*snippets[0])
        code_card.move_to([0, -0.38, 0])

        bridge = VGroup(
            self.make_code_chip("完整覆盖", GREEN),
            Arrow(LEFT * 0.45, RIGHT * 0.45, color=MUTED, stroke_width=2, buff=0),
            self.make_code_chip("return tree[o]", BLUE),
            Arrow(LEFT * 0.45, RIGHT * 0.45, color=MUTED, stroke_width=2, buff=0),
            self.make_code_chip("路径回溯", ORANGE),
        )
        bridge.arrange(RIGHT, buff=0.14)
        bridge.to_edge(DOWN, buff=0.35)

        self.play(FadeIn(title, shift=DOWN * 0.12), FadeIn(subtitle), run_time=0.7)
        self.play(FadeIn(code_card, shift=UP * 0.12), run_time=0.8)
        self.wait(0.8)
        for snippet in snippets[1:]:
            next_card = self.make_code_block(*snippet)
            next_card.move_to(code_card)
            self.play(Transform(code_card, next_card), run_time=0.75)
            self.wait(1.0)
        self.play(FadeIn(bridge, shift=UP * 0.1), run_time=0.55)
        self.wait(1.4)

    def make_code_block(self, title: str, color: str, lines: list[str]) -> VGroup:
        box = RoundedRectangle(
            width=10.8,
            height=4.24,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.2,
            fill_color=PANEL,
            fill_opacity=0.97,
        )
        box.set_z_index(0)

        tab = RoundedRectangle(
            width=1.3,
            height=0.38,
            corner_radius=0.06,
            stroke_color=color,
            stroke_width=1.3,
            fill_color=color,
            fill_opacity=0.16,
        )
        tab.next_to(box.get_top(), DOWN, buff=0.18)
        tab.set_z_index(2)
        name = Text(title, font="Consolas", font_size=16, color=color)
        name.move_to(tab)
        name.set_z_index(3)

        code_lines = VGroup()
        for index, line in enumerate(lines, start=1):
            number = Text(f"{index:02}", font="Consolas", font_size=11, color="#647089")
            indent = (len(line) - len(line.lstrip(" "))) // 4
            text = self.make_highlighted_code_line(line, title, color)
            if text.width > 9.15:
                text.scale_to_fit_width(9.15)
            row = VGroup(number, text)
            row.set_z_index(3)
            row.arrange(RIGHT, buff=0.18, aligned_edge=DOWN)
            if indent:
                text.shift(RIGHT * indent * 0.18)
            code_lines.add(row)

        code_lines.arrange(DOWN, aligned_edge=LEFT, buff=0.09)
        code_lines.next_to(tab, DOWN, buff=0.22)
        code_lines.align_to(box, LEFT).shift(RIGHT * 0.42)
        code_lines.set_z_index(3)

        group = VGroup(box, tab, name, code_lines)
        group.accent_color = color
        return group

    def make_highlighted_code_line(self, line: str, current_name: str, accent: str) -> VGroup:
        token_colors = {
            "def": "#C792EA",
            "if": "#C792EA",
            "else": "#C792EA",
            "return": "#C792EA",
            "tree": "#80CBC4",
            "ans": "#82AAFF",
            "ql": "#F6C85F",
            "qr": "#F6C85F",
        }
        t2c = {
            word: color for word, color in token_colors.items() if word in line
        }
        for name in ("build", "query", "update"):
            if name in line:
                t2c[name] = accent if name == current_name else BLUE
        return Text(
            line,
            font="Consolas",
            font_size=15.2,
            color=INK,
            disable_ligatures=True,
            t2c=t2c,
        )

    def split_code_tokens(self, line: str) -> list[str]:
        tokens: list[str] = []
        index = 0
        multi_ops = ("<=", ">=", "==", "+=", "//")
        while index < len(line):
            char = line[index]
            if char == " ":
                tokens.append(" ")
                index += 1
                continue
            matched = next((op for op in multi_ops if line.startswith(op, index)), None)
            if matched:
                tokens.append(matched)
                index += len(matched)
                continue
            if char.isalpha() or char == "_":
                start = index
                while index < len(line) and (line[index].isalnum() or line[index] == "_"):
                    index += 1
                tokens.append(line[start:index])
                continue
            if char.isdigit():
                start = index
                while index < len(line) and line[index].isdigit():
                    index += 1
                tokens.append(line[start:index])
                continue
            tokens.append(char)
            index += 1
        return tokens

    def make_code_chip(self, text: str, color: str) -> VGroup:
        label = Text(text, font=FONT, font_size=14, color=INK)
        box = RoundedRectangle(
            width=max(1.38, label.width + 0.36),
            height=0.38,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=1.4,
            fill_color=color,
            fill_opacity=0.13,
        )
        label.move_to(box)
        return VGroup(box, label)

    def show_stage(self, text: str):
        stage = Text(text, font=FONT, font_size=20, color=BLUE)
        stage.move_to([0, 2.9, 0])
        self.play(FadeIn(stage, shift=DOWN * 0.1), run_time=0.35)
        self.wait(0.25)
        self.play(FadeOut(stage), run_time=0.35)

    def make_panel(self, title: str, lines: list[str]) -> VGroup:
        box = RoundedRectangle(
            width=2.4,
            height=2.72,
            corner_radius=0.08,
            stroke_color="#3B465C",
            stroke_width=2,
            fill_color=PANEL,
            fill_opacity=0.96,
        )
        box.move_to([5.9, 0.62, 0])
        box.set_z_index(6)
        title_mob = Text(title, font=FONT, font_size=15, color=INK)
        title_mob.set_z_index(8)
        title_mob.next_to(box.get_top(), DOWN, buff=0.18)
        line_mobs = VGroup(*[Text(line, font=FONT, font_size=12, color=MUTED) for line in lines])
        line_mobs.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        line_mobs.next_to(title_mob, DOWN, buff=0.18)
        line_mobs.align_to(box, LEFT).shift(RIGHT * 0.18)
        line_mobs.set_z_index(8)
        return VGroup(box, title_mob, line_mobs)

    def find_node(self, root: TreeNode, left: int, right: int) -> TreeNode:
        if root.left == left and root.right == right:
            return root
        if right <= root.left_child.right:
            return self.find_node(root.left_child, left, right)
        return self.find_node(root.right_child, left, right)

    def reset_tree(self, root: TreeNode):
        nodes = self.collect_nodes(root)
        self.play(
            *[
                node.circle.animate.set_stroke(EDGE, width=2.5, opacity=0.95).set_fill(NODE_FILL, opacity=0.95)
                for node in nodes
            ],
            *[node.label.animate.set_color(INK).set_opacity(1) for node in nodes],
            run_time=0.45,
        )

    def reset_array_cells(self, array_cells):
        self.play(
            *[
                cell["box"].animate.set_fill("#171C27", opacity=1).set_stroke("#3B465C", width=2)
                for cell in array_cells
            ],
            *[cell["index"].animate.set_color(MUTED) for cell in array_cells],
            run_time=0.45,
        )

    def node_color_animation(self, node: TreeNode, color: str, width: float):
        return AnimationGroup(
            node.circle.animate.set_stroke(color, width=width, opacity=1).set_fill(color, opacity=0.2),
            node.label.animate.set_color(INK).set_opacity(1),
        )

    def node_dim_animation(self, node: TreeNode):
        return AnimationGroup(
            node.circle.animate.set_stroke("#3B465C", width=2, opacity=0.45).set_fill("#151923", opacity=0.5),
            node.label.animate.set_color(MUTED).set_opacity(0.45),
        )
