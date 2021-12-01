import random

def jogar():
    imprimir_mensagem_de_abertura()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = letras_acertadas_com_(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)

        else: 
            erros += 1

        enforcou = erros == 3
        acertou = '_' not in letras_acertadas
        print('\n')
        print(letras_acertadas)
        print(f'\nErros : {erros} / 3')

    if(acertou):
        imprimir_mensagem_vencedor()
    else:
        imprimir_mensagem_perdedor(palavra_secreta)

    print('Fim do jogo')

# Imprimir mensagem de abertura
def imprimir_mensagem_de_abertura():
    print('=' * 26)
    print('BEM VINDO AO JOGO DA FORCA')
    print('=' * 26)

# Carregar arquivo .txt onde se encontram as palavras
def carregar_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip() # Retira os espaços em branco no começo e no fim da string
        palavras.append(linha) # Adiciona um item ao fim da lista
    arquivo.close()

    numero = random.randrange(0, len(palavras)) 
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

# Retorna '_' para cada letra da palavra
def letras_acertadas_com_(palavra_secreta):
    return['_' for letra in palavra_secreta]

# Recebe letra informada pelo usuário
def pede_chute():
    print('=' * 26)
    chute = input('Qual letra?')
    chute = chute.strip().upper()
    return chute 

# Se a letra informada pelo usuário for igual a letra contida na palavra sorteada, adicionar a letra na posição correta
def marca_chute_correto(chute, letras_acertdas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_acertdas[posicao] = letra
        posicao = posicao + 1

def imprimir_mensagem_vencedor():
    print('Parabéns, você ganhou!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprimir_mensagem_perdedor(palavra_secreta):
    print('=' * 26)
    print('Poxa, você foi enforcado! :(')
    print('===> A palavra era {}'.format(palavra_secreta))

