num = int(input('Digite um número para verificar se este é triangular: '))

# def numeroTriangular(num):
#     numComparacao = 0
#     teste = 0
#     while teste < num:
#         numComparacao += 1
#         teste = numComparacao * (numComparacao + 1) * (numComparacao + 2)
    
#     if teste == num:
#         return True
#     else:
#         return False
    
def numeroTriangular(num):
    for i in range(1, num+1):
        if (i * (i+1) * (i+2)) == num:
            return True
    return False


if numeroTriangular(num):
    print('O número digitado é triangular!')
else:
    print('O número digitado não é triangular!')