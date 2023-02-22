class Cliente:



    def __init__(self, nome):
        self.__nome = nome




    #@property é uma propriedade para substituir a função get_nome()
    @property 
    def nome(self):
        return self.__nome.title()


    #@setter mesma coisa que a função set_nome()
    @nome.setter
    def nome(self, nome):
        self.__nome= nome
        



    