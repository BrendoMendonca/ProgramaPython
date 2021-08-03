'''Programa que mostra a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa é interrompido quando o número solicitado for negativo. '''

while True:
    num = int(input("Digite um número: "))
    if num < 0:
        break
    print(f"Tabuada de multiplicação do número {num}")
    for i in range(0, 11, 1):
        print(f"{num} x {i} = {i*num}")