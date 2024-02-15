#Question 3: powerr of two
def power(n):
    bool = True
    if n<= 0:
     return False
    while n != 0:
      n /= 2;
      #check if the number after being divided by 2 is equal 1 and breaks the loop 
      # meaning if n === 1 then n is of power of 2
      if n == 1:
          break 
      #checks if n after being divided by 2 its remainder is 0 if not the bool is set to false
      #which means that the n number is not of power of two and then it breaks
      if n % 2 != 0 :
         bool=False
         break;   
    return bool   
print(power(16))    