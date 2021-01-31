from project.domain.user import User


class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self, filters=None):

        result = [User.from_dict(i) for i in self.data]

        if filters is None:
            return result

        print(filters)

        if "user_id__eq" in filters:
            result = [r for r in result if r.user_id == int(filters["user_id__eq"])]

        return result