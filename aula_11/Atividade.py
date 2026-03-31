idade = int(input("Informe sua idade:"))
salário = float(input("Informe sua renda mensal:"))
tempo_de_trabalho = float(input("Informe seu tempo de serviço em anos:"))

## Explicação do uso de Int e Float no código:
# O comando input() sempre lê o que o usuário digita como um texto (string).
# Para fazermos contas matemáticas ou comparações, precisamos converter esse texto:
# int()   -> Converte para NÚMEROS INTEIROS (sem casas decimais). 
#            Exemplo: Idade, quantidade de filhos, meses (18, 25, 3).

# float() -> Converte para NÚMEROS REAIS/DECIMAIS (com casas decimais). 
#            Exemplo: Dinheiro, altura, tempo fracionado (2500.50, 1.75, 2.5).



print (f" a idade informada é {idade}, a renda informada é {salário}, o tempo de trabalho informado é {tempo_de_trabalho}")

if idade < 18:
 print("empréstimo negado por conta da idade")
elif salário >= 5000:
 print("empréstimo aprovado com sucesso por conta da renda")
elif idade >= 18 and salário >= 2000 and tempo_de_trabalho >=2:
 print("empréstimo aprovado")

else:
 print("empréstimo não atende aos requisitos")