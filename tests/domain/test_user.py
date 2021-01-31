import datetime
from project.domain.user import User


def test_user_model_init():

    user = User(
        user_id = 1,
        username = "user",
        password = "123",
        email = "user@gmail.com",
        createdAt = str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    )

    assert user.user_id == 1
    assert user.username == "user"
    assert user.password == "123"
    assert user.email == "user@gmail.com"
    assert user.createdAt == str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    assert user.updatedAt == str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))


def test_user_model_from_dict():

    init_dict = {
        "user_id": 1,
        "username": "user",
        "password": "123",
        "email": "user@gmail.com",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    }

    user = User.from_dict(init_dict)

    assert user.user_id == 1
    assert user.username == "user"
    assert user.password == "123"
    assert user.email == "user@gmail.com"
    assert user.createdAt == str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    assert user.updatedAt == str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))


def test_user_model_to_dict():

    init_dict = {
        "user_id": 1,
        "username": "user",
        "password": "123",
        "email": "user@gmail.com",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    }

    user = User.from_dict(init_dict)

    assert user.to_dict() == init_dict


def test_user_model_comparison():

    init_dict = {
        "user_id": 1,
        "username": "user",
        "password": "123",
        "email": "user@gmail.com",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    }

    user1 = User.from_dict(init_dict)
    user2 = User.from_dict(init_dict)

    assert user1 == user2


