from constructs import Construct

from typing import Any


class CodeStarConnection(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.arn = (
            'arn:aws:codeconnections:'
            'us-west-2:919468641101:'
            'connection/f43ec9d6-125f-4093-a537-cac4e3fc6f5d'
        )
