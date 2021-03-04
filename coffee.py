# 실제 커피 자판기처럼 살 붙이기 (돈을 정확히 300원을 넣어야 커피를 만들어 줌.)
coffee = 10  # True

while True:
    money = int(input('돈을 넣어 주세요.'))
    if money == 300:
        print('돈을 넣었으니 커피를 줍니다.')
        coffee -= 1
        print('남은 커피는 %d개입니다.' % coffee)
    elif money > 300:
        print('거스름돈은 %d원 입니다.' % (money - 300))
        print('돈을 넣었으니 커피를 줍니다.')
        coffee -= 1
        print('남은 커피는 %d개입니다.' % coffee)
    else:
        print('다시 돈을 넣어 주세요.')
        print('남은 커피는 %d개입니다.' % coffee)

    if not coffee:
        print('커피가 다 떨어졌으니 판매를 중지합니다.')
        break