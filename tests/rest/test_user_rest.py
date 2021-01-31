import json
import datetime
from unittest import mock

from project.domain.user import User
from project.responses import ResponseSuccess


user_dict = {
    "user_id": "1",
    "username": "user1",
    "password": "123",
    "email": "user1@gmail.com",
    "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
    "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
}

users = [User.from_dict(user_dict)]


@mock.patch("application.rest.user.user_list_use_case")
def test_get(mock_use_case, client):
    mock_use_case.return_value = ResponseSuccess(users)

    http_response = client.get("/users")

    assert json.loads(http_response.data.decode("UTF-8")) == [user_dict]

    mock_use_case.assert_called()
    args, kwargs = mock_use_case.call_args
    assert args[1].filters == {}

    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"


@mock.patch("application.rest.user.user_list_use_case")
def test_get_with_filters(mock_use_case, client):
    mock_use_case.return_value = ResponseSuccess(users)

    http_response = client.get(
        "/users?filter_user_id__eq=1&filter_username__eq=user"
    )

    assert json.loads(http_response.data.decode("UTF-8")) == [user_dict]

    mock_use_case.assert_called()
    args, kwargs = mock_use_case.call_args
    assert args[1].filters == {"user_id__eq": "1", "username__eq": "user"}

    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"

