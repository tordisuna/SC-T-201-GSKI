from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Contact(object):
    name: str
    phone: str
    email: str
