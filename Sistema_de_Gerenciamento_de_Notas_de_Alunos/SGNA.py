
MEDIA_APROVACAO = 7.0
MEDIA_RECUPERACAO = 5.0
boletim_turma = []

print('🏫  Bem-vindo ao Sistema Escolar ')


while True:
    print('''  Menu Principal 
          [1] - Cadastrar Alunos
          [2] - Ver Boletim da Turma
          [3] - Sair
          ''')
    
    
    opcao = input(' Escolha uma opção: ')
    
    
    if opcao == '1':
        
        qtd_alunos = int(input('➡️  Quantos alunos serão cadastrados? '))
        
        
        for contador in range(0, qtd_alunos):
            print(f'📝   Cadastro do {contador + 1}º Aluno ---')
            nome = input('Nome do aluno: ')
            
            
            nota1 = float(input('Digite a 1ª nota: '))
            nota2 = float(input('Digite a 2ª nota: '))
            nota3 = float(input('Digite a 3ª nota: '))
            
            
            media = (nota1 + nota2 + nota3) / 3
            
            
            if media >= MEDIA_APROVACAO:
                situacao = 'Aprovado'
            elif media >= MEDIA_RECUPERACAO and media < MEDIA_APROVACAO:
                situacao = 'Recuperação'
            else:
                situacao = 'Reprovado'
                
            
            registro = f'🎓 Aluno: {nome} | Notas: {nota1:.1f}, {nota2:.1f}, {nota3:.1f} | Média: {media:.2f} | Situação: {situacao}'
            
            
            boletim_turma.append(registro)
            print(' Aluno cadastrado com sucesso!')

    elif opcao == '2':
        print(' Boletim Completo da Turma ')
        
        if not boletim_turma:
            print(' Nenhum aluno foi cadastrado ainda.')
        else:
            for aluno in boletim_turma:
                print(aluno)
                
    elif opcao == '3':
        print('❌  Finalizando o sistema escolar. Até logo!')
        break 
        
    else:
        print('❌  Por favor, escolha uma das opções do menu.')