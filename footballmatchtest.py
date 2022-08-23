from random import choice,choices
from time import sleep
from math import sqrt
import pandas as pd
import openpyxl as xl


class players:
    
    def __init__(self,id,name,pos,club,posx,posy,goals,saves,assist,card,injury,rating):
        self.id=id
        self.name=name
        self.pos=pos
        self.club=club
        self.posx=posx
        self.posy=posy
        self.goals=goals
        self.saves=saves
        self.assist=assist
        self.card=card
        self.injury=injury
        self.rating=rating
        
t1=pd.read_excel('database.xlsx', sheet_name="LIVERPOOL", header=1)
formationa=[['GK',[],[],1.5,0],
           ['LB',[],[],0,1],['CB',[],[],1,1],['CB',[],[],2,1],['RB',[],[],3,1],
           ['LMF',[],[],0.5,2],['CM',[],[],1.5,2],['RMF',[],[],2.5,2],
           ['LWF',[],[],0.5,3],['CF',[],[],1.5,3],['RWF',[],[],2.5,3]]
for i in range(len(t1)):
    if t1['SUSPENSION'][i]=='NO' and t1['CONDITION'][i]==0:
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
    teama.append(players(str(i+1)+'a',playera,formationa[i][0],'LIVERPOOL',formationa[i][3],formationa[i][4],0,0,0,0,0,0))
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
    if t2['SUSPENSION'][i]=='NO' and t2['COND'][i]==0:
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
    teamb.append(players(str(i+1)+'b',playerb,formationb[i][0],'M.CITY',formationb[i][3],formationb[i][4],0,0,0,0,0,0))
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
                     
        
smaxa=0
smaxb=0
carda=[]
cardb=[]
def dribble(key,at,duration):
    chx=choices([0,1,-1],weights=(4,2,2),k=1)[0]
    if key==1:
        dire=(4,2,1)
    else:
        dire=(1,2,4)
    chy=choices([1,0,-1],weights=dire,k=1)[0]
    if at.posx+chx>3 or at.posx+chx<0 or at.posy+chy>7 or at.posy+chy<0:
        dribble(key,at,duration)
    elif chx==0 and chy==0:
        dribble(key,at,duration)
    else:
        at.posx+=chx
        at.posy+=chy
        print(at.name,' moved to ',at.posx,at.posy)
        cchance=choices([0,1],weights=(15,1),k=1)[0]
        ichance=choices([0,1],weights=(25,1),k=1)[0]
        card='no card'
        if cchance==1:
            card=choices(['no card','yellow','red'],weights=(16,3,1),k=1)[0]
        injury=0
        if ichance==1:
            injury=choices([0,1,3,7,15],weights=(90,15,8,5,1),k=1)[0]
        if injury!=0:
            at.injury=injury
            print(at.name,' injured for ',injury,' days')
            
            if at.id[-1]=='a':
                at.id=str(len(carda)+1)+'ia'
                index=teama.index(at)
                
                if input('do you want to substitute? (Y or N)')=='Y':
                    subs()
                if globals()['smaxa']==1:
                    carda.append(at)
                    teama.remove(at)
                    squada.remove(at.name)
                at=teama[index]
            elif at.id[-1]=='b':
                at.id=str(len(cardb)+1)+'ib'
                index=teamb.index(at)
                
                if input('do you want to substitute? (Y or N)')=='Y':
                    subs()
                if globals()['smaxb']==1:
                    cardb.append(at)
                    teamb.remove(at)
                    squadb.remove(at.name)
                at=teama[index]
                
            
        if card=='red':
            de=deftrack(key,at)
            print(de.name,' got RED card')
            de.card=3
            de.rating-=10
            if de.id[-1]=='a':
                de.id=str(len(carda)+1)+'ca'
                carda.append(de)
                teama.remove(de)
                squada.remove(de.name)
            elif de.id[-1]=='b':
                de.id=str(len(cardb)+1)+'cb'
                cardb.append(de)
                teamb.remove(de)
                squadb.remove(de.name)    
            if input('do you want to substitute? (Y or N)')=='Y':
                subs() 
        elif card=='yellow':
            de=deftrack(key,at)
            de.rating-=3
            if de.card==0:
                de.card=1
                print(de.name,' got YELLOW card')
            elif de.card==1:
                de.card=2
                print(de.name,' got another YELLOW & suspended')
                if de.id[-1]=='a':
                    de.id=str(len(carda)+1)+'ca'
                    carda.append(de)
                    teama.remove(de)
                    squada.remove(de.name)
                elif de.id[-1]=='b':
                    de.id=str(len(cardb)+1)+'cb'
                    cardb.append(de)
                    teamb.remove(de)
                    squadb.remove(de.name)
            if input('do you want to substitute? (Y or N)')=='Y':
                subs()             
        move(key,at,duration)

