def dec2hex(n):
    b=16
    m=[]
    while n!=0:
      print(f"  {n}/{b}={n//b}+\033[035m{n%b}\033[m")
      if n%b==10:   m.append("A")
      elif n%b==11: m.append("B")
      elif n%b==12: m.append("C")
      elif n%b==13: m.append("D")
      elif n%b==14: m.append("E")
      elif n%b==15: m.append("F")
      else:         m.append(n%b)
      n=n//b

    m.reverse()
    v=m
    for i in range(len(m)//4*5):
      if i%5==0:
        v.insert(i," ")
    
    #print(m)
    return "".join(str(num) for num in v)