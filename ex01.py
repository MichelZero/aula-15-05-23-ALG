#
#
# 1- Faça um programa (em python) que calcule as 
# raízes da equação do 2 grau conforme a 
# fórmula de Bhaskara.
# ax² + bx + c = 0
# delta = b² - 4ac
# x1 = (-b + raiz((delta)))/((2a))
# x2 = (-b - raiz((delta) ))/ (2a)

# entrada de dados
a = int(input(("informe o valor de A: ")))
b = int(input(("informe o valor de B: ")))
c = int(input(("informe o valor de C: ")))

# processamento da dados
delta = b**2 -4*a*c

# Lógica de programação
# 1 - Se delta for negativo, não existe raiz
# 2 - Se delta for igual a zero, existe apenas uma raiz ou duas raízes iguais
# 3 - Se delta for positivo, existe duas raízes

if delta < 0:
  print(f"delta = {delta}, não existe raiz")
elif delta == 0:
  print(f"delta = {delta}, existe uma raiz")
  x1 = (-b + ((delta**(1/2))))/(2*a)
  print(f"X1 = {x1}")
elif delta > 0:
  print(f"delta = {delta}, existe duas raízes")
  x1 = (-b + ((delta**(1/2))))/(2*a)
  x2 = (-b - ((delta**(1/2))))/(2*a)
  print(f"X1 = {x1} e X2 = {x2}")
else:
  print("dados errados")
  
print("fim do programa")
  