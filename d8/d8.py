forest,visible=[],[]

with open('input.txt') as f:
    for line in f.readlines():
        row=[]
        for c in line.replace("\n",""):
            row.append(int(c))
        forest.append(row)

for x in range(len(forest)):
    for iteration in [range(len(forest[x])), reversed(range(len(forest[x])))]:
        
        m=-1
        for y in iteration:
            if forest[x][y] > m:
                m=forest[x][y]
                visible.append((x,y))
            

for y in range(len(forest[0])):
    for iteration in [range(len(forest)),reversed(range(len(forest)))]:
        m=-1
        for x in iteration:
            if forest[x][y] > m:
                m=forest[x][y]
                visible.append((x,y))

print(len(set(visible)))

views=[]
for x in range(1,len(forest)-1):
    for y in range(1,len(forest[0])-1):
        # x,y tree
        xr,tv=x,0
        while xr > 0 :
            xr-=1
            if forest[xr][y] < forest[x][y]:
                tv+=1
            elif forest[xr][y]>=forest[x][y]:
                tv+=1
                break
            else:
                break
        
        xr,bv=x,0
        while xr < len(forest)-1:
            xr+=1
            if forest[xr][y] < forest[x][y]:
                bv+=1
            elif forest[xr][y]>=forest[x][y]:
                bv+=1
                break
            else:
                break
        
        
        yr,lv=y,0
        while yr > 0 :
            yr-=1
            if forest[x][yr] < forest[x][y]:
                lv+=1
            elif forest[x][yr]>=forest[x][y]:
                lv+=1
                break
            else:
                break


        yr,rv=y,0
        while yr < len(forest[0]) -1:
            yr+=1
            if forest[x][yr] < forest[x][y]:
                rv+=1
            elif forest[x][yr]>=forest[x][y]:
                rv+=1
                break
            else:
                break

        treeview=rv*lv*tv*bv
        views.append(treeview)

print(max(views))