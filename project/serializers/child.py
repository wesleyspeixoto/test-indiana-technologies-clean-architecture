import json
import datetime


class ChildJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "child_id": str(o.child_id),
                "name": o.name,
                "createdAt": o.createdAt,
                "updatedAt": o.updatedAt,
            }
            return to_serialize
        except AttributeError as err:  
            return super().default(o)