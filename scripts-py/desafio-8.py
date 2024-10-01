# Coverter metros em milimetros e centimetros

m = float(input("Quantos metros você quer converter?\n"))

cm = m * 1000
mm = m * 10000

print('O valor {} em centímetros é {:.2f}\nE em milímetros é {:.2f}'.format(m,cm,mm))