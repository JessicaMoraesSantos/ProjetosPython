
# tuplas com as nomenclaturas separadas por categoria
num_menor_20 = ['','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']

dezenas = ['' , '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

centenas = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

numero = int(input('Digite o número: '))

print('-' * 10)
print(f'O numero {numero} por extenso é: ', end='');

if numero == 100:

    print('cem')
    print('-' * 10)

elif numero == 0:

    print('zero')
    print('-' * 10)

else:

    if numero > 100:

        print(centenas[int(str(numero)[0])], end='')

        numero = numero - int(str(numero)[0])*100

        if numero != 0:

            print(' e', end=' ' )
            

    if numero < 20:

        print(num_menor_20[numero])
        print('-' * 10)

        numero = 0

    elif numero >= 20:

        print(dezenas[int(str(numero)[0])], end=' ')
        

        numero = numero - int(str(numero)[0])*10
        
    if numero != 0:

        print('e', num_menor_20[numero])
        print('-' * 10)