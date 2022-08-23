from random import choice,choices
from time import sleep
from math import sqrt
import pandas as pd

class players:
    
    def __init__(self,id,name,pos,club,posx,posy,goals,assist,ycard,rcard,injurystat,rating):
        self.id=id
        self.name=name
        self.pos=pos
        self.club=club
        self.posx=posx
        self.posy=posy
        self.goals=goals
        self.assist=assist
        self.ycard=ycard
        self.rcard=rcard
        self.injurystat=injurystat
        self.rating=rating
        
        
        
'''teama=[players('1a','alisson','GK','liverpool',1.5,0,0,0,0,0,0,0),
       players('2a','robertson','LB','liverpool',0,1,0,0,0,0,0,0),
       players('3a','van dijk','CB','liverpool',1,1,0,0,0,0,0,0),
       players('4a','gomez','CB','liverpool',2,1,0,0,0,0,0,0),
       players('5a','trent arnold','RB','liverpool',3,1,0,0,0,0,0,0),
       players('6a','milner','LM','liverpool',0.5,2,0,0,0,0,0,0),
       players('7a','fabinho','CM','liverpool',1.5,2,0,0,0,0,0,0),
       players('8a','wjnaldum','RM','liverpool',2.5,2,0,0,0,0,0,0),
       players('9a','mane','LWF','liverpool',0.5,3,0,0,0,0,0,0),
       players('10a','firmino','CF','liverpool',1.5,3,0,0,0,0,0,0),
       players('11a','salah','RWF','liverpool',2.5,3,0,0,0,0,0,0)
       ]        
        
teamb=[players('1b','ederson','GK','man city',1.5,7,0,0,0,0,0,0),
       players('2b','zinchenko','LB','man city',0,6,0,0,0,0,0,0),
       players('3b','laporte','CB','man city',1,6,0,0,0,0,0,0),
       players('4b','stones','CB','man city',2,6,0,0,0,0,0,0),
       players('5b','walker','RB','man city',3,6,0,0,0,0,0,0),
       players('6b','bernardo','LM','man city',0.5,5,0,0,0,0,0,0),
       players('7b','rodri','CM','man city',1.5,5,0,0,0,0,0,0),
       players('8b','de bruyne','RM','man city',2.5,5,0,0,0,0,0,0),
       players('9b','sterling','LWF','man city',0.5,4,0,0,0,0,0,0),
       players('10b','aguero','CF','man city',1.5,4,0,0,0,0,0,0),
       players('11b','mehrez','RWF','man city',2.5,4,0,0,0,0,0,0)
       ]       ''' 


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
        move(key,at,duration)
        
        
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
        chbx,chby=passkick(at)
        at=discal(at,chbx,chby)
        if at.id[-1]=='b':
            key=2
        else:
            key=1
        globals()['ft']=0
        globals()['gt']=0 
        print(at.name,' got the ball from ',atold.name)
        move(key,at,duration)
    else:
        shot=choice(['goal','miss'])
        if shot=='goal':
            print(at.name,' scored a goal!!!!')
            globals()['chances']+=1
            sleep(1)
            if  at.id[-1]=='b':
                globals()['goala']+=1
                at=choice([teama[9],teama[10],teama[8]])
                key=1
                globals()['ft']=1
            else:
                globals()['goalh']+=1
                at=choice([teamb[9],teamb[10],teamb[8]])
                key=2
                globals()['ft']=1
            move(key,at,duration)    
        else:
            print(at.name,' missed a goal chance')
            globals()['chances']+=1
            sleep(1)
            if  at.id[-1]=='b':
                at=teama[0]
                key=1
            else:
                at=teamb[0]
                key=2
            move(key,at,duration)    
            
            
def move(key,at,duration):
    if at.pos=='GK':
        globals()['gt']=1
    duration+=1
    if duration<=90:
        #sleep(0.1)
        print(duration,end=' : ')
        if globals()['ft']==1 or globals()['gt']==1:
            h='pass'
        else:        
            h=choice(['drib','pass'])
        if h=='drib':
            duration-=0.5
            dribble(key,at,duration)            
        else: 
            passi(key,at,duration)           
    else:
        print('match over')   
        
toss=choice(['Liverpool','Man city'])   
print(toss, ' won the toss')    
if toss=='Liverpool':
    at=choice([teama[9],teama[10],teama[8]])
    key=1
else:
    at=choice([teamb[9],teamb[10],teamb[8]])
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
move(key,at,duration)
print(goalh,' - ',goala) 
print('total passes: ',count)
print('total chances : ',chances)        

#adding yellow card,red card,injury,position setter,half time,substituition
#again optimization
#displaying results
#adding team strength and individual strength
#once more optimization