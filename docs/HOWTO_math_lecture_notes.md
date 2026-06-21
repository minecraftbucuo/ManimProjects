# 彩色数学讲义 PDF 制作指南

这份指南教你用 LaTeX 把数学内容（题目、证明、总结）排版成带颜色的讲义风格 PDF。直接复制模板、填入内容、跑命令即可。

---

## 一、前提：装好 TeX Live

验证：

```bash
xelatex --version
```

能打印版本号就说明装好了。

> **为什么用 xelatex 而不是 pdflatex？** pdflatex 处理中文很麻烦（要配 CJK 包），xelatex 原生支持 UTF-8 和系统字体，中文开箱即用。

---

## 二、通用模板

把下面内容保存为 `lecture.tex`，这是完整可编译的骨架。你只需要改三处：**标题、副标题、正文内容**。

```latex
% !TEX program = xelatex
\documentclass[11pt,a4paper]{ctexart}

% ==================== 颜色 ====================
\usepackage{xcolor}
\definecolor{maincolor}{HTML}{1A7A6B}       % 主色（标题、顶栏、框边框）
\definecolor{accent}{HTML}{D4A843}          % 强调色（关键词高亮）
\definecolor{boxbg}{HTML}{F0F7F5}           % 问题框背景
\definecolor{borderblue}{HTML}{2E86AB}      % 方法框边框
\definecolor{proofbg}{HTML}{FDF8F0}         % 方法框背景
\definecolor{summarybg}{HTML}{F5F0FF}       % 总结框背景

% ==================== 页面 ====================
\usepackage[top=2.2cm, bottom=2.2cm, left=2.5cm, right=2.5cm, headheight=23.12pt]{geometry}

% ==================== 字体 ====================
% 只设西文主字体；中文由 ctex 自动处理（Windows→宋体/黑体，macOS→苹方，Linux→Fandol）
\setmainfont{TeX Gyre Pagella}

% ==================== 数学 ====================
\usepackage{amsmath,amssymb,amsfonts,mathtools}

% ==================== 彩色框 ====================
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable,most}

% ==================== 页眉页脚 ====================
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\color{maincolor}\sffamily\bfseries 数学讲义}
\fancyhead[R]{\color{gray}\sffamily \today}
\fancyfoot[C]{\color{gray}\sffamily\thepage}
\renewcommand{\headrulewidth}{1.5pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{maincolor}\leaders\hrule height \headrulewidth\hfill}}

% ==================== 章节标题样式 ====================
\usepackage{titlesec}
\titleformat{\section}
  {\color{maincolor}\sffamily\LARGE\bfseries}
  {\thesection}{1em}{}
  [\vspace{0.3cm}{\color{maincolor!40}\titlerule[2pt]}]

\titleformat{\subsection}
  {\color{maincolor!80}\sffamily\Large\bfseries}
  {\thesubsection}{1em}{}

% ==================== 表格 ====================
\usepackage{array,booktabs,colortbl}

% ==================== 杂项 ====================
\usepackage{enumitem}
\setlist{nosep, leftmargin=*}
\usepackage[hidelinks]{hyperref}

% ==================== 自定义命令 ====================
\newcommand{\highlight}[1]{\colorbox{accent!20}{\sffamily\bfseries #1}}

% ==================== 自定义环境 ====================

% 1. 问题框 —— 青绿边框 + 浅绿背景
\newtcolorbox[auto counter]{problembox}[1][]{
  enhanced,
  colframe=maincolor,
  colback=boxbg,
  coltitle=white,
  fonttitle=\sffamily\bfseries,
  title={\large 问题},
  attach boxed title to top left={xshift=4mm, yshift=-2mm},
  boxed title style={colback=maincolor, sharp corners},
  sharp corners,
  boxrule=1.2pt,
  left=4mm, right=4mm, top=5mm, bottom=4mm,
  before skip=1.2em, after skip=1.2em,
  #1
}

% 2. 方法/证明框 —— 蓝边框 + 暖白背景，第二个参数是标题文字
\newtcolorbox[auto counter]{methodbox}[2][]{
  enhanced,
  colframe=borderblue,
  colback=proofbg,
  coltitle=white,
  fonttitle=\sffamily\bfseries,
  title={#2},
  attach boxed title to top left={xshift=4mm, yshift=-2mm},
  boxed title style={colback=borderblue, sharp corners},
  sharp corners,
  boxrule=1.2pt,
  left=4mm, right=4mm, top=5mm, bottom=4mm,
  before skip=1.2em, after skip=1.2em,
  #1
}

% 3. 总结框 —— 淡紫背景
\newtcolorbox{summarybox}[1][]{
  enhanced,
  colframe=maincolor!60,
  colback=summarybg,
  coltitle=white,
  fonttitle=\sffamily\bfseries,
  title={\large $\blacktriangleright$ 总结},
  attach boxed title to top left={xshift=4mm, yshift=-2mm},
  boxed title style={colback=maincolor!70, sharp corners},
  sharp corners,
  boxrule=1.2pt,
  left=4mm, right=4mm, top=5mm, bottom=4mm,
  before skip=1.5em, after skip=1.2em,
  #1
}

% ==================== 文档开始 ====================
\begin{document}

% ---- 彩色顶栏标题 ----
\begin{tcolorbox}[
  enhanced,
  colframe=maincolor,
  colback=maincolor,
  sharp corners,
  boxrule=0pt,
  height=2.8cm,
  valign=center,
  before skip=-2.2cm,
  after skip=1.5cm,
  grow to left by=2.5cm,
  grow to right by=2.5cm,
]
  \begin{center}
    {\color{white}\sffamily\bfseries\Huge 你的主标题}\\[3pt]
    {\color{white!85}\sffamily\large 你的副标题}
  \end{center}
\end{tcolorbox}

\vspace{0.5cm}

\begin{flushright}
  {\color{gray}\sffamily \today}
\end{flushright}

% ==================== 正文从这里开始 ====================

\section{问题陈述}

\begin{problembox}
在这里描述你的问题。支持行内公式 $E = mc^2$ 和独立公式：
\[
  a^2 + b^2 = c^2
\]
\end{problembox}

\section{解法一：方法名称}

\begin{methodbox}{核心思路}
用一两句话概括这个方法的核心思想。可以用 \highlight{关键词} 高亮重要概念。
\end{methodbox}

\subsection*{第一步：某步骤}

推导过程写在这里。

\subsection*{第二步：某步骤}

更多公式：
\[
  \boxed{x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}}
\]

% ==================== 新页 ====================
\newpage

\section{总结}

\begin{summarybox}

\subsection*{方法对比}

\begin{tabular}{@{}>{\sffamily\bfseries}p{2.8cm} p{5.5cm} p{5.5cm}@{}}
\toprule
& \color{maincolor} \textbf{方法一} & \color{borderblue} \textbf{方法二} \\
\midrule
\textbf{切入点}   & ... & ... \\
\textbf{核心工具} & ... & ... \\
\bottomrule
\end{tabular}

\subsection*{结论}

最终答案：
\begin{center}
\begin{tcolorbox}[
  enhanced, colframe=accent!80, colback=accent!10,
  sharp corners, boxrule=1.5pt, width=6cm, center,
]
  {\color{maincolor}\sffamily\bfseries\LARGE 答案}
\end{tcolorbox}
\end{center}

\end{summarybox}

\end{document}
```

