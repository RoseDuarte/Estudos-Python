salario = float(input('Qual o salário do funcionario: R$'))
reajuste = salario + (salario * 15 / 100)

print('O salário do funcionário era R${:.2f}, com o rajuste de 15%, o novo salário fica R${:.2f}'.format(salario, reajuste))