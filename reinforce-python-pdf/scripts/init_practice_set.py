#!/usr/bin/env python3
"""Create an empty, non-destructive Python practice-set directory."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


def feedback_template(question_count: int) -> str:
    sections = [
        "# 做题反馈\n",
        "请在每题后的反馈区自由填写答案、思路、卡点或希望继续巩固的内容；下次出题会据此调整。\n",
    ]
    for number in range(1, question_count + 1):
        sections.append(f"## Q{number}\n\n> 反馈：\n>\n>\n")
    return "\n".join(sections)

ANSWERS_AND_OUTLINE = """# 答案与大纲

## 本次范围与覆盖

> 在此说明学习模块、用户指定专题与覆盖总结。

## 题目速览

| 题号 | 题型 | 难度 | 来源 | 选择原因 | 扩展状态 | 易错点 |
| --- | --- | --- | --- | --- | --- | --- |

## 逐题答案与知识点

> 每题依次写明答案、解释、知识点、学习目标、易错点、来源与选题原因。

## 覆盖与去重说明

> 在此核对专题要求，并记录已参考的历史练习。
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="material workspace (default: .)")
    parser.add_argument(
        "--questions",
        type=int,
        default=5,
        help="total question count used to create feedback blocks (default: 5)",
    )
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    if args.questions < 1:
        parser.error("--questions must be at least 1")
    stamp = datetime.now().strftime("%Y%m%d_%H%M")
    practice_root = root / "practice"
    practice_root.mkdir(exist_ok=True)
    target = practice_root / stamp
    if target.exists():
        parser.error(f"practice-set directory already exists: {target}")
    target.mkdir()

    files = {
        "题目.md": "# Python 巩固练习\n\n> 题目将在此处生成。\n",
        "答案与大纲.md": ANSWERS_AND_OUTLINE,
        "feedback.md": feedback_template(args.questions),
    }
    for filename, content in files.items():
        (target / filename).write_text(content, encoding="utf-8")
    print(target)


if __name__ == "__main__":
    main()
