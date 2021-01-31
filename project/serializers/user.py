import json
import datetime


class UserJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "user_id": str(o.user_id),
                "username": o.username,
                "password": o.password,
                "email": o.email,
                "createdAt": o.createdAt,
                "updatedAt": o.updatedAt,
            }
            return to_serialize
        except AttributeError as err:  
            return super().default(o)