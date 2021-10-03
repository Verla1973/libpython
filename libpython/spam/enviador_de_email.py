class Enviador:

    def enviar(cls, remetente, destinatario, assunto, corpo):
        if '@' in remetente:
            return remetente
        raise EmailInvalido(f'Email do remetente inválido{remetente}')


class EmailInvalido(Exception):
    pass