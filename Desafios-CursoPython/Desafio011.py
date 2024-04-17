largura = float(input('Qual a largura de sua parede: '))
altura = float(input('Qual a altura de sua parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, area))
tinta = area / 2
print('para pintar essa parede, você precisará de {}l de tinta'.format(tinta))