#Ler o nome da cidade e dizer se ela começa ou não com ao nome "SANTO"

cidade = str(input('Em qual cidade você nasceu?')).strip()
print(cidade[:5].upper() == 'SANTO')
