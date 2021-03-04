import random

def random_pop(data): #data는 list를 입력
    num = random.randint(0, len(data)-1) #인덱스 랜덤 반환
    return data.pop(num) #위에서 선택된 랜덤 인덱스를 list 내에서 뽑아 반환(pop함수는 뽑고 리스트 내에서 없어지므로 num 값이 중복이어도 상관없음.)

if __name__ == '__main__':
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data))