soma_total = 0

while True:
    m = int(input("Digite o valor de m (positivo): "))
    n = int(input("Digite o valor de n (positivo): "))

    if m <= 0 or n <= 0:
        print("Os valores devem ser positivos. Tente novamente.")
        continue

    if m <= n:
        print("O valor de m deve ser maior que n. Tente novamente.")
        continue

    soma = 0
    for i in range(n, m + 1):
        soma += i

    soma_total += soma

    opcao = input("Deseja digitar mais pares de valores? (S/N): ")
    if opcao.lower() != "s":
        break

print("A soma total é:", soma_total)
