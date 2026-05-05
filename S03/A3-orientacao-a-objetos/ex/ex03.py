"""
Exercício 3 - Classe Participacao
"""

class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, value):
        if value in ("", " "):
            raise ValueError('O prontuário não pode ser vazio.')
        self._prontuario = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if value in ("", " "):
            raise ValueError('O nome não pode ser vazio.')
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value in ("", " "):
            raise ValueError('O email não pode ser vazio.')
        self._email = value

    @classmethod
    def from_string(cls, repr_aluno):
        prontuario, nome, email = repr_aluno.split(sep=',')
        return cls(prontuario, nome, email)

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario
        return False

    def __hash__(self):
        return hash(self.prontuario)

    def __str__(self):
        return f'Aluno[prontuario={self.prontuario}, nome={self.nome}, email={self.email}]'

    def __repr__(self):
        return f'Aluno(prontuario={self.prontuario}, nome={self.nome}, email={self.email})'


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


class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if value <= 0:
            raise ValueError('O codigo não pode ser nulo.')
        self._codigo = value

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, value):
        if value in ("", " "):
            raise ValueError('A data não pode ser vazia.')
        self._data_inicio = value

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, value):
        if value in ("", " "):
            raise ValueError('O responsável não pode ser vazio.')
        self._data_fim = value

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)

    def __str__(self):
        return f'Participacao[codigo={self.codigo}, data inicio={self.data_inicio}, data fim={self.data_fim}, aluno={self.aluno}, projeto={self.projeto}]'

    def __repr__(self):
        return f'Participacao[codigo={self.codigo}, data inicio={self.data_inicio}, data fim={self.data_fim}, aluno={self.aluno}, projeto={self.projeto}]'


aluno1          = Aluno('SP0101', 'João da Silva', 'joao@email.com')

projeto1        = Projeto( 1, 'Laboratório de Desenvolvimento de Software', 'Pedro Gomes')

participacao1    = Participacao(1, '05/06', '14/11', aluno1, projeto1)
participacao2   = Participacao(2, '20/06', '20/12', aluno1, projeto1)

print(participacao1)
print(participacao2)
