class Programa:
     

    def __init__(self, nome, ano):
        self._nome  = nome.title()
        self.ano   = ano
        self._likes = 0




    @property
    def likes(self):
        return self._likes


    def dar_likes(self):
        self._likes += 1


    @property
    def nome(self):
        return self._nome


    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.tittle()




class Filme(Programa):


    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)   # super() CHAMA o inicializdor da CALSSE MÃE (PROGRAMA)
        self.duracao = duracao
       
       

 

class Serie(Programa):


    def __init__(self, nome, ano, temporadas):
        self._nome      = nome.title()
        self.ano        = ano
        self.temporadas = temporadas
        self._likes     = 0


   

      







vingadores = Filme("Vingadores - guerra infinita", 2018, 160)
print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}, Likes: {vingadores.likes}")

atlanta = Serie("Atlanta", 2018, 2)
print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}- Likes {atlanta.likes}")



