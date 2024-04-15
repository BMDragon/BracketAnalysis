import pandas as pd
import numpy as np

df1 = pd.read_excel('ConfChamps.xlsx')

dct = {}

for k in df1.keys():
    if k == 'Conferences':
        continue
    year = 1985
    for team in df1[k]:
        if team not in dct.keys():
            dct[team] = []
        dct[team].append(year)
        year += 1

def isCC(team, year):
    return team in dct.keys() and year in dct[team]

# [hihgher seed - 1, lower seed - 1, (0-num high seed wins, 1-total games played)]
CCvsCC = np.zeros((16, 16, 2))
ALvsAL = np.zeros((16, 16, 2))

# [CC seed - 1, AL seed - 1, (0-num CC wins, 1-total games played)]
CCvsAL = np.zeros((16, 16, 2))

f = open('gameLog.txt')

year1 = 1985
year2 = 2024
for yr in range(year1, year2+1, 1):
    rounds = 63
    if yr == 2020:
        continue
    if yr == 2021:
        rounds = 62
    assert yr == int(f.readline())
    for x in range(rounds):
        string = f.readline()
        # team1
        split = string.find(' ')
        seed1 = int(string[:split])
        string = string[split+1:]
        split = string.find('-')
        sub = string[:split]
        sub2 = string[split+1:]
        split = sub.find(' ', len(sub)-4)
        team1 = sub[:split]
        score1 = int(sub[split+1:])
        split = sub2.find(' ')
        score2 = int(sub2[:split])
        sub2 = sub2[split+1:]
        split = sub2.find(' ')
        seed2 = int(sub2[:split])
        team2 = sub2[split+1:]

        # print(str(seed1) + ' ' + team1 + ' ' + str(score1) + '-' + str(score2) + ' ' + str(seed2) + ' ' + team2)

        if isCC(team1, yr) and isCC(team2, yr):
            if seed1 <= seed2:
                if score1 > score2:
                    CCvsCC[seed1-1, seed2-1, 0] += 1
                CCvsCC[seed1-1, seed2-1, 1] += 1
            else:
                if score1 < score2:
                    CCvsCC[seed2-1, seed1-1, 0] += 1
                CCvsCC[seed2-1, seed1-1, 1] += 1

        elif not isCC(team1, yr) and not isCC(team2, yr):
            if seed1 <= seed2:
                if score1 > score2:
                    ALvsAL[seed1-1, seed2-1, 0] += 1
                ALvsAL[seed1-1, seed2-1, 1] += 1
            else:
                if score1 < score2:
                    ALvsAL[seed2-1, seed1-1, 0] += 1
                ALvsAL[seed2-1, seed1-1, 1] += 1
        
        elif isCC(team1, yr) and not isCC(team2, yr):
            if score1 > score2:
                CCvsAL[seed1-1, seed2-1, 0] += 1
            CCvsAL[seed1-1, seed2-1, 1] += 1

        elif not isCC(team1, yr) and isCC(team2, yr):
            if score2 > score1:
                CCvsAL[seed2-1, seed1-1, 0] += 1
            CCvsAL[seed2-1, seed1-1, 1] += 1
    
np.save('CCvsCCmatrix', CCvsCC)
np.save('CCvsALmatrix', CCvsAL)
np.save('ALvsALmatrix', ALvsAL)