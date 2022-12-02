elvcal,elv=[0],0
with open('input.txt') as f:
    for line in f.readlines():
        if line == '\n':
            elv+=1
            elvcal.append(0)
        else:
            elvcal[elv]+= int(line)

print(max(elvcal)) # for first puzzle
print(sum(sorted(elvcal,reverse=True)[0:3])) #second puzzle
