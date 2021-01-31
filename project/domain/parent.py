import dataclasses
import datetime


@dataclasses.dataclass
class Parent:
    parent_id: int
    name: str
    createdAt: str
    updatedAt: str


    @classmethod
    def from_dict(self, d):
        return self(**d)


    def to_dict(self):
        return dataclasses.asdict(self)