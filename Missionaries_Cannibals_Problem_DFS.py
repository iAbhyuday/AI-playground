#Abhyuday Tripahi 


from collections import OrderedDict

# frontier as OrederedDict 
frontier = OrderedDict()
exp = dict()
class state:
    def __init__(self,state,dir):
        self.dir =dir
        self.sta = state
        self.parent = None
        self.action="           "
        self.pathCost=0

    def is_goal_state(self,other):
        for i in range(len(other.sta)):
            if(other.sta[i]!=self.sta[i]):
                return False
        if other.dir != self.dir:
            return False
        return True

    def move(self):
        ml = self.sta[0]  # missionaries on left bank
        cl = self.sta[1]  # cannibals on left bank
        mr = self.sta[2]  # missionaries on right bank
        cr = self.sta[3]  # missionaries on right bank
        
        
        # constraints when moving left to right
        if self.dir>0:
            
            if((ml-1>=cl or ml-1==0) and ml-1>=0 and (mr+1>=cr)):
               
                x =state([ml-1,cl,mr+1,cr],-1)
                x.parent =self
                x.pathCost =self.pathCost+1
                x.action = "1M  0C ====>"
                if(checkNadd(x)):
                    frontier[x.code()] =x
            if((cl-1<=ml or ml==0) and cl-1>=0 and (cr+1 <=mr or mr==0)):
                
                x =state([ml-1,cl,mr+1,cr],-1)
                x.parent =self
                x.pathCost =self.pathCost+1
                x.action = "0M 1C ====>"
                if(checkNadd(x)):
                    frontier[x.code()] =x
                    
                
            if((ml-2>=cl or ml-2==0) and ml-2>=0 and mr+2>=cr):
                
                x =state([ml-2,cl,mr+2,cr],-1)
                x.parent =self
                x.pathCost =self.pathCost+1
                x.action ="2M 0C ====>"
                if checkNadd(x):
                    frontier[x.code()] =x

            if((cl-2<=ml or ml==0) and cl-2>=0 and (cr+2<=mr or mr==0)):
                
                x =state([ml,cl-2,mr,cr+2],-1)
                x.parent =self
                x.pathCost =self.pathCost+1
                x.action ="0M 2C ====>"
                if checkNadd(x):
                    frontier[x.code()] =x


            if(ml-1>=cl-1 and cl-1<=ml-1 and cl-1>=0 and ml-1>=0 and mr+1>=cr+1 and cr+1<=mr+1):
                
                x =state([ml-1,cl-1,mr+1,cr+1],-1)
                x.parent =self
                x.pathCost =self.pathCost+1
                x.action = "1M 1C ====>"
                if checkNadd(x):
                    frontier[x.code()] =x
         
        # constraints when moving right to left bank
        elif self.dir<0:
            
            if((mr-1>=cr or mr-1==0) and mr-1>=0 and ml+1>=cl):
                
                x=state([ml+1,cl,mr-1,cr],1)
                x.parent =self
                x.pathCost =self.pathCost+1
                x.action ="<==== 1M 0C"
                if checkNadd(x):
                    frontier[x.code()] =x
                    
            if((cr-1<=mr or mr==0) and cr-1>=0 and (cl+1<=ml or ml==0)):
                
                x =state([ml,cl+1,mr,cr-1],1)
                x.parent =self
                x.pathCost =self.pathCost+1
                x.action = "<==== 0M 1C"
                if checkNadd(x):
                    frontier[x.code()] =x
                
            if((mr-2>=cr or mr-2==0) and mr-2>=0 and ml+2>=cl):
               
                x =state([ml+2,cl,mr-2,cr],1)
                x.parent =self
                x.pathCost =self.pathCost+1
                x.action = "<==== 2M 0C"
                if checkNadd(x):
                   frontier[x.code()] =x


            
            if((cr-2<=mr or mr==0) and cr-2>=0 and (cl+2<=ml or ml==0)):
                
                x =state([ml,cl+2,mr,cr-2],1)
                x.parent =self
                x.pathCost =self.pathCost+1
                x.action="<==== 0M 2C"
                if checkNadd(x):
                    frontier[x.code()] =x
            

            if(mr-1>=cr-1 and cr-1<=mr-1 and mr-1>=0 and cr-1>=0 and ml+1>=cl+1 and cl+1<=ml+1):
                
                x =state([ml+1,cl+1,mr-1,cr-1],1)
                x.parent =self
                x.pathCost =self.pathCost+1
                x.action = "<==== 1M 1C"
                if checkNadd(x):
                    frontier[x.code()] =x

        

    def __str__(self):
        
        
        return "M: "+str(self.sta[0])+" "+"C: "+str(self.sta[1])+"    "+self.action+"    "+"M: "+str(self.sta[2])+" "+"C: "+str(self.sta[3])

    def code(self):
        return "M: "+str(self.sta[0])+" "+"C: "+str(self.sta[1])+"M: "+str(self.sta[2])+" "+"C: "+str(self.sta[3])+str(self.dir)
        


def checkNadd(state):
    # checking Explored and Frontier
    if(state.code() not in exp or (state.code() in frontier and frontier[state.code()].pathCost>state.pathCost)):
        
        return True
    return False

# helper function to print the solution path        
def trail(state):
    if(state.parent==None):
        return state
    print(trail(state.parent))
    return state

if __name__=="__main__":
    init = state([3,3,0,0],1)
    goal =state([0,0,3,3],-1)

    b =init
    frontier[str(b)]=b
    while len(frontier)!=0:
        # frontier set to LIFO Fashion for DFS
        x =frontier.popitem(last=True)[1]
        # Checking for Goal State
        if x.is_goal_state(goal):
            trail(x)
            print(x)
            print(f"Achieved ! : {x.pathCost}")
        
            break
        exp[x.code()] =1
        x.move()
    

 