def deftrack(key,at):
    dislis=[]
    if key==1:
        for i in teamb:
            dislis.append([i,sqrt(pow((i.posx-at.posx),2)+pow((i.posy-at.posy),2))])
        dislis.sort(key=lambda dislis:dislis[1])
        de=dislis[0][0]
        
    elif key==2:
        for i in teama:
            dislis.append([i,sqrt(pow((i.posx-at.posx),2)+pow((i.posy-at.posy),2))])
        dislis.sort(key=lambda dislis:dislis[1])
        de=dislis[0][0]
    return de        
        
        
def discal(at,chbx,chby):
    dislist=[]
    if globals()['ft']!=1 or key==1:
        for i in teama:
            dislist.append([i,sqrt(pow((i.posx-chbx),2)+pow((i.posy-chby),2))])
    if globals()['ft']!=1 or key==2:    
        for i in teamb:
            dislist.append([i,sqrt(pow((i.posx-chbx),2)+pow((i.posy-chby),2))])    
    dislist.sort(key=lambda dislist:dislist[1])    
    k=dislist[0][0]
    if k.id==at.id:
        k=dislist[1][0]    
    return k
        

def passkick(at): 
    x=at.posx
    y=at.posy
    chbx=choices([x+1,x-1,x,x+2,x-2,x+3,x-3],weights=(3,3,3,2,2,1,1),k=1)[0]
    if key==1:
        dire=(5,3,3,3,2,2,1)
    else:
        dire=(3,5,3,2,3,1,2)
    chby=choices([y+1,y-1,y,y+2,y-2,y+3,y-3],weights=dire,k=1)[0]
    if chbx>3 or chbx<0 or chby>7 or chby<0:
        passkick(at)
    return chbx,chby
    
def passi(key,at,duration):
    if key==1:
        gdist=sqrt(pow((at.posx-1.5),2)+pow((at.posy-7),2))
    else:
        gdist=sqrt(pow((at.posx-1.5),2)+pow((at.posy-0),2))
    if gdist<1:
        p=(1,0)
    elif gdist<=1.2:
        p=(3,1)
    elif gdist<=2:
        p=(2,2)
    else:
        p=(0,1)
    kick=choices(['shoot','pass'],weights=p,k=1)[0] 
    if kick=='pass':
        globals()['count']+=1
        atold=at
        globals()['atold']=at
        chbx,chby=passkick(at)
        at=discal(at,chbx,chby)
        if at.id[-1]=='b':
            key=2
        else:
            key=1
        globals()['ft']=0
        globals()['gt']=0 
        print(at.name,' got the ball from ',atold.name)
        if atold.id[-1]==at.id[-1]:
            atold.rating+=1
        else:
            at.rating+=1
            atold.rating-=1
        move(key,at,duration)
    else:
        shot=choice(['goal','miss'])
        if shot=='goal':
            print(at.name,' scored a goal!!!!')
            at.goals+=1
            at.rating+=20
            if at.id[-1]==globals()['atold'].id[-1]:
                print('assist by ',globals()['atold'].name)
                globals()['atold'].assist+=1
                globals()['atold'].rating+=5
            globals()['chances']+=1
            sleep(1)
            if input('do you want to substitute? (Y or N)')=='Y':
                subs()
            if  at.id[-1]=='b':
                globals()['goala']+=1
                teama[0].rating-=5
                at=choice([teama[len(teama)-2],teama[len(teama)-1],teama[len(teama)-3]])
                key=1
                pset()
                globals()['ft']=1
            else:
                globals()['goalh']+=1
                teamb[0].rating-=5
                at=choice([teamb[len(teamb)-2],teamb[len(teamb)-1],teamb[len(teamb)-3]])
                key=2
                pset()
                globals()['ft']=1
            move(key,at,duration)    
        else:
            print(at.name,' missed a goal chance')
            globals()['chances']+=1
            sleep(1)
            if input('do you want to substitute? (Y or N)')=='Y':
                subs()
            if  at.id[-1]=='b':
                teama[0].rating+=5
                teama[0].saves+=1
                at.rating-=5
                at=teama[0]
                key=1
            else:
                teamb[0].rating+=5
                teamb[0].saves+=1
                at.rating-=5
                at=teamb[0]
                key=2
            move(key,at,duration)    
