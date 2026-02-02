#!/usr/bin/env python3
"""
ADR 및 아이디어 요약 자동 생성 스크립트

사용법:
    python scripts/generate_summary.py

기능:
    1. decisions/ 폴더의 ADR 파일 파싱
    2. ideas/ 폴더의 아이디어 파일 파싱
    3. 각 README.md의 목록 자동 업데이트
    4. CHANGELOG.md 생성
    5. 관계 그래프 생성 (RELATIONS.md)
"""

import os
import re
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Document:
    """문서 메타데이터"""
    number: str
    title: str
    status: str
    date: str
    filename: str
    related: list[str]
    supersedes: Optional[str] = None
    doc_type: str = "adr"  # adr 또는 idea


def parse_adr(filepath: Path) -> Optional[Document]:
    """ADR 파일 파싱"""
    content = filepath.read_text(encoding="utf-8")

    # 제목 추출 (# ADR-NNNN: 제목)
    title_match = re.search(r"^# ADR-(\d+): (.+)$", content, re.MULTILINE)
    if not title_match:
        return None

    number = title_match.group(1)
    title = title_match.group(2).strip()

    # 상태 추출
    status_match = re.search(r"\*\*상태\*\*:\s*(.+?)(?:\n|$)", content)
    status = status_match.group(1).strip() if status_match else "알 수 없음"

    # 날짜 추출
    date_match = re.search(r"\*\*날짜\*\*:\s*(\d{4}-\d{2}-\d{2})", content)
    date = date_match.group(1) if date_match else "알 수 없음"

    # 관련 ADR 추출
    related_match = re.search(r"\*\*관련 ADR\*\*:\s*(.+?)(?:\n|$)", content)
    related = []
    if related_match and related_match.group(1).strip() != "-":
        related = re.findall(r"ADR-(\d+)", related_match.group(1))

    # 대체된 ADR 추출
    supersedes_match = re.search(r"\*\*대체된 ADR\*\*:\s*\[ADR-(\d+)\]", content)
    supersedes = supersedes_match.group(1) if supersedes_match else None

    return Document(
        number=number,
        title=title,
        status=status,
        date=date,
        filename=filepath.name,
        related=related,
        supersedes=supersedes,
        doc_type="adr"
    )


def parse_idea(filepath: Path) -> Optional[Document]:
    """아이디어 파일 파싱"""
    content = filepath.read_text(encoding="utf-8")

    # 제목 추출 (# IDEA-NNN: 제목)
    title_match = re.search(r"^# IDEA-(\d+): (.+)$", content, re.MULTILINE)
    if not title_match:
        return None

    number = title_match.group(1)
    title = title_match.group(2).strip()

    # 상태 추출
    status_match = re.search(r"\*\*상태\*\*:\s*(.+?)(?:\n|$)", content)
    status = status_match.group(1).strip() if status_match else "알 수 없음"

    # 제안일 추출
    date_match = re.search(r"\*\*제안일\*\*:\s*(\d{4}-\d{2}-\d{2})", content)
    date = date_match.group(1) if date_match else "알 수 없음"

    # 관련 아이디어 추출
    related_match = re.search(r"\*\*관련 아이디어\*\*:\s*(.+?)(?:\n|$)", content)
    related = []
    if related_match and related_match.group(1).strip() != "-":
        related = re.findall(r"IDEA-(\d+)", related_match.group(1))

    return Document(
        number=number,
        title=title,
        status=status,
        date=date,
        filename=filepath.name,
        related=related,
        doc_type="idea"
    )


def generate_adr_table(documents: list[Document]) -> str:
    """ADR 테이블 생성"""
    lines = [
        "| 번호 | 제목 | 상태 | 날짜 | 관련 ADR |",
        "|------|------|------|------|----------|"
    ]

    for doc in sorted(documents, key=lambda x: x.number):
        related = ", ".join([f"[ADR-{r}]({r.zfill(4)}-*.md)" for r in doc.related]) or "-"
        lines.append(
            f"| [ADR-{doc.number}]({doc.filename}) | {doc.title} | {doc.status} | {doc.date} | {related} |"
        )

    return "\n".join(lines)


def generate_idea_table(documents: list[Document]) -> str:
    """아이디어 테이블 생성"""
    lines = [
        "| 번호 | 제목 | 상태 | 제안일 | ADR 링크 |",
        "|------|------|------|--------|----------|"
    ]

    for doc in sorted(documents, key=lambda x: x.number):
        lines.append(
            f"| [IDEA-{doc.number}]({doc.filename}) | {doc.title} | {doc.status} | {doc.date} | - |"
        )

    return "\n".join(lines)


