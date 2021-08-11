import random
plus_num = random.randint(1,9)
answer = []

for i in range(4):
    while plus_num in answer:
        plus_num = random.randint(1,9)
    answer.append(plus_num)

answer_num = answer[0]*1000 + answer[1]*100 + answer[2]*10 + answer[3]

def check(number):
    while len(number) != 4:
        print ('네자리 숫자를 입력해주세요')
        number = input()
    return number

def guess(number):
    s = 0
    b = 0
    question = []
    for i in range(4):
        question.append(int(number[i]))
    for j in range(4):
        if question[j] == answer[j]:
            s += 1
        else:
            for k in range(4):
                if question[j] == answer[k]:
                    b+=1
    if answer != question:
        print('%ds%db'%(s,b))


number = input('숫자를 입력하세요 \n')
number = check(number)
guess(number)
try_num = 1

while answer_num != int(number):
    number = input('숫자를 입력하세요 \n')
    number = check(number)
    guess(number)
    try_num += 1

print('정답입니다\n%d번째에 맞췄습니다'%try_num)
