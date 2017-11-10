#맛집 고르기
import random

choice = input("한식, 중식, 일식, 중 한가지를 고르시오 : ")
if choice == "한식":
    h_list = ["김가네", "운암정", "안씨막걸리", "백채 김치찌개", "정식당"]
    print(random.choice(h_list))
if choice == "중식":
    c_list = ["백리향", "팔선", "유에", "유유안", "이대리중식당"]
    print(random.choice(c_list))
if choice == "일식":
    j_list = ["스시조", "다께"]
    print(random.choice(j_list))
if choice == "양식":
    f_list = ["페닌슐라", "떼레노", "트라토리아onuel", "Arzak", "Fatduck"]
    print(random.choice(f_list))
