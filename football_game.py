
from random import randrange
from time import sleep
class players:
    def __init__(self,name,position,club,national,rating):
        self.name=name
        self.position=position
        self.club=club
        self.national=national
        self.rating=rating
p14=players('alisson','GK','LIV','brazil',94)
p13=players('van dijk','CB','LIV','brazil',95) 
p12=players('henderson','CMF','LIV','england',90) 
p11=players('salah','ST','LIV','egypt',97) 
p24=players('hart','GK','MC','england',92) 
p23=players('kompany','CB','MC','belgium',94) 
p22=players('de bruyne','CMF','MC','belgium',96) 
p21=players('aguero','ST','MC','argentina',96)
         
team1=[p11,p12,p13,p14]
team2=[p21,p22,p23,p24]
goalh=0
goala=0
toss=randrange(1,3)    
def result():
    print(goalh,' - ',goala)
def match():
    x=0
    y=0
    
    duration=0
    
    if globals()['toss']==1:
        key=1
        at=team1[x].name
        de=team2[y].name
        print("LIV kicks off")
        sleep(2)
    else:
        key=2
        de=team1[x].name
        at=team2[y].name
        print("MC kicks off")
        sleep(2)
        
    move(x,y,key,at,de,duration)
    print('match over')
    result()
    
        
        
def move(x,y,key,at,de,duration):
    if duration==45:
        print('half time')
        result()
        sleep(5)
        x=0
        y=0
        if globals()['toss']==2:
            key=1
            at=team1[x].name
            de=team2[y].name
            print("LIV kicks off")
            sleep(2)
        else:
            key=2
            de=team1[x].name
            at=team2[y].name
            print("MC kicks off")
            sleep(2)
    duration+=1
    
    if duration<=90:
        sleep(0.1)
        print(duration,end=' : ')
        if y==3:
            shot=randrange(0,2)
            dive=randrange(0,2)
            if shot==dive:
                print(at,' gave a shot but ',de,' saved it')
                
                key=2
                x=0
                y=2
                de=team1[x].name
                at=team2[y].name
                move(x,y,key,at,de,duration)
            else:
                print(at,' scored a goal!!!!')
                globals()['goalh']+=1
                print('score',end=' : ')
                result()
                sleep(3)
                
                key=2
                x=0
                y=0
                de=team1[x].name
                at=team2[y].name
                move(x,y,key,at,de,duration)
        elif x==3:
            shot=randrange(0,2)
            dive=randrange(0,2)
            if shot==dive:
                print(at,' gave a shot but ',de,' saved it')
                
                key=1
                x=2
                y=0
                at=team1[x].name
                de=team2[y].name
                move(x,y,key,at,de,duration)
            else:
                print(at,' scored a goal!!!!')
                globals()['goala']+=1
                print('score',end=' : ')
                result()
                sleep(3)
                
                key=1
                x=0
                y=0
                at=team1[x].name
                de=team2[y].name
                move(x,y,key,at,de,duration)
        else:    
            method=randrange(0,3)
            
            if method==0:
                print(at,' overcame ',de,' and moving')
                if key==1:
                    y+=1
                    de=team2[y].name
                    move(x,y,key,at,de,duration)
                else:
                    x+=1
                    de=team1[x].name
                    move(x,y,key,at,de,duration)
                        
                
            elif method==1:
                if key==1 and x==0:
                    print('that was a misspass and ',de,' got the ball')
                    key=2
                    at,de=de,at
                    move(x,y,key,at,de,duration)
                elif key==2 and y==0:
                    print('that was a misspass and ',de,' got the ball')
                    key=1
                    at,de=de,at
                    move(x,y,key,at,de,duration)
                else:
                    print(at,' passed the ball and ',end='')
                    
                    if key==1:
                        x-=1
                        y+=1
                        at=team1[x].name
                        de=team2[y].name
                        print(at,' got the ball')
                        move(x,y,key,at,de,duration)
                    else:
                        y-=1
                        x+=1
                        de=team1[x].name
                        at=team2[y].name
                        print(at,' got the ball')
                        move(x,y,key,at,de,duration)
            else:
                if key==1:
                    print(at,' passed the ball but ',de,' blocked the ball')
                    key=2
                    at,de=de,at
                    move(x,y,key,at,de,duration)
                else:
                    print(at,' passed the ball but ',de,' blocked the ball')
                    key=1
                    at,de=de,at
                    move(x,y,key,at,de,duration)
    else:
        return('match over')                            
print('-----------Welcome to PyFutBol----------')
a=int(input('1.match\n2.records\n3.contribute'))
if a==1:
    b=input('1.quick match\n2.league\n3.champions league')
elif a==2:
    b=input('1.player records\n2.team records\n3.competition records\n4.')
elif a==3:
    b=input('1.add player\n2.add team\n3.create competition\n4.edit players\n5.edit teams\n6.edit competition')                
                
            
        
                
                
        
            
        
        
       