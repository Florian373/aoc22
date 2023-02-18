import numpy as np
from copy import deepcopy
names={}
pressures=[]
connects=[]
from itertools import product

with open("d16/input.txt") as f:
    lines=f.readlines()

for i,l in enumerate(lines):
    names[l[6:8]]=i
    pressures.append(int(l.split(" ")[4].replace("rate=","").replace(";","")))
    connects.append(l.replace(",","").replace("\n","").split(" ")[9:])
    

relevant=["AA"]
for n,i in names.items():
    if pressures[i]>0:
        relevant.append(n)

dists=deepcopy(connects)

for r in relevant:
    i=names[r]
    ffront,ftmp,visited=set(connects[i]),set(),set()
    d=1
    dists[i]=[]
    
    while len(ffront)>0:
        for f in ffront:
            if f==r:
                continue

            if f in relevant:
                dists[i].append([f,d])

            for neighbor in connects[names[f]]:
                ftmp.add(neighbor)

            visited.add(f)

        ffront=ftmp-visited
        ftmp.clear()
        d+=1



def search(turns,cur,open,accumulated):

    prospects=[]
    for n,d in dists[names[cur]]:
        if n in open:
            continue
        prospects.append([pressures[names[n]],n,d])
    prospects=sorted(prospects)

    if turns>30 or len(prospects)==0:
        return accumulated

    scores=[0]
    
    for p in prospects:
        pgain=p[0]*max(0,30-turns-p[2]-1)
        op=deepcopy(open)
        op.append(p[1])
        scores.append(search(turns+p[2]+1,p[1],op,accumulated+pgain))

    return max(scores)




def search2(turns,cur,open,accumulated,ubound=0,progress=False):

    prospects=[]
    for n,d in dists[names[cur[0]]]:
        if n in open or d+turns[0]>26:
            continue
        prospects.append([pressures[names[n]],n,d])
    
    prospects2=[]
    for n,d in dists[names[cur[1]]]:
        if n in open  or d+turns[1]>26:
            continue
        prospects2.append([pressures[names[n]],n,d])
    
    prospects2=sorted(prospects2,reverse=True)
    prospects=sorted(prospects,reverse=True)


    #bound
    bound=accumulated
    bturns,bpros=deepcopy(turns),deepcopy(prospects)
    while min(bturns)<=26 and len(bpros)>0:
        bound+=bpros[0][0]*max(0,26-min(bturns)-1-1)
        bturns[np.argmin(bturns)]+=2

    if bound < ubound:
        return 0



    if (turns[0]>26 and turns[1]>26) or (len(prospects)==0 and len(prospects2)==0):
        return accumulated

    scores=[0]
    if len(prospects)==0:
        prospects.append([0,None,0])
    elif len(prospects2)==0:
        prospects2.append([0,None,0])
    else:
        i=0
        for p0,p1 in product(prospects,prospects2):
            if p0[1]==p1[1]:
                continue
            pgain=p0[0]*max(0,26-turns[0]-p0[2]-1) + p1[0]*max(0,26-turns[1]-p1[2]-1)
            op=deepcopy(open)
            op.append(p0[1])
            op.append(p1[1])
            tu=deepcopy(turns)
            tu[0]+=p0[2]+1
            tu[1]+=p1[2]+1

            scores.append(search2(tu,[p0[1],p1[1]],op,accumulated+pgain,ubound=max(scores)))

            if progress:
                print(i/(len(prospects)*len(prospects2)))
                i+=1

    return max(scores)



print(search2([0,0],["AA","AA"],["AA"],0,progress=True))













#part 1
#print(search(0,"AA",["AA"],0))