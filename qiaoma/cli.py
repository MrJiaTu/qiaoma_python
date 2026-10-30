"""命令行入口。

用法::

    qiaoma                     # 打开做题界面
    qiaoma init --path <dir>   # 创建学习工作区
    qiaoma topics              # 打开课题选择器
    qiaoma list                # 查看各课题进度
    qiaoma hint variables01    # 打印某题提示
    qiaoma run variables01     # 运行某题检查
    qiaoma reset variables01 --yes   # 重置某题
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.text import Text

from .core.manifest import load_manifest
from .core.reset import reset_exercise
from .core.runner import run_check
from .core.state import State
from .core.workspace import find_workspace, init_workspace

console = Console()


def _require_workspace(explicit: str | None) -> Path:
    workspace = find_workspace(Path(explicit) if explicit else None)
    if workspace is None:
        console.print(
            "[red]还没有敲码工作区。[/red]请先运行：\n"
            "    qiaoma init --path ~/qiaoma-workspace"
        )
        raise SystemExit(1)
    return workspace


def _cmd_init(args: argparse.Namespace) -> None:
    path = Path(args.path).expanduser()
    init_workspace(path)
    console.print(f"[green]工作区已就绪：[/green]{path}")
    console.print(f"接下来运行：\n    cd {path}\n    qiaoma")


def _cmd_list(args: argparse.Namespace) -> None:
    workspace = _require_workspace(args.workspace)
    manifest = load_manifest(workspace)
    state = State.load(workspace)
    table = Table(title="敲码 · 学习进度")
    table.add_column("轨道")
    table.add_column("课题")
    table.add_column("进度")
    table.add_column("状态")
    for topic in manifest.topics:
        done, total = state.topic_progress(manifest, topic.id)
        status = "[green]已完成[/green]" if done == total else "进行中" if done else "未开始"
        table.add_row(topic.track, topic.name, f"{done}/{total}", status)
    done_all = sum(1 for e in manifest.exercises if state.is_done(e.id))
    console.print(table)
    console.print(f"总进度：{done_all}/{len(manifest.exercises)}")


def _cmd_hint(args: argparse.Namespace) -> None:
    """打印某题的提示；未解锁的题不给任何提示内容。"""
    workspace = _require_workspace(args.workspace)
    manifest = load_manifest(workspace)
    try:
        exercise = manifest.exercise(args.exercise)
    except KeyError as error:
        console.print(f"[red]{error}[/red]")
        raise SystemExit(1)
    state = State.load(workspace)
    message = state.lock_message(manifest, exercise)
    if message is not None:
        console.print(f"[red]{message}[/red]")
        raise SystemExit(1)
    console.print(f"[bold]{exercise.id} {exercise.title}[/bold]")
    if not exercise.hints:
        console.print("这道题没有提示。")
    for i, hint in enumerate(exercise.hints, 1):
        line = Text()
        line.append(f"提示 {i}: ", style="dim")
        line.append(hint)
        console.print(line)


def _cmd_run(args: argparse.Namespace) -> None:
    workspace = _require_workspace(args.workspace)
    manifest = load_manifest(workspace)
    try:
        exercise = manifest.exercise(args.exercise)
    except KeyError as error:
        console.print(f"[red]{error}[/red]")
        raise SystemExit(1)
    state = State.load(workspace)
    message = state.lock_message(manifest, exercise)
    if message is not None:
        console.print(f"[red]{message}[/red]")
        raise SystemExit(1)
    result = run_check(workspace, exercise)
    styles = {"passed": "green", "failed": "red", "blocked": "yellow"}
    # 判题消息含学员代码输出，按纯文本渲染
    console.print(Text(result.message, style=styles[result.status]))
    raise SystemExit(0 if result.passed else 1)


def _cmd_reset(args: argparse.Namespace) -> None:
    workspace = _require_workspace(args.workspace)
    manifest = load_manifest(workspace)
    try:
        exercise = manifest.exercise(args.exercise)
    except KeyError as error:
        console.print(f"[red]{error}[/red]")
        raise SystemExit(1)
    state = State.load(workspace)
    message = state.lock_message(manifest, exercise)
    if message is not None:
        console.print(f"[red]{message}[/red]")
        raise SystemExit(1)
    if not args.yes:
        answer = input(f"确定重置 {exercise.id}（当前修改会丢失）？[y/N] ")
        if answer.strip().lower() not in ("y", "yes"):
            console.print("已取消。")
            return
    reset_exercise(workspace, exercise)
    console.print(f"[green]已重置：[/green]{exercise.id}")


def _cmd_tui(args: argparse.Namespace, picker: bool) -> None:
    workspace = _require_workspace(args.workspace)
    from .app import QiaomaApp

    QiaomaApp(workspace, start_with_picker=picker).run()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="qiaoma",
        description="敲码：在终端里手敲 Python 代码学习",
    )
    parser.add_argument(
        "--workspace", "-w", default=None, help="指定工作区目录（默认自动探测）"
    )
    sub = parser.add_subparsers(dest="command")

    p_init = sub.add_parser("init", help="创建学习工作区")
    p_init.add_argument("--path", required=True, help="工作区目录，例如 ~/qiaoma-workspace")
    p_init.set_defaults(func=_cmd_init)

    p_topics = sub.add_parser("topics", help="打开课题选择器")
    p_topics.set_defaults(func=lambda a: _cmd_tui(a, picker=True))

    p_list = sub.add_parser("list", help="查看学习进度")
    p_list.set_defaults(func=_cmd_list)

    p_hint = sub.add_parser("hint", help="打印某题的提示")
    p_hint.add_argument("exercise", help="题目编号，例如 variables01")
    p_hint.set_defaults(func=_cmd_hint)

    p_run = sub.add_parser("run", help="运行某题的检查")
    p_run.add_argument("exercise", help="题目编号，例如 variables01")
    p_run.set_defaults(func=_cmd_run)

    p_reset = sub.add_parser("reset", help="重置某题为原始内容")
    p_reset.add_argument("exercise", help="题目编号，例如 variables01")
    p_reset.add_argument("--yes", action="store_true", help="跳过确认")
    p_reset.set_defaults(func=_cmd_reset)

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        _cmd_tui(args, picker=False)
        return
    args.func(args)


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
