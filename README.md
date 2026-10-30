# 敲码 qiaoma

在终端里**手敲代码**学 Python——rustlings / pythonlings 风格的中文练习工具传统手艺不要丢。

修复一道道「坏掉的小程序」，删掉未完成标记，隐藏检查自动重跑；通过即进入下一题。全程不离开终端，适合零基础入门到面试冲刺。

```
┌ 敲码 qiaoma ────────────────────────────────────────────────┐
│ 初级 · 变量与类型   variables01 食堂饭卡找零   课题 0/10      │
│ ┌──────────────────────────────────────────────────────┐    │
│ │ # 我还没做完                                          │    │
│ │ card_money = 50                                      │    │
│ │ noodle_price = 12.5                                  │    │
│ │ balance = card_money + noodle_price  # 咦，变多了？   │    │
│ └──────────────────────────────────────────────────────┘    │
│ ✔ 全部检查通过！                                             │
│ F1 提示  F2 重置  F3 题目  F4 课题  Ctrl+S 检查  Esc 退出    │
└─────────────────────────────────────────────────────────────┘
```

## 特色

- **280 道手敲题**：28 个课题 × 10 题，场景全部中国化（饭卡找零、个税阶梯、12306 限流、双十一优惠、红包算法……）
- **四条学习轨道**：初级 12 课题 → 中级 8 课题 → 算法手撕 5 课题 → 面试题 3 课题
- **终端内置编辑器**：边敲边判，停顿 2 秒或 Ctrl+S 自动重跑隐藏检查
- **渐进提示**：每题 2 条提示，F1 开关
- **进度持久化**：随时退出、随时续做；`qiaoma list` 查看各课题进度
- **顺序解锁**：课题之间自由选，课题内做完一题才解锁下一题。未解锁的题目显示为
  `🔒 题号 ???`，标题隐藏；`hint` / `run` / `reset` 同样拒绝执行

## 安装

需要 Python 3.10+。把仓库克隆到本地后，在仓库根目录执行。

**uv（推荐）**

需要先装 uv：https://docs.astral.sh/uv/

uv 能自己下载并管理 Python 版本，不用自己找安装包：

```bash
uv python list                  # 看本机有哪些 Python 版本
uv python install 3.12          # 装一个 3.10+ 的版本（不写版本号就取最新稳定版）

uv venv --python 3.12           # 用它建虚拟环境
uv pip install -e .
```

想让整个项目固定用某个版本，执行 `uv python pin 3.12`，它会在项目里写一个 `.python-version` 文件。

**pip + venv**

```bash
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

pip install -e .
```

要跑测试就换成开发依赖：`pip install -e ".[dev]"`（uv 用户 `uv pip install -e ".[dev]"`）。

## 快速开始

命令要在同一个虚拟环境里执行。uv 用户也可以不加激活，直接用 `uv run`：

```bash
qiaoma init --path ~/qiaoma-workspace   # 创建学习工作区（题目副本）
cd ~/qiaoma-workspace
qiaoma                                  # 打开做题界面

# uv 用户等价写法
uv run qiaoma init --path ~/qiaoma-workspace
```

## 命令一览

| 命令 | 说明 |
| --- | --- |
| `qiaoma` | 打开做题界面（从第一道未完成的题开始） |
| `qiaoma init --path <目录>` | 创建学习工作区 |
| `qiaoma topics` | 直接打开课题选择器 |
| `qiaoma list` | 查看各课题进度 |
| `qiaoma hint variables01` | 打印某题的提示 |
| `qiaoma run variables01` | 在命令行跑一次某题的检查 |
| `qiaoma reset variables01 --yes` | 把某题重置为原始内容 |

未解锁的题目，`hint` / `run` / `reset` 会被拒（输出提示哪道题挡路，退出码 1）。

## 做题界面快捷键

| 按键 | 动作 |
| --- | --- |
| F1 | 显示/隐藏提示 |
| F2 | 重置当前题目 |
| F3 | 题目列表（可跳转已解锁的题，未解锁显示 `🔒 题号 ???`） |
| F4 | 课题选择器（选定课题后先看该课题的题目列表与一句介绍） |
| Ctrl+S | 保存并立即检查 |
| Esc / Ctrl+Q | 退出 |

## 做题流程

1. 每道题是一段**有 bug 的中文场景代码**，顶部有 `# 我还没做完` 标记；
2. 在终端编辑器里修复代码；
3. 删除 `# 我还没做完` 那一行；
4. 检查自动重跑——通过后自动进入下一题。

## 课程地图

| 轨道 | 课题 |
| --- | --- |
| 初级（120 题） | 变量与类型 · 字符串 · 条件判断 · 循环 · 列表 · 字典与集合 · 函数 · 切片与推导式 · 异常处理 · 文件读写 · 模块与包 · 面向对象入门 |
| 中级（80 题） | 面向对象进阶 · 迭代器与生成器 · 装饰器 · 闭包与函数式 · 上下文管理器 · 类型注解与dataclass · 线程与进程 · async 异步编程 |
| 算法（50 题） | 数组与字符串双指针 · 栈队列哈希表 · 链表与二叉树 · 排序与二分 · 递归回溯与入门DP |
| 面试（30 题） | Python 核心面试题 · 大厂高频手撕题 · 场景设计题 |

## 项目结构

```
qiaoma/
├── core/                 # 清单、进度、判题运行器、重置、工作区
├── screens/ widgets/     # Textual TUI 界面
├── curriculum/           # 打包课程
│   ├── info.toml         # 课题顺序与提示
│   ├── exercises/<课题>/ # 题目文件（学员编辑）
│   └── checks/<课题>/    # 隐藏检查（与题目镜像）
tests/
├── solutions/<课题>/     # 280 份参考解答（保证每题可解）
└── ...                   # 核心模块单元测试 + TUI 冒烟测试
docs/design/               # 设计说明（顺序解锁、课题导航）
```

## 参与开发

```bash
pip install -e ".[dev]"
python -m pytest -q        # 全量测试（含 280 题参考解答可解性验证）
```

用 uv 的话：`uv pip install -e ".[dev]"`，然后 `uv run pytest -q`。

添加新课题：在 `qiaoma/curriculum/` 的 `exercises/`、`checks/` 增加镜像文件，
在 `info.toml` 登记课题与题目，并在 `tests/solutions/` 补上参考解答。

## 致谢

灵感来自 [rustlings](https://github.com/rust-lang/rustlings) 与
[pythonlings](https://github.com/abhiksark/pythonlings)，界面基于
[Textual](https://textual.textualize.io/)。

## 许可证

MIT，见 [LICENSE](LICENSE)。
