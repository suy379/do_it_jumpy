## 3과 5의 배수 합하기
## 1000 미만의 자연수(1~999)를 입력받고, 이 중 3의 배수와 5의 배수의 총합을 출력.

# 접근1. 1000 미만의 자연수 구하기
n = 1
while n <1000:
    print(n)
    n +=1

 # OR
for i in range(1,1000):
    print(i)

# 접근2. 3과 5의 배수를 구하기
# 2-1. 1000 미만의 3의 배수 구하기: 3으로 나눠서 나누어떨어지를 보면 된다!
result = []
for i in range(1,1000):
    if i % 3 == 0:
        result.append(i)
print(result)

# 2-2. 1000 미만의 5의 배수 구하기: 마찬가지로 5로 나눠서 나누어떨어지는지?
result = []
for i in range(1,1000):
    if i % 5 == 0:
        result.append(i)
print(result)

# 2-3. 1000 미만의 3과 5의 배수 구하기
result = []
for i in range(1,1000):
    if i %3 == 0 or i%5 == 0:
        result.append(i)
print(result)

# 최종: 1000 미만의 3과 5의 배수들의 총합 구하기
result =0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        result += i
print(result)