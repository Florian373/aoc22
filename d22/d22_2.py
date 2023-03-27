class Side:
    def __init__(self,attaches,sides,id,yx):
        self.attaches=attaches #left, right, up, down
        self.sides=sides #0-5
        self.id=id
        self.yx=yx


    def tb_rot(self,clockwise,exclude=[]):
        if clockwise:
            tmp=self.sides[0]
            self.sides[0]=self.sides[4]
            self.sides[4]=self.sides[2]
            self.sides[2]=self.sides[5]
            self.sides[5]=tmp
        else:
            tmp=self.sides[0]
            self.sides[0]=self.sides[5]
            self.sides[5]=self.sides[2]
            self.sides[2]=self.sides[4]
            self.sides[4]=tmp

        for a in self.attaches:
            if a !=None and not a in exclude:
                a.tb_rot(clockwise,[self])


    def lr_rot(self,clockwise,exclude=[]):
        if clockwise:
            tmp=self.sides[1]
            self.sides[1]=self.sides[4]
            self.sides[4]=self.sides[3]
            self.sides[3]=self.sides[5]
            self.sides[5]=tmp
        else:
            tmp=self.sides[3]
            self.sides[3]=self.sides[4]
            self.sides[4]=self.sides[1]
            self.sides[1]=self.sides[5]
            self.sides[5]=tmp

        for a in self.attaches:
            if a !=None and not a in exclude:
                a.lr_rot(clockwise,[self])


    def attach(self,side,other):
        if self.attaches[side] !=None:
            assert(self.attaches[side]==other)
        self.attaches[side]=other



    def roll_in(self,exclude):
        if self.attaches[0] != None and self.attaches[0] not in exclude:
            self.attaches[0].roll_in(exclude=[self])
            self.attaches[0].tb_rot(True,exclude=[self])
        if self.attaches[1] != None and self.attaches[1] not in exclude:
            self.attaches[1].roll_in(exclude=[self])
            self.attaches[1].lr_rot(True,exclude=[self])
        if self.attaches[2] != None and self.attaches[2] not in exclude:
            self.attaches[2].roll_in(exclude=[self])
            self.attaches[2].tb_rot(False,exclude=[self])
        if self.attaches[3] != None and self.attaches[3] not in exclude:
            self.attaches[3].roll_in(exclude=[self])
            self.attaches[3].lr_rot(False,exclude=[self])


def find_connect_byid2(cid,side):
    for (tcid,c) in enumerate(cube):
        if c.id==cid:
            side_id=tcid
            side_bid=c

    print(side_bid.id)
    for (i,s) in enumerate(side_bid.sides):
        if s==side:
            print('connects to ',i,' side,',cid,'  id: ',cube[i].id,' which translates to: ',cube[i].sides[side_id])




with open('d22/input.txt','r') as f:
    lines=f.readlines()

blocksize=50

i=0
arr=[]
while lines[i] != "\n":
    arr.append(lines[i].replace("\n",""))
    i+=1

mv=lines[i+1].replace("\n","")


sds=[]
si=0
for j in range(0,len(arr),blocksize):
    for i in range(0,len(arr[j]),blocksize):
        if arr[j][i]==" ":
            continue
        sds.append(Side([None,None,None,None],['t','r','b','l','u','d'],si,(j,i)))
        si+=1


def find_side_yx(yx):
    for s in sds:
        if s.yx==yx:
            return s
    return None

for s in sds:
    s.attach(0,find_side_yx((s.yx[0]-blocksize,s.yx[1])))     #top
    s.attach(1,find_side_yx((s.yx[0],s.yx[1]+blocksize)))     #right
    s.attach(2,find_side_yx((s.yx[0]+blocksize,s.yx[1])))     #bottom
    s.attach(3,find_side_yx((s.yx[0],s.yx[1]-blocksize)))     #top




sds[0].roll_in([])


cube_sides=[(0,2),(1,3),(2,0),(3,1),(4,5),(5,4)]
cube=[None,None,None,None,None,None]
for (j,cs) in enumerate(cube_sides):
    for (i,t) in enumerate(sds):
        if t.sides[cs[0]]=="u" and t.sides[cs[1]]=="d":
            print(cs,i)
            cube[j]=sds[i]



def find_connect_byid(cid,side,return_canonical=False):
    for (tcid,c) in enumerate(cube):
        if c.id==cid:
            side_id=tcid
            side_bid=c

    print(side_bid.id)
    for (i,s) in enumerate(side_bid.sides):
        if s==side:
            if return_canonical:
                return cube[i].sides[side_id]
            tr={'b':3,'t':1,'l':0,'r':2} #man
            return cube[i],tr[cube[i].sides[side_id]]



find_connect_byid2(4,'t')
find_connect_byid2(4,'r')
find_connect_byid2(4,'b')
find_connect_byid2(4,'l')





#possible movements y,x, right,bottom,left,top
msteps=[(0,1),(1,0),(0,-1),(-1,0)]
mcanon=['r','b','l','t']
minver=['l','t','r','b']
mi=0


def next_tile(start,step,mi):
    coord=(start[0]+step[0],start[1]+step[1])
    
    if coord[0]<0 or coord[0]>=len(arr) or coord[1]<0 or coord[1]>=len(arr[coord[0]]) or arr[coord[0]][coord[1]]==" ":
        #wrap around

        cur_side=find_side_yx((start[0]//blocksize*blocksize,start[1]//blocksize*blocksize))
        new_side,new_mi=find_connect_byid(cur_side.id,mcanon[mi])

        if mi==0:
            diff2edge=start[0]%blocksize
        elif mi==1:
            diff2edge=blocksize-(start[1]%blocksize)-1
        elif mi==2:
            diff2edge=blocksize-(start[0]%blocksize)-1
        elif mi==3:
            diff2edge=start[1]%blocksize

        if new_mi==0:   #r -->side l
            prosp=new_side.yx[0]+diff2edge,new_side.yx[1]
        elif new_mi==1: #d --> side t
            prosp=new_side.yx[0],new_side.yx[1]+(blocksize-1-diff2edge)
        elif new_mi==2: #l --> side r
            prosp=new_side.yx[0]+(blocksize-1-diff2edge),new_side.yx[1]+blocksize-1
        elif new_mi==3: #u --> side d
            prosp=new_side.yx[0]+blocksize-1,new_side.yx[1]+diff2edge


        if arr[prosp[0]][prosp[1]]==".":
            return prosp,new_mi
        else: # tile is blocked 
            return start,mi

    nt=arr[coord[0]][coord[1]]
    
    if nt == ".":
        return coord,mi
    elif nt =="#":
        return start,mi



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
            ak_coord,mi=next_tile(ak_coord,msteps[mi],mi)
            if(ak_coord==(11,10)):
                mi=mi
        if c=="R":
            mi+=1
        else : #c==L
            mi-=1
        mi=mi%len(msteps)
        num=0

for _ in range(num):
    ak_coord,mi=next_tile(ak_coord,msteps[mi],mi)


print(1000*(ak_coord[0]+1)+4*(ak_coord[1]+1)+[0,1,2,3][mi])