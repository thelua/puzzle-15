class Tabuleiro:
    def __init__(self, inicio):
        valores = inicio.split(" ")
        self.LADO = int(len(valores) ** 0.5) 
        self.estado = []
        index = 0
        for i in range(self.LADO):
            linha = []
            for j in range(self.LADO):
                valor = int(valores[index])
                linha.append(valor)
                index += 1
            self.estado.append(linha)


    def imprimir_tabuleiro(self):
        print("+", end="")
        for _ in range(self.LADO):
            print("------+", end="")
        print()
        for linha in self.estado:
            print("|", end="")
            for valor in linha:
                print("  {:<3} |".format(valor), end="")
            print("\n+", end="")
            for _ in range(self.LADO):
                print("------+", end="")
            print()
        print()

    def encontrar_posicao_vazia(self):
        for i in range(self.LADO):
            for j in range(self.LADO):
                if self.estado[i][j] == 0:
                    return i, j

    def cima(self):
        linha_vazia, coluna_vazia = self.encontrar_posicao_vazia()
        if linha_vazia < self.LADO - 1:
            self.estado[linha_vazia][coluna_vazia] = self.estado[linha_vazia + 1][coluna_vazia]
            self.estado[linha_vazia + 1][coluna_vazia] = 0

    def baixo(self):
        linha_vazia, coluna_vazia = self.encontrar_posicao_vazia()
        if linha_vazia > 0:
            self.estado[linha_vazia][coluna_vazia] = self.estado[linha_vazia - 1][coluna_vazia]
            self.estado[linha_vazia - 1][coluna_vazia] = 0

    def direita(self):
        linha_vazia, coluna_vazia = self.encontrar_posicao_vazia()
        if coluna_vazia > 0:
            self.estado[linha_vazia][coluna_vazia] = self.estado[linha_vazia][coluna_vazia - 1]
            self.estado[linha_vazia][coluna_vazia - 1] = 0

    def esquerda(self):
        linha_vazia, coluna_vazia = self.encontrar_posicao_vazia()
        if coluna_vazia < self.LADO - 1:
            self.estado[linha_vazia][coluna_vazia] = self.estado[linha_vazia][coluna_vazia + 1]
            self.estado[linha_vazia][coluna_vazia + 1] = 0

    def estado_final(self):
        return self.estado


class VerificadorVitoria:
    @staticmethod
    def verificar(estado):
        valor_esperado = 0
        for linha in estado:
            for valor in linha:
                if valor != valor_esperado:
                    return False
                valor_esperado += 1
        return True


if __name__ == "__main__":
    inicio = input()
    tabuleiro = Tabuleiro(inicio)
    tabuleiro.imprimir_tabuleiro()
    movimentos = input().lower()

    for movimento in movimentos:
        if movimento == 'u':
            tabuleiro.cima()
        elif movimento == 'd':
            tabuleiro.baixo()
        elif movimento == 'l':
            tabuleiro.esquerda()
        elif movimento == 'r':
            tabuleiro.direita()
        tabuleiro.imprimir_tabuleiro()

    if VerificadorVitoria.verificar(tabuleiro.estado_final()):
        print("Posição final: true")
    else:
        print("Posição final: false")
