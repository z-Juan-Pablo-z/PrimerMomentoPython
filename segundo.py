listaFrutas=[]

for i in range(10):
    nombreFruta = input('Ingrese el nombre de la fruta: ')
    listaFrutas.append(nombreFruta)
frutasInvertidas = listaFrutas[::-1]
print(listaFrutas)
print(frutasInvertidas)
