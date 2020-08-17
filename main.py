
  # num=int(input("Please enter a number: "))
  # divisor1=int(input("Please enter a divisor: "))
  # divisor2=int(input("Please enter another divisor: "))

def is_divisible_by(num, divisor1, divisor2):
  # num is divisible by 1
  if num%divisor1==0:
    if num%divisor2==0:
      return(f'This number is divisible by {divisor1} and {divisor2}.') 
    else:
      return(f'This number is divisible by {divisor1}.') 
  elif num%divisor2==0: 
      if num%divisor1==0:
        return(f'This number is divisible by {divisor1} and {divisor2}.') 
      else:
        return(f'This number is divisible by {divisor2}.')
  elif num%divisor1!=0:
    if num%divisor2==0:
      return(f'This number is divisible by {divisor2}.')
    else:
      return(f'This number is not divisible by either {divisor1} or {divisor2}.')
  elif num%divisor2!=0:
    if num%divisor1==0:
      return(f'This number is divisible by {divisor1}.')
    else:
      return(f'This number is not divisible by either {divisor1} or {divisor2}.')
  else:
    return (f'This number is not divisible by either {divisor1} or {divisor2}.')
    

  
print(is_divisible_by(8,5,3))
