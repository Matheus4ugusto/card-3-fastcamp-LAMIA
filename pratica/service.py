from models import User


# armazenamento
database = []


def register_user(user_data: dict):

    # Converte o dicionário em objeto User
    user = User(**user_data)

    # Insere o user
    database.append(user)

    return user


def list_users():

    return database