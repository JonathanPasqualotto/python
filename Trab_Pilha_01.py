import os
os.system('clear')
binario = 0
lista = []
def converteBinario(dividendo):
  quociente = 1
  while quociente >= 1:
    resto = dividendo%2
    lista.insert(0,resto)
    quociente = dividendo // 2
    dividendo = quociente
  binario = ''.join([str(item) for item in lista])
  return binario



dividendo = int(input("Digite um numero para ser convertido em Binário: \n"))
numero_digitado = converteBinario(dividendo)

print("O número %s quando convertido em binário.\nVale: %s" %(dividendo,numero_digitado))