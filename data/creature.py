from .init import conn, curs
from ..model.creature import Creature

curs.execute("""create table if not exists creature(
                name text primary key,
                description text,
                location text)""")

def row_to_model(row: tuple) -> Creature:
    return Creature(*row)

def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()

def get_one(name: str) -> Creature:
    qry = "select * from creature where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    return row_to_model(curs.fetchone())

def get_all() -> list[Creature]:
    qry = "select * from creature"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(creature: Creature):
    qry = "insert into creature values (:name, :description, :location)"
    params = model_to_dict(creature)
    curs.execute(qry, params)
    return get_one(creature.name)

def modify(creature: Creature):
    qry = """update creature
            set location=:location,
                name=:name,
                description=:description
            where name=:name0"""
    params = model_to_dict(creature)
    params["name0"] = creature.name
    res = curs.execute(qry, params)
    return get_one(creature.name)

def replace(creature: Creature):
    return creature

def delete(name: str):
    qry = "delete from creature where name = :name"
    params = {"name": name}
    res = curs.execute(qry, params)
    return bool(res)


