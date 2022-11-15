print('{:=^40}'.format(' LOJAS MICHELLE MENDES '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparcelas = int(input('Quantas parcela? '))
    parcela = total / totalparcelas
    print('Sua compra será parcela em 2x de R$ {:.2f} COM JUROS'.format(totalparcelas, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')
print('Sua compra de {:.2f} vai custar R$ {:.2f} no final.'.format(preço, total))
