# Retorna el i-esimo dígito de x
def digito(x, i):
    contador = largo(x) - 1
    while x != 0:
        if i == contador:
            return x % 10
        contador -= 1
        x = x // 10
    return -1


# Retorna el numero de digitos de x
def largo(x):
    contador = 0
    while x != 0:
        x = x // 10
        contador += 1
    return contador


# Retorna si un numero es introesco o no
def introesco(x):
    c1 = 0
    c3 = 0
    c0 = 0
    c = 0
    while c < largo(x):
        d = digito(x, c)
        if d == 1:
            c1 += 1
        elif d == 3:
            c3 += 1
        elif d == 0:
            c0 += 1
        c += 1
    if c1 >= 2 and c3 >= 1 and c0 >= 1:
        return True
    return False


###########################
# ESCRIBE TU CODIGO AQUI #
##########################
