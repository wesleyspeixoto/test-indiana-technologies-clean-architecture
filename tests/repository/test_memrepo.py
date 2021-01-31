import pytest
import datetime

from project.domain.user import User
from project.repository.memrepo import MemRepo


@pytest.fixture
def user_dicts():
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


def test_repository_list_without_parameters(user_dicts):
    repo = MemRepo(user_dicts)

    users = [User.from_dict(i) for i in user_dicts]

    assert repo.list() == users


def test_repository_list_with_code_equal_filter(user_dicts):
    repo = MemRepo(user_dicts)

    users = repo.list(
        filters={"user_id__eq": 1}
    )

    assert len(users) == 1
    assert users[0].user_id == 1


