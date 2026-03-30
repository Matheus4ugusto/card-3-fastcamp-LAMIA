from pydantic import BaseModel, EmailStr, Field
from enum import Enum


# valores possiveis para o usuario
class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"

class User(BaseModel):
    # Campo obrigatório com tamanho mínimo
    name: str = Field(..., min_length=3, description="Nome do usuário")

    # Validação email
    email: EmailStr

    # Maior de idade
    age: int = Field(..., ge=18, description="Idade mínima de 18 anos")

    # Valor default
    role: Role = Field(default=Role.USER)