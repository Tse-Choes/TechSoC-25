def exp(b,p):
  n=2
  x=b
  if p < 0:
    return 1/exp(b,abs(p))
  elif p == 0:
    return 1
  while n<=p:
    x *= x
    n+=n
  n //= 2
  x=x*exp(b,p-n)
  return x
