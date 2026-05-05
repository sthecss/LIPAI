"""
Exercício 2 - Classe Projeto
"""


class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if value <= 0:
            raise ValueError('O codigo não pode ser nulo.')
        self._codigo = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if value in ("", " "):
            raise ValueError('O titulo não pode ser vazio.')
        self._titulo = value

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, value):
        if value in ("", " "):
            raise ValueError('O responsável não pode ser vazio.')
        self._responsavel = value

    @classmethod
    def from_string(cls, repr_projeto):
        codigo, titulo, responsavel = repr_projeto.split(sep=',')
        return cls(int(codigo), titulo, responsavel)

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)

    def __str__(self):
        return f'Projeto[codigo={self.codigo}, titulo={self.titulo}, responsavel={self.responsavel}]'

    def __repr__(self):
        return f'{self.codigo},{self.titulo},{self.responsavel}]'


projeto1 = Projeto.from_string( '1,Laboratório de Desenvolvimento de Software,Pedro Gomes')
projeto2 = Projeto( 2, 'Laboratório de Desenvolvimento de Software', 'Pedro Gomes')


print(projeto1)
print(projeto2)
