import sys
from termcolor import colored, cprint
from copy import deepcopy
from queue import PriorityQueue as pq
frontier = pq()
explored = dict()
import time
class board: 
    def __init__(self,state):
        self.state= state 
        self.parent =None
        self.level =0
        self.ch=[]
        self.loners=0
        self.actions =0
        self.gots=0
        self.hvalue=0
    def isolation(self):
        check=False
        
        for i in range(7):
            for j in range(7):
                h1=False
                h2=False
                v1 =False
                v2 = False
                if(self.state[i][j]==1):
                    if(j+2<7):
                        if(self.state[i][j+1]!=1 and self.state[i][j+2]!=1):
                            h1=True
                    else:
                        h1=True


                    if(j-2>=0):
                        if(self.state[i][j-1]!=1 and self.state[i][j-2]!=1):
                            h2=True
                    else:
                        h2=True
                    if(i+2<7):
                        if(self.state[i+1][j]!=1 and self.state[i+2][j]!=1):
                            v1=True
                    else:
                        v1=True
                    if(i-2>=0):
                        if(self.state[i-1][j]!=1 and self.state[i-2][j]!=1):
                            v2=True
                    else:
                        v2=True
                if(h1 and h2 and v1 and v2):
                    self.loners+=1
                    
    
        

    def moves(self):
        

        for i in range(7):
            for j in range(7):
                if(self.state[i][j]==1):
                    self.gots+=1
                    if(j+2<7):
                        if(self.state[i][j+1]==1 and self.state[i][j+2]==0):
                            x =deepcopy(self.state)
                            x[i][j]=0
                            x[i][j+1]=0
                            x[i][j+2]=1
                            b = board(x)
                            b.parent = self
                            b.level = self.level+1
                            self.ch.append(b)
                            self.actions+=1
                            
                    if(j-2>0):
                        if(self.state[i][j-1]==1 and self.state[i][j-2]==0):
                            x =deepcopy(self.state)
                            x[i][j]=0
                            x[i][j-1]=0
                            x[i][j-2]=1
                            b = board(x)
                            b.parent = self
                            b.level = self.level+1
                            self.ch.append(b)
                            self.actions+=1
                            
                            

                    if(i+2<7):
                        if(self.state[i+1][j]==1 and self.state[i+2][j]==0):
                            x =deepcopy(self.state)
                            x[i][j]=0
                            x[i+1][j]=0
                            x[i+2][j]=1
                            b = board(x)
                            b.parent = self
                            b.level = self.level+1
                            self.ch.append(b)
                            self.actions+=1
                            
                    if(i-2>0):
                        if(self.state[i-1][j]==1 and self.state[i-2][j]==0):
                            x =deepcopy(self.state)
                            x[i][j]=0
                            x[i-1][j]=0
                            x[i-2][j]=1
                            b = board(x)
                            b.parent = self
                            b.level = self.level+1
                            self.ch.append(b)
                            self.actions+=1
                            
        self.isolation()
        self.hvalue=hval(self)
        


    def is_goal_state(self,other):
        for i in range(7):
            for j in range(7):
                if(self.state[i][j]!=other[i][j]):
                    return False
        return True

    def __lt__(self,other):
        return self.hvalue<other.hvalue

    def __str__(self):
        s = ""
        for i in range(7):
            for j in range(7):
                s+=str(self.state[i][j])
        return s




                    
def hval(st):
    return pow(st.gots-1,2)+0.8*st.actions-0.8*cval(st)
def cval(st):
    x=0
    for i in range(2,5):
        for j in range(1,6):
            if(st.state[i][j]==1):
                x+=1
    return x

def pr(st):
    for i in range(7):
        for j in range(7):
            if(st[i][j]==1):
                cprint("*",'green',end="   ")
            elif(st[i][j]==0):
                cprint("0",'red',end="   ")
            else:
                print(" ",end="   ")
        print("\n")   
def trail(state):
    if(state.parent==None):
        return state
    pr(trail(state.parent).state)
    print("\n\n")
    return state         
if __name__ =="__main__":
    cn=0
    start =time.time()
    stat = [[-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,1,1,1,1],[-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1]]
    sd =[[-1,-1,0,0,0,-1,-1],[-1,-1,0,1,0,-1,-1],[1,1,1,1,0,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1]]
    finalState = [[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1]]
    print("Init : ")
    pr(sd)
    print("\n\n")
    print("FinalState :")
    pr(finalState)
    print("\n\n")
    b = board(stat)
    b.moves()
    frontier.put((b.hvalue,b))
    while(not frontier.empty()):
        x = frontier.get()[1]

        if(x.is_goal_state(finalState)):
            trail(x)
            pr(x.state)
            print(f"Achieved ! {cn} steps.")
            endtime=time.time()
            print(f"Time taken : {endtime-start}")
            break
        explored[str(x)]=1
       # print(f"Level : {x.level} Loners: {x.loners} Pegs: {x.gots} Actions: {x.actions} Heuristic: {x.hvalue}  cn: {cn}")
        cn+=1
       

        for i in x.ch:
         
            i.moves()
            if(str(i) not in explored.keys()):
                if((i.actions==0 and i.gots>=2) or (i.loners>=5) ):
                    pass
                else:
                
                    frontier.put((i.hvalue-i.level,i))

        