---

## 三、数学内容常用写法

| 需求 | 写法 | 说明 |
|:---|:---|:---|
| 行内公式 | `$E = mc^2$` | 嵌在段落中 |
| 独立公式 | `\[ a^2 + b^2 = c^2 \]` | 居中独占一行 |
| 多行对齐 | `\begin{align*} x &= 1 \\ y &= 2 \end{align*}` | 按 `&` 位置对齐 |
| 方程组 | `\begin{cases} x = 1 \\ y = 2 \end{cases}` | 左边大括号 |
| 加框公式 | `\boxed{n = 4}` | 结论加框强调 |
| 高亮文字 | `\highlight{质数}` | 金色背景标注关键词 |
| 矩阵 | `\begin{pmatrix} a & b \\ c & d \end{pmatrix}` | 圆括号矩阵 |
| 分段函数 | `\begin{cases} ... \end{cases}` | 左花括号 |
| 换页 | `\newpage` | 强制分页 |

---

## 四、编译命令

假设源文件叫 `lecture.tex`：

```bash
# 第一遍
xelatex -interaction=nonstopmode lecture.tex

# 第二遍（解析交叉引用和自动编号）
xelatex -interaction=nonstopmode lecture.tex

# 第三遍（确保稳定）
xelatex -interaction=nonstopmode lecture.tex

# 删除临时文件
rm -f lecture.aux lecture.log lecture.out lecture.toc
```

