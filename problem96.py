f=open('sudoku.txt')
dataset=([['0','0','3','0','2','0','6','0','0'],['9','0','0','3','0','5','0','0','1'],['0','0','1','8','0','6','4','0','0','0'],
          ['0','0','8','1','0','2','9','0','0'],['7','0','0','0','0','0','0','0','8'],
         ['0','0','6','7','0','8','2','0','0'],['0','0','2','6','0','9','5','0','0'],['8','0','0','2','0','3','0','0','9'],['0','0','5','0','1','0','3','0','0']])
def guester(h_pos,v_pos):
    options=[]
    neighbour_h=dataset[h_pos]
    neighbour_v=(dataset[1][v_pos]+dataset[2][v_pos]+dataset[3][v_pos]+dataset[4][v_pos]+
    dataset[5][v_pos]+dataset[6][v_pos]+dataset[7][v_pos]+dataset[8][v_pos]+dataset[0][v_pos])
    if h_pos<3 and v_pos<3:
        neighbour_cage=(dataset[0][0]+dataset[0][1]+dataset[0][2]+dataset[1][0]+
    dataset[1][1]+dataset[1][2]+dataset[2][0]+dataset[2][1]+dataset[2][2])
    elif h_pos<3 and v_pos<6:
        neighbour_cage = (dataset[0][3] + dataset[0][4] + dataset[0][5] + dataset[1][3] +
                          dataset[1][4] + dataset[1][5] + dataset[2][3] + dataset[2][4] + dataset[2][5])
    elif h_pos<3 and v_pos<9:
        neighbour_cage = (dataset[0][6] + dataset[0][7] + dataset[0][8] + dataset[1][6] +
                          dataset[1][7] + dataset[1][8] + dataset[2][6] + dataset[2][7] + dataset[2][8])
    elif h_pos<6 and v_pos<3:
        neighbour_cage = (dataset[3][0] + dataset[3][0] + dataset[3][0] + dataset[4][1] +
                          dataset[4][1] + dataset[4][1] + dataset[5][2] + dataset[5][2] + dataset[5][2])
    elif h_pos<6 and v_pos<6:
        neighbour_cage = (dataset[3][3] + dataset[3][4] + dataset[3][5] + dataset[4][3] +
                          dataset[4][4] + dataset[4][5] + dataset[5][3] + dataset[5][4] + dataset[5][5])
    elif h_pos<6 and v_pos<9:
        neighbour_cage = (dataset[3][6] + dataset[3][7] + dataset[3][8] + dataset[4][6] +
                          dataset[4][7] + dataset[4][8] + dataset[5][6] + dataset[5][7] + dataset[5][8])
    elif h_pos<9 and v_pos<3:
        neighbour_cage = (dataset[6][0] + dataset[6][0] + dataset[6][0] + dataset[7][1] +
                          dataset[7][1] + dataset[7][1] + dataset[8][2] + dataset[8][2] + dataset[8][2])
    elif h_pos<9 and v_pos<6:
        neighbour_cage = (dataset[6][3] + dataset[6][4] + dataset[6][5] + dataset[7][3] +
                          dataset[7][4] + dataset[7][5] + dataset[8][3] + dataset[8][4] + dataset[8][5])
    elif h_pos<9 and v_pos<9:
        neighbour_cage = (dataset[6][6] + dataset[6][7] + dataset[6][8] + dataset[7][6] +
                          dataset[7][7] + dataset[7][8] + dataset[8][6] + dataset[8][7] + dataset[8][8])

    for i in range(1,10):
        i=str(i)
        if i in neighbour_h or i in neighbour_v or i in neighbour_cage:
            continue
        else:
            options.append(i)
    if options==[]:
        return False
    return options

for h_pos in range (9):
    for v_pos in range(9):
        a=guester(h_pos,v_pos)
        if a==False or len(a)==0:
            break
        if dataset[h_pos][v_pos]=='0':
            dataset[h_pos][v_pos]=a[0]
        else:
            continue

print(dataset)


