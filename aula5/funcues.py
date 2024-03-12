'''
As funções são utilizadas para modular o código, ou seja,
dividi-lo em partes menores, que podem ser reutilizadas.

Estrutura:
 
def nome_funcao(param1, param2):
    faz algo
    return valor

Exemplo:
'''
#função 1
def calcularAreaTriangulo(base,altura):
    area = (base * altura) / 2
    return area

def login(usuario, senha):
    if usuario == 'admin' end senha == '123':
       return True
    else:
        return False
    
#chamar a função
login("ivan, '123")