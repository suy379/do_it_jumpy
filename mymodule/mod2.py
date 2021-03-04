pi=3.141592

class Math:
    def solv(self,r): #반지름 계산
        return pi*(r**2)

def sum0(a,b):
    return a+b

if __name__ == '__main__':
    print(pi)
    a=Math() #인스턴스
    print(a.solv(2))
    print(sum0(pi, 4.4))
