with open("d24/input.txt") as f:
    lines=f.readlines()


up,down,left,right=set(),set(),set(),set()
for (y,l) in enumerate(lines):
    for (x,a) in enumerate(l):
        if a=="<":
            left.add((y,x))
        elif a==">":
            right.add((y,x))
        elif a=="^":
            up.add((y,x))
        elif a=="v":
            down.add((y,x))

start=(0,1)
ymin=0; ymax=len(lines)-1; xmin=0; xmax=len(l)-1
end=(ymax,xmax-1)

def valid(coord,player=False):
    if player and (coord==start or coord==end):
        return True
    if coord[0]>ymin and coord[0]<ymax and coord[1]>xmin and coord[1]<xmax:
        return True
    else:
        return False
    

def move(coord,dir):
    prosp=(coord[0]+dir[0],coord[1]+dir[1])
    if valid(prosp): 
        return prosp
    if prosp[0] == ymin:
        prosp=(ymax-1,prosp[1])
    elif prosp[0] == ymax:
        prosp=(ymin+1,prosp[1])
    elif prosp[1] == xmin:
        prosp=(prosp[0],xmax-1)
    elif prosp[1] == xmax:
        prosp=(prosp[0],xmin+1)
    return prosp

def walk(player_inits,state,goals):
    turns=0
    for i in range(len(goals)):
        goal,player=goals[i],player_inits[i]
        while not goal in player:
            next_state=[
                set([move(x,[-1,0]) for x in state[0]]),
                set([move(x,[1,0]) for x in state[1]]),
                set([move(x,[0,1]) for x in state[2]]),
                set([move(x,[0,-1]) for x in state[3]])
            ]
            t=set([move(x,[-1,0]) for x in state[0]])
            next_player=set()
            for p in player:
                prospects=[
                    p,
                    (p[0]-1,p[1]),
                    (p[0]+1,p[1]),
                    (p[0],p[1]-1),
                    (p[0],p[1]+1),
                ]

                for c in prospects:
                    if valid(c,player=True) and not c in next_state[0].union(next_state[1],next_state[2],next_state[3]):
                        next_player.add(c)

            player=next_player
            state=next_state
            turns+=1
    return turns

player=set([start])
state=[up,down,right,left]

print(walk([set([start]),set([end]),set([start])],state,[end,start,end]))