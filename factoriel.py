def factoriel (n) :
  f=1
  for i in range (1,n+1):
    f=f*i
  return f 
n=int(input("donner un entier "))
while n <0:
  n=int(input("le number soit ete postif "))
if n >0:
    print(n,"!=",factoriel(n))
elif n==0:
    print(n,"!=0")

else:
    print("eruer")
  
  