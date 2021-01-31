import pytest
from unittest import mock
import datetime

from project.domain.child import Child
from project.use_cases.child_list import child_list_use_case
from project.requests.child_list import build_child_list_request
from project.responses import ResponseTypes


@pytest.fixture
def domain_childs():

    child1 = Child(
        child_id = 1,
        name = "child1",
        createdAt = str(datetime.datetime(2013, 2, 21, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2013, 4, 21, 13, 5, 23, 781750))
    )

    child2 = Child(
        child_id = 2,
        name = "child2",
        createdAt = str(datetime.datetime(2015, 6, 21, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2015, 6, 23, 13, 5, 23, 781750))
    )

    child3 = Child(
        child_id = 3,
        name = "child3",
        createdAt = str(datetime.datetime(2016, 3, 8, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2016, 4, 10, 13, 5, 23, 781750))
    )

    child4 = Child(
        child_id = 4,
        name = "child4",
        createdAt = str(datetime.datetime(2017, 8, 23, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2017, 10, 25, 13, 5, 23, 781750))
    )

    return [child1, child2, child3, child4]


def test_child_list_without_parameters(domain_childs):
    repo = mock.Mock()
    repo.list.return_value = domain_childs

    request = build_child_list_request()

    response = child_list_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=None)
    assert response.value == domain_childs


def test_child_list_with_filters(domain_childs):
    repo = mock.Mock()
    repo.list.return_value = domain_childs

    qry_filters = {"child_id__eq": 5}
    request = build_child_list_request(filters=qry_filters)

    response = child_list_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response.value == domain_childs


def test_child_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception("Just an error message")

    request = build_child_list_request(filters={})

    response = child_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.SYSTEM_ERROR,
        "message": "Exception: Just an error message",
    }


def test_child_list_handles_bad_request():
    repo = mock.Mock()

    request = build_child_list_request(filters=5)

    response = child_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.PARAMETERS_ERROR,
        "message": "filters: Is not iterable",
    }