input_id = input("아이디를 입력해주세요: ")

members = {'dlehrud':'이도경', 'Prop':'교수님', 'No':'노진구'} # id : 닉네임

def login(input_id, members):
    if input_id in members.keys():
        print('Hello,', members[input_id])
    else:
        print('새로오신분 환영합니다')
        nickname = input('사용하실 닉네임을 입력해주십시오: ')
        members[input_id] = nickname
    return members[input_id], members

nickname, members = login(input_id, members)

print("{}님 반갑습니다. {}(HP 100)으로 게임을 시작합니다".format(nickname, nickname))
print("길을 가다가 퉁퉁이를 만났습니다.")

while True:
    print("1. 싸운다 2. 도망간다")
    num = int(input("선택: "))

    if num == 1:
        print("퉁퉁이에게 이긴다")
        break
    elif num == 2:
        print("퉁퉁이에게 진다")
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력해주십시오.")
