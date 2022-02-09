# 학생 출석부를 갱신하는 프로그램 구현 이름 순으로 나열하며 성씨가 같으면 다음 자리까지만 비교 무한루프로 구현하며 재입력 여부를 물어본 후 n을 입력시 무한루프 탈출 중복되지 않는 이름만 갱신

list_Student = ["김태양", "박종현", "심민석", "이상규"]

def PrintStudent():
    print("\n현재 출석부")
    for i in list_Student:
        print(i)

def CheckName(name):
    if name in list_Student:
        print("이미 등록되어있는 학생입니다.")
    else:
        nIndex = 0
        for i in range(len(list_Student)):
            if name > list_Student[i]:
                nIndex += 1
            elif name == list_Student[i]:
                if name[1] > list_Student[i][1]:
                    nIndex += 1
        list_Student.insert(nIndex, name)

while True:
    PrintStudent()
    strName = input("학생 이름을 입력하세요 : ")
    CheckName(strName)
    PrintStudent()
    strAnswer = input("다음 학생을 기입하겠습니까? (y/n) : ")
    if strAnswer == 'n' or strAnswer == 'N':
        break
