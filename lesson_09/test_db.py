from sqlalchemy import create_engine
from sqlalchemy.sql import select, insert, update, delete, text as txt
from sqlalchemy import MetaData

db_connection_string = "postgresql+psycopg2://postgres:Helotmst@localhost/QA"
engine = create_engine(db_connection_string)
metadata_obj = MetaData()
newid = 0
t = txt("SELECT MAX(USER_ID) FROM USERS")


def test_db_connection():
    t = txt("SELECT * FROM STUDENT")
    with engine.connect() as connection:
        result = connection.execute(t)
        assert result.rowcount == 1673


def test_db_insert():

    emailuser = "MYOWNER@mail.ru"
    subject = 1
    with engine.connect() as connection:
        ID = connection.execute(t).fetchone()[0]
        metadata_obj.reflect(bind=engine)
        ins = metadata_obj.tables["users"]
        newid = ID + 1
        intstr = insert(ins).values(
            user_id=newid, user_email=emailuser, subject_id=subject
        )
        connection.execute(intstr)
        connection.commit()
        assert connection.execute(t).fetchone()[0] == newid
        de = delete(ins).where(ins.c.user_id == newid)
        connection.execute(de)
        connection.commit()


def test_db_update():
    subject = 1
    emailuser = "MYunique@mail.ru"
    with engine.connect() as connection:
        metadata_obj.reflect(bind=engine)
        ins = metadata_obj.tables["users"]
        ID = connection.execute(t).fetchone()[0]
        newid = ID + 1
        intstr = insert(ins).values(
            user_id=newid, user_email=emailuser, subject_id=subject
        )
        connection.execute(intstr)
        connection.commit()
        upd = (
            update(ins)
            .where(ins.c.user_id == newid)
            .values(user_email="oldschool@ay.ru")
        )
        connection.execute(upd)
        connection.commit()
        row = connection.execute(
            select(ins).where(
                ins.c.user_email == "oldschool@ay.ru", ins.c.user_id == newid
            )
        )
        assert row.rowcount == 1
        de = delete(ins).where(ins.c.user_id == newid)
        connection.execute(de)
        connection.commit()


def test_db_delete():
    subject = 1
    emailuser = "MYuniqueemailtoDelete@mail.ru"
    with engine.connect() as connection:
        metadata_obj.reflect(bind=engine)
        ins = metadata_obj.tables["users"]
        ID = connection.execute(t).fetchone()[0]
        newid = ID + 1
        intstr = insert(ins).values(
            user_id=newid, user_email=emailuser, subject_id=subject
        )
        connection.execute(intstr)
        connection.commit()
        de = delete(ins).where(ins.c.user_id == newid, ins.c.user_email == emailuser)
        connection.execute(de)
        connection.commit()
        row = connection.execute(select(ins).where(ins.c.user_email == emailuser))
        assert row.rowcount == 0