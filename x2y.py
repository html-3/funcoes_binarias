def tradutor(x,n):
    # torna o valor x em um valor decimal v
    # torna o valor x em uma lista b de digitos decimais
    v = 0
    b = []
    bases = {
        "0":0,
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "A":10,
        "B":11,
        "C":12,
        "D":13,
        "E":14,
        "F":15,
        "G":16,
        "H":17,
        "I":18,
        "J":19,
        "K":20,
        }

    for i in x:
        b.append(bases[i])

    return b

# como dividir um número em uma base conhecida mas ortodoxa?

def transformador(x,n,m):
    # n é a base de x e m é a base a ser transformada
    # n, m ∈ {1,2,3...20}
    c = x
    v = []
    bases = {
        0:"0",
        1:"1",
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9",
        10:"A",
        11:"B",
        12:"C",
        13:"D",
        14:"E",
        15:"F",
        16:"G",
        17:"H",
        18:"I",
        19:"J",
        20:"K",
        }
    # nao sei como deveria ser feito...
    if n>m:
        # x deve ser dividio por m
        for i in c:
            while y>m:
                # mano to cansado vou dormir
                # mas a ideia é a sguinte
                # cada digito y dum numero x qualquer deve ser dividio pela nova base m
                # no caso q o digito y seja inferior à m
                # y vai ser multiplicado pela base m e adicionado ao próximo dígito da sequência
                # processo é repetido 
        while c!=0:
            print(f"{c} / {m} = {c//m} + {c%m}")
            v.append(bases[n%b])
            c = c//m
    elif m>n:
        # x deve ser multiplicado por m
    else:
        print("As bases sao as mesmas!")
    