velocidade = int(input('Digite a velocidade que o veículo alcançou na via: '))
multa = (velocidade - 80) * 7
print('Você estava passando pela via e acabou encontrando um radar!!')
if velocidade > 80:
    print('Infelizmente o seu carro estava a {}Km/h, ultrapassando o limite de 80Km/h, portanto sua multa será de R${:.2f}.'.format(velocidade, multa))
else:
    print('Você estava a {}Km/h, dentro do limite da via, portanto siga viagem!!'.format(velocidade))
print('Você chegou ao seu destino!!')
