from sqlalchemy.orm import Session
from app.crud.database import engine
import app.models.user as usersModels

# Create the database tables automatically (for production, use Alembic migrations instead)
usersModels.Base.metadata.create_all(bind=engine)

class CRUDUser:
    def get_user_by_username(self, db: Session, username: str) -> dict | None:
        return db.query(usersModels.User).filter(usersModels.User.username == username).first()
    
    def create_user(self, db: Session, user: dict) -> dict | None:
        db_item = usersModels.User(username=user["username"], role_type=user["role_type"], hashed_password=user["hashed_password"])
        db.add(db_item)
        db.commit()
        db.refresh(db_item) # Refresh to get the generated ID from the database
        return db_item