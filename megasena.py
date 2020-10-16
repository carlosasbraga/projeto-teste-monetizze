from typing import List
import traceback
import random

class QuantidadeInvalida(Exception):
    """
    Exceção garante que valores diferentes dos exigidos para a quantidade de dezenas sejam escolhidos
    """
    def __init__(self, quantidade: int, msg = 'Quantidade de dezenas invalida. Apenas 6, 7, 8, 9 ou 10 são aceitas'):
        self.quantidade = quantidade
        self.message = msg
        super().__init__(self.message)

    def __str__(self):
        return f'{self.quantidade} -> {self.message}'

class MegaSena():
    """
    Classe gera jogos de loteria com 6 a 10 dezenas e sorteia o resultado, dispondo em tabela de html. 

    Obs: Escolhi confiar nos inputs para agilizar o processo de desenvolvimento, pois a única regra de 
    negócio que exige validação da classe seria a definição de quantidadeDesenas.

    Atributos:
        quantidadeDezenas: número de dezenas que será utilizado na geração de jogos; pode apenas estar entre 6 e 10
        totalJogos: número de jogos a serem gerados
        jogos: lista dos jogos gerados; seu tamanho sempre será dado por totalJogos
        resultado: lista de 6 inteiros 
    """
    quantidadesValidas = [6, 7, 8, 9, 10]

    def __init__(self, quantidadeDezenas: int, totalJogos: int):
        self.__totalJogos = int(totalJogos)

        # Aqui garantimos que apenas as quantidades de dezenas válidas sejam utilizadas
        if quantidadeDezenas in MegaSena.quantidadesValidas:
            self.__quantidadeDezenas = quantidadeDezenas
        else:
            raise QuantidadeInvalida(quantidadeDezenas)

    def __gerarUmJogo(self):
        return sorted(random.sample(range(1, 61), self.getQuantidadeDezenas()))

    def gerarJogos(self):
        totalJogos = self.getTotalJogos()
        self.setJogos([self.__gerarUmJogo() for i in range(totalJogos)])

    def sortear(self):
        self.setResultado(sorted(random.sample(range(1, 61), 6)))

    def confereJogos(self) -> str:
        html = '<html><table border="1"><tr><th>Jogo</th><th>Dezenas Sorteadas</th></tr>'
        
        for jogo in self.getJogos():
            numSorteadas = len([num for num in jogo if num in self.getResultado()])
            html += '<tr><td>{}</td>'.format(str(jogo).replace('[', '').replace(']','')) + '<br><td>{}</td>'.format(str(numSorteadas))
            html += "</tr>"

        html += '</table></html>'
        
        return html

    # Getters e setters
    def getQuantidadeDezenas(self) -> int:
        return self.__quantidadeDezenas

    def setQuantidadeDezenas(self, quantidadeDezenas: int):
        # Aqui garantimos que apenas as quantidades de dezenas válidas sejam utilizadas
        if quantidadeDezenas in MegaSena.quantidadesValidas:
            self.__quantidadeDezenas = quantidadeDezenas
        else:
            raise QuantidadeInvalida(quantidadeDezenas)

    def getTotalJogos(self) -> int:
        return self.__totalJogos

    def setTotalJogos(self, totalJogos: int):
        self.__totalJogos = totalJogos

    def getResultado(self) -> List[int]:
        return self.__resultado

    def setResultado(self, resultado: List[int]):
        self.__resultado = resultado

    def getJogos(self) -> List[List[int]]:
        return self.__jogos

    def setJogos(self, jogos: List[List[int]]):
        self.__jogos = jogos

