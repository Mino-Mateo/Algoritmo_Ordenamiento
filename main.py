#Funcino Imprimir en Pantalla
def imprimir_Arreglo(arreglo):
  for i in range(len(arreglo) - 1):
    print(f'[{arreglo[i]}]', end="")


#Funcion Algoritmo de la Burbuja
def algoritmo_Burbuja(arreglo):
  for i in range(len(arreglo) - 1):
    for j in range(len(arreglo) - 1 - i):
      if arreglo[j] > arreglo[j + 1]:
        aux = arreglo[j]
        arreglo[j] = arreglo[j + 1]
        arreglo[j + 1] = aux


#Arreglo
listaSueldos = [20.8, 150.5, 170.5, 180.8, 190.30, 75.6, 200]

#Lista Desordenada
print("\nLISTA DESORDENADA")
imprimir_Arreglo(listaSueldos)
print(" ")

#Ordenamiento
algoritmo_Burbuja(listaSueldos)
print(" ")

#Lista Ordenada
print("\nLISTA ORDENADA")
imprimir_Arreglo(listaSueldos)
