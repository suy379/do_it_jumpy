import sys
## 모듈에서 실행 시 in_put, out_put에 넣는 인자로는 "~.txt"로 되어있어야 함!
#ex. 도스>python tabto4.py src.txt dst.txt
in_put = sys.argv[1]
out_put = sys.argv[2]

#tab으로 된 파일을 읽어들여 스페이스 4개로 변경
f = open(in_put, 'r')
tab_content = f.read()
f.close()

space_content = tab_content.replace('\t',' '*4)
print(space_content)

#out_put 파일에 저장
f = open(out_put, 'w')
f.write(space_content)
f.close()