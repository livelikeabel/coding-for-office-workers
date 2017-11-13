"""
사용자에게 가위, 바위, 보 중 하나를 물어봅니다. -> input 사용
사용자가 가위, 바위, 보를 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가릅니다.
->  1. 리스트 사용. 1) 나의 가위바위보, 2)컴퓨터 가위바위보
    2. 랜덤으로 하나 뽑기
    3. if 를 사용하여 로직 구현하기
다합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝이 납니다.
->(클래스 만들어야 하나?)
    1. User의 승리카운트, 패배카운트를 체크한다.
    2. 3번 이기거나 질때 까지 반복문으로 돌린다.
힌트

리스트를 한 개를 사용하고 사용자의 입력을 받아야 합니다.
앞서 사용했던 임의 뽑기를 다시 사용합니다. 검색 키워드 : random, randint, shuffle
컴퓨터에게 가위, 바위, 보의 승패를 가르쳐줘야 합니다.

"""
import random

win_count = 0
lose_count = 0

while win_count or lose_count < 4:
    user_choice = input("'가위, 바위, 보'중 하나를 선택해 주세요 : ") #예외처리 해야하나?
    print("당신의 선택 : {}".format(user_choice))

    choices = ["가위", "바위", "보"]
    computer_choice = random.choice(choices)
    print("컴퓨터의 선택 : {}".format(computer_choice))

    if user_choice == "가위":
        if computer_choice == "가위":
            print("비겼습니다.")
        if computer_choice == "바위":
            print("졌습니다.")
            lose_count += lose_count + 1
        if computer_choice == "보":
            print("이겼습니다.")
            win_count += win_count + 1

    elif user_choice == "바위":
        if computer_choice == "바위":
            print("비겼습니다.")
        if computer_choice == "보":
            print("졌습니다.")
            lose_count += lose_count + 1
        if computer_choice == "가위":
            print("이겼습니다.")
            win_count += win_count + 1

    elif user_choice == "보":
        if computer_choice == "보":
            print("비겼습니다.")
        if computer_choice == "가위":
            print("졌습니다.")
            lose_count += lose_count + 1
        if computer_choice == "바위":
            print("이겼습니다.")
            win_count += win_count + 1

    print("스코어 : {}번 이기고, {}번 졌습니다.".format(win_count, lose_count))
