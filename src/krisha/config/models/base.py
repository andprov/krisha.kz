from dataclasses import dataclass


@dataclass
class BaseConfigModel:
    def __post_init__(self):
        self._validate()

    def _validate(self):
        raise NotImplementedError
