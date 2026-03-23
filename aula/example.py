from enum import auto, IntFlag
from typing import Any

from pydantic import (
    BaseModel,
    Field, EmailStr, SecretStr, ValidationError,
)


class Role(IntFlag):
    Author = auto()
    Editor = auto()
    Developer = auto()
    Admin = Author | Editor | Developer


class User(BaseModel):
    name: str = Field(examples=["Matheus Augusto"])
    email: EmailStr = Field(
        examples=["example@example.com"],
        description="The email address of the user",
        frozen=True,
    )
    password: SecretStr = Field(
        examples=["Password123"], description="The password of the user"
    )
    role: Role = Field(default=None, description="The role of the user")

def validate(data: dict[str, Any]) -> None:
    try:
        user = User.model_validate(data)
        print(user)
    except ValidationError as e:
