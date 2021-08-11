class Ranking:
    def __init__(self):
        self.list = []
        self.dict = {}
    def rank(self,name,score):
        self.list.append(score)
        self.dict[score] = name
        self.list.sort()
    def show(self):
        grade = 0
        for s in self.list:
            n = self.dict[s]
            grade +=1
            print(grade, '|', n, '(', s,')')

event_list = []

def new_event():
    event = input('추가할 종목을 입력하세요.\n')
    if event in event_list:
        print('이미 랭킹이 존재하는 종목입니다.')
    else:
        print('%s이(가) 추가되었습니다.'%event)
        globals()[event] = Ranking()
    print()

def new_rank():
    event = input('랭킹을 추가할 종목을 입력하세요\n')
    a,b = input('이름을 입력하세요.\n'), input('점수를 입력하세요.\n')
    globals()[event].rank(a, b)
    print()

def show_rank():
    event = input('랭킹을 확인할 종목을 입력하세요\n')
    print()
    print('종목 :',event)
    globals()[event].show()
    print()

while True:
    what = input('새로운 종목을 추가하려면 1, 기존 종목에 랭킹을 추가하려면 2, 특정 종목의 랭킹을 확인하려면 3을 입력하세요.\n')
    try:
        what = int(what)
        if what == 1:
            new_event()
        elif what == 2:
            new_rank()
        elif what == 3:
            show_rank()
        else: print('올바른 숫자를 입력하세요.')
        print()
    except:
        print('오류가 났습니다. 관리자에게 문의하세요.')
        print()
