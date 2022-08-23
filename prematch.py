import pandas as pd
from random import choices

class players:
    
    def __init__(self,id,name,pos,club,posx,posy,goals,assist,ycard,rating):
        self.id=id
        self.name=name
        self.pos=pos
        self.club=club
        self.posx=posx
        self.posy=posy
        self.goals=goals
        self.assist=assist
        self.ycard=ycard
        self.rating=rating

t1=pd.read_excel('database.xlsx', sheet_name="LIVERPOOL", header=1)
formationa=[['GK',[],[],1.5,0],
           ['LB',[],[],0,1],['CB',[],[],1,1],['CB',[],[],2,1],['RB',[],[],3,1],
           ['LMF',[],[],0.5,2],['CM',[],[],1.5,2],['RMF',[],[],2.5,2],
           ['LWF',[],[],0.5,3],['CF',[],[],1.5,3],['RWF',[],[],2.5,3]]
for i in range(len(t1)):
    if t1['SUSPENSION'][i]=='NO' and t1['CONDITION'][i]=='FIT':
        k=t1['POSITIONS'][i].split(',')
        for j in range(len(k)):
            for z in range(len(formationa)):
                if formationa[z][0]==k[j]:
                    formationa[z][1].append(t1['NAME'][i])
                    formationa[z][2].append(3-j)
squada=['']   
playera='' 
teama=[]                 
for i in range(len(formationa)):
    formationa[i][2]=tuple(formationa[i][2])
    while playera in squada:
        playera=choices(formationa[i][1],weights=formationa[i][2],k=1)[0]
    print(formationa[i][0],playera)
    teama.append(players(str(i+1)+'a',playera,formationa[i][0],'LIVERPOOL',formationa[i][3],formationa[i][4],0,0,0,0))
    squada.append(playera)
print('subs')
lisa=[formationa[0][1],
     formationa[1][1]+formationa[2][1]+formationa[3][1]+formationa[4][1],
     formationa[1][1]+formationa[2][1]+formationa[3][1]+formationa[4][1],
     formationa[5][1]+formationa[6][1]+formationa[7][1],
     formationa[5][1]+formationa[6][1]+formationa[7][1],
     formationa[8][1]+formationa[9][1]+formationa[10][1],
     formationa[8][1]+formationa[9][1]+formationa[10][1]]

for item in lisa:
    while playera in squada:
        playera=choices(item,k=1)[0]
    squada.append(playera)
    print(playera)
   
    

t2=pd.read_excel('database.xlsx', sheet_name="M.CITY", header=1)
formationb=[['GK',[],[],1.5,7],
           ['LB',[],[],0,6],['CB',[],[],1,6],['CB',[],[],2,6],['RB',[],[],3,6],
           ['LMF',[],[],0.5,5],['CM',[],[],1.5,5],['RMF',[],[],2.5,5],
           ['LWF',[],[],0.5,4],['CF',[],[],1.5,4],['RWF',[],[],2.5,4]]
for i in range(len(t2)):
    if t2['SUSPENSION'][i]=='NO' and t2['COND'][i]=='FIT':
        k=t2['POSITIONS'][i].split(',')
        for j in range(len(k)):
            for z in range(len(formationb)):
                if formationb[z][0]==k[j]:
                    formationb[z][1].append(t2['NAME'][i])
                    formationb[z][2].append(3-j)
squadb=['']   
playerb='' 
teamb=[]                 
for i in range(len(formationb)):
    formationb[i][2]=tuple(formationb[i][2])
    while playerb in squadb:
        playerb=choices(formationb[i][1],weights=formationb[i][2],k=1)[0]
    print(formationb[i][0],playerb)
    teamb.append(players(str(i+1)+'b',playerb,formationb[i][0],'LIVERPOOL',formationb[i][3],formationb[i][4],0,0,0,0))
    squadb.append(playerb)
print('subs')
lisb=[formationb[0][1],
     formationb[1][1]+formationb[2][1]+formationb[3][1]+formationb[4][1],
     formationb[1][1]+formationb[2][1]+formationb[3][1]+formationb[4][1],
     formationb[5][1]+formationb[6][1]+formationb[7][1],
     formationb[5][1]+formationb[6][1]+formationb[7][1],
     formationb[8][1]+formationb[9][1]+formationb[10][1],
     formationb[8][1]+formationb[9][1]+formationb[10][1]]

for item in lisb:
    while playerb in squadb:
        playerb=choices(item,k=1)[0]
    squadb.append(playerb)
    print(playerb)    
             
        
    