velocidade_usuario = int (input('Insira a velocidade:'))

if velocidade_usuario < 80:
    print('Não houve multa')
elif velocidade_usuario < 90:
    print('Não houve multa')
elif velocidade_usuario > 90:
    print('Levou multa leve')
elif velocidade_usuario > 91 and 100:
    print ('levou multa grave')
elif velocidade_usuario > 110:
    print('Levou multa gravissima')        