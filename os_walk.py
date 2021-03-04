#os.walk를 이용하면 시작 디렉터리부터 하위 디렉터리까지 차례대로 방문한다.
import os

for (path, dir, files) in os.walk('C:\Python'):
    #path: 경로명, dir:디렉토리명, files:파일명(ex. path:C:\Python\mymodule, dir:mymodule, file:mod2.py)
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            #print(dir)
            print("%s\%s"% (path, filename))
