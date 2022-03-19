#-Construir un programa que permita ingresar N (cantidad digitada por el
#usuario) números enteros y cuente cuantos múltiplos de 2 y de 3 fueron
#ingresados (+1)
numeros=[]
multiplosDos=0
multiplosTres=0
longitudLista= int(input("Digite la cantidad que desea ingresar"))
for i in range(longitudLista):
    numero = int(input("Digite un numero para validar "))
    numeros.append(numero)
for i in range(longitudLista):
    if(((numeros[i]%2)==0) and ((numeros[i]%3)==0)):
        multiplosDos+=1
        multiplosTres+=1
    elif((numeros[i]%2)==0):
        multiplosDos+=1
    elif((numeros[i]%3)==0):
        multiplosTres+=1
    else:
        print("El numero digitado no es multiplo de 2 ni de 3")
print(f"Los numeros digitados fueron{numeros}")
print(f"La cantidad de numeros multiplos de 2 son: {multiplosDos}")
print(f"La cantidad de numeros multiplos de 3 son: {multiplosTres}")


