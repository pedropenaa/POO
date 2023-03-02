"""

Crie uam classe para representar uma pessoa, com atributos privados nome, idade e altura.
Crie os metodos publicos necessarios para sets e gets e tambem um metodo para imprimir os dados de uma pessoa

"""

class Pessoa:

    def __init__(self, nome, idade, altura):
        self._nome = nome 
        self._idade = idade 
        self._altura = altura


    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        return self._idade
    @property
    def altura(self):
        return self._altura
    
    @nome.setter
    def nome(self, novo_nome):
        self._novo_nome = novo_nome

    @idade.setter
    def idade(self, nova_idade):
        self._nova_idade = nova_idade

    @altura.setter
    def altura(self, nova_altura):
        self._nova_altura = nova_altura



    def __str__(self) -> str:
        return f" Nome: {self._nome}, Idade: {self._idade}, altura: {self._altura} "
    






pessoa = Pessoa("Pedro", 21, 1.87)
print(pessoa)



    
    