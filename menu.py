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
        print(f" \033[033m{c} -\033[m \033[032m{i}\033[m")
        c+=1
    linha(s)
    e=intread(" \033[032mEscolha:\033[m ")
    return e
