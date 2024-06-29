nome  = input('Escreva o Nome do aluno: ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
resultado = (nota1 + nota2 + nota3 + nota4) / 4
print('Nome:',nome)
print('A média final foi: %.1f' %resultado)

if resultado >= 5:
    print('Parabéns Você foi aprovado!')

else:
    print ('Você foi reprovado!')