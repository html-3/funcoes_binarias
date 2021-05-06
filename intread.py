def intread(n):
    while 1:
        try:
            n=int(input(n))
        except (ValueError, TypeError):
            print('Erro: Digite um valor válido.')
            continue
        else:
            return n
#g=2
#g=intread("")