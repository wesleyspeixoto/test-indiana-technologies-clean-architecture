import datetime
from project.domain.child import Child


def test_child_model_init():

    child = Child(
        child_id = 1,
        name = "child",
        createdAt = str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    )

    assert child.child_id == 1
    assert child.name == "child"
    assert child.createdAt == str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    assert child.updatedAt == str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))


def test_child_model_from_dict():

    init_dict = {
        "child_id": 1,
        "name": "child",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    }

    child = Child.from_dict(init_dict)

    assert child.child_id == 1
    assert child.name == "child"
    assert child.createdAt == str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    assert child.updatedAt == str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))


def test_child_model_to_dict():

    init_dict = {
        "child_id": 1,
        "name": "child",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    }

    child = Child.from_dict(init_dict)

    assert child.to_dict() == init_dict


def test_child_model_comparison():

    init_dict = {
        "child_id": 1,
        "name": "child",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    }

    parent1 = Child.from_dict(init_dict)
    parent2 = Child.from_dict(init_dict)

    assert parent1 == parent2


