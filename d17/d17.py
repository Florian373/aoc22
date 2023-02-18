from tqdm import tqdm
from copy import deepcopy

class Stone:
    def __init__(self,type,starting_height) -> None:
        if type=="-":
            self.coords=[(0,0),(0,1),(0,2),(0,3)]
        elif type=="+":
            self.coords=[(0,1),(1,0),(1,1),(1,2),(2,1)]
        elif type=="L":
            self.coords=[(0,0),(0,1),(0,2),(1,2),(2,2)]
        elif type=="I":
            self.coords=[(0,0),(1,0),(2,0),(3,0)]
        elif type==".":
            self.coords=[(0,0),(0,1),(1,0),(1,1)]

        self.offset=(starting_height,2)
        self.moved=0
        self.type=type

    def abs_cords(self):
        return [(x[0]+self.offset[0],x[1]+self.offset[1]) for x in self.coords]

    def move(self,direction,blocked):   #return true if stone hit ground
        if direction=="d":
            mod=(-1,0)
        elif direction=="<":
            mod=(0,-1)
        elif direction==">":
            mod=(0,1)

        self.moved+=1

        for c in self.coords:
            prospect=(c[0]+mod[0]+self.offset[0],c[1]+mod[1]+self.offset[1])
            if prospect[1]<0 or prospect[1]>=7 or prospect in blocked:
                return True

        self.offset=(self.offset[0]+mod[0],self.offset[1]+mod[1])



with open("d17/input.txt") as f:
    airflow=f.readlines()[0].replace("\n","")

def get_air_push(airflow):
    while 1:
        for (i,a) in enumerate(airflow):
            yield i,a


stonetypes=["-","+","L","I","."]

def calc_tower(num_stones,blocked=None,allow_skip=True):
    if blocked is None:
        blocked=set([(-1,0),(-1,1),(-1,2),(-1,3),(-1,4),(-1,5),(-1,6)])

    gap=get_air_push(airflow)
    find_repeat,abs_height={},{}
    i,erg=0,0

    while i < num_stones:
        ak_stone=Stone(stonetypes[i%(len(stonetypes))],max(blocked)[0]+4)
        
        if i==402:
            i=i
        while True:
            #one side and one down-step
            index,mv=next(gap)
            if index==0:    #check for repeating sequence (especially relevant for part 2)
                adjust_blocked=tuple(sorted([(x[0]-min(blocked)[0],x[1]-min(blocked)[1]) for x in blocked]))
                check=(ak_stone.type, ak_stone.moved, max(blocked)[0]-min(ak_stone.abs_cords())[0], adjust_blocked)
                if check in find_repeat and allow_skip:
                    print('found at ',i, 'at', find_repeat[check])
                    diff=i-find_repeat[check]
                    #fast forward
                    reps=(num_stones-i)//diff
                    i+=diff*reps
                    erg+=(max(blocked)[0]-abs_height[find_repeat[check]])*reps
                    allow_skip=False
                find_repeat[check]=i
                abs_height[i]=max(blocked)[0]


            ak_stone.move(mv,blocked)

            if ak_stone.move("d",blocked):
                for c in  ak_stone.coords:
                    blocked.add((c[0]+ak_stone.offset[0],c[1]+ak_stone.offset[1]))
                

                cutoff=min([max(list(filter(lambda x: x[1]==i, blocked)))[0] for i in range(7)]) #finds lowest high-coordinate for each stack
                blocked=set(filter(lambda x: x[0]>=cutoff-1, blocked))
                break
        i+=1

    return erg+max(blocked)[0]+1





print(calc_tower(2022,allow_skip=False))
print(calc_tower(2022,allow_skip=True))   #check for correctness


print(calc_tower(1000000000000,allow_skip=True))

