while True:
  n = int(input())
  if n!=0:
    for i in range(n):
      v = input().split()
      c = 0
      p = 0
      for i in v:
        if int(i) <=127:
          c+=1
          p = v.index(i)
      if c!=1:
        print("*")
      else:
        if p==0:
          print("A")
        elif p==1:
          print("B")
        elif p==2:
          print("C")
        elif p==3:
          print("D")
        elif p==4:
          print("E")
  else:
    break