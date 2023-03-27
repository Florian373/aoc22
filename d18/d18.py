import numpy as np

with open("d18/input.txt") as f:
    lines=f.readlines()


coords=[]
for l in lines:
    coords.append(tuple([int(x) for x in l.replace("\n","").split(",")]))

coords=set(sorted(coords))


def get_prospects(c):
    #up down left right before, behind
    return [
        (c[0],c[1]+1,c[2]),
        (c[0],c[1]-1,c[2]),
        (c[0],c[1],c[2]+1),
        (c[0],c[1],c[2]-1),
        (c[0]+1,c[1],c[2]),
        (c[0]-1,c[1],c[2]),
    ]



count=0
for c in coords:
    prospects=get_prospects(c)
    for p in prospects:
        if p not in coords:
            count+=1

print(count)


def lim_break(c,limits):
    if c[0]>limits[0] or c[1]>limits[1] or c[2]>limits[2] or c[0]<-1 or c[1]<-1 or c[2]<-1:
        return True
    else:
        return False


##part 2
from copy import deepcopy
count2=0
nc=np.array(list(coords))
limits=(np.max(nc[:,0])+1,np.max(nc[:,1])+1,np.max(nc[:,2])+1)

ffront=set([(np.max(nc[:,0])+1,np.max(nc[:,1]),np.max(nc[:,2]))])
visited=set()

while len(ffront):
    ffront_tmp=set()
    for c in ffront:
        pros=get_prospects(c)
        for p in pros:
            if lim_break(p,limits) or p in visited:
                continue
            elif p in coords:
                count2+=1
            else:
                ffront_tmp.add(p)    
                
        visited.add(c)
    ffront=deepcopy(ffront_tmp)

print(count2)

