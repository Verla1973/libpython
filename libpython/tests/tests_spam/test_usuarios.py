import pytest

from libpython.spam.db import Conexao
from libpython.spam.db import Sessao
from libpython.spam.models import Usuario


def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome ='Eskurinho Dev')
    sessao_obj.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome ='Eskurinho Dev'), Usuario(nome ='Verlã Dev')]
    for usuario in usuarios:
        sessao_obj.salvar(self=usuario)
    assert usuarios == sessao_obj.listar()
