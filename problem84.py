from random import randint
def cc():
    cards=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,'GO','JAIL')
    card=cards[randint(0,15)]
    return card
def choice():
    cards=(0,0,0,0,0,0,'GO','JAIL','C1','E3','H2','R1','NEXTR','NEXTR','NEXTU','BACK3')
    card = cards[randint(0, 15)]
    return card






def table(cube1,cube2,last_pos='GO'):
    cage=('GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3','JAIL',
       'C1','U1','C2','C3','R2','D1','CC2','D2','D3','FP',
       'E1','CH2','E2','E3','R3','F1','F2','U2','F3','G2J',
       'G1','G2','CC3','G3','R4','CH3','H1','T2','H2')
    if cube1+cube2>=0:
        move=(cage.index(last_pos)+cube1+cube2)%40
        intermediate_pos=cage[move]
        current_pos=cage[move]
    else:
        move=(cage.index(last_pos)+cube1+cube2)
        intermediate_pos=cage[move]
        current_pos = cage[move]
    if intermediate_pos=='G2J':
        current_pos='JAIL'
        return current_pos
    if intermediate_pos=='CC1' or intermediate_pos=='CC2' or intermediate_pos=='CC3':
        procCC=(cc())
        if procCC==0:
            return current_pos
        else:
            current_pos=procCC
            return current_pos

    if intermediate_pos=='CH1' or intermediate_pos=='CH2' or intermediate_pos=='CH3':
        procCH=choice()
        if procCH=='NEXTR':
            if intermediate_pos=='CH1':
                current_pos='R2'
                return current_pos
            elif intermediate_pos=='CH2':
                current_pos ='R3'
                return current_pos
            else:
                current_pos='R1'
                return current_pos
        elif procCH=='NEXTU':
            if intermediate_pos=='CH1':
                current_pos='U1'
                return current_pos
            elif intermediate_pos=='CH2':
                current_pos='U2'
                return current_pos
            else:
                current_pos='U1'
                return current_pos
        elif procCH=="BACK3":
            current_pos=table(-3,0,current_pos)
            return current_pos
        elif procCH==0:
            return current_pos
        else:
            return procCH

    else:
        return current_pos


def throw_cube():
    cube=randint(1,4)
    return cube

i=0
mytable=table(0,0)
all_pos=[]
counter_double=0
while i<20000:
    cube1=throw_cube()
    cube2=throw_cube()
    if cube1==cube2:
        counter_double+=1
        if counter_double==3:
            mytable='JAIL'
            print('на зону')
            counter_double=0
            continue
    else:
        counter_double=0
    my_pos=table(cube1,cube2,mytable)
    all_pos.append(my_pos)
    mytable=my_pos
    i+=1
my_dict={i:all_pos.count(i) for i in all_pos}
sorted_values = sorted(my_dict.values()) # Sort the values
sorted_dict = {}
for i in sorted_values:
    for k in my_dict.keys():
        if my_dict[k] == i:
            sorted_dict[k] = my_dict[k]
            break

print(sorted_dict)


