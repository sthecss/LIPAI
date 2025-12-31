"""
Exercício 1 - Classe Aluno
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
        return f'{self.prontuario},{self.nome},{self.email})'


aluno1 = Aluno.from_string('SP0101,João da Silva,joao@email.com')
aluno2 = Aluno('SP0102', 'João da Silva', 'joao@email.com')
print(aluno1)
print(aluno2)
