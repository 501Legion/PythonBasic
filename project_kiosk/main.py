####################################
## Project: 조선별다방
## Writer: GayCarrier
## Company: 조선대학교
## Reg_date: 2024.10.14
## Update_date: 2024.10.14
## License:
## Contents: 콘솔 프로그래밍을 활용한 커피 전문점에서 사용하는 키오스크

# 키오스크

# 1. 메인 메뉴 출력(커피, 쥬스, 스무디, 베이커리)
# 2. 메인 메뉴 선택(사용자)
# 3. 서브 메뉴 출력(커피 or 스무디 or 베이커리)
# 4. 서브 메뉴 선택(사용자)
# 5. 고객 주문 메뉴 목록에 저장(선택한 서브 메뉴)
# 6. 추가 주문 여부?(yes or no)
# 7-1. yes: 1번으로 보내기
# 7-2. no: 최종주문 내역으로 보내기
# 8. 최종주문 내역 출력

from service_kiosk import print_menu
from service_kiosk import select_menu

###################
## 1. 메뉴 만들기 ##
###################
main_menu = {
    1: "커피",
    2: "스무디",
    3: "베이커리"
}

coffee_menu = {
    1: "아메리카노",
    2: "카라멜마끼아또",
}


coffee_price = {
    1: 3500,
    2: 4000,
}

smoothie_menu = {
    1: "블루베리",
    2: "망고",
    3: "흑임자",
    4: "딸기"
}

smoothie_price = {
    1: 5000,
    2: 4000,
    3: 3000,
    4: 2000
}

bakery_menu = {
    1:"조각 케이크",
    2:"롤 케이크",
    3:"샌드위치"
}

bakery_price = {
    1:5000,
    2:10000,
    3:8000
}

order_list = []

while True:
    # 1. 메인메뉴 출력
    print("★" * 50)
    print("★★ 별다방조선")
    print_menu(main_menu, 3)

    ## 2. 메인메뉴 선택
    order = select_menu(3)

    ## 3. 서브메뉴 출력 및 선택
    if order == 1:      # 커피
        print_menu(coffee_menu, 2)
        sub_order = select_menu(2)
        order_list.append([coffee_menu[sub_order], coffee_price[sub_order]])
    elif order == 2:    # 스무디
        print_menu(smoothie_menu, 4)
        sub_order = select_menu(4)
        order_list.append([smoothie_menu[sub_order], smoothie_price[sub_order]])
    elif order == 3:    # 베이커리
        print_menu(bakery_menu, 3)
        sub_order = select_menu(3)
        order_list.append([bakery_menu[sub_order], bakery_price[sub_order]])
    
    for item in order_list:
        print(f"주문기록: {item}")

# 6번 추가 주문하시겠습니까? -> input()
# 결과 : y/n
# y : 1번으로 이동
# n: 출력(주문 페이지로 이동)
    print(">> MSG: 추가 주문하시겠습니까?")
    while True:
        yn = input(">> y/n: ")

        if yn == "y":
            pass
        elif yn == "n":
            pass
        else:
            print(">> WARING: 올바른 값을 입력하세요.")



# 5. 메뉴 서비스
# select_num이 1,2,3,4인 경우
    if select_num == 1:
        pass

