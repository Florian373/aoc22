score=0

with open('input.txt') as f:
    for line in f.readlines():
        line=line.replace('\n','')
        fh=line[0:len(line)//2]
        sh=line[len(line)//2:]

        first=True
        for c in fh:
            if c in sh and first:
                if ord(c) <= 90:
                    score+= ord(c)-38
                else:
                    score+= ord(c)-96
                first=False

print(score)


score2=0
with open('input.txt') as f:
    while True:
        l1,l2,l3=f.readline(),f.readline(),f.readline()
        if l1=='':
            break

        first=True
        for c in l1:
            if c in l2 and c in l3 and first:
                if ord(c) <= 90:
                    score2+= ord(c)-38
                else:
                    score2+= ord(c)-96
                first=False


print(score2)
