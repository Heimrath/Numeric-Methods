import numpy as np
import sympy as sp

def regra_trapezio(funcao, limite_inferior, limite_superior, num_trapezios, casas_decimais):
    funcao_sympy = sp.simplify(funcao)                                                          # Simplificando a função
    funcao_lambda = sp.lambdify('x', funcao_sympy, 'numpy')                                     # Convertendo a função para lambda
                                                 
    # Criando os pontos
    valores_x = np.linspace(limite_inferior, limite_superior, num_trapezios + 1)                # Criando os pontos x igualmente espaçados
    valores_y = funcao_lambda(valores_x) # Criando os pontos y

    # Calculando a soma dos trapézios
    h = (limite_superior - limite_inferior) / num_trapezios # Calculando o h
    integral_aproximada = h * (valores_y[0] / 2 + sum(valores_y[1:-1]) + valores_y[-1] / 2)     # Calculando a integral aproximada

    # Calculando o erro de arredondamento
    erro_arredondamento = num_trapezios * (0.5 * 10**(-casas_decimais)) * h                      

    # Exibindo a tabela
    print("\nTabela de valores: \n")
    print(f"{'x':<15}{'f(x)':<15}")
    print("-" * 30)
    for xi, yi in zip(valores_x, valores_y):                                                    # Agrupa em pares x e y
        print(f"{xi:<15.{casas_decimais}f}{yi:<15.{casas_decimais}f}")                          
    print("-" * 30)

    # Exibindo os resultados
    print(f"\nResultado da soma dos trapézios: {integral_aproximada:.{casas_decimais}f}")
    print(f"Erro de arredondamento: {erro_arredondamento:.{casas_decimais + 1}f}")

# Entrada do usuário
funcao = input("Digite a função f(x): ").lower()
limite_inferior = float(sp.simplify(input("Digite o limite inferior: ")))
limite_superior = float(sp.simplify(input("Digite o limite superior: ")))
num_trapezios = int(input("Digite o número de trapézios: "))
casas_decimais = int(input("Digite o número de casas decimais: "))

# Chamando a função
regra_trapezio(funcao, limite_inferior, limite_superior, num_trapezios, casas_decimais)