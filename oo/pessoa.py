class Pessoa():

    def __init__(self, nome=None, idade=35):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá, {id(self)}'


if __name__ == "__main__":
    p = Pessoa('Dênison')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = 'Jhonny'
    print(p.nome)
    print(p.idade)
