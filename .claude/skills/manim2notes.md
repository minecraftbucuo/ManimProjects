---
name: manim2notes
description: 将数学文件夹中的 Manim 动画脚本提炼为彩色 LaTeX 讲义 PDF，输出到 docs 目录，文件名与源 py 文件一致。
argument-hint: <python_file_name>
scope: project
---

# Manim 数学动画 → PDF 讲义

将 `数学/` 目录下的 Manim 动画脚本（.py）自动提炼为彩色数学讲义 PDF，放在 `docs/` 目录。

## 执行步骤

### 1. 读取源文件

读取 `数学/<name>.py`，理解其中演示的数学问题和推导过程。

识别要素：
- **问题陈述**：题目是什么（通常在封面或开场文字中）
- **解法步骤**：每个 `Scene` / 方法章节的推导逻辑
- **关键公式**：`MathTex` 中的 LaTeX 公式
- **最终答案**：结论是什么

### 2. 按模板生成 LaTeX

严格遵循 `docs/HOWTO_math_lecture_notes.md` 的模板风格：

- 使用相同的 `\documentclass{ctexart}` + 颜色定义 + 页面设置
- 使用相同的自定义环境：`problembox`、`methodbox`、`summarybox`
- 彩色顶栏标题 → 主标题用问题概括，副标题写具体表达式
- 根据源脚本判断结构：确实存在多种独立方法时，才用 `\section{解法X：方法名}` 分节；如果只是同一条推导链的连续环节，使用知识点/推导环节作章节标题，例如 `\section{约数个数定理}`、`\section{分解目标值}`、`\section{最小值分析}`
- 避免标题层级套娃：不要出现 `步骤一` 下面再写 `第一步`、`第二步`；主章节写“讲什么”，小标题写具体动作或内容，例如 `标准素因数分解`、`正因数个数公式`、`目标值分解`、`对应的素因子结构`、`两种结构比较`
- 核心思路用 `methodbox` 框起来，标题写「核心思路」
- 关键概念用 `\highlight{}` 高亮
- 最终答案放在总结页的彩色答案框中

### 3. 文件命名

输出文件放在 `docs/` 目录，**纯文件名与源 py 文件保持一致**：

| 输入 | 输出 |
|:---|:---|
| `数学/20260620.py` | `docs/20260620.tex` → `docs/20260620.pdf` |

### 4. 编译 PDF



```bash
cd "<project_root>/docs"
xelatex -interaction=nonstopmode <name>.tex
xelatex -interaction=nonstopmode <name>.tex
xelatex -interaction=nonstopmode <name>.tex
```

### 5. 清理

```bash
cd "<project_root>/docs"
rm -f <name>.aux <name>.log <name>.out <name>.toc
```

### 6. 确认

用 `ls -lh docs/<name>.pdf docs/<name>.tex` 确认两个文件都存在，并报告给用户。

## 关键规则

- **永远不要自己编造数学内容**——所有公式和推导必须来自 py 文件中 `MathTex` 的内容
- **先判断推导结构**：多种独立方法才写「解法一、解法二」；单一推导链必须写成知识点/推导环节，禁止硬拆成多个「解法」
- **标题层级必须自然**：章节标题不要写「步骤一、步骤二」后又在小节写「第一步、第二步」；章节写主题，小节写具体内容，避免重复套娃
- **文件名必须一致**：py 叫什么，tex/pdf 就叫什么
- **风格必须匹配 HOWTO**：相同的 `\definecolor`、相同的 `tcolorbox` 环境、相同的章节样式
- **中文必须留在文本模式**：`$...$` 里只能放英文、数字、数学符号
- **禁止 emoji**：用 `$\blacktriangleright$` 等数学符号代替
- **不要手动设置中文字体**：`ctexart` 会自动处理，只设 `\setmainfont{TeX Gyre Pagella}` 即可