subsa=[]
subsb=[]
def subs():
    steam=input('select team?')
    if steam=='LIVERPOOL':
        if len(subsa)<3:
            print('playing 11',squada[1:12])
            print('subs',squada[12:])
            out=input('leaving player')
            inn=input('entering player')
            for i in teama:
                if i.name==out:
                    oldid=i.id
                    i.id=str(len(subsa)+1)+'sa'
                    subsa.append(i)
                    teama.append(players(oldid,inn,i.pos,i.club,i.posx,i.posy,0,0,0,0,0,0))
                    teama.remove(i)
                    
                    squada.remove(inn)
                    squada.insert(squada.index(out),inn)
                    squada.remove(out)
                    print(inn, ' in ', out , ' out')
                    
            
        else:
            print('max subs reached')
            globals()['smaxa']=1
    elif steam=='M.CITY':
        if len(subsb)<4:
            print('playing 11',squadb[1:12])
            print('subs',squadb[12:])
            out=input('leaving player')
            inn=input('entering player')
            for i in teamb:
                if i.name==out:
                    oldid=i.id
                    i.id=str(len(subsb)+1)+'sb'
                    subsb.append(i)
                    teamb.append(players(oldid,inn,i.pos,i.club,i.posx,i.posy,0,0,0,0,0,0))
                    teamb.remove(i)
                    
                    
                    squadb.remove(inn)
                    squadb.insert(squadb.index(out),inn)
                    squadb.remove(out)
                    print(inn, ' in ', out , ' out')
                    
        else:
            print('max subs reached') 
            globals()['smaxb']=1
    else:
        print('invalid team')
    if input('do you want to substitute again?(Y or N)')=='Y':
                subs()

def pset():
    for i in range(len(teama)):
        teama[i].posx=formationa[i][3] 
        teama[i].posy=formationa[i][4]
    for i in range(len(teamb)):    
        teamb[i].posx=formationb[i][3]
        teamb[i].posy=formationb[i][4]
                   
            
def move(key,at,duration):
    if at.pos=='GK':
        globals()['gt']=1
    if duration==45:
        print('half time')
        if input('do you want to substitute? (Y or N)')=='Y':
            subs()
        
        pset()
        if toss=='Liverpool':
            at=choice([teamb[len(teamb)-2],teamb[len(teamb)-1],teamb[len(teamb)-3]])
            key=2
        else:
            at=choice([teama[len(teama)-2],teama[len(teama)-1],teama[len(teama)-3]])
            key=1
        print(at.name, 'kicks off')  
        sleep(1)
        
    duration+=0.5
    if duration<=90:
        #sleep(0.1)
        print(duration,end=' : ')
        if globals()['ft']==1 or globals()['gt']==1:
            h='pass'
        else:        
            h=choice(['drib','pass'])
        if h=='drib':
            
            dribble(key,at,duration)            
        else: 
            passi(key,at,duration)           
    else:
        print('match over')   
        
