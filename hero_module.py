class Hero:
    def __init__(self, name, hp, exp):
        Hero.strName = name
        Hero.nHp = hp
        Hero.nExp = exp
        Hero.nLevel = 1
        Hero.nX = 0
        Hero.nY = 0

    def __del__(self):
        print("플레이어 \"{}\" 캐릭터 삭제".format(Hero.strName))

    def __repr__(self):
        print("내가 이해한게 맞다면 객체 호출하면 나오는거임")
        return "맞냐?"

    def Move(self):
        #print("현재 플레이어 {}의 위치 : ({}, {})".format(Hero.strName, Hero.nX, Hero.nY))
        print(f"현재 플레이어 {Hero.strName}의 위치 : ({Hero.nX}, {Hero.nY})")
        x = input("x좌표를 몇만큼 이동하겠습니까? : ")
        y = input("y좌표를 몇만큼 이동하겠습니까? : ")

        x = int(x)
        y = int(y)

        Hero.nX += x
        Hero.nY += y

        #print("이동후 현재 플레이어 {}의 위치 : ({}, {})".format(Hero.strName, Hero.nX, Hero.nY))
        print(f"이동 후 현재 플레이어 {Hero.strName}의 위치 : ({Hero.nX}, {Hero.nY})")

    def HpCtrl(self, hp):
        #print("현재 플레이어 {}의 체력 : {}".format(Hero.strName, Hero.nHp))
        print(f"현재 플레이어 {Hero.strName}의 체력 : {Hero.nHp}")

        Hero.nHp += hp

        #print("갱신된 플레이어 {}의 체력 : {}".format(Hero.strName, Hero.nHp))
        print(f"갱신된 플레이어 {Hero.strName}의 체력 : {Hero.nHp}")
    def GiveExp(self, exp):
        #print("현재 플레이어 {}의 레벨 : {}".format(Hero.strName, Hero.nLevel))
        #print("현재 플레이어 {}의 경험치 : {}".format(Hero.strName, Hero.nExp))

        print(f"현재 플레이어 {Hero.strName}의 레벨 : {Hero.nLevel}")
        print(f"현재 플레이어 {Hero.strName}의 경험치 : {Hero.nExp}")

        Hero.nExp += exp

        if Hero.nExp >= 100:
            Hero.nLevel += 1
            Hero.nExp -= 100

        #print("갱신된 플레이어 {}의 레벨 : {}".format(Hero.strName, Hero.nLevel))
        #print("갱신된 플레이어 {}의 경험치 : {}".format(Hero.strName, Hero.nExp))
        print(f"갱신된 플레이어 {Hero.strName}의 레벨 : {Hero.nLevel}")
        print(f"갱신된 플레이어 {Hero.strName}의 경험치 : {Hero.nExp}")