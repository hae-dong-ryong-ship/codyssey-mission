"""
나만의 프롬프트 관리 프로그램
- 외부 라이브러리 없이 Python 기본 문법만 사용
- Python 3.10 이상 (match-case 문법 사용)
"""
# ──────────────────────────────────────────
# 1. 기본 데이터
# ──────────────────────────────────────────

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# TODO: 아래 예시를 '이전 미션에서 직접 작성한 프롬프트'로 바꿔주세요. (최소 3개)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": (
            "당신은 10년 경력의 전문 블로거입니다.\n"
            "주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.\n"
            "서론, 본론, 결론 구조를 갖추고,\n"
            "독자의 관심을 끄는 제목을 3개 제안해주세요."
        ),
        "category": "텍스트 생성",
        "favorite": True,
    },
    {
        "title": "제품 썸네일 생성",
        "content": (
            "다음 제품의 매력적인 썸네일 이미지를 생성해주세요.\n"
            "밝은 스튜디오 조명, 흰색 배경, 제품이 중앙에 오도록 배치하고\n"
            "16:9 비율, 고해상도, 미니멀한 스타일로 표현해주세요."
        ),
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": (
            "당신은 15년 경력의 IT 컨설턴트입니다.\n"
            "비전공자도 이해할 수 있도록 쉬운 비유를 사용하고,\n"
            "답변 마지막에는 항상 실행 가능한 다음 단계 3가지를 제안해주세요."
        ),
        "category": "페르소나",
        "favorite": False,
    },
    {
        "title": "뉴스 요약 프롬프트",
        "content": (
            "아래 뉴스 기사를 3줄로 요약해주세요.\n"
            "1줄: 핵심 사건, 2줄: 원인과 배경, 3줄: 예상되는 영향\n"
            "마지막에 관련 키워드 5개를 해시태그 형식으로 붙여주세요."
        ),
        "category": "자동화",
        "favorite": False,
    },
]

# ──────────────────────────────────────────
# 2. 공통(보조) 함수
# ──────────────────────────────────────────

def input_not_empty(message):
    """빈 값이 아닐 때까지 반복해서 입력받는다."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("⚠️  입력값이 비어 있습니다. 다시 입력해주세요.")


def input_multiline(message):
    """여러 줄을 입력받는다. 빈 줄을 입력하면 입력이 끝난다."""
    while True:
        print(message + " (여러 줄 입력 가능, 입력을 마치려면 빈 줄에서 Enter)")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        if lines:
            return "\n".join(lines)
        print("⚠️  내용이 비어 있습니다. 다시 입력해주세요.")


def format_prompt(prompt):
    """목록에 표시할 한 줄 문자열을 만든다. 예: [텍스트 생성] 제목 ⭐"""
    star = " ⭐" if prompt["favorite"] else ""
    return f"[{prompt['category']}] {prompt['title']}{star}"


def print_prompts(numbered_prompts):
    """(번호, 프롬프트) 목록을 출력한다. 번호는 전체 목록 기준 번호이다."""
    for number, prompt in numbered_prompts:
        print(f"{number}. {format_prompt(prompt)}")


def select_category(allow_custom=False):
    """카테고리 목록을 보여주고 선택된 카테고리 이름을 돌려준다.
    잘못 입력하면 None을 돌려준다."""
    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}) {category}")
    custom_number = len(CATEGORIES) + 1
    if allow_custom:
        print(f"{custom_number}) 직접 입력")

    choice = input("선택: ").strip()
    if not choice.isdigit():
        print("⚠️  숫자를 입력해주세요.")
        return None

    number = int(choice)
    if 1 <= number <= len(CATEGORIES):
        return CATEGORIES[number - 1]
    if allow_custom and number == custom_number:
        return input_not_empty("카테고리 이름: ")

    print("⚠️  목록에 없는 번호입니다.")
    return None


# ──────────────────────────────────────────
# 3. 기능 함수
# ──────────────────────────────────────────

def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input_not_empty("제목: ")
    content = input_multiline("내용:")

    category = None
    while category is None:
        print("\n카테고리 선택:")
        category = select_category(allow_custom=True)

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,  # 즐겨찾기 기본값은 False
    })
    print("\n✅ 프롬프트가 추가되었습니다!")


def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    print_prompts(enumerate(prompts, start=1))
    print(f"\n총 {len(prompts)}개의 프롬프트")


# ──────────────────────────────────────────
# 4. 메인 루프
# ──────────────────────────────────────────

def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        match choice:
            case "1":
                add_prompt()
            case "2":
                show_list()
            case "0":
                print("프로그램을 종료합니다. 안녕히 가세요! 👋")
                break
            case _:
                print("⚠️  잘못된 입력입니다. 0~7 사이의 번호를 입력해주세요.")


if __name__ == "__main__":
    main()
