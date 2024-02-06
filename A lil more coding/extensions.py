cases = int(input())

files = []

for i in range(cases):
    files.append(input())

extends = [["txt",0]]
for j in files:
    dot = False
    ext = ""
    for h in j:
        if dot:
            ext += h
        if h == '.':
            dot = True
    for o in range(len(extends)):
        if ext in extends[o]:
            extends[o][1] += 1
            break
        if o == len(extends)-1:
            extends.append([ext,1])
if extends[0] == extends["txt",0]:
    extends.remove(["txt",0])
for e in extends:
    print(e[0],e[1])