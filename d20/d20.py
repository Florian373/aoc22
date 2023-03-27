import numpy as np

with open("d20/input.txt") as f:
    lines=f.readlines()



arr=[]
for l in lines:
    arr.append(int(l.replace("\n","")))


orig=list(range(len(arr)))


for i in range(len(arr)):
    s=np.where(np.array(orig)==i)[0].item()
    
    tmp,_=arr.pop(s),orig.pop(s)
    mov=(s+tmp)%(len(arr))
    if mov==0: mov=len(arr) #wrap around

    arr.insert(mov,tmp)
    orig.insert(mov,i)
    


v0=np.where(np.array(arr)==0)[0].item()
print(arr[(v0+1000)%len(arr)]+arr[(v0+2000)%len(arr)]+arr[(v0+3000)%len(arr)])



##part 2
arr=[]
for l in lines:
    arr.append(int(l.replace("\n",""))*811589153)


orig=list(range(len(arr)))


for _ in range(10):
    for i in range(len(arr)):
        s=np.where(np.array(orig)==i)[0].item()
        
        tmp,_=arr.pop(s),orig.pop(s)
        mov=(s+tmp)%(len(arr))
        if mov==0: mov=len(arr) #wrap around

        arr.insert(mov,tmp)
        orig.insert(mov,i)


v0=np.where(np.array(arr)==0)[0].item()
print(arr[(v0+1000)%len(arr)]+arr[(v0+2000)%len(arr)]+arr[(v0+3000)%len(arr)])
