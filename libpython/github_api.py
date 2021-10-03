import requests
#criada nova ramificação

usuario = str(input('Digite o nome de usuário: '))


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário do github
    :param usuario: String contendo o nome de usuário no github
    :return: string com o link do avatar
    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar(usuario))
