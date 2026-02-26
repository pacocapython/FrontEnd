q = int(input('digite a quantidade de minutos que você consumiu '))

a = q - 100
b = a * 2.00
c = 50 + b

if q >= 100:
    print("O valor que você terá que pagar é", c)
if q > 100:
    print(f'você utilizou todos os minutos pagos, serão cobrados R${b} a mais')
elif q < 100:
    print(f'não há valor a ser pago')
#GABRIEL GUSTAVO SOUZA DE VARGAS