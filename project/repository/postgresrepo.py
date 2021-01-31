from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from project.domain import user
from project.repository.postgres_objects import Base, User


class PostgresRepo:
    def __init__(self, configuration):
        connection_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            configuration["POSTGRES_USER"],
            configuration["POSTGRES_PASSWORD"],
            configuration["POSTGRES_HOSTNAME"],
            configuration["POSTGRES_PORT"],
            configuration["APPLICATION_DB"],
        )

        self.engine = create_engine(connection_string)
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine

    def _create_user_objects(self, results):
        return [
            user.User(
                user_id=q.user_id,
                username=q.username,
                password=q.password,
                email=q.email,
                createdAt=q.createdAt,
                updatedAt=q.updatedAt,
            )
            for q in results
        ]

    def list(self, filters=None):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        query = session.query(User)

        if filters is None:
            return self._create_user_objects(query.all())

        if "user_id__eq" in filters:
            query = query.filter(User.user_id == filters["user_id__eq"])

        return self._create_user_objects(query.all())