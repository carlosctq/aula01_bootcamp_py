
# 1) Solicita ao usuário que digite seu nome

nome = input('Digite o seu nome: ')

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

salario = float(input('Digite o seu salario: '))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

constante_bonus = 1000

bonus = float(input('Digite o seu bonus (ATENCAO: o bonus e percentual 1.0 para 100 porcento etc): '))

# 4) Calcule o valor do bônus final
valor_bonus = constante_bonus + salario * bonus

# 5) Imprima cálculo do KPI para o usuário

print(f'O calculo do seu bonus é 1.000 + {salario} + {bonus}')

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

print(f'O funcionario {nome} recebera R$ {valor_bonus:.2f}'.replace('.',','))

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
