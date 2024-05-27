from sqlmodel import create_engine, Session ,select, SQLModel ,  Field
from fastapi import FastAPI , Depends,HTTPException 
from pydantic import BaseModel
from typing import Optional , Annotated

class todo(SQLModel, table=True):
    id:int | None = Field(default=None, primary_key=True)
    todo:str
    complete:bool
    
connection_string = "postgresql://neondb_owner:3IMLJdWzk5sC@ep-empty-hill-a52qb0bi-pooler.us-east-2.aws.neon.tech/todoWithFastapi?sslmode=require"

engine = create_engine(connection_string, echo=True)
app:FastAPI = FastAPI()


def crate_table():
    SQLModel.metadata.create_all(engine)




# @app.on_event("startup")
# def on_startup():
#     crate_table()

if __name__ == "__main__":
    crate_table()


@app.get("/" )
def get_todo():
    with Session(engine) as session:
        todos = session.exec(select(todo)).all()
        return todos
    
    
@app.post("/")
def create_todo(todo:todo):
    with Session(engine) as session:
        session.add(todo)        
        session.commit()
        session.close()
        return todo

@app.patch("/id/{id}")
def update_todo(id:int,complete:bool,updating_todo:todo):
    with Session(engine) as session:
        update_todo = session.get(todo,id)
        update_todo.todo = updating_todo
        update_todo.complete = complete
        session.add_all(update_todo)
        session.commit()
        session.close()
        return update_todo


@app.delete("/id/{id}")
def delete_todo(id:int):
    with Session(engine) as session:
        delete_todo = session.get(todo,id)
        print(delete_todo)
        if not todo:
            raise HTTPException(status_code=404, detail="Hero not found")
        session.delete(delete_todo)
        session.commit()
        return {"ok": True}
        