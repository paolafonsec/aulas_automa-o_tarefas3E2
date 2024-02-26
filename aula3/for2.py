#Repetição simples: 10 vezes - de 0 a 9
for i in range(0,10):
    print(i, "Vezes")
    
    #Repetição com passo <> 1: repetição 5 vezes de 2 em dois 
    print("Exemplo 2")
for i in range(0,10, 2):
    print(i,"número")

    #Repetição decrescente
    print("Exemplo 3")
for i in range(10,0,-1):
    print(i,"Número")

    #Repetição com lista
    print("Exemplo 4.1 - imprime o nome da lista")
    alunos = ["Julia","kayky","Inessa","Adriano"]
for nome in alunos:
    print(nome)

    print("Exemplo 4.2 - imprime posição e nome")
for index, nome in enumerate (alunos):
    print(index,nome)

