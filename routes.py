import uvicorn
from fastapi import FastAPI, HTTPException
from models import Base, engine, session, User
from schemas import UserSchema, UpdateUserSchema
from datetime import datetime

app = FastAPI()


@app.get("/api/users/{id}", response_model=UserSchema, responses={200: {'description': 'Success'}, 404: {'description': 'User not found'}})
async def get_user(id: int):
    """
    Function displays complete user information
    """
    user = session.query(User).filter(User.id == id).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.put("/api/users/{id}", response_model=UpdateUserSchema, responses={200: {'description': 'Success'}, 404: {'description': 'User not found'}})
async def update_user(id: int, user_data: UpdateUserSchema):
    """
    Function updates user data
    """
    user = session.query(User).filter(User.id == id).first()
    if user:
        if user_data.username:
            user.username = user_data.username
        if user_data.email:
            user.email = user_data.email
        session.commit()
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete("/api/users/{id}", responses={200: {'description': 'Success'}, 404: {'description': 'User not found'}, 500: {'description': 'Internal Server Error'}})
async def delete_user(id: int):
    """
    Function deletes user
    """
    user = session.query(User).filter(User.id == id).first()
    if user:
        try:
            session.delete(user)
            session.commit()
            return {"message": "User deleted successfully"}
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=str(e))
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.get("/api/users", response_model=list[UserSchema], responses={200: {'description': 'Success'}})
async def get_users():
    """
    Function gets all users
    """
    users = session.query(User).all()
    return users


@app.post("/api/users", responses={201: {'description': 'Created'}, 400: {'description': 'Bad Request'}})
async def create_user(user_data: UserSchema):
    """
    Function add to DB new user
    """
    try:
        user = User(username=user_data.username, email=user_data.email, registration_date=datetime.utcnow())
        session.add(user)
        session.commit()
        return "ok", 201
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    uvicorn.run(app, host="127.0.0.1", port=8000)
