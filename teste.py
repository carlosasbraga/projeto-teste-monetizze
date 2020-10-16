from megasena import MegaSena

teste = MegaSena(6, 3)
teste.gerarJogos()
teste.sortear()

print(teste.getQuantidadeDezenas())
print(teste.getTotalJogos())
print(teste.getJogos())
print(teste.getResultado())

with open('resultados_loteria.html', 'w') as f:
    f.write(teste.confereJogos())