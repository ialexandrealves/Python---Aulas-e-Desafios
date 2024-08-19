import random

valor_aleatorio = random.randint(1,10)

acerto = False
 
while acerto == False:
    chute = int(input("Insira um numero: "))
    if chute > valor_aleatorio:
        print("Valor maior que o numero")
    elif chute < valor_aleatorio:
        print("valor menor que o numero")
    elif chute == valor_aleatorio:
        print("Acertou!")
        acerto = True
    
