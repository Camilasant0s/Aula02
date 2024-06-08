#Solicitar ao usuario para digitar dois números
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número:'))

#Operações Aritméticas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
divisao_inteira = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2

#Exibir os Resultados
print("\n Resultados das Operações Aritmeticas")
print("Soma:", soma)
print("Substração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Divisão Inteira:", divisao_inteira)
print("Módulo:", modulo)
print("Potência:", potencia)

#Comparações com operações
print("\n Resultados das operações com Comparações")
print("Igualdade:", num1 == num2)
print("Diferença:",num1 != num2)
print("Maior:", num1 > num2)
print("Menor:", num1 < num2)
print("Maior ou Igual:", num1 >= num2)
print("Menor ou Igual:", num1 <= num2)

#Operações de Atribuição
print("\n Resultados dos Operadores de Atribuições")
num1 += 5
print("num1 +=5:", num1)
num2 /= 2
print("num2/2:", num2)

#Verificar Presença na lista de Elementos
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if num1 in lista_numeros:
    print(f"o número {num1} está na lista de números")
else:
    print(f"o número {num1} não está na lista de números")


#Compare a identidade de objetos
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("\n Resultados das Operações de Identidade de Objetos")
print("x is z:", x is z)
print("x is y:", x is y)
print("x is not y:", x is not y)

