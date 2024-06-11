import time
start = time.time()
def prime_factors(n):
  m = n
  l1 = []
  while True:
    for i in range(2,m+1):
      if m%i == 0 :
        l1.append(i)
        m = m//i
        break
    else:
      break
  return l1      

print(prime_factors(79748467941457156))
end = time.time()
print(end-start)