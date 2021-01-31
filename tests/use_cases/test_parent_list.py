import pytest
from unittest import mock
import datetime

from project.domain.parent import Parent
from project.use_cases.parent_list import parent_list_use_case
from project.requests.parent_list import build_parent_list_request
from project.responses import ResponseTypes


@pytest.fixture
def domain_parents():

    parent1 = Parent(
        parent_id = 1,
        name = "parent1",
        createdAt = str(datetime.datetime(2013, 2, 21, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2013, 4, 21, 13, 5, 23, 781750))
    )

    parent2 = Parent(
        parent_id = 2,
        name = "parent2",
        createdAt = str(datetime.datetime(2015, 6, 21, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2015, 6, 23, 13, 5, 23, 781750))
    )

    parent3 = Parent(
        parent_id = 3,
        name = "parent3",
        createdAt = str(datetime.datetime(2016, 3, 8, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2016, 4, 10, 13, 5, 23, 781750))
    )

    parent4 = Parent(
        parent_id = 4,
        name = "parent4",
        createdAt = str(datetime.datetime(2017, 8, 23, 13, 5, 23, 781750)),
        updatedAt = str(datetime.datetime(2017, 10, 25, 13, 5, 23, 781750))
    )

    return [parent1, parent2, parent3, parent4]



def test_parents_list_without_parameters(domain_parents):
    repo = mock.Mock()
    repo.list.return_value = domain_parents

    request = build_parent_list_request()

    response = parent_list_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=None)
    assert response.value == domain_parents


def test_parent_list_with_filters(domain_parents):
    repo = mock.Mock()
    repo.list.return_value = domain_parents

    qry_filters = {"parent_id__eq": 5}
    request = build_parent_list_request(filters=qry_filters)

    response = parent_list_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response.value == domain_parents


def test_parent_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception("Just an error message")

    request = build_parent_list_request(filters={})

    response = parent_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.SYSTEM_ERROR,
        "message": "Exception: Just an error message",
    }


def test_parent_list_handles_bad_request():
    repo = mock.Mock()

    request = build_parent_list_request(filters=5)

    response = parent_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.PARAMETERS_ERROR,
        "message": "filters: Is not iterable",
    }