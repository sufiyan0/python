from sqlmodel import Field, SQLModel, create_engine, Session, select
# from pydentic import BaseModel



class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    last_name: str
    age: int | None = None
    
connection_string = "postgresql://neondb_owner:ILJdzk5s@ep-empty-hill-a52qb0bi-pooler.us-east-2.aws.neon.tech/todo?sslmode=require"
engine = create_engine(connection_string, echo= True) 


def create_heroes():
    hero_1 = Hero(name="Tony", last_name="Stark")
    hero_2 = Hero(name="Peter", last_name="Parker", age=18)
    hero_3 = Hero(name="Bruce", last_name="Banner")
    session = Session(engine)
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()
    session.close()
    
    
def update_hero():
    session = Session(engine)
    statement = select(Hero).where(Hero.id == 3)
    result = session.exec(statement)
    hero = result.one()
    hero.age = 24
    session.add(hero)
    session.commit()
    session.close()
    
def delete_hero():
    session = Session(engine)
    statement = select(Hero).where(Hero.id == 3)
    result = session.exec(statement)
    hero = result.one()
    session.delete(hero)
    session.commit()
    session.close()

def select_heroes():
    with Session(engine) as session:
        statement = select(Hero)
        results = session.exec(statement)
        for hero in results:
            print(hero)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    # create_db_and_tables()
    # create_heroes()
    # update_hero()
    # delete_hero()
    select_heroes()
    
   

     