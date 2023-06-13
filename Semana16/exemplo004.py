def entrada():
    try:
        n1 = int(input('informe um número: '))
    except ValueError:
        return None
    else:
        return n1
    finally:
        print('Fim da execução...')

print(entrada())