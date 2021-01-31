import sqlalchemy
import pytest
import datetime

from project.repository.postgres_objects import Base, User


@pytest.fixture(scope="session")
def pg_session_empty(app_configuration):
    conn_str = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
        app_configuration["POSTGRES_USER"],
        app_configuration["POSTGRES_PASSWORD"],
        app_configuration["POSTGRES_HOSTNAME"],
        app_configuration["POSTGRES_PORT"],
        app_configuration["APPLICATION_DB"],
    )
    engine = sqlalchemy.create_engine(conn_str)
    connection = engine.connect()

    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    DBSession = sqlalchemy.orm.sessionmaker(bind=engine)
    session = DBSession()

    yield session

    session.close()
    connection.close


@pytest.fixture(scope="session")
def pg_test_data():
    return [
    {
        "user_id": 1,
        "username": "user1",
        "password": "123",
        "email": "user1@gmail.com",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    },
    {
        "user_id": 2,
        "username": "user2",
        "password": "123",
        "email": "user2@gmail.com",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    },
    {
        "user_id": 3,
        "username": "user3",
        "password": "123",
        "email": "user3@gmail.com",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    },
    {
        "user_id": 4,
        "username": "user4",
        "password": "123",
        "email": "user4@gmail.com",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    },
]


@pytest.fixture(scope="function")
def pg_session(pg_session_empty, pg_test_data):
    for r in pg_test_data:
        new_user = User(
            user_id=r["user_id"],
            username=r["username"],
            password=r["password"],
            email=r["email"],
            createdAt=r["createdAt"],
            updatedAt=r["updatedAt"],
        )
        pg_session_empty.add(new_user)
        pg_session_empty.commit()

    yield pg_session_empty

    pg_session_empty.query(User).delete()