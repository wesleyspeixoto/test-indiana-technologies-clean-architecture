import dataclasses
import datetime


@dataclasses.dataclass
class User:
    user_id: int
    username: str
    password: str
    email: str
    createdAt: str
    updatedAt: str


    @classmethod
    def from_dict(self, d):
        return self(**d)


    def to_dict(self):
        return dataclasses.asdict(self)