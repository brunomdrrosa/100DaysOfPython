# Soma
def somar(n1, n2):
  return n1 + n2

# Subtração
def subtrair(n1, n2):
  return n1 - n2

# Multiplicação
def multiplicar(n1, n2):
  return n1 * n2

# Divisão
def dividir(n1, n2):
  return n1 / n2

# Dicionário com as operações
operacoes = {
  "+": somar,
  "-": subtrair,
  "*": multiplicar,
  "/": dividir,
}

from arteCalculadora import logo

def calculadora():
    print(logo)

    numero1 = float(input("Qual o primeiro número? "))
    for key in operacoes:
        print(key)
    continuar = True

    while continuar:
        simbolo_operacao = input("Escolha uma operação da linha acima: ")
        numero2 = float(input("Qual o segundo número? "))
        funcao_calculadora = operacoes[simbolo_operacao]
        resposta = funcao_calculadora(numero1, numero2)

        print(f"{numero1} {simbolo_operacao} {numero2} = {resposta}")

        if input(f"Digite 'S' para continuar calculando com {resposta}, ou digite 'N' para abrir a calculadora novamente: ") == "S":
            numero1 = resposta
        else:
            continuar = False
            calculadora()

calculadora()