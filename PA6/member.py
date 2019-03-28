from dataclasses import dataclass, field


@dataclass
class Member(object):
    name: str
    phone: str
    email: str = fi
    year_of_birth: int
