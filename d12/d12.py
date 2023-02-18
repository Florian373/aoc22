from copy import deepcopy
MAX_Y,MAX_X=158,40
MAX_D=1

class Coord:
    def __init__(self,x,y) -> None:
        self.x, self.y = x, y

    def possible(self):
        return (self.x >= 0 and 
                self.y >= 0 and 
                self.x <= MAX_X and
                self.y <= MAX_Y
                )

    def neigh(self,direction):
        if direction == "up":
            return Coord(self.x-1,self.y)
        if direction == "down":
            return Coord(self.x+1,self.y)
        if direction == "left":
            return Coord(self.x,self.y-1)
        if direction == "right":
            return Coord(self.x,self.y+1)

    def possible_directions(self,field,visited,inverse=False):
        possible=[]
        for d in ["up","down","left","right"]:
            prospect=self.neigh(d)
            if (prospect.possible() and 
                isinstance(visited[prospect.x][prospect.y],str) and 
                (ord(field[prospect.x][prospect.y])-ord(field[self.x][self.y]) <= MAX_D or inverse) and
                (ord(field[self.x][self.y])-ord(field[prospect.x][prospect.y]) <= MAX_D or not inverse)
                ):
                possible.append(prospect)
        return possible



field=[]
dist=[]
start,end=Coord(0,0),Coord(0,0)
with open('d12/input.txt') as f:
    lines=f.readlines()
    for (i,l) in enumerate(lines):
        if "S" in l:
            start=Coord(i,l.find("S"))
            l=l.replace("S","a")
        if "E" in l:
            end=Coord(i,l.find("E"))
            l=l.replace("E","z")
        field.append(list(l.replace("\n","")))


##part 1
#flood fill
sfront=[start]
steps=1
sfield=deepcopy(field)
sfield[start.x][start.y]=0

while len(sfront)>0:
    nfront=[]
    for c in sfront:
        for nc in c.possible_directions(field,sfield):
            sfield[nc.x][nc.y]=steps
            nfront.append(nc)
    sfront=nfront
    steps+=1

print(sfield[end.x][end.y])



##part 2


start=end
sfront=[start]
steps=1
sfield=deepcopy(field)
sfield[start.x][start.y]=0

while len(sfront)>0:
    nfront=[]
    for c in sfront:
        for nc in c.possible_directions(field,sfield,inverse=True):
            sfield[nc.x][nc.y]=steps
            nfront.append(nc)
    sfront=nfront
    steps+=1

prosps=[]
for l1,l2 in zip(field,sfield):
    for c,s in zip(l1,l2):
        if c == "a" and isinstance(s,int):
            prosps.append(s)

print(min(prosps))

