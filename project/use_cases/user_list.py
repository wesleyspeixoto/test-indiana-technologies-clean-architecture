from project.responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
    build_response_from_invalid_request,
)


def user_list_use_case(repo, request):
    if not request:
        return build_response_from_invalid_request(request)
    try:
        users = repo.list(filters=request.filters)
        return ResponseSuccess(users)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)