def update_readme(readme_path: Path, table_content: str):
    """README.md 업데이트"""
    content = readme_path.read_text(encoding="utf-8")

    # AUTO-GENERATED 섹션 교체
    pattern = r"(<!-- AUTO-GENERATED-START -->).*?(<!-- AUTO-GENERATED-END -->)"
    replacement = f"\\1\n{table_content}\n\\2"

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    readme_path.write_text(new_content, encoding="utf-8")


def generate_changelog(adr_docs: list[Document], idea_docs: list[Document], output_path: Path):
    """CHANGELOG.md 생성"""
    content = [
        "# 변경 이력 (Changelog)",
        "",
        "> 이 파일은 자동 생성됩니다. 직접 수정하지 마세요.",
        f"> 마지막 업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        "",
    ]

    # 날짜별로 그룹화
    all_docs = adr_docs + idea_docs
    by_date = {}
    for doc in all_docs:
        if doc.date not in by_date:
            by_date[doc.date] = []
        by_date[doc.date].append(doc)

    for date in sorted(by_date.keys(), reverse=True):
        content.append(f"## {date}")
        content.append("")

        for doc in by_date[date]:
            if doc.doc_type == "adr":
                content.append(f"### ADR-{doc.number}: {doc.title}")
                content.append(f"- **상태**: {doc.status}")
                if doc.supersedes:
                    content.append(f"- **대체**: ADR-{doc.supersedes}를 대체함")
            else:
                content.append(f"### IDEA-{doc.number}: {doc.title}")
                content.append(f"- **상태**: {doc.status}")
            content.append("")

        content.append("---")
        content.append("")

    output_path.write_text("\n".join(content), encoding="utf-8")


def generate_relations(adr_docs: list[Document], output_path: Path):
    """관계 그래프 생성 (RELATIONS.md)"""
    content = [
        "# ADR 관계도",
        "",
        "> ADR 간의 관계를 시각화합니다.",
        "",
        "```mermaid",
        "graph TD"
    ]

    for doc in adr_docs:
        node_id = f"ADR{doc.number}"
        status_class = "accepted" if "수락" in doc.status else "deprecated" if "폐기" in doc.status else "proposed"
        content.append(f"    {node_id}[ADR-{doc.number}: {doc.title}]")

        for related in doc.related:
            content.append(f"    {node_id} --> ADR{related}")

        if doc.supersedes:
            content.append(f"    {node_id} -.->|대체| ADR{doc.supersedes}")

    content.append("")
    content.append("    classDef accepted fill:#10b981,color:white")
    content.append("    classDef deprecated fill:#ef4444,color:white")
    content.append("    classDef proposed fill:#f59e0b,color:white")
    content.append("```")
    content.append("")
    content.append("## 범례")
    content.append("")
    content.append("- 실선 화살표: 관련 ADR")
    content.append("- 점선 화살표: 대체 관계")

    output_path.write_text("\n".join(content), encoding="utf-8")


def main():
    base_path = Path(__file__).parent.parent
    decisions_path = base_path / "decisions"
    ideas_path = base_path / "ideas"

    # ADR 파싱
    adr_docs = []
    for filepath in decisions_path.glob("*.md"):
        if filepath.name.startswith("_") or filepath.name == "README.md":
            continue
        doc = parse_adr(filepath)
        if doc:
            adr_docs.append(doc)

    # 아이디어 파싱
    idea_docs = []
    for filepath in ideas_path.glob("*.md"):
        if filepath.name.startswith("_") or filepath.name == "README.md":
            continue
        doc = parse_idea(filepath)
        if doc:
            idea_docs.append(doc)

    # README 업데이트
    if adr_docs:
        adr_table = generate_adr_table(adr_docs)
        update_readme(decisions_path / "README.md", adr_table)
        print(f"✓ decisions/README.md 업데이트 완료 ({len(adr_docs)}개 ADR)")

    if idea_docs:
        idea_table = generate_idea_table(idea_docs)
        update_readme(ideas_path / "README.md", idea_table)
        print(f"✓ ideas/README.md 업데이트 완료 ({len(idea_docs)}개 아이디어)")

    # CHANGELOG 생성
    generate_changelog(adr_docs, idea_docs, base_path / "CHANGELOG.md")
    print("✓ CHANGELOG.md 생성 완료")

    # 관계도 생성
    generate_relations(adr_docs, base_path / "RELATIONS.md")
    print("✓ RELATIONS.md 생성 완료")


if __name__ == "__main__":
    main()
