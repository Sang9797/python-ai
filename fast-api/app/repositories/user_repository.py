from sqlalchemy.orm import Session

from app.models.user_model import User


class UserRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def save(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def find_all(self) -> list[User]:
        return self.db.query(User).order_by(User.id).all()

    def find_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def find_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def delete(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()
