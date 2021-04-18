def dec2bin(n):
    b=2
    m=[]
    while n!=0:
      print(f"  {n}/{b}={n//b}+\033[035m{n%b}\033[m")
      m.append(n%b)
      n=n//b
        
    if (len(m)+1)%4==0: m.append(0)
    if (len(m)+2)%4==0: m.extend([0,0])
    if (len(m)+3)%4==0: m.extend([0,0,0])
    
    m.reverse()
    v=m
    for i in range(len(m)//4*5):
      if i%5==0:
        v.insert(i," ")
    
    #print(m)
    return "".join(str(num) for num in v)