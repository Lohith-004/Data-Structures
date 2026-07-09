# Amstrong number

def isArmstrong(num):
    k = len(str(num))
    arm_sum = 0
    n = num
  
    while n > 0:
        ld = n % 10
        arm_sum += ld**k
        n = n // 10
      
    return arm_sum == num
