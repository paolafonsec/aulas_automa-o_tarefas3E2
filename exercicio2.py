'''
Exercício 2
------------------------------------------------------------
Crie um programa que recebe 2 numeros reias como entrada e um 
operarador matemático.De acordo com o operarador matematico fornecido
o programa deve calcular e apresentar o resultado da operação.
Exemplo de Entrada
1.2
2.3
+

Exemplo Saida 
O resultado da soma é 3.5
'''

n1 = float(input("Digite um número:  "))
n2 = float(input("Digite um número:  "))
op = input("Digite operador matemático: ")

#processando
if op == '+':
    resultado = n1 + n2
    print('o resultado da soma é' , resultado)
elif op == '-':
    resultado = n1 - n2
    print('o resultado da subtração é' , resultado)
elif op == '/':
    resultado = n1 / n2
    print('o resultado da divisão é' , resultado)
elif op == '*':
    resultado = n1 * n2
    print('o resultado da multiplicação é' , resultado)
else :
    print('Operador desconhecido')
