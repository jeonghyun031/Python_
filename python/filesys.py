import pickle
import os
import uuid
import shutil

FILENAME = "media_data.pkl"
BACKUP_FILENAME = "media_data_backup.pkl"

def load_data():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return {}
    return {}

def save_data(data):
    try:
        if os.path.exists(FILENAME):
            shutil.copy(FILENAME, BACKUP_FILENAME)  # 기존 파일 백업
        with open(FILENAME, "wb") as f:
            pickle.dump(data, f)
    except Exception as e:
        print(f"데이터 저장 중 오류 발생: {e}")

def generate_unique_id(existing_ids):
    while True:
        new_id = f"auto_{uuid.uuid4().hex[:8]}"
        if new_id not in existing_ids:
            return new_id

def display_all_media(media_data):
    print("\n전체 콘텐츠 목록:")
    if not media_data:
        print("저장된 콘텐츠가 없습니다.")
        return
   
    for media_id, media_info in media_data.items():
        print(f"- ID: {media_id}, 제목: {media_info['title']}, 타입: {media_info['type']}, 태그: {media_info['tags']}")

def search_by_tag(media_data):
    search_tag = input("\n검색할 태그 입력: ").strip().lower()
    results = [
        f"- ID: {mid}, 제목: {data['title']}, 타입: {data['type']}, 태그: {data['tags']}"
        for mid, data in media_data.items()
        if any(tag.lower() == search_tag for tag in data["tags"])
    ]
    print("\n".join(results) if results else "\n- 검색 결과가 없습니다.")

def edit_tags(media_data):
    media_id = input("\n태그를 수정할 콘텐츠 ID 입력: ").strip()
    if media_id not in media_data:
        print("\n- 해당 ID의 콘텐츠를 찾을 수 없습니다.")
        return

    new_tags = input("새로운 태그 입력 (쉼표 구분): ").strip()
    media_data[media_id]["tags"] = [tag.strip() for tag in new_tags.split(",")] if new_tags else []

    save_data(media_data)
    print("\n태그가 수정되었습니다.")

def add_media_entry(media_data):
    media_id = input("\n콘텐츠 ID 입력: ").strip()
    if not media_id or media_id in media_data:
        media_id = generate_unique_id(media_data)

    title = input("제목 입력: ").strip()
    if not title:
        title = "Untitled"

    media_type = input("타입 (image/video/audio): ").strip().lower()
    if media_type not in ["image", "video", "audio"]:
        media_type = "image"

    tags = input("태그 입력 (쉼표 구분): ").strip()
    tag_list = [tag.strip() for tag in tags.split(",")] if tags else ["default_tag"]

    media_data[media_id] = {
        "title": title,
        "type": media_type,
        "tags": tag_list
    }

    save_data(media_data)
    print("\n데이터가 저장되었습니다.")

def main():
    media_data = load_data()
    while True:
        print("\n멀티미디어 태그 관리 시스템")
        print("1. 콘텐츠 등록")
        print("2. 태그로 검색")
        print("3. 콘텐츠 태그 수정")
        print("4. 전체 콘텐츠 보기")
        print("5. 종료")

        choice = input("\n메뉴 선택 (1~5): ").strip()

        if choice == "1":
            add_media_entry(media_data)
        elif choice == "2":
            search_by_tag(media_data)
        elif choice == "3":
            edit_tags(media_data)
        elif choice == "4":
            display_all_media(media_data)
        elif choice == "5":
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("\n잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()