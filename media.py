nome = float(input('Escreva o Nome do aluno: '))
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
resultado = (nota1 + nota2) / 2
print(f'Nome: [nome]')
print(f'Resultado:'[resultado])

if resultado >= 5:
    print('Parabéns Você foi aprovado!')


elif resultado <= 4:
    print ('Você foi reprovado!')