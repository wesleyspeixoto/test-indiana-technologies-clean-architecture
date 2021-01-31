import json
import datetime

from project.serializers.user import UserJsonEncoder
from project.domain.user import User


def test_serialize_domain_user():

    user = User(
        user_id = 1,
        username = "user",
        password = "123",
        email = "user@gmail.com",
        createdAt = str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    )

    expected_json = f"""
        {{
            "user_id": "1",
            "username": "user",
            "password": "123",
            "email": "user@gmail.com",
            "createdAt": "{str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))}",
            "updatedAt": "{str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))}"
        }}
    """

    json_user = json.dumps(user, cls=UserJsonEncoder)

    assert json.loads(json_user) == json.loads(expected_json)