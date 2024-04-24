import sys
sys.setrecursionlimit(999999)

def cubic_series(n):
  if n == 1:
    return 1
  return n**3 + cubic_series(n-1)



def div(a,b):
  if a < b:
    return 0
  return 1 + div(a-b,b)

def mod(a,b):
    if a<b:
        return a
    return mod(a-b,b)



def lastDigit(x):
    return mod(x,10)

def allButLast(x):
    return div(x,10)



def sumDigits(n):
    if abs(allButLast(n)) <= 0:
        return lastDigit(n)
    return lastDigit(n) + sumDigits(abs(allButLast(n)))

#fix

    
def skip_power(n,k):
  if n < 0:
    return 0
  if n<k:
    return n
  return n**k + skip_power(n-k,k)

def skip_valid_power(a,b):
  value = skip_power(a,b)
  if value >=1000 and value <=999999 :
    if sumDigits(value)%7 == 0:
      return True
  return False
