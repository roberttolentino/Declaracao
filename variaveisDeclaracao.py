nomeDestinatario = input("Digite o nome do destinatário: ")
nomeCliente = input("Digite o nome do Cliente: ")
nomeEvento = input("Digite o nome do evento: ")
qtdeEntrada = float(input("Digite o valor da entrada: "))
qtdeConsumacao = float(input("Digite o valor da consumação: "))
print("Declaro para o senhor " + nomeDestinatario + " que o senhor " + nomeCliente
      + " esteve presente no evento " + nomeEvento)
print(" pagou para entrar um valor de R$ ", qtdeEntrada)
if qtdeConsumacao <= 0:
    print("sem consumação no local")
else:
    print(" e consumiu o valor de R$ ", qtdeConsumacao)
