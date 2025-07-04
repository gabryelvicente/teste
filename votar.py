print('Escolha a sua opção: \n 1 = Branco \n 2 = Verde \n 3 = Vermelho')
escolha = int(input('Digite a sua opção: '))
if (escolha == 1):
    print('Votação encerrada! Você escolheu branco.')
elif (escolha == 2):
    print('Votação encerrada! Você escolheu verde.')
elif (escolha == 3):
    print('Votação encerrada! Você escolheu vermelho.')
else:
    print('Voto inválido. Refaça o voto.')