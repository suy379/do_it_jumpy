def sum0(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print('더할 수 있는 것이 아닙니다.')
        return
    else:
        return sum0(a,b)

if __name__ == '__main__':
    print(safe_sum('a', 1))
    print(safe_sum(1, 4))
    print(sum0(10, 10.4))
