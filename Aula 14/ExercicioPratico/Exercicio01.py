def patos_coelhos( tc, tp):
    coelhos = (tp - 2 * tc) / 2
    patos = tc - coelhos
    return patos, coelhos

tc = 1
tp = 4

patos, coelhos = patos_coelhos(tc,tp)

print(f'''Total de patos = {patos} 
Total de coelhos = {coelhos}''')
