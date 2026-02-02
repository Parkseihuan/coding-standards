# 빠른 시작 가이드

## 새 결정(ADR) 기록하기

<!-- tabs:start -->

#### **1단계: 템플릿 복사**

```bash
cp decisions/_template.md decisions/0004-새로운-결정.md
```

#### **2단계: 내용 작성**

파일을 열고 다음 항목을 작성합니다:

- 제목
- 상태: `제안됨` / `수락됨` / `폐기됨`
- 날짜
- 컨텍스트 (왜 이 결정이 필요한가?)
- 결정 내용
- 고려한 대안들
- 예상 결과

#### **3단계: 요약 생성 & 커밋**

```bash
python scripts/generate_summary.py
git add .
git commit -m "docs: 새 ADR 추가"
git push
```

<!-- tabs:end -->

---

## 새 아이디어 제안하기

<!-- tabs:start -->

#### **1단계: 템플릿 복사**

```bash
cp ideas/_template.md ideas/003-새-아이디어.md
```

#### **2단계: 내용 작성**

- 상태: `초안` → `검토중` → `채택됨`/`거절됨`
- 배경, 아이디어 요약, 예상 이점/문제점

#### **3단계: 커밋**

```bash
python scripts/generate_summary.py
git add . && git commit -m "docs: 새 아이디어 제안"
```

<!-- tabs:end -->

---

## 아이디어 → ADR 전환

아이디어가 채택되면:

1. 아이디어 상태를 `채택됨`으로 변경
2. 새 ADR 생성
3. 아이디어에 `전환된 ADR` 링크 추가

```markdown
- **전환된 ADR**: [ADR-0005](../decisions/0005-xxx.md)
```

---

## 기존 결정 변경/대체

```markdown
# 새 ADR 파일에서
- **대체된 ADR**: [ADR-0003](./0003-xxx.md)

# 기존 ADR 파일에서
- **상태**: 대체됨  (← 변경)
```

---

## 자주 쓰는 명령어

| 작업 | 명령어 |
|------|--------|
| 요약 재생성 | `python scripts/generate_summary.py` |
| 로컬 미리보기 | `npx docsify-cli serve docs` |
| 변경사항 확인 | `git status` |
| 커밋 | `git add . && git commit -m "메시지"` |
| 푸시 | `git push` |
