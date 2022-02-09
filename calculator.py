# 기본적인 사칙연산 계산 함수가 내장된 cal_module을 이용하여 무한루프 형식의 정수 계산기를 만들어라 계산이 끝나고 y를 입력하면 프로그램 종료
import cal_module as cal

while True:
    a = input("\n첫번째 정수를 입력하시오 : ")
    b = input("두번째 정수를 입력하시오 : ")
    c = input("연산자를 입력하세요 (+ - * /) : ")
    result = 0

    a = int(a)
    b = int(b)

    if c == '+':
        result = cal.sum(a, b)
    elif c == '-':
        result = cal.min(a, b)
    elif c == '*':
        result = cal.mul(a, b)
    elif c == '/':
        result = cal.div(a, b)
    else:
        print("잘못된 연산자 입력값입니다")

    #print("연산 결과 : {} {} {} = {}".format(a, c, b, result))
    print(f"연산 결과 : {a} {c} {b} = {result}")
    cRepeat = input("프로그램을 종료하시겠습니까? (y/n) : ")
    if cRepeat == 'y' or cRepeat == 'Y':
        break
