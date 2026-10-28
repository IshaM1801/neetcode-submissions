class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position)==1:
            return 1
        d={}
        stack=[]
        fleet=0
        m=-1
        for ind,i in enumerate(position):
            d[i]=speed[ind]
        
        d=dict(sorted(d.items(),reverse=True))
        for k,v in d.items():
            d[k]=(target-k)/v
       
        for values in d.values():
            
           
                
            if values<=m :
                if fleet==0:
                    fleet+=1
                continue
            else:
                
                fleet+=1
               
            stack.append(values)
           
            m=max(m,values)
            
        return fleet