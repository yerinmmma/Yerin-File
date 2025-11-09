from restaurant import 한식, 중식, 양식, 일식, 분식, 기타

print("==== 식당 추천 프로그램 ====")

while True:
    print("\n카테고리를 선택하세요:")
    print("1. 한식  2. 중식  3. 양식  4. 일식  5. 분식  6. 기타  0. 종료")
    choice = input("선택: ")

    if choice == '0':  # 종료 조건
        print("프로그램 실행을 종료합니다.")
        break
    elif choice == "1":  # 한식 선택 시
        korean = 한식()  # 한식 클래스의 인스턴스 생성
        식당추천 = korean.r_category()  # 무작위로 3개의 식당 추천

        for key, value in 식당추천:
            print(f"\n식당 이름: {key}")
            for v in value:
                print(v)
    elif choice == '2':  # 한식 선택 시
        chinese = 중식()  # 한식 클래스의 인스턴스 생성
        식당추천 = chinese.r_category()  # 무작위로 3개의 식당 추천

        for key, value in 식당추천:
            print(f"\n식당 이름: {key}")
            for v in value:
                print(v)

    elif choice == '3':  # 양식 선택 시
        western = 양식()  # 양식 클래스의 인스턴스 생성
        식당추천 = western.r_category()  # 무작위로 3개의 식당 추천

        for key, value in 식당추천:
            print(f"\n식당 이름: {key}")    
            for v in value:
                print(v)
    elif choice == '4':
        japanese = 일식()
        식당추천 = japanese.r_category()

        for key, value in 식당추천:
            print(f"\n식당 이름: {key}")    
            for v in value:
                print(v)
    elif choice == '5':
        snack= 분식()
        식당추천 = snack.r_category()

        for key, value in 식당추천:
            print(f"\n식당 이름: {key}")    
            for v in value:
                print(v)
                
    elif choice == '6':
        other = 기타()
        식당추천 = other.r_category()

        for key, value in 식당추천:
            print(f"\n식당 이름: {key}")    
            for v in value:
                print(v)



