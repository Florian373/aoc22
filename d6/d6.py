
for slen in [4,14]:
    with open('input.txt') as f:
        for line in f.readlines():
            for i in range(slen,len(line)):
                if len(set(line[i-slen:i])) == slen:
                    print(i)
                    break

