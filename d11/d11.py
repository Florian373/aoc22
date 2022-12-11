class Monkey:
    def __init__(self,has,mod,cal,mls,thr) -> None:
        self.has_items=has
        self.modulo=mod
        self.calc=cal
        self.monkeylist=mls
        self.throws=thr
        self.insp_count=0


    def turn(self,manage_op="new//3"):
        for (i,old) in enumerate(self.has_items):
            new=eval(self.calc)
            new=eval(manage_op)
            check=int( new % self.modulo == 0)
            
            
            self.monkeylist[self.throws[1-check]].has_items.append(new)
            self.insp_count+=1
        self.has_items=[]
        
def read_inp():
    mlist=[]
    with open('d11/input.txt') as f:
        lines=f.readlines()
        i=0
        while i < len(lines):
            # Monkey N
            items=lines[i+1].replace("Starting items:","").replace("\n","").replace(" ","")
            items=[int(x) for x in items.split(",")]
        
            op=lines[i+2].replace("Operation: new = ","").replace("\n","").replace(" ","")
            
            m=int(lines[i+3].replace("Test: divisible by","").replace("\n",""))

            t1=int(lines[i+4].replace("If true: throw to monkey","").replace("\n",""))
            t2=int(lines[i+5].replace("If false: throw to monkey","").replace("\n",""))

            mlist.append(Monkey(items,m,op,mlist,[t1,t2]))
            i+=7
    return mlist

mlist=read_inp()
for _ in range(20):
    for monkey in mlist:
        monkey.turn()

ilist=sorted([x.insp_count for x in mlist])
print(ilist[-1]*ilist[-2])


##part 2
mlist=read_inp()
manage_mod=1
for x in mlist:
    manage_mod*=x.modulo


for _ in range(10000):
    for monkey in mlist:
        monkey.turn(manage_op="new%"+str(manage_mod))

ilist=sorted([x.insp_count for x in mlist])
print(ilist[-1]*ilist[-2])