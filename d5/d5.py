ship=["","","","","","","","",""]
ship2=["","","","","","","","",""]


with open('input.txt') as f:
    for line in f.readlines():
        if line.startswith(" 1 "):
            break

        for i in range(9):
            c=line[1+i*4]

            if c!=" ":
                ship[i] = ship[i] + c
                ship2[i] = ship2[i] + c




with open('input.txt') as f:
    for line in f.readlines():
        if not line.startswith("move"):
            continue

        line=line.replace("move ","").replace(" from ",",").replace(" to ",",")
        count,fr,to = [int(x) for x in line.split(",")]

        mov=ship[fr-1][0:count]
        ship[fr-1]=ship[fr-1][count:]
        ship[to-1]=mov[::-1]+ship[to-1]


        mov2=ship2[fr-1][0:count]
        ship2[fr-1]=ship2[fr-1][count:]
        ship2[to-1]=mov2+ship2[to-1]


for i in range(9):
    print(ship[i][0:1],end="")

print("")    
for i in range(9):
    print(ship2[i][0:1],end="")