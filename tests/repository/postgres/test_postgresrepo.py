import pytest
from project.repository import postgresrepo

pytestmark = pytest.mark.integration


def test_repository_list_without_parameters(
    app_configuration, pg_session, pg_test_data
):
    print(app_configuration)
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_users = repo.list()

    assert set([r.user_id for r in repo_users]) == set(
        [r["user_id"] for r in pg_test_data]
    )


def test_repository_list_with_user_id_equal_filter(
    app_configuration, pg_session, pg_test_data
):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_users = repo.list(
        filters={"user_id__eq": 1}
    )
    

    assert len(repo_users) == 1
    assert repo_users[0].user_id == 1


