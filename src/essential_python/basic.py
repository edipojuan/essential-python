def soma(a, b):
    return a + b

x = 5
y = 7
resultado = soma(x, y)

print("Resultado:", resultado)


# Entenda variáveis e tipos de dados (int, float, str, bool).

a = 10
b = 3.5
c = "Olá, Mundo!"
d = True

print(type(a))  # int
print(type(b))  # float
print(type(c))  # str
print(type(d))  # bool

# Aprenda a usar print() para exibir saída e input() para receber entrada.

nome = 'test' # input("Digite seu nome: ")
print("Olá,", nome)

# Conheça indentação (essencial em Python).

if a > 5:
    print("a é maior que 5")
else:
    print("a é 5 ou menor")

# Condicionais (if, elif, else) para tomada de decisões.

nota = 85
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("F")

# Laços de repetição (for, while) para iterações.

for i in range(5):
    print("Número:", i)

# Compreenda break e continue para controle de fluxos.

contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue  # Pula o número 5
    if contador == 8:
        break  # Sai do loop quando contador é 8
    print("Contador:", contador)

# Listas ([]) para coleções ordenadas.

frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")
print(frutas)

# Dicionários ({}) para pares chave-valor.

pessoa = {"nome": "Alice", "idade": 30}
print(pessoa["nome"])

# Tuplas e conjuntos (básico, para entender diferenças).

tupla = (1, 2, 3)
conjunto = {1, 2, 3, 3}  # Conjunto não permite duplicatas
print(tupla)
print(conjunto)

# Operações como append, pop, e slicing.

frutas.pop()  # Remove o último item
print(frutas)
print(frutas[0:2])  # Slicing
print(frutas)

# Defina funções com def nome_funcao():

def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))

# Entenda parâmetros, retorno (return) e escopo de variáveis.

def multiplicar(x, y=2):  # y tem valor padrão
    return x * y

print(multiplicar(5))  # Usa o valor padrão de y
print(multiplicar(5, 3))  # Sobrescreve o valor padrão

# Explore funções built-in (ex.: len(), range()).

print(len(frutas))  # Tamanho da lista
print(list(range(3)))  # [0, 1, 2]

# Use try, except para lidar com exceções (ex.: erros de divisão por zero).

try:
    resultado = 10 / 0
except Exception as e:
    print(f"Erro: Divisão por zero não é permitida. {e}")

# Experimente com bibliotecas básicas como math ou random.

import math
import random
print(math.sqrt(16))  # Raiz quadrada
print(random.randint(1, 10))  # Número aleatório entre 1 e
print(random.choice(frutas))  # Escolhe uma fruta aleatória
