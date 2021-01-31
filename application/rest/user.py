import json
import datetime
from flask import Blueprint, Response, request

from project.repository.memrepo import MemRepo
from project.use_cases.user_list import user_list_use_case
from project.serializers.user import UserJsonEncoder
from project.responses import ResponseTypes
from project.requests.user_list import build_user_list_request


blueprint = Blueprint("user", __name__)

STATUS_CODES = {
    ResponseTypes.SUCCESS: 200,
    ResponseTypes.RESOURCE_ERROR: 404,
    ResponseTypes.PARAMETERS_ERROR: 400,
    ResponseTypes.SYSTEM_ERROR: 500,
}

users = [
    {
        "user_id": 1,
        "username": "user1",
        "password": "123",
        "email": "user1@gmail.com",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    },
    {
        "user_id": 2,
        "username": "user2",
        "password": "123",
        "email": "user2@gmail.com",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    },
    {
        "user_id": 3,
        "username": "user3",
        "password": "123",
        "email": "user3@gmail.com",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    },
    {
        "user_id": 4,
        "username": "user4",
        "password": "123",
        "email": "user4@gmail.com",
        "createdAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750)),
        "updatedAt": str(datetime.datetime(2018, 9, 21, 13, 5, 23, 781750))
    },
]



@blueprint.route("/users", methods=["GET"])
def user_list():
    qrystr_params = {
        "filters": {},
    }

    for arg, values in request.args.items():
        if arg.startswith("filter_"):
            qrystr_params["filters"][arg.replace("filter_", "")] = values

    request_object = build_user_list_request(
        filters=qrystr_params["filters"]
    )

    repo = MemRepo(users)
    response = user_list_use_case(repo, request_object)

    return Response(
        json.dumps(response.value, cls=UserJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODES[response.type],
    )