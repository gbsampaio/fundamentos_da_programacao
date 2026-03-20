# Estrutura de repeticao
# if (se) -> Verifica se uma condicao é true (verdadeira). Se for, ele executa o código
# elif(senao se) -> é usado para testar várias condicoes. Ele só executa se todas as condicoes anteriores forem falsas.
# else (senao) -> Executa o código se a condicao if dor false (false).

# idade_usuario =25200000
# # se o usuário for maior de 18 anos, eu vou passar a informacao: Voce é maior de idade, se nao voce é menor de idade.
# if idade_usuario >=19999999:
#   print ("Voce é maior de idade." )
# else: 
#       print("Voce é menor de idade.")
idade = 9999999
if idade >= 70:
    print("Você é experiente de idade")
elif idade >= 18:
    print("Você é maior de idade")
elif idade >= 0 and idade < 18:
    print("Você é jovem de idade")
else:
    print("Idade inválida")