# Verificar se tem a palavra "Silva" no nome

nome = str(input('Qual é seu nome completo?')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))