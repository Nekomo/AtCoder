a,b,c,k=[int(i)for i in input().split()]
if k <= a:
  print(k)
elif k<=a + b:
  print(a)
else:
  print(a-(k-a-b))