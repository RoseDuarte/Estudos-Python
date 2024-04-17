atual = float(input('Qual o valor do produto: R$'))
novo = atual - (atual * 5 / 100)

# atual - 5%

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(atual, novo))
