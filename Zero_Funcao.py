import sys
import sympy as sp


class ZeroFuncao:
    def __init__(self, funcao, a, b, erro):
        self.funcao = funcao
        self.a = a
        self.b = b
        self.erro_esp = erro

    def transformar_funcao(self):
        try:
            # Definimos a variável simbólica x
            x = sp.Symbol('x')
            
            # Transforma a função em uma função simbólica
            f_simbolica = sp.sympify(self.funcao)

            # Transforma em uma função numérica
            self.f = sp.lambdify(x, f_simbolica, 'numpy')
        except ValueError:
            sys.exit("Não foi possível transformar a função fornecida em uma função matemática")


    def calcular_funcao(self, x0):
        f = self.f
        return f(x0)

    def achar_zero(self):
        a = self.a
        b = self.b
        erro_esp = self.erro_esp
        cont = 1
        while True:
            x0 = (a + b) / 2
            erro = (b - a) / 2
            f_a = self.calcular_funcao(a)
            f_b = self.calcular_funcao(b)
            f_x0 = self.calcular_funcao(x0)

            if erro <= erro_esp or f_x0 == 0:
                break

            print(f"a = {a}\nx0{cont} = {x0}\nb = {b}\n|ε| <= {erro}")

            cont += 1

            print(f"\nConsideremos [{a}; {x0}] e [{x0}; {b}]")
            print(f"f({a}) = {f_a:.6f}\nf({x0}) = {f_x0:.6f}\nf({b}) = {f_b:.6f}\n")

            if f_a * f_x0 < 0:
                b = x0
            else:
                a = x0
        
        print(f"O zero da função está em:\nx0{cont} = {x0:.6f}\nf({x0:.6f}) = {f_x0:.6f}")
        print(f"|ε| <= {erro:.6f} < {erro_esp * 100}%")


def main():
    # Recebe a função 
    entrada = input("Digite a função: f(x) = ")

    while True:
        # Recebe os intervalos
        try:
            a = float(input("Intervalo (a) = "))
            b = float(input("Intervalo (b) = "))
        except ValueError:
            print("Digite um valor válido para a e b")
            continue
        break
  
    while True:
        try:
            erro = float(input("Digite o erro em %: "))
            if 0 <= erro <= 100:
                erro = erro / 100
            else:
                raise ValueError
        except ValueError:
            print("Digite um valor entre 0 e 100 para o erro")
            continue
        break
    
    print("----------------------------------------x----------------------------------------")
    zf = ZeroFuncao(entrada, a, b, erro)
    zf.transformar_funcao()
    f_a = zf.calcular_funcao(a)
    f_b = zf.calcular_funcao(b)

    if f_a * f_b >= 0:
        print("Erro: f(a) e f(b) não possuem sinais opostos.")
        print(f"f({a}) = {f_a:.6f}, f({b}) = {f_b:.6f}")
        print("O método da bisseção não pode garantir uma raiz neste intervalo.")            
        sys.exit()

    zf.achar_zero()

if __name__ == "__main__":
    main()