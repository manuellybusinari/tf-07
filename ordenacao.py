def quick_sort(valores):
    if len(valores) <= 1:
        return valores

    pivo = valores[len(valores) // 2]

    menores = [x for x in valores if x < pivo]
    iguais = [x for x in valores if x == pivo]
    maiores = [x for x in valores if x > pivo]

    return quick_sort(menores) + iguais + quick_sort(maiores)


# Testando o algoritmo com uma lista fora de ordem
print(quick_sort([7, 3, 9, 1, 5]))