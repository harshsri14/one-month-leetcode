# https://leetcode.com/problems/poor-pigs

import math
def poorPigs(buckets, minutesToDie, minutesToTest) :
    '''
     if x is a min number of pigs then for 1 tests answer we can say that:
         2^x >= buckets
        so x >= log2(buckets)
           x = ceil(log2(buckets))
     how??
      1 tests we can say for 2 buckets:
           p0    1 pig for 2 buckets
      b0 - 0      
      b1 - 1
      
          p0 p1  2pigs for 4 buckets
      b0 - 0 0
      b1 - 0 1
      b2 - 1 0
      b3 - 1 1
     if p0 dies = b2 is poisonous
     if p1 dies = b1 is poisonous
     if both dies = b3 is poisonous
     if no one dies = b0 is poisonous

     similarly 3 pigs for 8 buckets
     so generaly for 2^x buckets we need atmost x pigs 

     for 2 tests ans:
          3^x >= buckets (3 choices 0,1,2)
     like for 2 pigs we need 3^2 buckets = 9;
     
              p0 p1 
      b0 -    0  0  
      b1 -    0  1   1 shows that drink b1 bucket to p1 pig during first test 
      b2 -    0  2    2shows that drink p1 pig in second test
      b3 -    1  0   
      b4 -    1  1 
      b5 -    1  2 
      b6 -    2  0
      b7 -    2  1 
      b8 -    2  2
        
    '''
    
    return math.ceil(math.log(buckets) / math.log((minutesToTest/minutesToDie) + 1))


buckets = 1000
minutesToDie = 15
minutesToTest = 60

print(poorPigs(buckets, minutesToDie, minutesToTest))
