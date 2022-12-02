choice_score={'Rock':1,'Paper':2,'Scissors':3}
beats={'Rock':'Scissors','Paper':'Rock','Scissors':'Paper'}
loses={'Scissors':'Rock','Rock':'Paper','Paper':'Scissors'}
ocode={'A':'Rock','B':'Paper','C':'Scissors'}
mcode={'X':'Rock','Y':'Paper','Z':'Scissors'}

score,score2=0,0
with open('input.txt') as f:
    for line in f.readlines():
        line= line.replace('\n','').split(' ')
        opp, me = line[0],line[1]

        # first part
        if mcode[me]==ocode[opp]:
            score+=3
        elif beats[mcode[me]] == ocode[opp]:
            score+=6
        score+=choice_score[mcode[me]]

        # second part
        if me=='Y':
            score2+=3
            me=ocode[opp]
        elif me=='Z':
            score2+=6
            me=loses[ocode[opp]]
        else:
            me=beats[ocode[opp]]

        score2+=choice_score[me]
        
print(score)
print(score2)