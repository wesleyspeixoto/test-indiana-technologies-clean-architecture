import json
import datetime

from project.serializers.parent import ParentJsonEncoder
from project.domain.parent import Parent


def test_serialize_domain_parent():

    parent = Parent(
        parent_id = 1,
        name = "parent",
        createdAt = str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    )

    expected_json = f"""
        {{
            "parent_id": "1",
            "name": "parent",
            "createdAt": "{str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))}",
            "updatedAt": "{str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))}"
        }}
    """

    json_parent = json.dumps(parent, cls=ParentJsonEncoder)

    assert json.loads(json_parent) == json.loads(expected_json)