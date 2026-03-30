from service import register_user, list_users
from pydantic import ValidationError


# Dados de exemplo
user_data = {
    "name": "Matheus",
    "email": "matheus@email.com",
    "age": 22
}


try:
    # Tenta registrar usuário
    user = register_user(user_data)

    print("Usuário registrado com sucesso!")
    print(user)

except ValidationError as e:
    # Caso algum campo seja inválido
    print("Erro de validação:")
    print(e)


print("\nLista de usuários cadastrados:")

for user in list_users():
    print(user)