#import hero_module as hero
from hero_module import Hero

strName = input("캐릭터의 이름을 입력하세요 : ")

#player = hero.Hero(strName, 100, 0)
player = Hero(strName, 100, 0)

while True:
    nAct = input("\n행동을 선택하세요 : (1 : 이동 2 : 체력 수정 3 : 경험치 지급 0 : 프로그램 종료) ")
    nAct = int(nAct)

    if nAct == 1:
        player.Move()
    elif nAct == 2:
        hp = input("\nhp 변경량 입력 : ")
        hp = int(hp)
        player.HpCtrl(hp)
    elif nAct == 3:
        exp = input("\nexp 지급량 입력 : ")
        exp = int(exp)
        player.GiveExp(exp)
    elif nAct == 0:
        break
    else:
        print("잘못된 행동 입력값입니다.")