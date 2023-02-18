with open("d15/input.txt") as f:
    lines=f.readlines()

not_b=set()
srow=2000000
binrow=set()

sensors=[] #format (x,y,mh_dist)
for l in lines:
    l=l.replace("Sensor at x=","").replace(" y=","").replace(": closest beacon is at x=",",")
    x,y,sx,sy = [int(x) for x in l.split(",")]

    mh_dist=abs(sx-x) + abs(sy-y)
    sensors.append([x,y,mh_dist])
    if sy==srow:
        binrow.add((sx,sy))

"""
for s in sensors:
    mh_to = abs(srow - s[1])-s[2]
    i=0
    while mh_to<=0:
        not_b.add((s[0]+i,srow))
        not_b.add((s[0]-i,srow))
        mh_to+=1
        i+=1

#subtract the known beacons
print(len(not_b)-len(binrow))

"""
not_b=[]
for s in sensors:
    mh_to = abs(srow - s[1])-s[2]
    if mh_to<=0:
        not_b.append([s[0]+mh_to,s[0]-mh_to])

count=0
rmax=-2000000000
for nb in sorted(not_b):
    if rmax > nb[0]:
        if rmax <nb[1]:
            count+=nb[1]-rmax
    elif rmax > nb[0] and rmax > nb[1]:
        pass
    else:
        count+=nb[1]-nb[0]
    rmax=max(nb[1],rmax)

        

#subtract the known beacons
print(count-len(binrow)+1)



##part 2
for srow in range(4000000):
    if srow % 1000000==0:
        print(srow)
    not_b=[]
    for s in sensors:
        mh_to = abs(srow - s[1])-s[2]
        if mh_to<=0:
            not_b.append([s[0]+mh_to,s[0]-mh_to])

    count=0
    rmax=-2000000000
    for nb in sorted(not_b):
        if rmax > nb[0]:
            if rmax <nb[1]:
                count+=nb[1]-rmax
        elif rmax > nb[0] and rmax > nb[1]:
            pass
        else:
            count+=1
            if count >=1 and rmax==nb[0]-2:
                print(4000000*(rmax+1)+srow)
                break

        rmax=max(nb[1],rmax)
        if rmax>4000000:
            break