f= open('C:\Python\새파일.txt', 'w') #열기
for i in range(1,11):
    data = '%d번째 줄입니다.\n'%i
    f.write(data)                            #쓰기
f.close()