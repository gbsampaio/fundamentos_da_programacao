idade = int(input("Informe a idade do motorista: "))
tipo_veiculo = input("Informe o tipo de veículo (carro, moto, caminhao, onibus): ")
cadastro = input("Possui cadastro no shopping? (sim/nao): ")
vip = input("É cliente VIP? (sim/nao): ")

print(f"Resumo: Motorista com {idade} {'ano' if idade == 1 else 'anos'}, veículo do tipo {tipo_veiculo}. Cadastro: {cadastro}. VIP: {vip}.")

if idade < 18:
    print("Entrada negada: Motorista menor de idade não pode entrar dirigindo.")
    
elif tipo_veiculo == "caminhao" or tipo_veiculo == "onibus":
    print("Entrada negada: Veículos de grande porte não permitidos.")

elif vip == "sim":
    print("Entrada aprovada: Cliente VIP reconhecido (liberação rápida).")
    
elif cadastro == "sim":
    print("Entrada aprovada: Cliente possui cadastro ativo.")

else:
    print("Entrada negada: O veículo não atende aos requisitos do estacionamento.")