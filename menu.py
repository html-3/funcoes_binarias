from intread import intread
s=40

def linha(s=40):
    l=int(s/2-1)
    print('-'*l+'/'*(s-2*l)+'-'*l)

def head(t,s):
    linha(s)
    print(t.center(s))
    linha(s)

def opcoes(p):
    c=0
    for i in p:
        print(f"{c} - {i}")
        c+=1
    linha(s)
    e=intread("Escolha:")
    return e
