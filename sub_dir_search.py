import os

## dirname 디렉토리 내의 파일들을 경로를 붙여 모두 반환
# def search(dirname):
#     filenames = os.listdir(dirname) #dirname 디렉토리 내의 파일들 반환
#     for filename in filenames:
#         full_filename = os.path.join(dirname, filename) #디렉토리+파일명을 붙여서 출력
#         print(full_filename)

## dirname 디렉토리 내의 파일 중, .py 확장자만 출력
def search(dirname):
    filenames = os.listdir(dirname) #dirname 디렉토리 내의 파일들 반환 ---> 파일뿐 아니라, 폴더(서브 디렉토리)도 같이 출력됨!!
    for filename in filenames:
        full_filename = os.path.join(dirname, filename) #디렉토리+파일명을 붙여서 출력
        ext = os.path.splitext(full_filename)[-1] #확장자를 기준으로 full_filename을 잘라줌
        if ext == '.py': #But, 이렇게 하면 폴더 내 .py가 있는 경우는 출력X
            print(full_filename)

## 그런데 주의점. 앞서 os.listdir(dirname)을 출력할 때 폴더도 같이 나오는데, 이 폴더 안에 .py 확장자가 있을 수 있다!
# 얘도 출력하고자 할 땐?
def search2(dirname):
    try:
        filenames = os.listdir(dirname) #파일, 폴더 함꼐 출력.
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename): #file_filename이 폴더인 경우!
                search2(full_filename)
            else: #file_filename이 파일인 경우
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py': #이땐 확장자가 .py인 것만 출력
                    print(full_filename)
    except PermissionError:
        pass #PermissionError가 뜨면 그냥 출력x


#search('C:\Python')
search2('C:\Python')
