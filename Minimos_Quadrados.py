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

import matplotlib.pyplot as plt
from math import sqrt
import sys

class MinQuadrados:
    N = 0

    def __init__(self, valores_x, valores_y):
        MinQuadrados.N = len(valores_x)
        self.valores_x = valores_x
        self.valores_y = valores_y
        print(f"\nx = {self.valores_x}")
        print(f"y = {self.valores_y}")

        self.chama_metodos()

    def formatar(self, valor):
        return f"{valor:.6f}".rstrip('0').rstrip('.')

    def medias(self):
        self.soma_x = sum(self.valores_x)
        self.soma_y = sum(self.valores_y)
        self.soma_xy = sum(x * y for x,y in zip(self.valores_x, self.valores_y))

        self.media_x =  self.soma_x / MinQuadrados.N
        self.media_y = self.soma_y / MinQuadrados.N
        self.media_xy = self.soma_xy / MinQuadrados.N

        print(f"\nMédia de x = {self.formatar(self.media_x)}")
        print(f"Média de y = {self.formatar(self.media_y)}")
        print(f"Média de xy = {self.formatar(self.media_xy)}")

    def desvio_padrao(self):
        self.desviop_x = sqrt((sum((x - self.media_x)**2 for x in self.valores_x) / MinQuadrados.N))
        self.desviop_y = sqrt((sum((y - self.media_y)**2 for y in self.valores_y) / MinQuadrados.N))

        print(f"\nDesvio padrão de x = {self.formatar(self.desviop_x)}")
        print(f"Desvio padrão de y = {self.formatar(self.desviop_y)}")

    def covariancia(self):
        self.covariancia_xy = self.media_xy - (self.media_x * self.media_y)

        print(f"\nCovariância (x, y) = {self.formatar(self.covariancia_xy)}")

    def coeficientes(self):
        self.r = self.covariancia_xy / (self.desviop_x * self.desviop_y)   
        
        print(f"\nr (Pearson) = {self.formatar(self.r)}")
        print(f"r^2 (Determinação) = {(self.r**2) * 100:.2f}%")

    def sist_linear(self):
        self.b = (MinQuadrados.N * self.soma_xy - self.soma_x * self.soma_y) / (MinQuadrados.N * sum(x**2 for x in self.valores_x) - self.soma_x * self.soma_x) 
        self.a = (sum(self.valores_y) - sum(self.valores_x) * self.b) / MinQuadrados.N

        print(f"\nf(x) = {self.formatar(self.a)} + {self.formatar(self.b)}x")

        while True:
            try:
                variavel = float(input("\nDigite um valor para x: "))
            except ValueError:
                print("Digite um número válido para x!")
                continue
            else:
                print(self.formatar(self.a + self.b * variavel))
                break

    def grafico(self):
        # Plota os pontos de dispersão
        plt.plot(self.valores_x, self.valores_y, 'go', label="Pontos de dispersão")
        
        # Calcula os valores da reta de regressão
        x_reta = [min(self.valores_x), max(self.valores_x)]  # Usa os extremos de X
        y_reta = [self.a + self.b * x for x in x_reta]       # Calcula os valores correspondentes de Y
        
        # Plota a reta de regressão
        plt.plot(x_reta, y_reta, 'r-', label="Reta de regressão")

         # Adiciona linhas verticais conectando os pontos à reta
        for x, y in zip(self.valores_x, self.valores_y):
            y_na_reta = self.a + self.b * x  # Calcula o valor de Y na reta para o ponto X
            plt.plot([x, x], [y, y_na_reta], 'b--')  # Linha azul tracejada conectando o ponto à reta
        
        # Configurações do gráfico
        plt.xlabel("Eixo X")
        plt.ylabel("Eixo Y")
        plt.title("Reta de regressão linear de X para Y")
        plt.legend()  # Adiciona a legenda
        plt.show()

    def chama_metodos(self):
        try:
            self.medias()
            self.desvio_padrao()
            self.covariancia()
            self.coeficientes()
            self.sist_linear()
            self.grafico()
        except ZeroDivisionError:
            print("\nDivisão por zero! Não será possível continuar, digite novos valores para x e y")
            sys.exit()
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")
            sys.exit()           


def main():
    while True:
        try:
            entrada = input("\nDigite os valores de x separados por espaço: ")
            numeros_x = list(map(float, entrada.split()))

            entrada = input("Digite os valores de y separados por espaço: ")
            numeros_y = list(map(float, entrada.split()))
        except ValueError:
            print("\n---> Insira números válidos para x e y! <---")
            continue
        
        if len(numeros_x) == 0 or len(numeros_x) != len(numeros_y):
            print(f"\nVerifique os numeros inseridos!\nX possui: {len(numeros_x)} numeros\nY possui: {len(numeros_y)} numeros")
            continue

        MinQuadrados(numeros_x, numeros_y)  
         
        # 6 5 8 8 7 6 10 4 9 7
        # 8 7 7 10 5 8 10 6 8 6

       
main()

