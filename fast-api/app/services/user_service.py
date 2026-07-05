from app.exceptions import ResourceNotFoundError
from app.models.user_model import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def create_user(self, request: UserCreate) -> UserResponse:
        existing_user = self.user_repository.find_by_email(request.email)
        if existing_user:
            raise ValueError("Email already exists")

        user = User(name=request.name, email=request.email)
        saved_user = self.user_repository.save(user)
        return UserResponse.model_validate(saved_user)

    def get_all_users(self) -> list[UserResponse]:
        users = self.user_repository.find_all()
        return [UserResponse.model_validate(user) for user in users]

    def get_user_by_id(self, user_id: int) -> UserResponse:
        user = self._get_user_or_raise(user_id)
        return UserResponse.model_validate(user)

    def update_user(self, user_id: int, request: UserUpdate) -> UserResponse:
        user = self._get_user_or_raise(user_id)
        user.name = request.name
        updated_user = self.user_repository.save(user)
        return UserResponse.model_validate(updated_user)

    def delete_user(self, user_id: int) -> None:
        user = self._get_user_or_raise(user_id)
        self.user_repository.delete(user)

    def _get_user_or_raise(self, user_id: int) -> User:
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise ResourceNotFoundError(f"User with id {user_id} was not found")
        return user
