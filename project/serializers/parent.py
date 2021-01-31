import json
import datetime


class ParentJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "parent_id": str(o.parent_id),
                "name": o.name,
                "createdAt": o.createdAt,
                "updatedAt": o.updatedAt,
            }
            return to_serialize
        except AttributeError as err:  
            return super().default(o)