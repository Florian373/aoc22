def order(left,right):
    for l,r in zip(left,right):
        if isinstance(l,list) and isinstance(r,int):
            r=[r]
        if isinstance(r,list) and isinstance(l,int):
            l=[l]
        
        if isinstance(l,list) and isinstance(r,list):
            comp=order(l,r)
            if comp != None:
                return comp
        elif isinstance(l,int) and isinstance(r,int) and l==r:
            continue
        elif isinstance(l,int) and isinstance(r,int) and l<r:
            return True
        elif isinstance(l,int) and isinstance(r,int) and l>r:
            return False

    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False
    else:
        return None        

def ord_i(left,right):
    if order(left,right):
        return 1
    else:
        return -1



with open("d13/input.txt") as f:
    lines=f.readlines()

count,i,pair=0,0,1
while i < len(lines):
    left=eval(lines[i].replace("\n",""))
    right=eval(lines[i+1].replace("\n",""))
    if order(left,right):
        count+=pair
    pair+=1
    i+=3

print(count)


## part 2
packets=[[[6]],[[2]]]
i=0
while i < len(lines):
    left=eval(lines[i].replace("\n",""))
    right=eval(lines[i+1].replace("\n",""))
    packets.extend([left,right])
    i+=3


from functools import cmp_to_key
#packets=sorted(packets, key=cmp_to_key(order))
packets.sort(key=cmp_to_key(ord_i),reverse=True)


print(
    (packets.index([[2]]) +1) * (packets.index([[6]])+1)
)

print(
    (packets.index([[2]]) +1) , (packets.index([[6]])+1)
)
