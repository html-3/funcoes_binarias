def intread(n):
    while 1:
        try:
            n=int(input(n))
        except (ValueError, TypeError):
            print('\033[031mErro: Digite um valor válido.\033[m')
            continue
        else:
            return n
#g=2
#g=intread("")