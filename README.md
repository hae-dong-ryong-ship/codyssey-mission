# 📝 나만의 프롬프트 관리 프로그램

GenAI 미션을 수행하며 흩어져 있던 프롬프트를 한곳에 모아 **분류 · 검색 · 즐겨찾기**로 관리하는 Python 콘솔 프로그램입니다.
외부 라이브러리 없이 Python 기본 문법(변수, 조건문, 반복문, 리스트, 딕셔너리, 함수)만으로 구현했습니다.

## 🛠 개발 환경

- Python 3.10 이상 (`match-case` 문법 사용)
- VSCode + Python Extension
- Git / GitHub

## ▶️ 실행 방법

```bash
# 1. 저장소 내려받기
git clone https://github.com/<내-아이디>/prompt-manager.git
cd prompt-manager

# 2. 실행 (Windows는 python, macOS/Linux는 python3)
python main.py
```

## ✨ 기능 목록

| 번호 | 기능 | 설명 |
|---|---|---|
| 1 | 프롬프트 추가 | 제목, 내용(여러 줄), 카테고리를 입력해 새 프롬프트 등록. 빈 값은 다시 입력 요청 |
| 2 | 프롬프트 목록 | 전체 프롬프트를 번호 · 카테고리 · 즐겨찾기(⭐)와 함께 출력 |
| 3 | 카테고리별 조회 | 선택한 카테고리의 프롬프트만 출력 |
| 4 | 프롬프트 검색 | 키워드가 제목 또는 내용에 포함된 프롬프트 검색 |
| 5 | 프롬프트 상세 보기 | 번호로 선택한 프롬프트의 전체 내용 출력 |
| 6 | 즐겨찾기 관리 | 번호로 선택한 프롬프트의 즐겨찾기 추가/해제 |
| 7 | 즐겨찾기 목록 | 즐겨찾기한 프롬프트만 모아 보기 |
| 0 | 종료 | 프로그램 종료 |

> 데이터는 프로그램 실행 중에만 유지되며, 종료하면 기본 데이터로 초기화됩니다.

## 🖥 실행 결과

기능별 실행 화면은 👉 [RESULT.md](RESULT.md) 에서 확인할 수 있습니다.

## 🗂 프롬프트 카테고리

| 카테고리 | 설명 |
|---|---|
| 텍스트 생성 | 블로그 글, 이메일, 보고서 등 글을 만드는 프롬프트 |
| 이미지 생성 | 썸네일, 일러스트 등 이미지 생성용 키워드/지시문 |
| 영상 생성 | 광고 스크립트, 영상 콘셉트 등 영상 제작용 프롬프트 |
| 페르소나 | AI에게 특정 역할·말투·전문성을 부여하는 설계안 |
| 자동화 | 요약, 분류 등 노코드 자동화 흐름에 넣는 프롬프트 |
| 기타 | 위에 속하지 않는 프롬프트 (직접 입력한 카테고리도 사용 가능) |

## 🧱 코드 구조

```
main.py
├── 기본 데이터        CATEGORIES, prompts
├── 보조 함수          input_not_empty(), input_multiline(), format_prompt(),
│                      print_prompts(), select_category(), get_prompt_by_number()
├── 기능 함수          show_menu(), add_prompt(), show_list(), show_by_category(),
│                      search_prompt(), show_detail(), toggle_favorite(), show_favorites()
└── 메인 루프          main()
```
