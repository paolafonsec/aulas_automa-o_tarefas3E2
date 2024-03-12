'''
Exercicio 3
--------------------------------------------------------------------------------
Crie um programa que execute reoitivamente o programa do 
exercicio 2.Apos a apresentaçãodo do resultado o programa deve
pergunta se o usúario deseja continuar a calcular, se a resposta 
for S (Sim) o programa deve continuar se a resposta for N (Não)
 o programa deve terminar.
 '''

while True:
     desejo = input("Desejo continuar? [S/N]")
     if desejo == "N" :
          break
     else:
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
    
    