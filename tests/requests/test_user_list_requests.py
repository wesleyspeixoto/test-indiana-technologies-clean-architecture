import pytest

from project.requests.user_list import build_user_list_request


def test_build_user_list_request_without_parameters():
    request = build_user_list_request()

    assert request.filters is None
    assert bool(request) is True


def test_build_user_list_request_with_empty_filters():
    request = build_user_list_request({})

    assert request.filters == {}
    assert bool(request) is True



def test_build_user_list_request_with_invalid_filters_parameter():
    request = build_user_list_request(filters=5)

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "filters"
    assert bool(request) is False


def test_build_user_list_request_with_incorrect_filter_keys():
    request = build_user_list_request(filters={"a": 1})

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "filters"
    assert bool(request) is False


@pytest.mark.parametrize(
    "key", ["user_id__eq", "username__eq", "password__eq", "email__eq", "createdAt__eq", "updatedAt__eq"]
)
def test_build_user_list_request_accepted_filters(key):
    filters = {key: 1}

    request = build_user_list_request(filters=filters)

    assert request.filters == filters
    assert bool(request) is True


@pytest.mark.parametrize("key", ["user_id__lt", "user_id__gt"])
def test_build_user_list_request_rejected_filters(key):
    filters = {key: 1}

    request = build_user_list_request(filters=filters)

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "filters"
    assert bool(request) is False  