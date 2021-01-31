import datetime
from project.domain.parent import Parent


def test_parent_model_init():

    parent = Parent(
        parent_id = 1,
        name = "parent",
        createdAt = str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    )

    assert parent.parent_id == 1
    assert parent.name == "parent"
    assert parent.createdAt == str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    assert parent.updatedAt == str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))


def test_parent_model_from_dict():

    init_dict = {
        "parent_id": 1,
        "name": "parent",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    }

    parent = Parent.from_dict(init_dict)

    assert parent.parent_id == 1
    assert parent.name == "parent"
    assert parent.createdAt == str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    assert parent.updatedAt == str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))


def test_parent_model_to_dict():

    init_dict = {
        "parent_id": 1,
        "name": "parent",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    }

    parent = Parent.from_dict(init_dict)

    assert parent.to_dict() == init_dict


def test_parent_model_comparison():

    init_dict = {
        "parent_id": 1,
        "name": "parent",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    }

    parent1 = Parent.from_dict(init_dict)
    parent2 = Parent.from_dict(init_dict)

    assert parent1 == parent2


