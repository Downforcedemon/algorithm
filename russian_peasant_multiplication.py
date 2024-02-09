import math
import pandas as pd 


n1 = 89
n2 = 18
halving = [n1]
while (min(halving) > 1):    
    halving.append(math.floor(min(halving) / 2))      
 

doubling= [n2]
while(len(doubling) < len(halving)): 
    doubling.append(max(doubling) * 2)
  

    # put both lists into a dataframe
half_double = pd.DataFrame(zip(halving,doubling))  
half_double = half_double.loc[half_double[0]%2 == 1,:]  
print(half_double)
answer = sum(half_double.loc[:,1])
print(answer)



