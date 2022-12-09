from math import ceil

class Point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

    def touches(self, other):
        xdiff=abs(self.x - other.x)
        ydiff=abs(self.y - other.y)

        return max([xdiff,ydiff])==1

    def follow(self, other):
        if self.touches(other):
            return
        
        xdiff=other.x - self.x
        ydiff=other.y - self.y
        if abs(xdiff) == 2 :
            self.x+= xdiff/2
            if abs(ydiff) == 1:
                self.y+=ydiff
            elif abs(ydiff) == 2:
                self.y+=ydiff/2

        elif abs(ydiff)==2:
            self.y+= ydiff/2
            if abs(xdiff) == 1:
                self.x+=xdiff
            if abs(xdiff) == 2:
                self.x+=xdiff/2

    def move(self,direction):
        if direction == "U":
            self.x-=1
        elif direction == "D":
            self.x+=1
        elif direction == "R":
            self.y+=1
        elif direction == "L":
            self.y-=1
        

visited=set()
visited.add((0,0))
head,tail=Point(0,0), Point(0,0)
with open('d9/input.txt') as f:
    for line in f.readlines():
        d,num = line.replace("\n","").split(" ")
        
        for _ in range(int(num)):
            head.move(d)
            tail.follow(head)
            visited.add((tail.x,tail.y))

print(len(visited))


##part 2
visited=set()
visited.add((0,0))
head,tail=Point(0,0), [Point(0,0)  for x in range(9)]
with open('d9/input.txt') as f:
    for line in f.readlines():
        d,num = line.replace("\n","").split(" ")
        
        for _ in range(int(num)):
            head.move(d)
            tail[0].follow(head)
            for i in range(1,9):
                tail[i].follow(tail[i-1])
            visited.add((tail[-1].x,tail[-1].y))

print(len(visited))