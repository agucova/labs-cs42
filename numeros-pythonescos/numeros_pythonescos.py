# Retorna el i-esimo dígito de x
def digito(x,i):
    contador=largo(x)-1
    while x!=0:
        if i==contador:
            return x%10
        contador-=1
        x = x // 10
    return -1

# Retorna el numero de digitos de x
def largo(x):
    contador=0
    while x!=0:
        x=x//10
        contador+=1
    return contador

def pythonesco(x):

	#########################################
	# ESTA ES LA FUNCION QUE DEBES ESCRIBIR #
    #########################################


# Código Principal - NO TOCAR
num = int(input())
res = pythonesco(num)
print(res)