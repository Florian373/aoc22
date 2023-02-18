from copy import deepcopy
with open("d14/input.txt") as f:
    lines=f.readlines()

def move(c,rock):
    for check in [(c[0],c[1]+1),(c[0]-1,c[1]+1),(c[0]+1,c[1]+1)]: #down left right
        if check not in rock:
            return check
    return c    
    



rock=set()
for line in lines:
    line=line.replace("\n","").split(" -> ")
    for i in range(1,len(line)):
        x1,y1=[int(x) for x in line[i-1].split(",")]
        x2,y2=[int(x) for x in line[i].split(",")]

        for x in range(min(x1,x2),max(x1,x2)+1):
            rock.add((x,y1))
        for y in range(min(y1,y2),max(y1,y2)+1):
            rock.add((x1,y))

maxy=max(x[1] for x in rock)
rock2=deepcopy(rock)
done=False
count=0

while not done:
    sand=(500,0)
    count+=1

    while sand != move(sand,rock):
        sand=move(sand,rock)
        if sand[1]>maxy:
            done=True
            break
    rock.add(sand)


print(count-1)


##part 2
rock=rock2
for x in range(
   -10000,
    20000
    ):
    rock.add((x,maxy+2))



done=False
count=0

while not done:
    sand=(500,0)
    count+=1

    while sand != move(sand,rock):
        sand=move(sand,rock)
    rock.add(sand)

    if sand==(500,0):
        done=True


print(count)

