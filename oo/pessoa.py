class Pessoa():

    # atributo de classe
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, {id(self)}'


if __name__ == "__main__":
    joao = Pessoa(nome='João Victor', idade=15)
    denison = Pessoa(joao, nome='Dênison Fábio', idade=36)
    print(Pessoa.cumprimentar(denison))
    print(id(denison))
    print(denison.cumprimentar())
    print(denison.nome)
    print(denison.idade)

    for filho in denison.filhos:
        print(f'nome do filho: {filho.nome}')
    
    denison.sobrenome = 'Oliveira'
    del denison.filhos
    denison.olhos = 1
    del denison.olhos
    print(denison.__dict__)
    print(joao.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(joao.olhos)
    print(denison.olhos)
    print(id(Pessoa.olhos), id(denison.olhos), id(joao.olhos))