`-interaction=nonstopmode` 的意思是遇到非致命错误不暂停，适合批处理。如果你在调试模板本身，去掉它可以看到完整报错信息。

**为什么要跑三遍？**

- 第一遍：生成 PDF 骨架，同时把章节编号、框体编号写入 `.aux` 辅助文件
- 第二遍：读 `.aux`，把编号填回正文（所以交叉引用在第二遍才正确）
- 第三遍：确保所有引用收敛不再变化

短文档两遍可能就够了，三遍是保险做法。

---

## 五、踩过的坑（及解决方案）

### 坑 1：中文在数学模式里变成空白

**现象**：编译日志出现 `Missing character: There is no 数 (U+6570) in font TeXGyrePagella`，PDF 里中文消失。

**原因**：把中文塞进了 `$...$` 数学模式。数学模式默认用拉丁字体，没有中文字形。

**错误**：
```latex
\newcommand{\highlight}[1]{\colorbox{accent!20}{$\displaystyle #1$}}
% \highlight{质数} → "质数" 进入数学模式 → 拉丁字体无此字形 → 丢失
```

**正确**：
```latex
\newcommand{\highlight}[1]{\colorbox{accent!20}{\sffamily\bfseries #1}}
% "质数" 留在文本模式，由黑体渲染
```

> **记住**：`$...$`、`$$...$$`、`\[...\]` 里只能放英文、数字、数学符号。中文、日文、韩文一律放在外面。

### 坑 2：emoji 导致编译直接崩溃

**现象**：`xdvipdfmx:fatal: Invalid font: -1 (2)`，不输出 PDF。

**原因**：LaTeX 的标准字体里没有 emoji（📝🎯✅ 等），xdvipdfmx 在嵌入字体阶段崩溃。

**解决**：用 LaTeX 数学符号替代。例如 `$\blacktriangleright$`、`$\bullet$`、`$\checkmark$`。

### 坑 3：手动设置中文字体反而出问题

**现象**：写了 `\setCJKmainfont{某某字体}` 之后编译不稳定或字体异常。

**原因**：`ctexart` 文档类在启动时已经自动检测操作系统并配好了中文字体。手动覆盖会打断这个自动配置。

**正确做法**：**永远不写 `\setCJKmainfont`、`\setCJKsansfont`、`\setCJKmonofont`**。只设西文主字体，中文完全交给 ctex：

```latex
\setmainfont{TeX Gyre Pagella}   % 只设这个
% 下面这些都不要写：
% \setCJKmainfont{...}
% \setCJKsansfont{...}
% \setCJKmonofont{...}
```

ctex 在各平台的默认字体：

| 平台 | 衬线（正文） | 无衬线（标题） |
|:---|:---|:---|
| Windows | SimSun（宋体） | SimHei（黑体） |
| macOS | Songti SC | Heiti SC |
| Linux | FandolSong | FandolHei |

### 坑 4：fancyhdr 页眉高度警告

**现象**：`Package fancyhdr Warning: \headheight is too small (12.0pt)`

**解决**：在 `\usepackage{geometry}` 时加上 `headheight=23.12pt`：

```latex
\usepackage[..., headheight=23.12pt]{geometry}
```

---

## 六、换配色

所有颜色集中在模板顶部的 `\definecolor`，改 HTML 色值即可全局生效：

```latex
\definecolor{maincolor}{HTML}{1A7A6B}       % 改这里 → 所有标题/边框/顶栏变色
\definecolor{accent}{HTML}{D4A843}          % 改这里 → 所有关键词高亮变色
\definecolor{boxbg}{HTML}{F0F7F5}           % 改这里 → 所有问题框背景变色
\definecolor{borderblue}{HTML}{2E86AB}      % 改这里 → 所有方法框边框变色
\definecolor{proofbg}{HTML}{FDF8F0}         % 改这里 → 所有方法框背景变色
\definecolor{summarybg}{HTML}{F5F0FF}       % 改这里 → 所有总结框背景变色
```

当前预设的是一套"青绿 + 金色"配色，你可以换成任意色系——比如蓝灰学术风、红棕古典风、紫金豪华风，只改这 6 个值就行。

---

## 七、操作总结

整个流程就三步：

```
1. 复制模板 → 保存为 lecture.tex
2. 填入标题、正文、公式
3. 终端跑 xelatex lecture.tex（跑三遍）
```

输出的 `lecture.pdf` 就是带彩色顶栏、框体、高亮关键词的数学讲义。
