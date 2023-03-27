with open("d21/input.txt") as f:
    lines=f.readlines()



mk={}
for l in lines:
    name=l.replace("\n","").split(": ")[0]
    rest=l.replace("\n","").split(": ")[1]
    try:
        rest=int(rest)
    except:
        rest=rest.split(" ")
    mk[name]=rest



def monkey(name,hmn_none=False):
    s=mk[name]
    if name=='humn':
        name=name
    if name=='humn' and hmn_none:
        return None

    if isinstance(s,int): return s

    m1,m2=monkey(s[0],hmn_none=hmn_none),monkey(s[2],hmn_none=hmn_none)
    if m1==None or m2==None: return None

    if s[1]=="+":
        return m1+m2
    elif s[1]=="-":
        return m1-m2
    elif s[1]=="*":
        return m1*m2
    elif s[1]=="/":
        return m1/m2


def monkey_search(name,target):
    if name=="humn":
        return target
    
    if int(target)!=target:
        target=target

    s=mk[name]
    m1,m2=monkey(s[0],True),monkey(s[2],True)

    nsearch=None
    if m1==None:
        nsearch,cal=s[0],m2
    if m2==None:
        nsearch,cal=s[2],m1
    if nsearch==None:
        nsearch=nsearch


    if name=='root':
        return monkey_search(nsearch,cal)

    if s[1]=="+":
        return monkey_search(nsearch,target-cal)
    elif s[1]=="*":
        return monkey_search(nsearch,target/cal)
    
    elif s[1]=="-":
        if m1==None:
            return monkey_search(nsearch,target+cal)
        elif m2==None:
            return monkey_search(nsearch,cal-target)

    
    elif s[1]=="/":
        if m1==None:
            return monkey_search(nsearch,target*cal)
        elif m2==None:
            return monkey_search(nsearch,target/cal)




print(monkey('root'))
print(monkey_search('root',monkey('root')))