#총 페이지 수를 출력
import math
def getTotalPage(m, n): #m: 게시물의 총 건수, n: 한 페이지에 보여줄 게시물 수
    if m/n == 1.0:
        return m/n
    else:
        return math.ceil(m/n)

#다음 방법도 가능!
def getTotalPage(m, n):
    if m%n==0:
        return m//n
    else:
        return m//n + 1 #몫+1한 값을 반환(올림과 같은 기능)

print(getTotalPage(5, 10))
print(getTotalPage(10, 10))
print(getTotalPage(25, 10))