import sys
# 도스 창에서 이 모듈 실행, sys.argv의 [0]는 memo.py이고 그 뒤에 붙는 내용들이 각각 [1], [2]임.
# 도스에서 경로 설정(cd C:\Python)
option = sys.argv[1]

 # 수정 모드
if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a') #굳이 경로설정 안해도 C:\Python에 저장됨.
    f.write(memo)
    f.write('\n') #수정 모드니까 줄바꿈을 해서 저장되도록 함.
    f.close()

## 도스 창에서 memo.txt 파일에 정상적으로 쓰였는지를 알기 위해선: type memo.txt를 쓰면됨.

 # 출력 모드
elif option == '-v':
    f = open('memo.txt', 'r')
    memo = f.read()
    f.close()
    print(memo)