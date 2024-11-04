# Definindo a lista original
lista_original = list(range(16))

# Gerando as sublistas
intervalo_1_9 = lista_original[1:10]
intervalo_8_13 = lista_original[8:14]
numeros_pares = [num for num in lista_original if num % 2 == 0]
numeros_impares = [num for num in lista_original if num % 2 != 0]
multiplos_2 = [num for num in lista_original if num % 2 == 0]
multiplos_3 = [num for num in lista_original if num % 3 == 0]
multiplos_4 = [num for num in lista_original if num % 4 == 0]
lista_reversa = lista_original[::-1]

# Calculando a razão entre a soma do intervalo de 10 a 15 e do intervalo de 3 a 9
intervalo_10_15 = lista_original[10:16]
intervalo_3_9 = lista_original[3:10]
razao_somas = sum(intervalo_10_15) / sum(intervalo_3_9)

# Exibindo os resultados
print("Intervalo de 1 a 9:", intervalo_1_9)
print("Intervalo de 8 a 13:", intervalo_8_13)
print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)
print("Múltiplos de 2:", multiplos_2)
print("Múltiplos de 3:", multiplos_3)
print("Múltiplos de 4:", multiplos_4)
print("Lista reversa:", lista_reversa)
print("Razão entre somas:", razao_somas)