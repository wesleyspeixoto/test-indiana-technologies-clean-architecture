import pytest
from unittest import mock
import datetime

from project.domain.user import User
from project.use_cases.user_list import user_list_use_case
from project.requests.user_list import build_user_list_request
from project.responses import ResponseTypes


@pytest.fixture
def domain_users():

    user1 = User(
        user_id = 1,
        username = "user1",
        password = "123",
        email = "user@gmail.com",
        createdAt = str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    )

    user2 = User(
        user_id = 2,
        username = "user2",
        password = "123",
        email = "user@gmail.com",
        createdAt = str(datetime.datetime(2015, 6, 21, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2015, 6, 23, 13, 5, 23, 781750))
    )

    user3 = User(
        user_id = 3,
        username = "user3",
        password = "123",
        email = "user@gmail.com",
        createdAt = str(datetime.datetime(2016, 3, 8, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2016, 4, 10, 13, 5, 23, 781750))
    )

    user4 = User(
        user_id = 4,
        username = "user4",
        password = "123",
        email = "user@gmail.com",
        createdAt = str(datetime.datetime(2017, 8, 23, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2017, 10, 25, 13, 5, 23, 781750))
    )

    return [user1, user2, user3, user4]



def test_users_list_without_parameters(domain_users):
    repo = mock.Mock()
    repo.list.return_value = domain_users

    request = build_user_list_request()

    response = user_list_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=None)
    assert response.value == domain_users


def test_user_list_with_filters(domain_users):
    repo = mock.Mock()
    repo.list.return_value = domain_users

    qry_filters = {"user_id__eq": 5}
    request = build_user_list_request(filters=qry_filters)

    response = user_list_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response.value == domain_users


def test_user_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception("Just an error message")

    request = build_user_list_request(filters={})

    response = user_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.SYSTEM_ERROR,
        "message": "Exception: Just an error message",
    }


def test_user_list_handles_bad_request():
    repo = mock.Mock()

    request = build_user_list_request(filters=5)

    response = user_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.PARAMETERS_ERROR,
        "message": "filters: Is not iterable",
    }