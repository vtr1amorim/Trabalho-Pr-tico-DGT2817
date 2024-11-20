# Inicializando a variável de controle de saída
saida = ''

# Função para realizar a adição
def adicao(a, b):
    return a + b

# Função para realizar a subtração
def subracao(a, b):
    return a - b

# Função para realizar a multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a divisão
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

# Função calculadora que chama as funções de operação dependendo do tipo de operação
def calculadora(num1, num2, operacao):
    resultado = 0
    if operacao == '+' or operacao == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao':
        resultado = subracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisao':
        resultado = divisao(num1, num2)
    return resultado

# Laço while que mantém o programa ativo até o usuário decidir sair
while saida.lower() != 'n':
    # Solicita os dados ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (pode ser o nome ou o sinal da operação: +, -, *, /): ").strip()

    # Chama a função calculadora e armazena o resultado
    resultado = calculadora(num1, num2, operacao)

    # Exibe o resultado da operação
    print(f"Resultado da operação: {resultado}")

    # Pergunta ao usuário se ele deseja continuar
    saida = input("Deseja continuar? (S/N): ").strip()

# Fim do programa
print("Programa encerrado.")