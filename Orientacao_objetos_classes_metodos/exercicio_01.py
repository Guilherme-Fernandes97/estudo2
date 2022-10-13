# Classes

class TV:

    cor = "Preta"
     
    def __init__(self, tamanho):
        self.ligado = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal


# Programa

tv_sala = TV(55)
tv_quarto = TV(60)

tv_sala.mudar_canal("Globo")
tv_quarto.mudar_canal("Sportv")

print(tv_sala.tamanho)
print(tv_quarto.tamanho)