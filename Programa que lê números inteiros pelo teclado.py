""" Programa que lê números inteiros pelo teclado.
O programa para quando o usuário digitar o valor 999.
No final, mostra quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)."""

soma = quantidade = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    quantidade +=1
    soma += n

print(f"Você digitou {quantidade} número(s) e a soma deles é: {soma}")