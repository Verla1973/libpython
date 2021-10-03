import pytest

from libpython.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['renzon.python.pro.br',
    'manoads2019@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'luciano@python.pro.br',
        'Cursos Python Pro',
        'Primeira turma encerrada'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['renzon',
    'manoads2019@gmail.com']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            'remetente',
            'luciano@python.pro.br',
            'Cursos Python Pro',
            'Primeira turma encerrada'
    )

