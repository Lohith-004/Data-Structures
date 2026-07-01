#Count the number of digits in an integer

#Loop based approach
n = 5438

num = n
count = 0

while num > 0:
  count += 1
  num = num // 10

return count

#Algorithmic approach
from math import *

def countDigits(num):
  return int(log10(num)+1)

#For negative numbers - Alogorithmic approach
from math import log10

def countDigits(num):
    if num == 0:
        return 1
    return int(log10(abs(num))) + 1
