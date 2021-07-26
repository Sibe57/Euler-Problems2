from collections import *

def score(hand):
    cards=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    nominal = hand[0] + hand[2] + hand[4] + hand[6] + hand[8]
    nominal_sorted=sorted(nominal)
    a=list()
    a.append(cards.index(hand[0]))
    a.append(cards.index(hand[2]))
    a.append(cards.index(hand[4]))
    a.append(cards.index(hand[6]))
    a.append(cards.index(hand[8]))
    a_sorted=sorted(a)
    if 'A' in hand and 'K' in hand and 'Q' in hand and 'J' in hand and 'T' and hand[1]==hand[3]==hand[5]==hand[7]==hand[9]:
        return [10,0,0,0,0] #flash_royal

    elif a_sorted==[0,1,2,3,12] and hand[1]==hand[3]==hand[5]==hand[7]==hand[9]:
        return [9,-1,0,0,0,0] #Strit Flash from A
    elif a_sorted[0]==a_sorted[1]-1==a_sorted[2]-2==a_sorted[3]-3==a_sorted[4]-4 and hand[1]==hand[3]==hand[5]==hand[7]==hand[9]:
        return [9,a_sorted[-1],0,0,0,0] #Strit Flash

    elif len(set(nominal))==2:
        d = defaultdict(list)
        b=dict(Counter(a))
        for key, value in b.items():
            d[value].append(key)
        if nominal_sorted[0]==nominal_sorted[-2] or nominal_sorted[1]==nominal_sorted[-1]:
            return [8, (d[4][0]),0,0,0] #Four of a Kind

        else:
            return [7, (d[3][0]),(d[2][0]),0,0] #Full House

    elif hand[1]==hand[3]==hand[5]==hand[7]==hand[9]:
        return [6,max(a),0,0,0] #Flash

    elif a_sorted==[0,1,2,3,12]:
        return [5,-1,0,0,0,0] #Strit from A
    elif a_sorted[0]==a_sorted[1]-1==a_sorted[2]-2==a_sorted[3]-3==a_sorted[4]-4:
        return [5,a_sorted[-1],0,0,0,0] #Strit

    elif len(set(nominal))==3:
        d = defaultdict(list)
        b = dict(Counter(a))
        for key, value in b.items():
            d[value].append(key)
        if nominal_sorted[0] == nominal_sorted[2] or nominal_sorted[-1] == nominal_sorted[2] or nominal_sorted[1] == nominal_sorted[2]== nominal_sorted[3]:
            return [4, (d[3][0]),0,0,0] #Triple

        else:
            if max(a_sorted)!=a_sorted[-2]:
                return [3,a_sorted[-2],a_sorted[1],a_sorted[-1],0] #2pair
            else:
                if a_sorted[2]==a_sorted[1]:
                    return [3, a_sorted[-1], a_sorted[1], a_sorted[0],0] #2pair
                else:
                    return [3, a_sorted[-1], a_sorted[0], a_sorted[2],0] #2pair

    elif len(set(nominal))==4:
        d = defaultdict(list)
        b = dict(Counter(a))
        for key, value in b.items():
            d[value].append(key)
        a_sorted.remove(d[2][0])
        a_sorted.remove(d[2][0])
        return [2,(d[2][0]),a_sorted[-1],a_sorted[-2],a_sorted[-3]] #1pair

    elif len(set(nominal))==5:
        return [1,a_sorted[-1],a_sorted[-2],a_sorted[-3],a_sorted[-4],a_sorted[-5]] #high card
counter_win1=0
counter_win2=0
f=open('poker.txt')
for i in f:
    a=i.split(' ')
    hand1=''.join(a[:5])
    hand2=''.join(a[5:])
    hand2=hand2[:-1]
    score_hand1=score(hand1)
    score_hand2=score(hand2)

    if score_hand1[0]>score_hand2[0]:
        counter_win1+=1
    elif score_hand1[0]<score_hand2[0]:
        counter_win2 += 1
        continue
    else:
        if score_hand1[1] > score_hand2[1]:
            counter_win1 += 1
        elif score_hand1[1] < score_hand2[1]:
            counter_win2 += 1
            continue
        else:
            if score_hand1[2] > score_hand2[2]:
                counter_win1 += 1
            elif score_hand1[2] < score_hand2[2]:
                counter_win2 += 1
                continue
            else:
                if score_hand1[3] > score_hand2[3]:
                    counter_win1 += 1
                elif score_hand1[3] < score_hand2[3]:
                    counter_win2 += 1
                    continue
                else:
                    if score_hand1[4] > score_hand2[4]:
                        counter_win1 += 1
                    elif score_hand1[4] < score_hand2[4]:
                        counter_win2 += 1
                        continue
                    else:
                        if score_hand1[5] > score_hand2[5]:
                            counter_win1 += 1
                        elif score_hand1[5] < score_hand2[5]:
                            counter_win2 += 1
                            continue
                        else:
                            print('ERROR')
print(counter_win1)
print(counter_win2)



