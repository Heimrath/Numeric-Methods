'''
    média de X - seis decimais, se não for exato
    média de Y - seis decimais, se não for exato
    média de XY - seis decimais, se não for exato
    desvio padrão de X - seis decimais, se não for exato
    desvio padrão de Y - seis decimais, se não for exato
    covariância de X e Y - seis decimais, se não for exato
    coeficiente de correlação de Pearson - seis decimais, se não for exato
    coeficiente de determinação - esse em porcentagem e com duas casas de arredondamento
    sistema linear (para ter as somas)
    equação da reta de regressão linear de X em função de Y (com seis casas decimais de arredondamento)
    escolhendo um valor qualquer para a variável independente, obter a resposta: valor da variável dependente por meio da equação da reta de regressão linear (com seis casas decimais de arredondamento)
    Se possível uma representação gráfica dos pontos plotados (dispersão) e a reta de regressão
'''

from math import sqrt


class MinQuadrados:
    N = 0

    def __init__(self, valores_x, valores_y):
        MinQuadrados.N = len(valores_x)
        self.valores_x = valores_x
        self.valores_y = valores_y
        print(f"X = {self.valores_x}")
        print(f"Y = {self.valores_y}")

    def formatar(self, valor):
        return f"{valor:.6f}".rstrip('0').rstrip('.')

    def medias(self):
        self.media_x = (sum(self.valores_x) / MinQuadrados.N)
        self.media_y = sum(self.valores_y) / MinQuadrados.N
        self.media_xy = sum(x * y for x,y in zip(self.valores_x, self.valores_y)) / MinQuadrados.N
        print(f"Média de X = {self.formatar(self.media_x)}")
        print(f"Média de Y = {self.formatar(self.media_y)}")
        print(f"Média de XY = {self.formatar(self.media_xy)}")

    def desvio_padrao(self):
        self.desviop_x = sqrt((sum((x - self.media_x)**2 for x in self.valores_x) / MinQuadrados.N))
        self.desviop_y = sqrt((sum((y - self.media_y)**2 for y in self.valores_y) / MinQuadrados.N))
        print(f"Desvio padrão de X = {self.formatar(self.desviop_x)}")
        print(f"Desvio padrão de Y = {self.formatar(self.desviop_y)}")

    def covariancia(self):
        self.covariancia_xy = self.media_xy - (self.media_x * self.media_y)
        print(f"Covariância (X, Y) = {self.formatar(self.covariancia_xy)}")

    def coeficientes(self):
        self.r = self.covariancia_xy / (self.desviop_x * self.desviop_y)
        print(f"r (Pearson) = {self.formatar(self.r)}")
        print(f"r^2 (Determinação) = {(self.r**2) * 100:.2f}%")



def main():
    while True:
        entrada = input("Digite os valores de x separados por espaço: ")
        numeros_x = list(map(float, entrada.split()))

        entrada = input("Digite os valores de y separados por espaço: ")
        numeros_y = list(map(float, entrada.split()))

        if len(numeros_x) != len(numeros_y):
            print(f"Verifique os numeros inseridos!\nX possui: {len(numeros_x)} numeros\nY possui: {len(numeros_y)} numeros")
            continue

        quad = MinQuadrados(numeros_x, numeros_y)
        
        quad.medias()
        quad.desvio_padrao()
        quad.covariancia()
        quad.coeficientes()
       
main()

