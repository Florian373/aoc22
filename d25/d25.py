def dec_to_sn(num):
    erg,factor,carry="",1,0
    if num==0:
        return "0"
    
    while (num+carry):
        rest=(num%(factor*5))//factor +carry
        if rest <=2:
            erg=str(rest)+erg
            carry=0
        elif rest==3:
            erg="="+erg
            carry=1
        elif rest==4:
            erg="-"+erg
            carry=1
        elif rest==5: #4+carry
            erg="0"+erg
            carry=1
        num-=(num%(factor*5))
        factor*=5

    return erg


def sn_to_dec(num):
    factor,erg=1,0
    for c in reversed(num):
        if c=="=":
            erg-=(2*factor)
        elif c=="-":
            erg-=(factor)
        elif int(c)<=2:
            erg+=factor*int(c)
        factor*=5
    return erg




for i in range(102):
    assert(sn_to_dec(dec_to_sn(i))==i)

with open("d25/input.txt") as f:
    lines=f.readlines()

erg=0
for l in lines:
    erg+=sn_to_dec(l.replace("\n",""))

print(dec_to_sn(erg))

