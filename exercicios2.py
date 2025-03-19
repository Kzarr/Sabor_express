from getpass import getpass
#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
def numero_impar_par():
    try: #try except para evitar entradas inválidas
        numero = int(input('Escolha um número: '))
    except ValueError:
        print('Por favor, insira um número válido')
        return # return para encerrar a função caso encontre um erro

    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')

# 2 Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo 
# com as seguintes condições:
# Criança: 0 a 12 anos; 
# Adolescente: 13 a 18 anos; 
# Adulto: acima de 18 anos.

def qual_faixa_etaria():
    idade = int(input('Diga-me sua idade e direi a qual sua faixa etária: '))

    if idade <= 12:
        print('Você é uma criança')
    elif 13 <= idade <= 18:
        print('Você é um(a) adolescente')
    else:
        print('Você é adulto(a)')

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos 
# correspondem aos valores esperados determinados por você.
nome_registrado = 'Matheus'
senha_registrada = 'MT222'
def checando_credenciais():
    tentativas = 3
    
    while tentativas > 0:
        nome_inserido = input('Por favor, diga-me seu nome: ').strip
        senha_inserida = getpass('Por favor, diga-me sua senha: ').strip

        if nome_inserido == nome_registrado and senha_inserida == senha_registrada:
            print('Login bem-sucedido!')
            break
        else:
            tentativas -= 1
            print(f'Nome de usuário ou senha incorretos. Tentativas restantes: {tentativas}')

    if tentativas == 0:
        print('Número máximo de tentativas permitidas. Tente novamente mais tarde')

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual 
# quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições: 
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

def qual_seu_quadrante():
    try: # método para verificar se o valor inserido é um número válido
        x = int(input('Por favor, insira a coordenada x: '))
        y = int(input('Por favor, insira a coordenada y: '))
    except ValueError:
        print('Por favor, insira valores numéricos inteiros válidos.')
        return # return para a função não continuar caso o valor interido seja NaN
    
    if x > 0 and y > 0:
        print('Você se encontra no primeiro quadrante cartesiano.')
    elif x < 0 and y > 0:
        print('Você se encontra no segundo quadrante cartesiano.')
    elif x < 0 and y < 0:
        print('Você se encontra no terceiro quadrante cartesiano.')
    elif x > 0 and y < 0:
        print('Você se encontra no quarto quadrante cartesiano.')
    else:
        if x == 0 and y == 0:
            print('O ponto está localizado na origem.')
        elif x == 0:
            print('O ponto está localizado no eixo Y.')
        elif y == 0:
            print('O pronto está localizado no eixo X.')

