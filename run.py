from time import sleep
from menu import opcoes,head,linha,s
from intread import intread
from dec2bin import dec2bin

p=["Sair",
       "Decimal inteiro para binário",
       "Decimal fracional para binário",
       "Binário inteiro para decimal",
       "Binário fracional para decimal",
       "Decimal para hexadecimal",
       "Hexadecimal para binário"] 
e=-1

while True:
    head("       \033[032mOperacoes de Mudanca de Base\033[m",s)
    e=opcoes(p)
    linha(s)
    if e==0:
        print(" \033[032mSaindo...\033[m","\n")
        break
    elif e==1:
        n=intread(" \033[032mInsira um valor:\033[m ")
        print(f"\n  R:\033[035m{dec2bin(n)}\033[m \n")
        sleep(5)
    #elif e==2:
    #elif e==3:
    #elif e==4: