class Programa:
     

    def __init__(self, nome, ano):
        self._nome  = nome.title()
        self.ano   = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.tittle()


    def  __str__ (self):
        return f"{self._nome}  - {self.ano} - {self._likes} Likes"





class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)   # super() CHAMA o inicializdor da CALSSE MÃE (PROGRAMA) , reduz codigo repetitivo
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome}  - {self.ano} - {self.duracao} min  - {self._likes} Likes"

       

 

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome}  - {self.ano} - {self.temporadas} temporadas  - {self._likes} Likes"
      










# EXEMPLO DE FILMEEEEE
vingadores = Filme("Vingadores guerra infinita", 2018, 160)
vingadores.dar_like()




# EXEMPLO DE SERIE
atlanta = Serie("Atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()




filmes_e_series = [vingadores, atlanta]
for programa in filmes_e_series:
    print(programa)
