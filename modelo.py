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
        self._nome = novo_nome.title()


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
      



class Playlist(list):
    def __init__(self, nome, progamas):
        self.nome = nome
        self.programas = progamas



    



 



vingadores = Filme("Vingadores guerra infinita", 2018, 160)
todo_mundo_panico = Filme("Todo mundo em panico", 1999,100 )
demolidor= Serie("Demolidor",2016,2)
atlanta = Serie("Atlanta", 2018, 2)



vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
demolidor.dar_like()
demolidor.dar_like()
todo_mundo_panico.dar_like()
todo_mundo_panico.dar_like()
atlanta.dar_like()
atlanta.dar_like()





filmes_e_series = [vingadores, atlanta, demolidor, todo_mundo_panico]
playlist_fim_de_semana = Playlist("Fim de Semana", filmes_e_series)






for programa in playlist_fim_de_semana.programas:
    print(programa)
