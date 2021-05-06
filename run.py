from time import sleep
from menu import opcoes,head,linha,s
from intread import intread
from dec2bin import dec2bin
from dec2hex import dec2hex

p=["Sair",
       "Decimal inteiro para binário",
       "Decimal fracional para binário",
       "Binário inteiro para decimal",
       "Binário fracional para decimal",
       "Decimal para hexadecimal",
       "Hexadecimal para binário"] 
e=-1

while True:
    head("Operacoes de Mudanca de Base",s)
    e=opcoes(p)
    
    if e==0:
        print("Saindo...","\n")
        break
    elif e==1:
        n=intread("Insira um valor:")
        print(f"\nR:{dec2bin(n)}\n")
        
    #elif e==2:
    #elif e==3:
    #elif e==4:
    elif e==5:
        n=intread(" Insira um valor:")
        print(f"\nR: {dec2hex(n)}\n")
    sleep(2)