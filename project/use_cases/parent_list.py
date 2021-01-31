from project.responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
    build_response_from_invalid_request,
)


def parent_list_use_case(repo, request):
    if not request:
        return build_response_from_invalid_request(request)
    try:
        parents = repo.list(filters=request.filters)
        return ResponseSuccess(parents)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)