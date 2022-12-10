cycles=[]
curval=1

with open('d10/input.txt') as f:
    for line in f.readlines():
        lsp=line.replace("\n","").split(" ")
        if lsp[0] == "noop":
            cycles.append(curval)
        elif lsp[0] == "addx":
            cycles.extend([curval,curval])
            curval += int(lsp[1])

#20th, 60th, 100th, 140th, 180th, and 220th
signal=0
for i in [20,60,100,140,180,220]:
    signal+= i*cycles[i-1]
print(signal)


print(cycles)
print(len(cycles))

for j in range(6):
    for i in range(40):
        if abs(cycles[j*40 + i]-i)<=1:
            print("#",end="")
        else:
            print(".",end="")

    print("")

