

# 2 - Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem 
# ser um triângulo.
# Indique, caso os lados formem um triângulo, se 
# ele é: equilátero, isósceles ou escaleno.

# Sabemos que:
# Três lados formam um triângulo quando a soma de 
# quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

# entrada de dados
ladoA = int(input(" informe o lado A: "))
ladoB = int(input(" informe o lado B: "))
ladoC = int(input(" informe o lado C: "))

if (ladoA + ladoB < ladoC) or (ladoA + ladoC < ladoB) or (ladoC + ladoB < ladoA):
  print("não é um triangulo!")
elif (ladoA == ladoB) and (ladoB == ladoC):
  print("é um triângulo equilátero!")
elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
  print("é um triângulo isósceles")
else:
  print("é um triangulo escaleno!")
  
  print("fim do programa!")