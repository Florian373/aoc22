count,count2=0,0
with open('input.txt') as f:
    for line in f.readlines():
        f1,f2,s1,s2=[int(x) for x in line.replace(",","-").split("-")]
        if (f1>=s1 and f2<=s2) or (s1>=f1 and s2<=f2):
            count+=1

        if (f1>=s1 and f1<=s2) or (f2>=s1 and f2 <=s2) or (s1>=f1 and s1<=f2) or (s2>=f1 and s2 <=f2):
            count2+=1

print(count,count2)