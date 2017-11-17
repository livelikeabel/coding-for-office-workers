import random

def input_user_numbers():
    numbers = input(" 1~9사이의 숫자 3개를 입력해 주세요! : ") #type is str
    return [int (i) for i in numbers] #int로 형 변환 하여list를 return

def ai_numbers():
    return random.sample(range(1, 10), 3)

def strike(user, ai):
    strike_num = 0
    if user[0] == ai[0]:
        strike_num += 1
    if user[1] == ai[1]:
        strike_num += 1
    if user[2] == ai[2]:
        strike_num += 1
    return strike_num

def ball(user, ai):
    ball_num = 0
    if user[0] == ai[1] or user[0] == ai[2]:
        ball_num += 1
    if user[1] == ai[0] or user[1] == ai[2]:
        ball_num += 1
    if user[2] == ai[0] or user[2] == ai[1]:
        ball_num += 1
    return ball_num

def nothing(user, ai):
    nothing_num = 0
    if user[0] != ai[0] and user[0] != ai[1] and user[0] != ai[2]:
        nothing_num += 1
    if user[1] != ai[0] and user[1] != ai[1] and user[1] != ai[2]:
        nothing_num += 1
    if user[2] != ai[0] and user[2] != ai[1] and user[2] != ai[2]:
        nothing_num += 1
    return nothing_num

#실행
print(" Abel's baseball game Start!")
ai_numbers = ai_numbers()
strike_num = 0
while strike_num < 3:
    user_numbers = input_user_numbers()
    #print(ai_numbers) # 정답(컴퓨터 숫자) 보기
    strike_num = strike(user_numbers, ai_numbers)
    ball_num = ball(user_numbers, ai_numbers)
    nothing_num = nothing(user_numbers, ai_numbers)

    print(" strike : {} \n ball : {} \n nothing : {}"
          .format(strike_num, ball_num, nothing_num))

print(" congratulations!!")
