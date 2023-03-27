with open('d22/input.txt','r') as f:
    lines=f.readlines()


i=0
arr=[]
while lines[i] != "\n":
    arr.append(lines[i].replace("\n",""))
    i+=1

mv=lines[i+1].replace("\n","")


#possible movements y,x, right,down,left,up
msteps=[(0,1),(1,0),(0,-1),(-1,0)]
mi=0


def next_tile(start,step):
    coord=(start[0]+step[0],start[1]+step[1])
    
    if coord[0]<0 or coord[0]>=len(arr) or coord[1]<0 or coord[1]>=len(arr[coord[0]]) or arr[coord[0]][coord[1]]==" ":
        #wrap around
        wstep=(step[0]*-1,step[1]*-1)
        nc=(coord[0]+wstep[0],coord[1]+wstep[1])
        while nc[0]>=0 and nc[0]<len(arr) and nc[1]>=0 and nc[1]<len(arr[nc[0]]) and arr[nc[0]][nc[1]]!=" ":
            nc=(nc[0]+wstep[0],nc[1]+wstep[1])

        nc=(nc[0]-wstep[0],nc[1]-wstep[1]) #roll back one
        if arr[nc[0]][nc[1]]==".":
            return nc
        else: # tile is blocked 
            return start

    nt=arr[coord[0]][coord[1]]
    
    if nt == ".":
        return coord
    elif nt =="#":
        return start



#find start
i=0
while arr[0][i] in [" ","#"]:
    i+=1
ak_coord=(0,i)

num=0
for c in mv:
    if c.isdigit():
        num=num*10+int(c)
    else:
        for _ in range(num):
            ak_coord=next_tile(ak_coord,msteps[mi])
        if c=="R":
            mi+=1
        else : #c==L
            mi-=1
        mi=mi%len(msteps)
        num=0

for _ in range(num):
    ak_coord=next_tile(ak_coord,msteps[mi])


print(1000*(ak_coord[0]+1)+4*(ak_coord[1]+1)+[0,1,2,3][mi])