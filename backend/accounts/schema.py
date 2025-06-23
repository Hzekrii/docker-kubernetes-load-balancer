from datetime import datetime

import strawberry
import jwt
from strawberry.types import Info
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from typing import Optional
from accounts.models import User
from mysite import settings


def create_jwt_token(user):
    jwt_config = settings.STRAWBERRY_DJANGO["JWT_AUTH"]
    payload = {
        "user_id": str(user.id),
        "username": user.username,
        "exp": datetime.utcnow() + jwt_config["JWT_EXPIRATION_DELTA"],
        "iat": datetime.utcnow(),
    }
    token = jwt.encode(
        payload,
        jwt_config["JWT_SECRET_KEY"],
        algorithm=jwt_config["JWT_ALGORITHM"]
    )
    return token

def get_user_from_token(token):
    try:
        jwt_config = settings.STRAWBERRY_DJANGO["JWT_AUTH"]
        payload = jwt.decode(
            token,
            jwt_config["JWT_SECRET_KEY"],
            algorithms=[jwt_config["JWT_ALGORITHM"]]
        )
        user = User.objects.get(id=payload["user_id"])
        return user
    except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist):
        return None

@strawberry.type
class UserType:
    id: strawberry.ID
    username: str
    email: Optional[str]
    is_active: bool

    @classmethod
    def from_instance(cls, user):
        return cls(
            id=strawberry.ID(str(user.id)),
            username=user.username,
            email=user.email,
            is_active=user.is_active
        )

@strawberry.input
class UserInput:
    username: str
    password: str
    email: Optional[str] = None

@strawberry.input
class LoginInput:
    username: str
    password: str

@strawberry.type
class AuthSuccess:
    user: UserType
    token: str  # In a real app, you'd implement proper token auth

@strawberry.type
class AuthError:
    message: str

AuthResult = strawberry.union("AuthResult", (AuthSuccess, AuthError))

@strawberry.type
class Mutation:
    @strawberry.mutation
    def register(self, info: Info, input: UserInput) -> AuthResult:
        try:
            user = User.objects.create(
                username=input.username,
                email=input.email,
                password=make_password(input.password)
            )
            token = create_jwt_token(user)
            return AuthSuccess(
                user=UserType(
                    id=strawberry.ID(str(user.id)),
                    username=user.username,
                    email=user.email,
                    is_active=user.is_active
                ),
                token=token # Replace with JWT or session token
            )
        except Exception as e:
            return AuthError(message=str(e))

    @strawberry.mutation
    def login(self, info: Info, input: LoginInput) -> AuthResult:
        request = info.context["request"]
        user = authenticate(
            request,
            username=input.username,
            password=input.password
        )
        if user is not None:
            login(request, user)
            token = create_jwt_token(user)
            return AuthSuccess(
                user=UserType(
                    id=strawberry.ID(str(user.id)),
                    username=user.username,
                    email=user.email,
                    is_active=user.is_active
                ),
                token=token  # Replace with JWT or session token
            )
        return AuthError(message="Invalid credentials")

    @strawberry.mutation
    def logout(self, info: Info) -> bool:
        request = info.context["request"]
        logout(request)
        return True

@strawberry.type
class Query:
    @strawberry.field
    def me(self, info: Info) -> Optional[UserType]:
        user = info.context["request"].user
        if user.is_authenticated:
            return UserType(
                id=strawberry.ID(str(user.id)),
                username=user.username,
                email=user.email,
                is_active=user.is_active
            )
        return None

schema = strawberry.Schema(query=Query, mutation=Mutation)