import json
import datetime

from project.serializers.child import ChildJsonEncoder
from project.domain.child import Child


def test_serialize_domain_child():

    child = Child(
        child_id = 1,
        name = "child",
        createdAt = str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    )

    expected_json = f"""
        {{
            "child_id": "1",
            "name": "child",
            "createdAt": "{str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))}",
            "updatedAt": "{str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))}"
        }}
    """

    json_child = json.dumps(child, cls=ChildJsonEncoder)

    assert json.loads(json_child) == json.loads(expected_json)