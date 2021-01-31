from project.responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
    build_response_from_invalid_request,
)


def child_list_use_case(repo, request):
    if not request:
        return build_response_from_invalid_request(request)
    try:
        childs = repo.list(filters=request.filters)
        return ResponseSuccess(childs)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)