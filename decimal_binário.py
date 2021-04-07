#funcao transforma um número decimal inteiro para binário

def decimal_inteiro_binario(n):
    b=2
    m=[]
    while n!=0:
      print(f"{n}/{b}={n//b}+{n%b}")
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
    
    print("".join(str(num) for num in v))
    return m

def decimal_fracao_binario(n):
    b=2
    
    m=[]
    i=0
    while i<32:
      if n*b>=1:
        print(f"{n}*{b}={round(n*b-1,2)}+1")
        m.append(1)
        n=round(n*b-1,4)
      else:
        print(f"{n}*{b}={round(n*b,2)}+0")
        m.append(0)
        n=round(n*b,4)
      if n==0: break
      i=i+1
      
    if (len(m)+1)%4==0: m.extend([0])
    if (len(m)+2)%4==0: m.extend([0,0])
    if (len(m)+3)%4==0: m.extend([0,0,0])

    v=m
    for i in range(len(m)//4*5):
      if i%5==0:
        v.insert(i," ")

    print(" 0."+"".join(str(num) for num in v))
    return m