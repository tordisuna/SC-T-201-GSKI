from dataclasses import dataclass, field, asdict


@dataclass(compare=True)
class Sport(object):
    name: str
