# Inicia a repetição contínua
while True:
    
    # Solicita o nome primeiro
    nome = input("Digite o nome: ")
    
    # VALIDAÇÃO DE PARADA: Se digitar 'sair', o break encerra o loop
    if nome == "sair":
        print("Sistema encerrado.")
        break
        
    # Se não digitou 'sair', o programa continua e pede o resto dos dados
    idade = int(input("Digite a idade: "))
    convite = input("Possui convite? S/N: ")
    
    # REGRAS DE ACESSO (if / elif / else com and/or)
    if idade < 16:
        print("Entrada negada")
        
    elif idade >= 16 and convite == "S":
        print("Entrada permitida")
        
    else: # Cai aqui se for maior de 16, mas não tiver convite (convite == 'N')
        print("Entrada negada")