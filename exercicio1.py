'''
Exercicio 1
----------------------------------------------------------------------------------------------------------
Crie um programa que receba entrada dois numeros reias 
O programa deve imprimir as quatros operaçoes matematicas entre 
os dois números (soma,subtração,divisao, e multiplicação).
'''
n1 = float(input('Digite o primeiro número1:' ))
n2 = float(input('Digite o segundo número2:' ))

subtracao=n1 - n2
soma =n1 + n2
divisao= n1 / n2
multiplicacao = n1 * n2

print(f"Subtração: {subtracao}")
print(f"Soma: {soma}")
print(f"divisao: {divisao}")
print(f"multiplicacao: {multiplicacao}")