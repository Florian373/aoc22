import itertools
def show_board(elves):
    for y in range(-5,15):
        for x in range(-5,20):
            if (y,x) in elves:
                print('#',end='')
            else:
                print('.',end='')
        print('')

    print('')
    print('')


with open("d23/input.txt") as f:
    lines=f.readlines()


elves=set()
for (i,l) in enumerate(lines):
    for (j,e) in enumerate(l):
        if e=="#":
            elves.add((i,j))

#north, south, west, east
checks=[[(-1,-1),(-1,0),(-1,1)],[(1,-1),(1,0),(1,1)],[(-1,-1),(0,-1),(1,-1)],[(-1,1),(0,1),(1,1)]]


turns=0
pre_elves=set()


while pre_elves != elves: ##p1: for _ in range(10)
    proposed,block=set(),set()
    epro={}# dict of elv, proposed move

    for e in elves:
        if sum([(e[0]+x[0],e[1]+x[1]) in elves for x in set(list(itertools.chain(*checks)))])==0: #checks if none of the squares are set
            epro[e]=e
            continue

        for c in checks:
            if (not (e[0]+c[0][0],e[1]+c[0][1]) in elves) and (not (e[0]+c[1][0],e[1]+c[1][1]) in elves) and  (not (e[0]+c[2][0],e[1]+c[2][1]) in elves):
                prosp=(e[0]+c[1][0],e[1]+c[1][1])
                if prosp in proposed:
                    block.add(prosp)
                else:
                    proposed.add(prosp)
                    epro[e]=prosp
                break
        if e not in epro.keys():
            epro[e]=e

    pre_elves=elves
    elves=set()
    turns+=1
    for e,p in epro.items():
        if p in block:
            elves.add(e)
        else:
            elves.add(p)


    ctmp=checks.pop(0)
    checks.append(ctmp)
#    show_board(elves)


xmin,xmax,ymin,ymax=100,0,100,0
for e in elves:
    if e[0]<ymin:
        ymin=e[0]
    elif e[0]>ymax:
        ymax=e[0]
    
    if e[1]<xmin:
        xmin=e[1]
    elif e[1]>xmax:
        xmax=e[1]

#p1
#print((abs(ymin-ymax)+1)*(abs(xmin-xmax)+1) - len(elves))

print(turns)


