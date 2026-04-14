idade = int (input ("informe a sua idade:") )
nota = float (input ("informe a sua nota:") )
frequencia = float (input ("informe a taxa de frequencia:") )



print (f" a idade informada é {idade} anos, a nota informada é {nota}, a frequencia informada é {frequencia}%")


if idade < 18:
    print ("matricula negada por conta da idade")
elif nota > 9:
    print ("matricula aprovada por conta da nota")
elif idade >= 18 and nota >= 6 and frequencia >= 75:
    print ("matricula aprovada") 
else:
    print ("matricula negada por não atender aos requisítos mínimos")