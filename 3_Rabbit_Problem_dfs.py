#Abhyuday Tripahi 
from collections import OrderedDict

from copy import deepcopy,copy
frontier = OrderedDict()
explored =dict()
class Left:
    def __init__(self,position):
        self.position=position
    def move(self,zero_position):
        d = zero_position-self.position

        if d>0 and d<=2:
            self.position+=d
            return True
        return False

    def __eq__(self,other):
        if isinstance(other,Left) and self.position==other.position:
            return True
        return False
    def __str__(self):
        return "L"

class Right:
    def __init__(self,position):
        self.position=position
    def move(self,zero_position):
        d = (-1)*(zero_position-self.position)

        if d>0 and d<=2:
            self.position-=d
            return True
        return False
    def __eq__(self,other):
        
        if isinstance(other,Right) and self.position==other.position:
            return True
        return False
    def __str__(self):
        return "R"

state = [Right(0),Right(1),Right(2),0,Left(4),Left(5),Left(6)]
def trail(state):
    if(state.parent==None):
        return state
    print(trail(state.parent))
    return state

class board:
    def __init__(self,state):
        self.state = state
        self.zero_pos = self.state.index(0)
        self.parent=None
        self.pathCost=0
        

    def is_goal_state(self,state):
        for i in range(len(self.state)):
            if(self.state[i]!=state[i]):
                return False
        return True

    def __eq__(self,other):
         for i in range(len(self.state)):
            if(self.state[i]!=state[i]):
                return False

         if(self.zero_pos!=other.zero_pos or self.parent!=other.parent):
             return False
         return True
    
    def __str__(self):
        s=""
        for i in self.state:
            s+=str(i)+"  "
        return s
            

    def genChild(self):
        
        
        for i in range(0,len(self.state)):
        
            x =deepcopy(self)
        
            if(x.state[i]!=0 and x.state[i].move(x.zero_pos)):
        
                x.state[x.zero_pos]=deepcopy(x.state[i])
                x.state[i]=0
                x.parent = self
                x.zero_pos=i
                x.pathCost= self.pathCost+1
                
                
                if(str(x) not in explored or (str(x) in frontier and frontier[str(x)].pathCost>x.pathCost)):
                    #if(str(x) in explored and explored[str(x)].pathCost>x.pathCost):
                    frontier[str(x)]=x


                    
        

         
if __name__=='__main__':
    
    state1 = [Left(0),Left(1),Left(2),0,Right(4),Right(5),Right(6)]

    b = board(state1)
    
    frontier[str(b)] = b
    while(len(frontier)!=0):
        x = frontier.popitem(last=True)[1]

      #  print(x,end=f"  ==> pathCost: {x.pathCost}\n")
        if x.is_goal_state(state):
            trail(x)
            print(x)
            print(f"Achieved ! : {x.pathCost}")
        explored[str(x)]=1
        if(x.genChild()):
            break
        







    
    


            





    


        


        
        

            
        

                
        