toss=choice(['Liverpool','Man city'])   
print(toss, ' won the toss')    
if toss=='Liverpool':
    at=choice([teama[len(teama)-2],teama[len(teama)-1],teama[len(teama)-3]])
    key=1
else:
    at=choice([teamb[len(teamb)-2],teamb[len(teamb)-1],teamb[len(teamb)-3]])
    key=2
print(at.name, 'kicks off')  
sleep(1)  
duration=0        
goalh=0
goala=0
ft=1
gt=0
count=0
chances=0
atold=''
move(key,at,duration)
print(goalh,' - ',goala) 
print('total passes: ',count)
print('total chances : ',chances)        
if input('do you want to save the results?(Y or N)')=='Y':
    wbook=xl.load_workbook('database.xlsx')
    wa=wbook['LIVERPOOL']
    wb=wbook['M.CITY']
    for x in range(2,len(wa['A'])):
        wa['L'][x].value='NO'  
    for x in range(2,len(wb['A'])):
        wb['L'][x].value='NO'    
    resa=teama+carda+subsa
    wa['V'][2].value+=1
    wb['V'][2].value+=1
    if goalh==goala:
        wa['X'][2].value+=1
        wb['X'][2].value+=1
    elif goalh>goala:
        wa['W'][2].value+=1
        wb['Y'][2].value+=1
    else:
        wa['Y'][2].value+=1
        wb['W'][2].value+=1
    for i in resa:
        print(i.name)
        for x in range(2,len(wa['A'])):
            if wa['A'][x].value==i.name:
                wa['E'][x].value+=1
                wa['F'][x].value+=i.goals
                wa['G'][x].value+=i.assist
                wa['H'][x].value+=i.saves
                if goala==0:
                    wa['I'][x].value+=1
                if i.card==1 or i.card==2:
                    wa['K'][x].value+=i.card
                elif i.card==3:
                    wa['J'][x].value+=1
                if i.card==2 or i.card==3:
                    wa['L'][x].value='SUSPENDED'
                if i.injury!=0:
                    wa['M'][x].value+=i.injury
                wa['N'][x].value=wa['O'][x].value
                wa['O'][x].value=wa['P'][x].value
                wa['P'][x].value=wa['Q'][x].value
                wa['Q'][x].value=wa['R'][x].value
                wa['R'][x].value=i.rating
                wa['S'][x].value=((wa['S'][x].value*(wa['E'][x].value-1))+i.rating)/wa['E'][x].value
    resb=teamb+cardb+subsb
    for i in resb:
        print(i.name)
        for x in range(2,len(wb['A'])):
            if wb['A'][x].value==i.name:
                wb['E'][x].value+=1
                wb['F'][x].value+=i.goals
                wb['G'][x].value+=i.assist
                wb['H'][x].value+=i.saves
                if goala==0:
                    wb['I'][x].value+=1
                if i.card==1 or i.card==2:
                    wb['K'][x].value+=i.card
                elif i.card==3:
                    wb['J'][x].value+=1
                if i.card==2 or i.card==3:
                    wb['L'][x].value='SUSPENDED'
                if i.injury!=0:
                    wb['M'][x].value+=i.injury
                wb['N'][x].value=wb['O'][x].value
                wb['O'][x].value=wb['P'][x].value
                wb['P'][x].value=wb['Q'][x].value
                wb['Q'][x].value=wb['R'][x].value
                wb['R'][x].value=i.rating
                wb['S'][x].value=((wb['S'][x].value*(wb['E'][x].value-1))+i.rating)/wb['E'][x].value
    for x in range(2,len(wa['A'])):
        
        if wa['M'][x].value!=0 and type(wa['M'][x].value)==int:
            wa['M'][x].value-=1
    for x in range(2,len(wb['A'])):
        
        if wb['M'][x].value!=0 and type(wb['M'][x].value)==int:
            wb['M'][x].value-=1
    wbook.save('database.xlsx')
        
        


#again optimization
#displaying results
#adding team strength and individual strength
#once more optimization