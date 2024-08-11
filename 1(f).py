def check(n):
   if n <= 1:
       return n
   else:
       return(check(n-1) + check(n-2))

nterms = 10
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(check(i))
