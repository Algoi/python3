---
name: reinforce-python-pdf
description: Create continuing Python practice sets from Markdown study notes and PDF learning materials in the current workspace. Use when the user asks to make Python review questions, exercises, quizzes, answer keys, or follow-up reinforcement based on local notes or PDFs, especially when every set must retain an outline, feedback file, source coverage, and avoid duplicating earlier questions.
---

# Python PDF practice sets

Create one self-contained practice-set directory per request. Use Markdown study notes stored in the selected learning module as the primary baseline; use that module's PDFs to verify notes or cover topics absent from the notes. Add a concise, explicitly labelled extension only when it materially helps: a needed prerequisite, a useful contrast, a likely misconception, or feedback-driven reinforcement. Do not add extensions merely to increase novelty or difficulty.

## Honor requested focus

Treat explicit constraints in the current request as the highest-priority scope: named concepts, module, difficulty, quantity, or question form. Before selecting questions for any request—including a bare `请出题` or a scoped request—always read every existing `答案与大纲.md` and `feedback.md` under `practice/`. For legacy practice sets, read the separate `答案.md` and `题目大纲.md` instead. For example, `全部都是列表的` means every question must test Python list concepts; keep the required question types and make the programming question list-focused as well. Use related prerequisites or extensions only when necessary to understand that focus, and label them. If a requested term has more than one plausible meaning in the current notes, ask a brief clarifying question; otherwise proceed and record the interpreted focus in the outline.

## Inspect context first

1. List leading-numbered module directories such as `01_python编程基础`. Follow a module named by the user; otherwise use the lowest-numbered available module (currently `01`) and state that scope in the outline. Do not automatically mix a higher-numbered module.
2. Read Markdown study notes recursively inside the selected module only. Treat them as the current, primary syllabus; record the relative note filename and heading for each candidate topic. Exclude generic workspace documentation such as root `readme.md` and everything under `practice/**`.
3. List PDFs in the selected module. Preserve their relative path in sources. Consult their text only to verify a note, resolve an ambiguity, find a topic the module's notes do not cover, or draw from a suitable PDF exercise. Record PDF file and page whenever used.
4. Find prior practice-set directories under `practice/`. A new-format set contains `题目.md`, `答案与大纲.md`, and `feedback.md`; also recognize legacy sets containing separate `答案.md` and `题目大纲.md`.
5. Before writing any new question, always read every prior `答案与大纲.md` and `feedback.md`, whether or not the user specified a topic; for legacy sets read `答案.md` and `题目大纲.md` too. Also read `题目.md` to prevent near-duplicates. Build a compact internal inventory of concepts, question forms, examples, difficulty, mistakes, and requested focus. Do not repeat an existing question or only rename its variables; vary both scenario and reasoning target.
6. Treat feedback as learner-specific evidence: re-test incorrect, uncertain, skipped, or requested concepts with a new angle; do not re-test concepts marked mastered unless useful as a brief prerequisite. If feedback is empty, state that it is a blank template and balance coverage from the module notes, then PDFs.

## Create the set

Determine the total question count first, then run `scripts/init_practice_set.py --root . --questions <总题数>` from the material workspace. It creates `practice/YYYYMMDD_HHMM` beneath the current directory (for example, `practice/20260713_1349`) and the three required files. Never overwrite an existing set; if the same-minute directory already exists, stop and report the collision rather than changing the naming format.

Fill all three files in UTF-8 Markdown:

- `题目.md`: title, brief instructions, difficulty labels, numbered questions, and source notes: use `来源：相对模块路径/笔记文件，标题` for notes, `来源：相对模块路径/文件名，第 N 页` for PDFs, and `扩展：知识点（扩展原因）` for extensions. Keep answers out of this file.
- `答案与大纲.md`: organize in this order: (1) `本次范围与覆盖` with selected module(s), requested focus, and coverage summary; (2) `题目速览` table with ID, type, difficulty, source, selection reason, extension status, and `易错点`; (3) `逐题答案与知识点`, with a subsection per question containing answer, concise explanation, runnable code or scoring points when appropriate, exact knowledge points, learning objective, common error/trap, source, and selection reason; (4) `覆盖与去重说明`, including the focus-compliance check and prior sets reviewed. Explain why plausible wrong answers fail for every deliberate mistake-prone question.
- `feedback.md`: keep every question's feedback in this one file. Include exactly one free-text feedback block for each actual question (`Q1` through the final question), with no mandatory sub-fields and no separate file per question. Do not alter a completed feedback file. Interpret its natural-language content when planning the next set.

Use this feedback block for every question:

```markdown
# 做题反馈

请在每题后的反馈区自由填写答案、思路、卡点或希望继续巩固的内容；下次出题会据此调整。

## Q1

> 反馈：
>
>
```

## Question-quality rules

- Include 3–5 non-programming questions plus exactly one `简单编程题` by default. The non-programming questions must include at least one `选择题`, one `填空题`, and one `判断题`; label each type in `题目.md`. If the user asks for another count, retain these four required types unless they explicitly override the structure.
- Make the programming question a focused, small exercise that directly demonstrates the concept being reinforced. Do not require an actual application, project design, or realistic business scenario.
- Prioritize high-frequency development knowledge: everyday data handling, control flow, functions, common string and collection operations, object use, reading code, and debugging common mistakes. Do not choose obscure syntax, trivia, or rare corner cases merely because they appear in the materials.
- Include a low-frequency point only when it is necessary to understand, safely use, or avoid a serious misconception about a high-frequency concept. Mark it in the outline as `必要理解点` and state that dependency; otherwise omit it.
- Prefer the vocabulary, syntax, and examples in the Markdown notes; use PDFs as the fallback and verification source. Do not rely on unintroduced libraries, advanced syntax, version-specific behavior, or trivia.
- Reuse a PDF's original exercise when it fits the current notes and feedback, but improve or combine it when necessary to make it meaningfully diagnostic; preserve its source reference.
- Cover multiple concepts deliberately, but keep each question focused. Mark prerequisite relationships in the outline rather than making a question depend on an unanswered earlier question.
- Identify every extension as `扩展` in both question and outline. State its added premise and why it is needed in the answer; keep it close to the current learning stage, even when it goes beyond the PDFs.
- Include one or two fair, mistake-prone checks when the covered topics permit—for example, boundary conditions, assignment versus comparison, mutation versus rebinding, or truthiness. Test understanding, not wording tricks: make the premise unambiguous and explain the misconception in the answer and outline.
- Verify every code answer by running it with the available `python3` when executable. Mention any version-sensitive behavior.
- Before finishing, check numbering, file existence, source references, answer completeness, feedback template, and absence of answers in `题目.md`.
